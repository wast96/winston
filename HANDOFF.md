# HANDOFF, Burn, O Sword! (燃えよ剣), Shiba Ryōtarō

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery: every
batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count. Rewrite it at
the end of every batch; always keep the paste-ready kickoff below as its first
section.

## Message to paste into the next chat

```
Burn, O Sword! B10

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then STYLE.md, then book.json. We are translating Burn, O Sword! (燃えよ剣) by Shiba Ryōtarō from a Japanese digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/burn-o-sword; expect the harness to open you on a stray per-task branch and consolidate per CLAUDE.md rule 2. Deliverable out/burn-o-sword.epub.

Batches 1 to 9 are DONE (ch01 to ch43). ch01 is the FROZEN register reference: reference/ch01_ref.md. Run ./setup.sh; if data/src/ is empty re-run scripts/ingest_epub.py source.epub (Japanese-aware: strips furigana, substitutes 8 gaiji, writes reference/furigana_readings.tsv). No source-note stream. Keep the source's own cover (data/figs/embed0009_HD.jpg), reused byte-identical, exactly as book.json already sets it; the commissioner likes it, do not change it. The known failing test "hook stands down on template stub" is EXPECTED (it only passes on the template placeholder kickoff); every other test passes.

Do Batch 10 = ch44 through ch48 (鳥羽伏見の戦い・その三 / The Battle of Toba-Fushimi (III); 鳥羽伏見の戦い・その四 / The Battle of Toba-Fushimi (IV); 大坂の歳三 / Toshizō at Osaka; 松林 / The Pine Wood; 西昭庵 / Saishō-an), end to end per the CLAUDE.md pipeline, RUN TO COMPLETION. This span carries the REST OF THE BATTLE OF TOBA-FUSHIMI and the GREAT COLLAPSE: the shogunal army's defeat over Keiō 4/1/3–6 (Jan 1868), the raising of the 錦の御旗 (Imperial brocade banner) that made the Tokugawa side "rebels" (朝敵), and then YOSHINOBU'S FLIGHT — his secret abandonment of the army and escape by warship (Kaiyō-maru) from Osaka Castle to Edo on the night of Keiō 4/1/6 (30 Jan 1868). Fact-check: the brocade-banner date and its effect; Yoshinobu's flight and the collapse of shogunal morale; Hayashi Gonsuke's death at Fushimi (he is the 63-year-old Aizu artillery commander introduced in ch43); and any dates/rosters in the battle set-pieces. Oyuki continues in the background (she is the invented heroine, flagged at ch32 — handle as fiction, no fact-check of her existence); she is at the Yutōya inn in Fushimi as of ch41. Do not stop mid-batch except for a genuine blocker or completion. For each chapter:
1. Build data/zh/<id>.txt from data/src with scripts/build_zh.py <id> <srcbase> "<title>" (title line "### <title>" then one body line per non-empty source paragraph, skipping the first two header lines). ch44=48_part0046, ch45=49_part0047, ch46=50_part0048, ch47=51_part0049, ch48=52_part0050. Fix any extractor splits (this source has had none: a narration line ending in 、 before a 「quote」 is the source's own lead-in, handled by the {j} join, NOT a split to merge). Recover scene breaks: the RELIABLE method is to grep the XHTML (data/src_epub/OEBPS/Text/partNNNN.xhtml) for runs of TWO OR MORE consecutive <p><br/></p> in the body and read the text on either side of each run — scripts/scene_map.py reports the same runs by "body paragraph N" but its N has drifted off-by-one against later chapters, so PLACE *** BY TEXT BOUNDARY, not by the reported index (the single pair right after the chapter title is only the title/body separator; a SINGLE <br/> is a paragraph break, not a scene break). Place *** in the reading at those points.
2. Translate to the FROZEN ch01 register. Names Japanese order, surname first, macrons; CONSULT reference/furigana_readings.tsv before romanizing ANY name or word (it has caught readings whole-book, e.g. B08's 花昌町→Kashō-chō and B09's 野津鎮雄→Shizuo, 野津道貫→Michitsura, 椎原→Shiihara). The source uses EXPRESSIVE gikun furigana (e.g. 将軍→たいじゅ, 京→ここ, 近藤→せんせい, 慶喜→うえさま) which are semantic, NOT phonetic, and must not be romanized. Consult glossary.json (299 rows; then authority.json) first, feeding decided renderings back. Use the {j} display-join marker so a quotation reads inline with its lead-in and attribution; verse lines take {p} (one per line). Keep an exchange one paragraph per speaker turn. Watch parity: every 「…」 quote line, every と…いった attribution line, and every 「………」/「───」 silence is its OWN source paragraph and needs its OWN reading line — earlier batches each dropped/merged/INVENTED a line at dialogue or narration seams; make_bilingual's count catches it, a positional re-read fixes it. ALWAYS re-check dense exchanges and run-on narration for count. OBEY STYLE.md (em-dash budget; no scene-primed idioms). Consult the voice sheets below; read the last two pages of ch43's English before starting ch44 (batch seam).
3. Author out/<id>_reading.md (## title, {j}, {p}, ***, blank-separated). Then the battery: bash scripts/check_chapter.sh <id> <srcbase> "<title_en>" runs reading_to_en + make_bilingual (parity refuses on mismatch) + verify_unit (--noise data/noise.txt) + gen_check_config + check_align + check_content + qc_entities + check_apparatus + check_register. Verify each chapter TAIL against the source explicitly (rule 4).
4. Footnotes per the reader model (first-appearance discipline; keep the "NOT re-noted" ledger in PROGRESS.md; note MORE than the glossary row) via apparatus_merge.py (each glossary row MUST carry a "section": people|places|organizations|terms field AND a "pinyin" field — qc_entities crashes on a row without "pinyin"; set pinyin = the romanized en. The merge nests the section and check_apparatus stays clean; render the glossary's DECIDED form verbatim, e.g. 御香宮→"Gokō-no-miya", 林権助→"Hayashi Gonsuke", 花昌町→"Kashō-chō", 御陵衛士→"the Goryō-eji", or qc_entities/check_content flag it; when the source shortens a name give the glossary a bare-surname en, and do NOT key a name that appears in FRAGILE COMPOUNDS — a Kyoto/Fushimi street like 三条通/京町通 is rendered by hand, NOT keyed, or it false-flags). A NOTE ANCHOR must be a verbatim substring of the reading file with LITERAL macrons (ō, not sh&#333;gi) AND WITHOUT embedded straight quotes/apostrophes (pick a clean run of words — an English possessive like "Magistrate's" or a "…"-wrapped phrase will not anchor cleanly); note BODIES use literal Unicode but numeric character references for any &-entity. Any figure from data/figs/ with a translated caption and real alt text (ch24-43 had none).
5. check_register.py --ref reference/ch01_ref.md out/<id>_reading.md; record in PROGRESS.md. If a chapter flags STILTED, add contractions to the INFORMAL speakers (Toshizō's blunt dialect, Kondō's intimate Bushū) ONLY — leave deliberately formal registers (a ceremonial official, quoted documents/memoir, a set-piece political analysis) alone. Battle/narration chapters run em-dash LOW and dialogue-light (B09 ran 5.8–12.0/1k, all under the ch01 ref 12.7); keep the source's ── interruptions and legitimate matched pairs, convert discretionary dash-asides to commas/parentheses (Shiba's own （）glosses → parentheses). Fact-check historical claims against real scholarship (never LLM-sourced; IGNORE Grok/Grokipedia), verdict in the note. Add numeral-noise rules to data/noise.txt as new numbered names/idioms/place-names appear (comment each; never noise a real quantity; use spelled forms the checker parses — but write LARGE composite tallies as DIGITS, e.g. "16,400", because the checker does NOT compose "sixteen thousand four hundred" into one value; write 3-digit tallies "one hundred and fifty" NOT "a hundred and fifty"; a romanized place/name whose kanji carries a numeral, e.g. 四ツ塚/平六郎, needs a noise rule because the digit vanishes; and 十倍 must be "ten times", not "tenfold", so the checker sees "ten").
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/burn-o-sword.epub); record ALL check results and EVERY digitization glitch in PROGRESS.md; update HANDOFF.md; commit and push to claude/burn-o-sword.

End the batch with BOTH chat deliverables (CLAUDE.md rule 1, enforced by the Stop hook): the built EPUB ATTACHED in the chat AND the Batch 11 kickoff PASTED VERBATIM in a fenced code block. Batch 11 = ch49 through ch53.

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
- B06 = ch24 to ch28, COMPLETE. Notes 181 to 208.
- B07 = ch29 to ch33, COMPLETE. Notes 209 to 234.
- B08 = ch34 to ch38, COMPLETE. Notes 235 to 272.
- B09 = ch39 to ch43, COMPLETE. ch39 剣の運命 / "The Sword's Fate" (the
  ABURANOKŌJI INCIDENT: Itō lured to Kondō's and speared/cut down; the body left
  as bait; the Goryō-eji ambushed retrieving it — Tōdō Heisuke, Hattori Takeo,
  Mōnai Kenmotsu killed; Nagakura's futile mercy to Tōdō), ch40 大暗転 / "The
  Great Turn" (Kondō unravels; the ŌSEI FUKKO / 王政復古; Toshizō's
  sword-and-fidelity creed to the dying Okita; Yoshinobu withdraws to Osaka; the
  corps sent to hold Fushimi; the last night in Kyoto and Toshizō's tears),
  ch41 伏見の歳三 / "Toshizō at Fushimi" (Fushimi geography; the new-modelled
  Chōshū army marches past; Toshizō glimpses OYUKI and loses her in an alley;
  Oyuki's interiority; KONDŌ SHOT at Sumizome by the Itō remnants; command passes
  to Toshizō), ch42 鳥羽伏見の戦い・その一 / "The Battle of Toba-Fushimi (I)" (the
  author visits the razed Fushimi site; MATSUMOTO RYŌJUN; the "lover not
  mistress" exchange; the political machinery — Iwakura, Ōkubo, the 討薩表; the
  Osaka-siege parallel; the eve of battle), ch43 鳥羽伏見の戦い・その二 / "(II)"
  (New Year vigil; the Meiji-general roll-call; HAYASHI GONSUKE and the Aizu
  Asobi/ju children's precepts; NOZU'S FIRST SHOT opens the Boshin War, ~5 p.m.
  Keiō 4/1/3 = 27 Jan 1868). Notes 273 to 310 (38 this batch). All checks green;
  qa_epub PASS (310/310/310); epubcheck 0/0/0/0. Continuous note number now 310.
  Glossary 299 rows. 43 of 71 chapters translated. See PROGRESS.md B09 for the
  full record: the noise additions and number-fixes, the pinyin-field fix for the
  3 new glossary rows, and the six fact-check verdicts (Aburanokōji date,
  Ōsei Fukko, Toba-Fushimi first shot, brocade banner, Matsumoto Ryōjun's
  Ōiso-not-Zushi correction, the Meiji generals).

## Tooling in place (do NOT revert)

- ingest_epub.py: Japanese-aware (furigana strip, 8 gaiji via
  data/gaiji_map.json, dumps reference/furigana_readings.tsv). From Step 0.
- data/gaiji_map.json: 遼 茨 頤 葛 芦, plus レ (kaeriten) and 㝎 (之定 variant).
- DISPLAY JOIN MARKER {j} (B01, whole-book): a reading line prefixed "{j} " is
  merged onto the preceding display paragraph at BUILD time. Chains. VERSE MARKER
  {p} (one per verse line, indented italic); also {v}/{d}/{g} for
  vignette/dateline/hourgloss. All are stripped by the parity/number/entity/
  content checks. reading_to_en.py counts BY LINE (one content line per source
  body line); {j}/{p}/*** lines and the ## title are handled/skipped.
- scripts/scene_map.py: reports 2+ <p><br/></p> runs, BUT its "body paragraph N"
  index has drifted off-by-one on later chapters. RELIABLE method: grep the XHTML
  for the <br/> runs and place *** by the TEXT on either side. Needs data/src_epub
  (re-run ingest if empty).
- scripts/reading_to_en.py, check_chapter.sh, apparatus_merge.py, build_zh.py,
  build_reading_epub.py, qa_epub.py — unchanged since B02-B04.
- scripts/qc_entities.py (B03 PATCH): SKIPS single-kanji glossary keys. DO NOT
  REVERT. NOTE: it requires every glossary row to have a "pinyin" field — a row
  added without it raises KeyError. Set pinyin = the romanized en on every new row.
- scripts/check_numbers.py PATCHES (target-side only, can only ADD a number):
  B04 reads "a/one hundred and <ten..nineteen>" (110-119); B07 folds ONES into
  the hundred+low band so "one hundred and two" = 百二 maps. Regression tests
  pass. DO NOT REVERT. Known limits learned in B09: the checker does NOT compose
  "sixteen thousand four hundred" into 16400 (write DIGITS for large composite
  tallies); "tenfold" is not read as 10 (write "ten times"); a 余 between numerals
  (七十余万) splits the run and orphans the tail unit (noise the compound, carry
  the value in words).
- data/noise.txt (B01 to B09): Japanese name/idiom/place numeral rules, each
  commented. Never noise a real quantity. B09 added (all commented): 九郎, 万世,
  四ツ辻 (ch39); 十八史略, 岡目八目 (ch40); 平六郎, 六、七十 (ch41); 八面六臂,
  四天王寺, 七十余万 (ch42); 十中八九, 四ツ塚, 元三郎, 百平 (ch43).
- STYLE.md (B01): the house style sheet (em-dash budget; scene-primed idioms).
  READ IT each batch; add to it when the commissioner corrects a line. No new
  rule in B09.
- reference/ch01_ref.md (B01): the FROZEN register reference. Do not edit.

## Voice sheets (one per major character; consult at every dialogue scene)

- NARRATOR: third person, wry and knowing, fond of the aside and the forward
  glance to events years ahead (B09 flashes forward to the Meiji careers of the
  Toba-Fushimi outpost officers, and to Yoshinobu's 1898 audience). KEEPS Shiba's
  own modern parentheticals (Western dates; present-day place-names; the author's
  own site-visit framing in ch42; quoted real letters/diaries/memoirs — Katsu
  Kaishū's reminiscence and private note in ch40, Shinohara's split memoir in
  ch39) AND his bracketed editorial glosses INSIDE dialogue and quotes (（利通）,
  （観樹）, etc.). KEEP them all — render as parentheses (preferred) or
  square-bracket glosses in quoted documents.
- HIJIKATA TOSHIZŌ ("Toshi"): the hero, ~34 (born into an age of disorder;
  "a bird flying by its own power," strongest in decline). Rough Bushū farm
  dialect off guard, contracted and blunt (おらァ, ねえ, 面白え). Cool, laconic, a
  natural tactician (scouts ground and draws his own maps, then burns them —敵情
  changes). Now SOLE FIELD COMMANDER of the Shinsengumi: Kondō handed him the
  corps after being shot (ch42). His creed (ch40): fidelity/節義 alone, the corps
  a band that will not betray the Tokugawa "down to the last man"; the sword as a
  thing of single purpose. OYUKI is his LOVER, "someone dear to me, not a
  mistress" (ch42); he sent her 150 of his 200 ryō and a letter, would not meet
  her to say goodbye. Secret haiku (pen-name Hōgyoku 豊玉). Sword: 和泉守兼定
  (Izumi-no-kami Kanesada, 二尺八寸) + wakizashi 堀川国広.
- KONDŌ ISAMI: warm, plain, big-jawed Bushū farmer's son; weeps easily; calls
  Toshizō "Toshi". After the Aburanokōji he UNRAVELS (ch40) — dashes about the
  politicians, dreads being "of the rebel army," goes "faint-hearted." SHOT in
  the right shoulder at Sumizome by the Itō remnants (ch41), the shoulder-blade
  cracked; handed the corps to Toshizō and was sent by boat to Osaka for
  Matsumoto Ryōjun's care (ch42). A kite in a fair wind, weak in decline
  (Toshizō's judgment). Sword: the Kotetsu.
- OKITA SŌJI: the finest blade; bright, glib, teasing, cool. His CONSUMPTION is
  now grave — bedridden, wasting, scarcely eating; dosed with the family medicine
  Koryōsan (ch40-41). His clear smile "frightens" Toshizō now. Pledged (ch40),
  "so long as there is life in me I will follow you." SENT TO OSAKA with Kondō
  (ch42); no longer at Fushimi.
- HAYASHI GONSUKE (林権助, given Yasusada): NEW in ch43. The 63-year-old Aizu
  commissioner of artillery, commander of the Aizu contingent at Fushimi; a
  bluff old man of arms, drinks by the bucketful, mimics the Aizu children's
  Asobi/ju precepts when drunk, versed in the Naganuma-ryū. Warm to Toshizō
  ("if you and I fight a hard fight, no enemy can stand"). FACT: killed in the
  Toba-Fushimi fighting — watch for his death in B10.
- ITŌ KASHITARŌ: DEAD (ch39, the Aburanokōji). Do not write as a living voice.
  His faction is broken: Tōdō Heisuke, Hattori Takeo, Mōnai Kenmotsu DIED in the
  ambush; Shinohara Tainoshin, Suzuki Mikisaburō, Kanō Michinosuke, Tomiyama
  Yahei ESCAPED and, with Abe Jūrō and Sahara Tarō, shot Kondō at Sumizome
  (ch41) — they are quartered at the Satsuma residence in Kyoto and may recur.
- OYUKI (お雪, given name Yuki): the HEROINE, WHOLLY INVENTED (Shiba's afterword;
  flagged at ch32). Edo-born samurai widow, a painter (art-name Kōka) of the
  Shijō-Maruyama school; paints only hydrangeas. Register: quiet, few wasted
  words, quick-witted, CRISP Edo/samurai speech with NO Kyoto softness — she
  COMMANDS rather than coaxes. Now Toshizō's LOVER. In B09 she came secretly to
  Fushimi (staying at the Yutōya inn on Kyōmachi-dōri), was nearly seen by
  Toshizō from the watchtower, and resolved to see him once and part — then kept
  missing him. Handle as fiction, no fact-check of her existence.
- SAITŌ HAJIME: captain of the Third Unit; Toshizō's SPY planted inside the
  Goryō-eji (from ch37). Did not surface in B09; still terse, still inside/near
  the Itō remnants' world. Watch for his re-emergence.
- NAGAKURA SHINPACHI: Matsumae-han deserter, Edo-bred, homesick for Edo (ch39);
  captain of the Second Unit (also holds Okita's First). At the Aburanokōji he
  broke ranks to try to save Tōdō (in vain). Led the Second Unit out first at
  Toba-Fushimi (ch43). Steady, capable, a man at peace with death.
- HARADA SANOSUKE: hot-blooded Iyo spearman, simple and animal-loyal to Kondō;
  claps loudest at Kondō's speeches; a belly-scar from an old botched suicide.
- KATSURA KOGORŌ (= Kido Takayoshi): the recurring Chōshū survivor, invoked in
  Katsu's ch40 reminiscence. SERIZAWA, NIIMI, KIYOKAWA, YAMANAMI, SHICHIRI: DEAD.

## Renderings settled / carry-forward

- Title "Burn, O Sword!"; author Shiba Ryōtarō. Names Japanese order, macrons.
- ONE rendering per referent, all in glossary.json (299 rows). RENDER THE DECIDED
  FORM VERBATIM: 旗本 "hatamoto", 御陵衛士 "the Goryō-eji", 高台寺 "Kōdai-ji",
  月真院 "Gettsuin", 花昌町 "Kashō-chō", 見廻組 "the Mimawarigumi", 和泉守兼定
  "Izumi-no-kami Kanesada", 堀川国広 "Horikawa Kunihiro". B09 new keys: 御香宮
  "Gokō-no-miya" (place), 林権助 "Hayashi Gonsuke" (person), 王政復古 "the
  Restoration of Imperial Rule" (term).
- RENDERED INLINE, NOT KEYED (appear in built chapters / fragile compounds,
  avoid cascade or false-flags): 慶喜 "Yoshinobu" (徳川慶喜 "Tokugawa Yoshinobu"),
  家康 "Ieyasu", 大坂 "Osaka", 岩倉 "Iwakura (Tomomi)", 大久保 "Ōkubo (Toshimichi)"
  (glossary 大久保一蔵 Ōkubo Ichizō for the ch-era name), 伏見 "Fushimi", 鳥羽
  "Toba", 桑名 "Kuwana" (keyed), 会津 "Aizu" (keyed). Kyoto/Fushimi STREETS by
  hand: 北小路通 "the Kitakōji avenue", 七条油小路 "Shichijō Aburanokōji", 京町通
  "Kyōmachi-dōri", 竹田街道 "the Takeda Highway", 鳥羽街道 "the Toba Highway".
  B09 one-off historical figures rendered by hand (not keyed): Gotō Shōjirō,
  Nagai Genba-no-kami Naomune, Matsudaira Masakata, Jō Izumi-no-kami, Shimazu
  Shikibu, Yoshii Tomozane/Kōsuke, Nozu Shizuo/Michitsura, Ōyama Yasuke/Iwao,
  Mōri Takumi, Yamada Akiyoshi, Miura Gorō, Tani Tateki, Yamaji Motoharu,
  Takigawa Harima-no-kami, Shiihara Koyata, Ishikawa Hyappei, Ōkawara Shinzō,
  Mutō Katsuzō, Sahara Tarō, Kiyohara Kiyoshi, Toyotomi Hideyori, Sanada
  Yukimura. 毛内監物 rendered "Mōnai Kenmotsu" (glossary key is 毛内有之介 Mōnai
  Arinosuke — same man).
- Era-year form kept with the numeral ("the third year of Keiō", "Keiō 4",
  "the first year of Meiji"). Shiba's own modern intrusions and bracketed glosses
  KEPT.
- COVER: keep data/figs/embed0009_HD.jpg byte-identical, as book.json sets it.
- Principal Characters page flags unchanged (Hijikata 1, Kondō 2, Okita 3, Inoue
  4, Nagakura 5, Shichiri 6, Harada 7, Katsura 8, Yamanami 9, Serizawa 10, Saitō
  Hajime 11, OYUKI 12).

## Where the book stands (story)

- ch01-ch07 (B01-B02): the Tama-country prologue; the core cast assembles.
- ch08-ch13 (B03): the dōjō ruined by epidemic; the Rōshigumi; Kyoto at Mibu.
- ch14-ch18 (B04): the founding; the name SHINSENGUMI (1863); the Serizawa purge.
- ch19-ch23 (B05): the CODE OF THE CORPS; the IKEDAYA INCIDENT (1864).
- ch24-ch28 (B06): the KINMON / HAMAGURI GATE INCIDENT; ITŌ recruited; YAMANAMI
  deserts.
- ch29-ch33 (B07): YAMANAMI'S SEPPUKU; Itō made staff officer; the Osae betrayal;
  OYUKI enters; the Satchō alliance; Itō turns to 討幕.
- ch34-ch38 (B08): the ITŌ SPLIT — the Goryō-eji formed at Kōdai-ji; Toshizō
  kills Shichiri; Saitō planted as a spy; Oyuki becomes his lover; the TAISEI
  HŌKAN reaches him; he returns to a storm-dark Kyoto.
- ch39-ch43 (B09): the ABURANOKŌJI killing of Itō and the ambush of the
  Goryō-eji; Kondō's collapse and the ŌSEI FUKKO; Yoshinobu's withdrawal to
  Osaka; the corps sent to hold Fushimi; Kondō SHOT at Sumizome, command to
  Toshizō; and the OPENING OF THE BOSHIN WAR — Nozu's first shot at Toba,
  Keiō 4/1/3 (27 Jan 1868). The battle is joined; the corps' Second Unit goes
  over the wall into the road.

## What is NEXT

- B10 = ch44 to ch48 (kickoff above): 鳥羽伏見の戦い・その三・その四 / 大坂の歳三
  / 松林 / 西昭庵. The rest of Toba-Fushimi and the GREAT COLLAPSE: the brocade
  banner, the defeat, YOSHINOBU'S FLIGHT by ship from Osaka to Edo. Then B11
  ch49-53, B12 ch54-58, B13 ch59-63, B14 ch64-68, B15 ch69-71 back matter +
  whole-book reconciliation + COMPLETION.

## Open items for the read-through (B10)

- BROCADE BANNER: fact-check the 錦の御旗 (Imperial brocade banner) — raised over
  the Satsuma-Chōshū side on Keiō 4/1/4–5, turning the Tokugawa army into 朝敵
  (rebels/enemies of the Court) and breaking its morale. B09 footnoted its
  imminence at ch43; its full appearance falls in B10.
- YOSHINOBU'S FLIGHT: fact-check his secret abandonment of the army and escape by
  the warship Kaiyō-maru from Osaka Castle to Edo on the night of Keiō 4/1/6
  (30 Jan 1868) — the decisive collapse of the shogunal cause.
- HAYASHI GONSUKE: fact-check his death at Toba-Fushimi (the ch43 Aizu artillery
  commander); watch for it in the battle chapters.
- OYUKI recurs in the background — keep her crisp Edo/samurai register; she was
  at the Yutōya inn in Fushimi (ch41). 西昭庵 (Saishō-an, ch48) may be a
  retreat/hermitage scene — read the source before assuming.

## Environment / traps state

- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches).
- data/src/ and data/src_epub/ are gitignored (regenerate via ingest if empty);
  scene-break detection needs data/src_epub, so re-run ingest before it if empty.
- SCENE BREAKS: place *** BY TEXT BOUNDARY (grep XHTML for 2+ <p><br/></p> runs);
  scene_map.py's index drifts. Single <br/> = paragraph break; the pair after the
  title = title/body separator.
- PARITY trap (PROVEN B04-B09): every quote, attribution (と…いった), and silence
  (「………」/「───」) is its own paragraph; a narration lead-in ending in 、 before a
  quote is its own line too (join it for display with {j} on the FOLLOWING line).
  Never add or drop a beat the source does not have; make_bilingual refuses on a
  count mismatch, a positional re-read fixes it. Re-check dense exchanges AND
  run-on narration.
- NUMBER-CHECK traps (B09 lessons): write LARGE composite tallies as DIGITS
  ("16,400") — the checker does not compose "sixteen thousand four hundred";
  "ten times" not "tenfold" (十倍); "one hundred and fifty" not "a hundred and
  fifty"; a 余 between numerals orphans the unit (noise the compound, carry the
  value in words); a romanized name/place whose kanji carries a numeral needs a
  commented noise rule (B09: 平六郎, 四ツ塚, 元三郎, 百平, 九郎); four-char idioms
  with digits need noise (岡目八目, 八面六臂, 十中八九, 万世). Real
  koku/troop/date/age/measure figures stay in word-form and DO carry the number.
- CONTENT/ENTITY trap: render the glossary's DECIDED form verbatim or it flags.
  Do NOT key a name in a FRAGILE COMPOUND. NEW glossary rows MUST carry both a
  "section" and a "pinyin" field (qc_entities KeyErrors on a row without pinyin).
- GLOSSARY CASCADE: adding a global key re-checks EVERY built chapter. Before
  adding, grep data/zh for the key; if an old chapter rendered it differently,
  match the old form OR edit the old chapter + re-derive + rebuild. B09's 3 new
  keys (御香宮, 林権助, 王政復古) were all new to the book — no cascade.
- REGISTER: battle/narration chapters run em-dash LOW and dialogue-light (noisy
  contraction stats are expected). If STILTED, contract the INFORMAL speakers
  only (Toshizō's dialect, Kondō's intimate Bushū); leave formal registers alone.
- NOTE-ANCHOR trap: the anchor must be a verbatim substring of the reading with
  LITERAL macrons and WITHOUT embedded straight quotes/apostrophes — an English
  possessive ("Magistrate's") or a "…"-wrapped phrase will NOT anchor; pick a
  clean run of words. Note bodies use literal Unicode but numeric refs for any
  &-entity.
- Known failing test, EXPECTED: tests/run_tests.py reports "hook stands down on
  template stub" FAIL (template-only). Not a translation gate. All other tests
  pass.
- All work is on branch claude/burn-o-sword.
