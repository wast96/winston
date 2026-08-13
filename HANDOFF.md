# HANDOFF, Burn, O Sword! (燃えよ剣), Shiba Ryōtarō

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery: every
batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count. Rewrite it at
the end of every batch; always keep the paste-ready kickoff below as its first
section.

## Message to paste into the next chat

```
Burn, O Sword! B09

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then STYLE.md, then book.json. We are translating Burn, O Sword! (燃えよ剣) by Shiba Ryōtarō from a Japanese digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/burn-o-sword; expect the harness to open you on a stray per-task branch and consolidate per CLAUDE.md rule 2. Deliverable out/burn-o-sword.epub.

Batches 1 to 8 are DONE (ch01 to ch38). ch01 is the FROZEN register reference: reference/ch01_ref.md. Run ./setup.sh; if data/src/ is empty re-run scripts/ingest_epub.py source.epub (Japanese-aware: strips furigana, substitutes 8 gaiji, writes reference/furigana_readings.tsv). No source-note stream. Keep the source's own cover (data/figs/embed0009_HD.jpg), reused byte-identical, exactly as book.json already sets it; the commissioner likes it, do not change it. The known failing test "hook stands down on template stub" is EXPECTED (it only passes on the template placeholder kickoff); every other test passes.

Do Batch 9 = ch39 through ch43 (剣の運命 / The Sword's Fate; 大暗転 / The Great Turn; 伏見の歳三 / Toshizō at Fushimi; 鳥羽伏見の戦い・その一 / The Battle of Toba-Fushimi (I); 鳥羽伏見の戦い・その二 / The Battle of Toba-Fushimi (II)), end to end per the CLAUDE.md pipeline, RUN TO COMPLETION. This span carries the ABURANOKŌJI INCIDENT payoff (Itō Kashitarō lured out and killed, and the ambush of the Goryō-eji who came for his body — 1867; fact-check the date, Keiō 3/11/18 = 13 Dec 1867, and the roster), and the OPENING OF THE BOSHIN WAR: the withdrawal from Kyoto to Fushimi/Ōsaka and the BATTLE OF TOBA-FUSHIMI (Keiō 4 / 1868 — fact-check dates, the brocade banner / 錦の御旗, and who fired first). Oyuki continues in the background (she is the invented heroine, flagged at ch32 — handle as fiction, no fact-check of her existence). Do not stop mid-batch except for a genuine blocker or completion. For each chapter:
1. Build data/zh/<id>.txt from data/src with scripts/build_zh.py <id> <srcbase> "<title>" (title line "### <title>" then one body line per non-empty source paragraph, skipping the first two header lines). ch39=43_part0041, ch40=44_part0042, ch41=45_part0043, ch42=46_part0044, ch43=47_part0045. Fix any extractor splits (this source has had none: a narration line ending in 、 before a 「quote」 is the source's own lead-in, handled by the {j} join, NOT a split to merge). Recover scene breaks: the RELIABLE method is to grep the XHTML (data/src_epub/OEBPS/Text/partNNNN.xhtml) for runs of TWO OR MORE consecutive <p><br/></p> in the body and read the text on either side of each run — scripts/scene_map.py reports the same runs by "body paragraph N" but its N has drifted off-by-one against later chapters, so PLACE *** BY TEXT BOUNDARY, not by the reported index (the single pair right after the chapter title is only the title/body separator; a SINGLE <br/> is a paragraph break, not a scene break). Place *** in the reading at those points.
2. Translate to the FROZEN ch01 register. Names Japanese order, surname first, macrons; CONSULT reference/furigana_readings.tsv before romanizing ANY name or word (it caught Rokusha/Momonoi in B02, Yamanami-not-Sannan in B03, Toshima/Mikura/Akazawa/Kujō in B04, Matsubara-an/Yoshimaro/Mizuo/Tantora in B05, Tojima/Makita/Kijima in B06, Akesato/Naomune/Onji Sakon/Hōgyoku in B07, and in B08 caught 花昌町→かしょうちょう KASHŌ-CHŌ, correcting B07's wrong "Hanashō-chō" whole-book — see the cascade note below; also Momonoi Shunzō, Tamako, Kichimatsu, Nui, and the gikun 慶喜→うえさま which is a semantic gloss, NOT phonetic). The source uses EXPRESSIVE gikun furigana (e.g. 将軍→たいじゅ, 京→ここ, 近藤→せんせい, 慶喜→うえさま) which are semantic, NOT phonetic, and must not be romanized. Consult glossary.json (296 rows; then authority.json) first, feeding decided renderings back. Use the {j} display-join marker so a quotation reads inline with its lead-in and attribution; verse lines take {p} (one per line). Keep an exchange one paragraph per speaker turn. Watch parity: every 「…」 quote line, every と…いった attribution line, and every 「………」/「───」 silence is its OWN source paragraph and needs its OWN reading line — B04-B08 each dropped/merged/INVENTED a line at dialogue or narration seams (B08: ch37 INVENTED an extra "Toshizō laughed" between a reply and the following narration; make_bilingual's count caught it, a positional re-read removed it). ALWAYS re-check dense exchanges and run-on narration for count. OBEY STYLE.md (em-dash budget; no scene-primed idioms). Consult the voice sheets below; read the last two pages of ch38's English before starting ch39 (batch seam).
3. Author out/<id>_reading.md (## title, {j}, {p}, ***, blank-separated). Then the battery: bash scripts/check_chapter.sh <id> <srcbase> "<title_en>" runs reading_to_en + make_bilingual (parity refuses on mismatch) + verify_unit (--noise data/noise.txt) + gen_check_config + check_align + check_content + qc_entities + check_apparatus + check_register. Verify each chapter TAIL against the source explicitly (rule 4).
4. Footnotes per the reader model (first-appearance discipline; keep the "NOT re-noted" ledger in PROGRESS.md; note MORE than the glossary row) via apparatus_merge.py (each glossary row MUST carry a "section": people|places|organizations|terms field; the merge nests it and check_apparatus stays clean; render the glossary's DECIDED form verbatim, e.g. 花昌町→"Kashō-chō", 御陵衛士→"the Goryō-eji", 小石川小日向柳町→"Yanagichō in Kohinata, Koishikawa", or qc_entities/check_content flag it; when the source shortens a name give the glossary a bare-surname en, and do NOT key a name that appears in FRAGILE COMPOUNDS — a Kyoto street like 三条通/四条通 is rendered by hand, NOT keyed, or it false-flags; 三条大橋 renders "Sanjō Great Bridge" like the ch15 四条大橋). A NOTE ANCHOR must be a verbatim substring of the reading file with LITERAL macrons (ō, not sh&#333;gi) AND literal straight quotes/apostrophes (anchor a phrase WITHOUT embedded " or ' when you can — pick a clean run of words); note BODIES use numeric character references for &-entities. Any figure from data/figs/ with a translated caption and real alt text (ch24-38 had none).
5. check_register.py --ref reference/ch01_ref.md out/<id>_reading.md; record in PROGRESS.md. If a chapter flags STILTED, add contractions to the INFORMAL speakers (Toshizō's blunt dialect, Kondō's intimate Bushū) ONLY — leave deliberately formal registers (Itō's set-piece debate, a ceremonial official, quoted documents/memoir) alone (ch33, ch36 needed this). The em-dash rate rides high in debate/interrupted-dialogue chapters (ch36 hit 16.8); convert discretionary dash-asides to commas/parentheses (Shiba's own （）glosses should be parentheses, not dashes) but KEEP the source's ── interruptions and legitimate matched pairs. Fact-check historical claims against real scholarship (never LLM-sourced; IGNORE Grok/Grokipedia), verdict in the note. Add numeral-noise rules to data/noise.txt as new numbered names/idioms/place-names appear (comment each; never noise a real quantity; use spelled forms the checker parses — "a hundred or so", and for 3-digit tallies "one hundred and two" NOT "a hundred and two"; a romanized place/name whose kanji carries a numeral, e.g. 一ツ橋/二十騎町, needs a noise rule because the digit vanishes).
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/burn-o-sword.epub); record ALL check results and EVERY digitization glitch in PROGRESS.md; update HANDOFF.md; commit and push to claude/burn-o-sword.

End the batch with BOTH chat deliverables (CLAUDE.md rule 1, enforced by the Stop hook): the built EPUB ATTACHED in the chat AND the Batch 10 kickoff PASTED VERBATIM in a fenced code block. Batch 10 = ch44 through ch48.

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
- B08 = ch34 to ch38, COMPLETE. ch34 与兵衛の店 / "Yohei's Place" (the Itō faction
  plots Toshizō's murder at Kaikō-ji; Shichiri offers to do it; the trap set at
  Yohei's night sake-shop), ch35 二条中洲の決闘 / "The Duel at Nijō Nakasu"
  (Toshizō KILLS Shichiri Kennosuke and cuts his way out; Okita rides to the
  rescue; the dying ambusher is Osae's lover, names Itō), ch36 菊章旗 / "The
  Chrysanthemum Banner" (the ITŌ SPLIT: the confrontation at the Kōshō-ji
  mansion, Tōdō Heisuke revealed as a defector, Shinohara's memoir quoted; the
  Goryō-eji formed at Kōdai-ji under the chrysanthemum crest; Saitō kills the
  deserter Takeda), ch37 お雪と / "With Oyuki" (Toshizō and Oyuki become lovers;
  the corps made hatamoto/Great Guard; the plan to lure and kill Itō is formed;
  Saitō Hajime planted as a spy in the Goryō-eji), ch38 江戸日記 / "Edo Diary"
  (Toshizō rides to Edo as a grand hatamoto, recruits, visits home, refuses a
  marriage; the Taisei Hōkan happens unbeknownst; he returns to a storm-dark
  Kyoto). Notes 235 to 272 (38 this batch). All checks green; qa_epub PASS
  (272/272/272); epubcheck 0/0/0/0. Continuous note number now 272. Glossary 296
  rows. 38 of 71 chapters translated. See PROGRESS.md B08 for the full record:
  the 花昌町→Kashō-chō whole-book correction, the ch37 invented-line miss, the
  ch38 Yanagichō glossary-form fix, the ch38 noise rules, and the seven
  fact-check verdicts.

## Tooling in place (do NOT revert)

- ingest_epub.py: Japanese-aware (furigana strip, 8 gaiji via
  data/gaiji_map.json, dumps reference/furigana_readings.tsv). From Step 0.
- data/gaiji_map.json: 遼 茨 頤 葛 芦, plus レ (kaeriten) and 㝎 (之定 variant).
- DISPLAY JOIN MARKER {j} (B01, whole-book): a reading line prefixed "{j} " is
  merged onto the preceding display paragraph at BUILD time. Chains. VERSE MARKER
  {p} (one per verse line, indented italic); also {v}/{d}/{g} for
  vignette/dateline/hourgloss. All are stripped by the parity/number/entity/
  content checks.
- scripts/scene_map.py: reports 2+ <p><br/></p> runs, BUT its "body paragraph N"
  index has drifted off-by-one on later chapters. RELIABLE method: grep the XHTML
  for the <br/> runs and place *** by the TEXT on either side. Needs data/src_epub
  (re-run ingest if empty).
- scripts/reading_to_en.py, check_chapter.sh, apparatus_merge.py, build_zh.py,
  build_reading_epub.py, qa_epub.py — unchanged since B02-B04.
- scripts/qc_entities.py (B03 PATCH): SKIPS single-kanji glossary keys. DO NOT
  REVERT.
- scripts/check_numbers.py PATCHES (target-side only, can only ADD a number):
  B04 reads "a/one hundred and <ten..nineteen>" (110-119); B07 folds ONES into
  the hundred+low band so "one hundred and two" = 百二 maps (write "one hundred
  and N", NOT "a hundred and N"). Regression tests pass. DO NOT REVERT.
- data/noise.txt (B01 to B08): Japanese name/idiom/place numeral rules, each
  commented. Never noise a real quantity. B08 added: 一ツ橋, 十軒町, 二十騎町,
  四六時中 (all ch38). B04-B07 additions still in place.
- STYLE.md (B01): the house style sheet (em-dash budget; scene-primed idioms).
  READ IT each batch; add to it when the commissioner corrects a line. No new
  rule in B08.
- reference/ch01_ref.md (B01): the FROZEN register reference. Do not edit.

## Voice sheets (one per major character; consult at every dialogue scene)

- NARRATOR: third person, wry and knowing, fond of the aside and the forward
  glance to events years ahead. Long descriptive sentences alternating with very
  short flat ones. KEEPS Shiba's own modern parentheticals (Western dates;
  present-day place-names; quoted real letters/diaries/memoirs — Nagakura,
  Tanaka Mitsuaki (ch32), Shinohara's split memoir (ch36), the Satō-house
  traditions (ch38)) AND his bracketed editorial glosses INSIDE dialogue and
  quotes (（紅葉の名所）, （利通）, （近藤・土方）, etc.). KEEP them all — render as
  parentheses (preferred, matches his （）) or square-bracket glosses in quoted
  documents.
- HIJIKATA TOSHIZŌ ("Toshi"): the hero, now 33 (ch38). Rough Bushū farm dialect
  off guard, contracted and blunt. Cool, laconic, a dandy, a natural tactician,
  class-obsessed, the cold ENGINE of the corps; cruelty matter-of-fact. Secret
  haiku (pen-name Hōgyoku 豊玉, known to Okita). Now hatamoto — a CAPTAIN OF THE
  GREAT GUARD (大御番組頭) since Keiō 3/6. OYUKI is now his LOVER (ch37 the
  consummation; he shows her a tenderness no one else sees). He has KILLED
  Shichiri (ch35). He plans to lure and kill Itō (ch37). His softness has made
  his reputation "grow" (ch38). Refuses marriage: "I have work to do — the
  Shinsengumi." Sword: 和泉守兼定 (Izumi-no-kami Kanesada) + wakizashi 堀川国広
  (Horikawa Kunihiro).
- KONDŌ ISAMI: warm, plain, big-jawed Bushū farmer's son; Bushū dialect; weeps
  easily; calls Toshizō "Toshi". GROWN VAIN (a mansion at Ushigome Nijikki-chō, a
  redeemed Osaka tayū Miyuki, teahouse wine with liaison officers). Now a
  COMMANDER OF THE GREAT GUARD (大御番組頭取). Resolved to apply the Code to Itō
  (ch33) and did — Takeda killed, Itō to come. Sword: the Kotetsu (長曾禰虎徹).
- OKITA SŌJI: 22-24, the finest blade; bright, glib, teasing, cool in a fight;
  knows Toshizō's haiku and heart; a picky eater. His CONSUMPTION is now grave —
  bedridden half the month (ch38); Toshizō doses him with the family medicine
  "Koryōsan". He rode to Toshizō's rescue at Nijō Nakasu (ch35) in a shrill panic
  rare for him.
- YAMANAMI KEISUKE: DEAD (ch29 seppuku). Do not write as a living voice.
- ITŌ KASHITARŌ: pale, handsome, refined, an actor's looks; Kokugaku scholar and
  Hokushin Ittō-ryū master; topple-the-shogunate ideologue. SPLIT from the corps
  (ch36): formed the GORYŌ-EJI (Guards of the Imperial Tomb) at Kōdai-ji Gettsuin
  under the chrysanthemum crest, funded by Satsuma (Ōkubo, Kirino). Educated Edo
  speech, "-kun"/"-san", set-piece debate register (formal, no forced
  contractions). He is MARKED FOR DEATH — Toshizō's plan (ch37) is to lure him
  out alone. The ABURANOKŌJI killing is B09's payoff. His faction now: Shinohara
  Tainoshin, brother Suzuki Mikisaburō, Tōdō Heisuke (revealed ch36), Mōnai
  Arinosuke (Kenmotsu), Arai Tadao, Kanō Michinosuke, Nakanishi Noboru, Utsumi
  Jirō, Tomiyama Yahei, Hattori Takeo, Sano Shimenosuke. (Saitō Hajime is INSIDE
  it as Toshizō's SPY.)
- OYUKI (お雪, given name Yuki): the HEROINE, WHOLLY INVENTED (Shiba's afterword;
  flagged at ch32). Edo-born samurai widow (of the fictional Ōgaki foot-guard
  Kada Shinjirō), a painter (art-name Kōka) of the Shijō-Maruyama school; her
  father an Edo jōfu foot-guard (okachi); she paints only hydrangeas. Register:
  quiet, few wasted words, quick-witted, CRISP Edo/samurai speech with NO Kyoto
  softness — she COMMANDS rather than coaxes, takes Toshizō up on every word.
  Now his LOVER (ch37). Her homely Edo touch (tatami-iwashi) is what he loves.
  Left-mitsudomoe crest omen shared with Toshizō.
- SAITŌ HAJIME: captain of the Third Unit, the corps' master-of-arms; a comrade
  since Edo. In B08 he KILLED the deserter Takeda Kanryūsai (ch36), then
  "bolted" to Itō's Goryō-eji — a PLANT, Toshizō's spy inside it (ch37). Terse.
- HARADA SANOSUKE: hot-blooded Iyo spearman, risen from chūgen; a belly-scar from
  an old botched suicide; rough, animal-loyal to Kondō.
- SHICHIRI KENNOSUKE: DEAD (ch35 — Toshizō cut him from brow to chin at Nijō
  Nakasu). The early antagonist (iai master, rusty kan-high voice, Chōshū ties)
  is finished. Do not revive.
- OSAE (佐絵 / お佐絵): the Fuchū shrine-daughter who betrayed Toshizō. Her lover
  in the ch35 ambush (Kasama Kijūrō) died naming Itō. Her tie to the plot is
  spent with Shichiri dead, but she may recur.
- TŌDŌ HEISUKE: jaunty Edo townsman (legend: a by-blow of Lord Tōdō of Tsu),
  Hokushin Ittō-ryū, loved by Kondō/Toshizō as one of their own — now REVEALED as
  a founding schemer of the Itō split (ch36). In the Goryō-eji. Ahead:
  Aburanokōji.
- KATSURA KOGORŌ (= Kido Takayoshi), SERIZAWA KAMO, NIIMI NISHIKI, KIYOKAWA
  HACHIRŌ: the last three DEAD; Katsura the recurring Chōshū survivor.

## Renderings settled / carry-forward

- Title "Burn, O Sword!"; author Shiba Ryōtarō. Names Japanese order, macrons.
- ONE rendering per referent, all in glossary.json (296 rows). RENDER THE DECIDED
  FORM VERBATIM: 旗本 "hatamoto", 京都守護職 "the Kyoto Protector", 参謀 "staff
  officer", 助勤 "jokin", 監察 "inspector", 局中法度 "the Code of the Corps",
  外島機兵衛 "Toshima Kihee", 常州 "Hitachi" (NOT Jōshū; 上州 is Jōshū),
  堀川国広 "Horikawa Kunihiro", 和泉守兼定 "Izumi-no-kami Kanesada", 御陵衛士
  "the Goryō-eji", 高台寺 "Kōdai-ji", 花昌町 "Kashō-chō", 小石川小日向柳町
  "Yanagichō in Kohinata, Koishikawa", 新徴組 "the Shinchōgumi", 見廻組 "the
  Mimawarigumi".
- B08 settled forms. People: Arai Tadao, Kanō Michinosuke (加納鵰雄 roster variant),
  Nakamura Hanjirō (= Kirino Toshiaki), Yohei, Kasama Kijūrō, Mōnai Arinosuke
  (Kenmotsu), Tomiyama Yahei, Ōkubo Ichizō (= Toshimichi), Hata Shigechika
  (秦林親, Shinohara's post-Restoration name), Tamesaburō, Daisaku/Ryōjun (brother),
  Kichimatsu, Nui (niece), Okoto, Otsune/Tamako (Kondō's wife/daughter), Rintarō
  & Omitsu (Okita's brother-in-law/sister). Rendered inline, NOT keyed (appear in
  built chapters, avoid cascade): 慶喜 "Yoshinobu", 桃井 "Momonoi". Places:
  Sennyū-ji, Kaikō-ji, Takahata Fudō, Gettsuin, Nijō Nakasu/riverbed, Kashō-chō.
  Terms: the Goryō-eji, the Kiheitai, Ishida Powder / Koryōsan, tatami-iwashi.
- KYOTO STREETS use "the X avenue" / render by hand, NOT glossary-keyed (fragile
  compounds): the Bōjō/Sanjō avenue, Horikawa Avenue, the Aburanokōji,
  Higashi-no-tōin, Nishi-no-tōin, Takoyakushi, etc. 三条大橋 = "Sanjō Great
  Bridge" (like ch15's 四条大橋 "Shijō Great Bridge").
- Era-year form kept with the numeral ("the second year of Keiō", "Keiō 3").
  Shiba's own modern intrusions and bracketed glosses KEPT.
- COVER: keep data/figs/embed0009_HD.jpg byte-identical, as book.json sets it.
- Principal Characters page flags: Hijikata (1), Kondō (2), Okita (3), Inoue (4),
  Nagakura (5), Shichiri (6), Harada (7), Katsura (8), Yamanami (9), Serizawa
  (10), Saitō Hajime (11), OYUKI (12).

## Where the book stands (story)

- ch01-ch07 (B01-B02): the Tama-country prologue; the core cast assembles.
- ch08-ch13 (B03): the dōjō ruined by epidemic; the Rōshigumi; Kyoto at Mibu.
- ch14-ch18 (B04): the founding; the name SHINSENGUMI (1863); the Serizawa purge.
- ch19-ch23 (B05): the CODE OF THE CORPS; the IKEDAYA INCIDENT (1864).
- ch24-ch28 (B06): the KINMON / HAMAGURI GATE INCIDENT; Kondō's vanity; ITŌ
  recruited; YAMANAMI deserts (New Year, Keiō 1).
- ch29-ch33 (B07): YAMANAMI'S SEPPUKU; the French-model recast, Itō made staff
  officer; the Osae betrayal; OYUKI enters; the Satchō alliance; Itō turns to
  討幕; Kondō resolves to apply the Code to Itō.
- ch34-ch38 (B08): the Itō faction plots Toshizō's death; Toshizō KILLS SHICHIRI
  at Nijō Nakasu; the ITŌ SPLIT — the Goryō-eji formed at Kōdai-ji under the
  chrysanthemum crest, backed by Satsuma; Takeda killed by Saitō (who then
  plants himself in the Goryō-eji as a spy); OYUKI becomes Toshizō's lover;
  Toshizō made a Great-Guard hatamoto; his Edo journey and the marriage he
  refuses; the TAISEI HŌKAN (Yoshinobu returns power, 14 Oct 1867) reaches him at
  Odawara; he returns to a storm-dark Kyoto. Toshizō's plan: lure Itō out alone.

## What is NEXT

- B09 = ch39 to ch43 (kickoff above): 剣の運命 / 大暗転 / 伏見の歳三 /
  鳥羽伏見の戦い・その一 / ・その二. The ABURANOKŌJI killing of Itō and the
  ambush of the Goryō-eji, then the withdrawal to Fushimi and the BATTLE OF
  TOBA-FUSHIMI (opening of the Boshin War, Jan 1868). Then B10 ch44-48, B11
  ch49-53, B12 ch54-58, B13 ch59-63, B14 ch64-68, B15 ch69-71 back matter +
  whole-book reconciliation + COMPLETION.

## Open items for the read-through (B09)

- ABURANOKŌJI: fact-check the Aburanokōji Incident date (Keiō 3/11/18 = 13 Dec
  1867), how Itō was lured (a farewell party) and killed, and the ambush of the
  Goryō-eji who came for the body (Tōdō Heisuke dies there; Shinohara escapes).
  Watch the faction roster and Saitō's role as the inside informer.
- TOBA-FUSHIMI: fact-check the battle dates (Keiō 4/1/3 onward, Jan 1868), the
  錦の御旗 (imperial brocade banner) that turned the shogunal army into "rebels",
  and who fired the first shot. Watch parity in the battle set-pieces (ch42-43).
- 大暗転 (ch40, "The Great Turn") — likely the political collapse after the
  Taisei Hōkan / the Ōsei Fukko coup (王政復古, 3 Jan 1868); fact-check.
- Oyuki recurs in the background — keep her crisp Edo/samurai register.

## Environment / traps state

- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches).
- data/src/ and data/src_epub/ are gitignored (regenerate via ingest if empty);
  scene-break detection needs data/src_epub, so re-run ingest before it if empty.
- SCENE BREAKS: place *** BY TEXT BOUNDARY (grep XHTML for 2+ <p><br/></p> runs);
  scene_map.py's index drifts. Single <br/> = paragraph break; the pair after the
  title = title/body separator.
- PARITY trap (PROVEN in B04-B08): every quote, attribution (と…いった), and
  silence (「………」/「───」) is its own paragraph; a narration lead-in ending in
  、 before a quote is its own line too. B08 NEW failure mode: ch37 INVENTED an
  extra "Toshizō laughed" between a reply and the following narration (191 vs 190;
  make_bilingual refused; a positional re-read removed it). Never add a beat the
  source does not have. ALWAYS re-check dense exchanges AND run-on narration.
- NUMBER-CHECK traps: a romanized name/place whose kanji carries a numeral needs
  a commented noise rule because the digit VANISHES (B08: 一ツ橋, 十軒町, 二十騎町,
  四六時中). 一 rendered as "a/one/single" resolves without noise; real
  koku/troop/date/age/measure figures stay in word-form; write 3-digit tallies
  "one hundred and two" (checker keys on "one"/digits).
- CONTENT/ENTITY trap: render the glossary's DECIDED form verbatim or it flags —
  B08 caught 小石川小日向柳町 (must be "Yanagichō in Kohinata, Koishikawa", not a
  fresh romanization) and dropped-name attributions (お雪→"she" must stay
  "Oyuki"). Do NOT key a name in a FRAGILE COMPOUND. SUBSTRING collisions both
  ways (お佐絵 contains 佐絵).
- GLOSSARY CASCADE: adding a global key re-checks EVERY built chapter. Before
  adding, grep data/zh for the key; if an old chapter rendered it differently,
  match the old form OR edit the old chapter + re-derive + rebuild. B08 did this
  for 花昌町: the furigana glosses it かしょうちょう (Kashō-chō), so B07's
  "Hanashō-chō" was WRONG — corrected whole-book (ch31, ch33 readings edited,
  en.json re-derived, 花昌町 keyed "Kashō-chō", rebuilt; no "Hanashō" remains).
  ALWAYS consult the furigana before romanizing, even a place you think you know.
- REGISTER: if STILTED, contract the INFORMAL speakers only (Toshizō's dialect,
  Kondō's intimate Bushū); leave formal registers alone (Itō's debate, a
  ceremonial official, quoted documents/memoir — ch33, ch36). Em-dash rate rides
  high in debate/interrupted chapters; convert discretionary dash-asides to
  commas/parentheses (Shiba's （）glosses → parentheses) but keep the source's ──
  interruptions and legitimate matched pairs.
- NOTE-ANCHOR trap: the anchor must be a verbatim substring of the reading with
  LITERAL macrons AND literal straight quotes/apostrophes; pick a clean run of
  words WITHOUT embedded " or ' when possible. Note bodies use numeric refs for
  &-entities only.
- Known failing test, EXPECTED: tests/run_tests.py reports "hook stands down on
  template stub" FAIL (template-only). Not a translation gate. All other tests
  pass.
- All work is on branch claude/burn-o-sword.
