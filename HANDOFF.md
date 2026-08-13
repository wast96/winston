# HANDOFF, Burn, O Sword! (燃えよ剣), Shiba Ryōtarō

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery: every
batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count. Rewrite it at
the end of every batch; always keep the paste-ready kickoff below as its first
section.

## Message to paste into the next chat

```
Burn, O Sword! B06

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then STYLE.md, then book.json. We are translating Burn, O Sword! (燃えよ剣) by Shiba Ryōtarō from a Japanese digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/burn-o-sword; expect the harness to open you on a stray per-task branch and consolidate per CLAUDE.md rule 2. Deliverable out/burn-o-sword.epub.

Batches 1 to 5 are DONE (ch01 to ch23). ch01 is the FROZEN register reference: reference/ch01_ref.md. Run ./setup.sh; if data/src/ is empty re-run scripts/ingest_epub.py source.epub (Japanese-aware: strips furigana, substitutes 8 gaiji, writes reference/furigana_readings.tsv). No source-note stream. Keep the source's own cover (data/figs/embed0009_HD.jpg), reused byte-identical, exactly as book.json already sets it; the commissioner likes it, do not change it. The known failing test "hook stands down on template stub" is EXPECTED (it only passes on the template placeholder kickoff); every other test passes.

Do Batch 6 = ch24 through ch28 (京師の乱 / Turmoil in the Capital; 長州軍乱入 / The Chōshū Army Storms In; 伊東甲子太郎 / Itō Kashitarō; 甲子太郎、京へ / Kashitarō Comes to Kyoto; 慶応元年正月 / New Year, First Year of Keiō), end to end per the CLAUDE.md pipeline, RUN TO COMPLETION. ch25 is the Kinmon (Hamaguri Gate) Incident of July 1864; ch26-27 bring in Itō Kashitarō and his faction (the seed of the later Kōdai-ji split); fact-check these carefully. Do not stop mid-batch except for a genuine blocker or completion. For each chapter:
1. Build data/zh/<id>.txt from data/src with scripts/build_zh.py <id> <srcbase> "<title>" (title line "### <title>" then one body line per non-empty source paragraph, skipping the first two header lines). ch24=28_part0026, ch25=29_part0027, ch26=30_part0028, ch27=31_part0029, ch28=32_part0030. Fix any extractor splits (this source has had none: a narration line ending in 、 before a 「quote」 is the source's own lead-in, handled by the {j} join, NOT a split to merge). Recover scene breaks with scripts/scene_map.py OEBPS/Text/partNNNN.xhtml (a run of TWO OR MORE consecutive <p><br/></p> in the body is a break; the single pair after the title is only the title/body separator; body-paragraph N maps to source line N+2). Place *** in the reading at those points.
2. Translate to the FROZEN ch01 register. Names Japanese order, surname first, macrons; CONSULT reference/furigana_readings.tsv before romanizing ANY name or word (it caught Rokusha/Momonoi in B02, Yamanami-not-Sannan in B03, Toshima/Mikura/Akazawa/Kujō in B04, and in B05: Matsubara-an-not-Shōhōan Seifu, 北添佶麿→Yoshimaro, 佐伯稜威雄→Mizuo, 丹虎→Tantora; note the source also uses EXPRESSIVE gikun furigana like 将軍→たいじゅ, 京→ここ, 近藤→せんせい, which are semantic glosses, NOT phonetic, and must not be romanized), and consult glossary.json (then authority.json) first, feeding decided renderings back. Use the {j} display-join marker so a quotation reads inline with its lead-in and attribution; keep an exchange one paragraph per speaker turn. Watch parity: every 「…」 quote line, every と…いった attribution line, and every 「………」 silence is its OWN source paragraph and needs its OWN reading line (B04 and B05 each dropped/merged lines in dialogue and narration seams; make_bilingual caught them; verify the count). OBEY STYLE.md (em-dash budget; no scene-primed idioms). Consult the voice sheets below; read the last two pages of ch23's English before starting ch24 (batch seam).
3. Author out/<id>_reading.md (## title, {j}, ***, blank-separated). Then the battery: bash scripts/check_chapter.sh <id> <srcbase> "<title_en>" runs reading_to_en + make_bilingual (parity refuses on mismatch) + verify_unit (--noise data/noise.txt) + gen_check_config + check_align + check_content + qc_entities + check_apparatus + check_register. Verify each chapter TAIL against the source explicitly (rule 4).
4. Footnotes per the reader model (first-appearance discipline; keep the "NOT re-noted" ledger in PROGRESS.md; note MORE than the glossary row) via apparatus_merge.py (each glossary row MUST carry a "section": people|places|organizations|terms field; the merge nests it and check_apparatus stays clean; render the glossary's DECIDED form verbatim, e.g. 旗本→"hatamoto" not "bannermen", or qc_entities/check_content flag it; when the source shortens a name give the glossary a bare-surname en, as with 古高→"Furutaka"). Any figure from data/figs/ with a translated caption and real alt text.
5. check_register.py --ref reference/ch01_ref.md out/<id>_reading.md; record in PROGRESS.md. Fact-check historical claims against real scholarship (never LLM-sourced; IGNORE Grok/Grokipedia), verdict in the note. Add numeral-noise rules to data/noise.txt as new numbered names/idioms/place-names appear (comment each; never noise a real quantity).
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/burn-o-sword.epub); record ALL check results and EVERY digitization glitch in PROGRESS.md; update HANDOFF.md; commit and push to claude/burn-o-sword.

End the batch with BOTH chat deliverables (CLAUDE.md rule 1, enforced by the Stop hook): the built EPUB ATTACHED in the chat AND the Batch 7 kickoff PASTED VERBATIM in a fenced code block. Batch 7 = ch29 through ch33.

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
- B05 = ch19 to ch23, COMPLETE. ch19 再会 / "Reunion", ch20 二帖半敷町の辻 / "The
  Crossroads at Nijōhanjiki-chō", ch21 局中法度書 / "The Code of the Corps", ch22
  池田屋 / "The Ikedaya", ch23 断章・池田屋 / "Ikedaya: A Coda". Notes 144 to 180
  (37 this batch). All checks green; qa_epub PASS; epubcheck 0/0/0/0. Continuous
  note number so far: 180. See PROGRESS.md B05 for the full record, the six
  fact-check verdicts, the two caught parity misses, the one content
  displacement fix, and every settled rendering.

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
- scripts/check_numbers.py (B04 PATCH, target-side only): spelled_numbers reads
  "a/one hundred and <ten..nineteen>" (110-119). DO NOT REVERT.
- scripts/build_zh.py (B04): mechanical data/zh/<id>.txt builder from data/src.
- data/noise.txt (B01 to B05): Japanese name/idiom/place numeral rules, each
  commented. Add more as numbered names / teen-elisions / place-names appear.
  Never noise a real quantity. B05 added: 三月亭, 為三郎 (ch19); 万事, 四つ手,
  四つ路, 七どん, 十数, 十七、八, 二帖半敷 (ch20); 無二 (ch21); 二階, 四郎兵衛,
  何百日, 万々, 六角, 四国屋 (ch22); 五吉郎, 新三郎 (ch23).
- STYLE.md (B01): the house style sheet (em-dash budget; scene-primed idioms).
  READ IT each batch; add to it when the commissioner corrects a line. No new
  rule in B05 (the one 3-em-dash list in ch21 fell under existing rule 1).
- reference/ch01_ref.md (B01): the FROZEN register reference. Do not edit.
- GLOSSARY en for shortened names: when the source drops to a bare surname, set
  the glossary "en" to that bare form (古高 -> "Furutaka", 野老山 -> "Tokoroyama")
  so check_content matches every paragraph. Do NOT add a bare given-name row
  that is a SUBSTRING of an existing honorific key (a bare 佐絵 over-matched
  お佐絵 in ch01-02 and was removed; the referent stays お佐絵 -> Osae).

## Voice sheets (one per major character; consult at every dialogue scene)

- NARRATOR: third person, wry and knowing, fond of the aside ("or so the story
  goes," "by the way," "come to think of it") and the forward glance to events
  years ahead. Long descriptive sentences alternating with very short flat ones.
  Period texture, never antiquarian. KEEPS Shiba's own modern parentheticals
  (the Western dates; "the Kyoto Hotel of today"; "pulled down in 1931"; the
  staff/line metaphor; quoted real letters and diaries): KEEP them all.
- HIJIKATA TOSHIZŌ ("Toshi"): the hero, 22 to 29 across the book. Rough Bushū
  farm dialect off guard, contracted and blunt. Cool, laconic, a dandy, a
  natural tactician. Class-obsessed. The cold ENGINE of the corps: designs the
  Code, keeps the working power as vice-commander, feeds Kondō's fame on purpose
  (at the Ikedaya he holds the ground floor so Kondō's name grows). His cruelty
  is matter-of-fact; his one soft spot is his SECRET HAIKU (pen-name Hōgyoku),
  which only Okita knows. Now believes himself a man who "can hold no love."
- KONDŌ ISAMI: warm, plain, big-jawed Bushū farmer's son; slow to surprise,
  generous, believes in 気組. Supreme commander in name; learning his letters.
  Weeps easily; calls Toshizō "Toshi." Bushū dialect. At the Ikedaya he leads
  the charge with five men and boasts of it in real letters home (kept). His
  sword is the Kotetsu. Toshizō props him up and works him from below.
- OKITA SŌJI: 20 to 22, Edo-born, the corps' finest blade. Bright, boyish, glib,
  teasing, needles Toshizō, clowns near danger, cool as ice in a fight. Quick
  Edo tongue, contracts freely. The ONE person who knows Toshizō's haiku and
  teases him for them. His CONSUMPTION shows from ch16 (the cough); watch it. At
  the Ikedaya he is lethal (cuts Yoshida Toshimaro, wounds Miyabe).
- YAMANAMI KEISUKE: the eldest ex-Shieikan man, learned Sendai adept; educated,
  controlled, faintly stiff and formulaic, a sincere expel-the-barbarian
  idealist. Toshizō despises him. In B05 promoted to GENERAL SECRETARY (総長, a
  grand empty title with no command; Shiba's staff-not-line). Now openly
  resents Toshizō, and is somewhat SYMPATHETIC TO CHŌSHŪ. His gentleness will
  destroy him (seppuku, 1865 — approaching). His stiffness is DELIBERATE
  register, not drift.
- HARADA SANOSUKE: hot-blooded Iyo spearman, risen from chūgen stock, a
  belly-scar from an old half-botched suicide; rough, animal-loyal to Kondō,
  quick to tears and to a fight, close-mouthed, a dry cackle. In the Ikedaya
  fight he is at the front door.
- SHICHIRI KENNOSUKE: the early antagonist, an iai master, fleshy jowls, cold
  mocking eyes, a RUSTY voice. Has Chōshū ties (his mother's people were Chōshū
  foot-guards) and frequents the Kawaramachi Chōshū residence. In B05 he steps
  out of the dark at Nijōhanjiki-chō, fights Toshizō, and ESCAPES AGAIN (ch20-21,
  "you and I are made never to get on"). He is grown shrewder, a debater now, no
  longer a mere cudgel-bully. STILL AT LARGE. Watch for his return.
- OSAE (佐絵 / お佐絵): the Fuchū shrine-daughter Toshizō loved in Bushū. In B05
  revealed as a LOYALIST GO-BETWEEN in Kyoto: a fallen Kujō waiting-woman who
  now shelters rōnin behind the Great Buddha, changes men, brokers court
  contacts, and set the Nijōhanjiki-chō trap. Brisk Bushū speech even now. Her
  tie to Shichiri and the plotters is live; she may recur.
- KATSURA KOGORŌ (= Kido Takayoshi): the Chōshū Kyoto resident-agent, cool,
  lucky past belief ("Kogorō the bolter"). In B05 he ESCAPES the Ikedaya by
  chance and lets Yoshida's party die to save the residence. A recurring
  survivor; his diary is quoted as real.
- SERIZAWA KAMO, NIIMI NISHIKI, KIYOKAWA HACHIRŌ: all DEAD (before B05). Do not
  revive as living voices.

## Renderings settled / carry-forward

- Title "Burn, O Sword!"; author Shiba Ryōtarō. Names Japanese order, macrons.
- ONE rendering per referent, all in glossary.json (198 rows). Enforced by
  check_content (people/places proper names) and qc_entities (all keys length
  >= 2). RENDER THE DECIDED FORM VERBATIM: e.g. 旗本 -> "hatamoto", 石田散薬 ->
  "Ishida Powder", or the checks flag it.
- B05 settled forms. Terms: 局中法度 "the Code of the Corps"; 総長 "general
  secretary" (Yamanami's post; NOT glossaried as a key to avoid case churn, but
  this is the fixed rendering); 見廻組 "the Mimawarigumi"; 虎徹 "Kotetsu";
  和泉守兼定 "Izumi-no-kami Kanesada". People: Osae (佐絵/お佐絵), Hayato,
  Tamesaburō, Sangetsutei Sekiha, Natsume Seibi, Matsubara-an Seifu; Iemochi
  (家茂), Sakai Hyōgo; Furutaka (古高, bare-surname en), Kishibuchi Heisuke,
  Shikokuya (Jūbei), Shimada Kai, Kawashima Katsuji, Hayashi Shintarō, Shūhei,
  Watanabe Kōemon, Risuke, Kumasaka Chōhan; Yoshida Toshimaro, Miyabe Teizō,
  Matsuda Jūsuke, Kitazoe Yoshimaro, Mochizuki Kameyata, Tokoroyama (野老山,
  Gokichirō), Ōtaka Matajirō, Tamamushi Sadayū, Sōbei, Okuzawa Shinzaburō, Andō
  Hayatarō, Nitta Kakuzaemon, Yamada Nobumichi. Places: Takeyamachi,
  Nijōhanjiki-chō, the Bukkō-ji, the Hōkyō-ji, the Kamo River, Muromachi, the
  Great Buddha; the Honkoku-ji, Sanjō-kobashi, Kōraibashi. Organizations: the
  Yoshikago, the Masuya, the Ibarakiya, the Tantora (丹虎, read Tantora), the
  Ikedaya. Era-year form kept with the numeral ("the first year of Genji").
  Shiba's own modern intrusions KEPT.
- COVER: keep data/figs/embed0009_HD.jpg byte-identical, as book.json sets it.
- Principal Characters page flags (unchanged): Hijikata (1), Kondō (2), Okita
  (3), Inoue (4), Nagakura (5), Shichiri (6), Harada (7), Katsura (8), Yamanami
  (9), Serizawa (10), Saitō Hajime (11).

## Where the book stands (story)

- ch01 to ch07 (B01 to B02): the Tama-country prologue. Toshizō the rakish
  farmer's son; the Rokusha killing and the Shichiri feud; the core cast
  assembles at the Edo dōjō.
- ch08 to ch13 (B03): Katsura outfences Shichiri; the Hachiōji raid; the 1862
  epidemic ruins the dōjō and drives the company into the Rōshigumi; Toshizō
  buys his Kanesada; in Kyoto at Mibu, Kiyokawa reveals the corps's secret
  imperial purpose, and Toshizō resolves to break away.
- ch14 to ch18 (B04): the founding. The Aizu patronage, the name SHINSENGUMI
  (spring 1863), the Western company organization, the night killings that build
  the corps's name, and the purge of the Serizawa faction (Sept 1863). Kondō
  sole head; Toshizō the cold engine beneath him.
- ch19 to ch23 (B05): consolidation and the great set-piece. Toshizō's secret
  haiku and the reunion with Osae, who proves a loyalist decoy; the honey-trap
  fight where Shichiri returns and escapes. The written CODE OF THE CORPS,
  enforced by seppuku (Sakai Hyōgo the first to die by it), Yamanami shelved as
  general secretary. Then the IKEDAYA INCIDENT (5th of the 6th month, Genji 1 =
  8 July 1864): Furutaka's arms depot found and its master arrested, the force
  split, and Kondō's small party surprising and cutting down the Chōshū-Tosa-
  Higo war-council. The raid makes the Shinsengumi famous across the realm.

## What is NEXT

- B06 = ch24 to ch28 (kickoff above): the aftermath of the Ikedaya. 京師の乱
  (turmoil in the capital); 長州軍乱入 (the KINMON / Hamaguri Gate Incident, the
  Chōshū army's July-1864 attack on the palace); and the entry of ITŌ KASHITARŌ
  (ch26-27), the learned swordsman-ideologue whose faction will later split off;
  慶応元年正月 (New Year, Keiō 1 = 1865). Then B07 ch29-33, B08 ch34-38, B09
  ch39-43, B10 ch44-48, B11 ch49-53, B12 ch54-58, B13 ch59-63, B14 ch64-68,
  B15 ch69-71 back matter + whole-book reconciliation + COMPLETION.

## Open items for the read-through

- ch24 京師の乱 ("Turmoil in the Capital"): the immediate fallout of the Ikedaya;
  watch for the corps's new fame and the Chōshū reaction.
- ch25 長州軍乱入 ("The Chōshū Army Storms In"): the KINMON no HEN / Hamaguri
  Gate Incident (19 July 1864), Chōshū's armed march on the palace and its
  defeat. Fact-check the date, the commanders (Kusaka Genzui dies here; already
  glossaried), the great fire (どんどん焼け), and the Shinsengumi's part.
- ch26-27 伊東甲子太郎 / 甲子太郎、京へ: the recruitment of ITŌ KASHITARŌ (born
  伊東大蔵; note the 甲子太郎 taken in the kinoe-ne year, Genji 1). A learned
  Hokushin Ittō-ryū adept and sonnō ideologue whose Kōdai-ji faction will later
  break with Kondō and be destroyed (the Aburanokōji affair). Consult the
  furigana for his name and his men; fact-check his provenance.
- ch28 慶応元年正月 ("New Year, First Year of Keiō"): the era changes Genji ->
  Keiō (1865). Watch for Yamanami's approaching seppuku (Feb 1865) and Okita's
  worsening cough.

## Environment / traps state

- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches).
- data/src/ and data/src_epub/ are gitignored (regenerate via ingest if empty);
  scene_map.py needs data/src_epub, so re-run ingest before it if empty.
- Scene-break convention: two or more consecutive blank <p><br/></p> inside the
  body = a break; the single pair after the title is only the title/body
  separator. Body-paragraph N (scene_map) = source line N+2. Use scene_map.py.
- PARITY trap, PROVEN again in B05: the source sets every quote, attribution
  (と…いった), and silence (「………」) as its own paragraph, AND a long narration
  can hide a second sentence that belongs to the next source line. B05 misses:
  ch22 merged two narration lines (the "picture afternoon" / "Gion near" pair);
  ch23 dropped ということである and merged the Matsuda lines. make_bilingual's
  count refused each time; a re-read against the source located them. Always
  re-check dense exchanges AND run-on narration for count.
- NUMBER-CHECK traps: teen/tens-elisions (十七、八 etc.), names and PLACE NAMES
  with numerals, and four-char idioms with 万/十/百 (万事, 無二, 何百日, 万々)
  each take a commented noise rule. Real koku/troop/date/measurement figures stay
  in the English word-forms.
- CONTENT/ENTITY trap: render the glossary's decided form verbatim in a
  paragraph that names a glossaried referent; when the source shortens a name,
  the glossary en must be the bare form the text uses (古高 -> "Furutaka"). A
  dropped parenthetical gloss counts as displacement (ch22 (水戸) restored).
- Known failing test, EXPECTED: tests/run_tests.py reports "hook stands down on
  template stub" FAIL (it only passes on the template placeholder kickoff). Not
  a translation gate. All other tests pass.
- All work is on branch claude/burn-o-sword.
