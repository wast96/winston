# PROGRESS: Burn, O Sword! (燃えよ剣), Shiba Ryōtarō

The running per-batch log. One section per batch: what was translated, which
checks ran and what they found, notes and glossary added, and anything flagged
for the read-through.

## Setup

- Source EPUB: 燃えよ剣（新装版）, Bungeishunjū e-book, 2020 (ASIN B086P34MVL).
  Vertical-rl Japanese; heavy furigana; 8 gaiji shipped as images. No author
  footnotes (no source-note stream).
- Ingest: 78 spine documents, 10 images, 349,309 source characters. Japanese-
  aware ingest strips furigana, substitutes the 8 gaiji via data/gaiji_map.json,
  and dumps reference/furigana_readings.tsv (2,025 readings).
- Structure: 68 titled novel chapters (ch01–ch68) + 3 back-matter units. Each
  novel chapter is a single spine document; scene breaks are internal, handled
  by set-off markers, not sections.

## B01 = ch01 「女の夜市」 / "The Women's Night Market" (VOICE GATE)

Scope: chapter 1 only, end to end, stopping at the first-chapter voice gate
(Step 0c). The opening: Hijikata Toshizō as a rakish, dangerous farmer's son in
Bushū Tama, on his way to the Darkness Festival at Fuchū, where he takes a
high-born woman in the dark and lifts her Norishige dagger.

### Checks (all green)

- make_bilingual.py ch01: 160 paragraph pairs (parity true by construction).
- check_numbers.py (--noise data/noise.txt): 160 pairs, 0 unresolved.
- verify_unit.py ch01: parity OK; numbers 0 unresolved; 15 anchors resolve.
- check_align.py ch01: 160/160, median ratio 3.33 en/(kanji+kana), alignment OK.
- check_content.py: 13 glossary names usable; 34 name occurrences, all in the
  paired paragraph (0 displaced).
- check_structure.py: parity OK, anchors OK, headings OK.
- qc_entities.py: 0 entity misses.
- check_apparatus.py: 0 failures, 0 warnings.
- build_reading_epub.py: 1/71 chapters, 15 notes, 0 source notes.
- qa_epub.py: PASS (78 documents, 15 refs/bodies/backlinks, all links resolve).
- epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings.

### Formatting recovered

- Two scene breaks (`***`), after body paragraphs 48 and 115. The source encodes
  a scene break as a run of two consecutive blank paragraphs (`<p><br/></p>`)
  within the body; the single blank pair right after the title is the title/body
  separator and is NOT a break. Verified against part0003.xhtml.
- Emphasis dots (傍点, `<span class="em-sesame">`) on 変りまげ etc. are inline
  emphasis; rendered as natural English, not as a set-off marker (the template
  has no inline-emphasis marker and parity is unaffected).
- No figures in this chapter (no `<img>` in the source).

### Notes added: 15 (continuous numbering 1–15)

Swept across the four domains for a reader with no Japanese background:
Shinsengumi (1), the ri (2), the Ansei era (3), the eighty-eighth night (4), the
samurai topknot as a class marker (5), the nanushi and Satō Hikogorō (6), the
Kurayami/Darkness Festival (7), the traditional hours (8), married Shinshū
clergy (9), Ishida Powder (10), the Ikedaya Affair as a forward reference (11),
tenryō / temple-and-shrine land and the samurai-less Tama country (12), yobai
night-courting (13), the swordsmith Norishige (14), and the Saruwatari priestly
house / court rank / Osae as invention (15).

First-appearance discipline: every note is on a first appearance in the book.
"NOT re-noted" ledger: none yet (ch01 is the first chapter; nothing recurs from
an earlier chapter).

### Fact-check verdicts (against real scholarship, not LLM sources)

- Kurayami Matsuri at the Ōkunitama Shrine (Rokusha Myōjin), Fuchū:
  CORROBORATED as a real festival held late April to early May, historically a
  night procession with the lamps put out ("darkness"). The licentious
  free-for-all is the novel's dramatization, said so in note 7 (not documented
  custom). Sources: Ōkunitama Shrine site; Fuchū city; Japanese Wikipedia.
- Ishida Sanyaku (Ishida Powder): CORROBORATED: a genuine Hijikata-family
  patent remedy, made and peddled ~1704–1948, Toyama-style consignment, several
  hundred customers. Its efficacy is the tradition's claim (note 10). Sources:
  Japanese Wikipedia; Kitatama Pharmacists' Assoc.; Hino tourism.
- Saruwatari (猿渡): CORROBORATED as the hereditary chief-priest house of the
  Ōkunitama Shrine, documented from the 14th century. Osae the sister appears to
  be Shiba's invention (note 15). Sources: Tokyo Jinjachō; Japanese Wikipedia
  (猿渡容盛); Kokugakuin repository.
- Etchū Norishige: CORROBORATED: a real late-Kamakura swordsmith, of the
  Masamune circle (Sōshū tradition); signature grain called matsukawa-hada
  ("pine-bark"), which Shiba renders as a "seaweed" grain (note 14). Genuine
  signed pieces are very few. Sources: Bunka.go.jp heritage DB; Touken World.

### Glossary rows added (nested; status in parentheses)

People: 土方歳三 Hijikata Toshizō (decided, principal), 近藤勇 Kondō Isami
(decided, principal), 佐藤彦五郎 Satō Hikogorō (attested), 小桜 Kozakura
(provisional), お佐絵 Osae (provisional), 猿渡 Saruwatari (attested), 梶川景次
Kajikawa Keiji (provisional). Places: 石田村 Ishida village (attested), 武州多摩
Bushū Tama (decided), 府中 Fuchū (attested), 八王子 Hachiōji (attested), 甲州街道
the Kōshū Highway (attested), 大国魂神社 the Ōkunitama Shrine (attested), 専修坊
Senjubō (provisional). Organizations: 新選組 the Shinsengumi (attested). Terms:
石田散薬 Ishida Powder (attested), 里 ri (decided), 名主 village headman (decided).

Principal Characters page: Hijikata Toshizō and Kondō Isami flagged
`principal: true`.

### Digitization glitches

None found. The source is clean commercial digital text; the only mechanical
transforms were the ingest's furigana stripping and the 8 gaiji substitutions
(handled at Step 0). No dittography, stray zero-width lines, or mojibake in the
ch01 body.

### Tooling changed this batch (see HANDOFF "do not revert")

- scripts/check_align.py: made scene-break/marker aware (skip `***`, strip
  `{vdgp}`), and count SOURCE characters as kanji+kana rather than kanji only.
  The China-template version counted `***` as a paragraph (shifting every pair
  after a break) and, counting only Han, produced a wildly unstable ratio on a
  Japanese source. Now: clean 160/160, stable median.
- scripts/check_content.py: skip `_`-prefixed / non-dict glossary sections
  (the `_about` string crashed name_map), and made the target reader scene-break
  aware.
- scripts/gen_check_config.py: NEW. Generates check_config.json (docs/sources
  for translated units) for check_structure.py and check_content.py. Rerun each
  batch.
- data/noise.txt: appended Japanese name/idiom numeral rules (歳三, 彦五郎,
  喜六, 六社, 八王子, 百姓, 二重), each commented. Without them the check flagged
  the 三 in 歳三 on ~60 paragraphs, etc. No real quantity was noised.

### Voice-gate revision 1: inline dialogue

The commissioner disliked the staccato where a quotation and its framing
narration fell on separate lines (lead-in / quote / attribution as three
paragraphs). Cause: the source (a Japanese novel) sets every quotation as its
own paragraph, and the one-line-per-source-paragraph parity carried that into
English, where fiction runs a short quote inline with its attribution.

Fix (whole-book, settled here before freezing the reference): a display-only
join marker. A reading line prefixed `{j} ` is appended to the preceding
display paragraph at build time (a single space, or none across an em-dash
seam). The reading file still keeps one line per source paragraph, so every 1:1
check stays honest; only the built page merges. Tooling:
- build_reading_epub.py: `collapsed()` merges `{j}` lines, em-dash aware.
- verify_unit / check_structure / check_align / check_content / check_reconcile
  / apply_format_markers: strip `{j}` alongside `{v}/{d}/{g}/{p}`.
ch01 now renders 124 display paragraphs from 160 source lines. All checks green,
qa_epub PASS, epubcheck 0/0 after the change; en.json and the numbers/entities
are byte-for-byte unchanged (the join is render-only).

### Known failing test (expected; not book-affecting)

`tests/run_tests.py` reports one failure: "hook stands down on template stub."
That test asserts the kickoff Stop hook stands down when HANDOFF.md still holds
the TEMPLATE's placeholder kickoff (first line "(First line: ..."). Since Step 0
authored a real book kickoff, HANDOFF no longer carries that placeholder, so the
hook correctly enforces and the test's premise no longer holds. It is a
template-maintenance test, not a translation gate; every other test passes
(check_numbers pass/fail fixtures, builder skeleton/OPF/orphan-anchor, and the
hook's enforce/pass/ignore/fail-open paths).

## B02 = ch02 to ch07 (六車斬り / 七里研之助 / わいわい天王 / 分倍河原 / 月と泥 / 江戸道場)

Scope: chapters 2 through 7, end to end, run to completion (no voice gate this
batch, ch01 already frozen). The arc: Toshizō kills the swordsman Rokusha
Sōhaku at Fuchū; the Hachiōji school hunts him under the disguise of the
waiwai-tennō; he and Okita ambush and rout them at Bubaigawara; and the feud
follows Shichiri Kennosuke to the Edo dojo, where the chapter closes on the
first entrance of Katsura Kogoro.

### Title correction (source furigana authority)

ch02 六車斬り: the survey's provisional English title was "Cutting Down Muruma"
and the antagonist "Muruma". The source's own ruby reads 六車宗伯 as
ろくしゃそうはく, i.e. Rokusha Sohaku, a deliberate echo of the 六社明神
(Rokusha Myojin) shrine he serves. Per the rule to consult the furigana before
romanizing any name, the reading is authoritative: corrected the chapter title
to "Cutting Down Rokusha" (book.json) and used Rokusha Sohaku throughout.

### Checks (all green)

Per chapter, parity is true by construction (make_bilingual refuses a count
mismatch), then verify_unit (parity + numbers with data/noise.txt + anchors),
check_align, check_content, qc_entities, check_register --ref, and an explicit
tail verification against the source.

- ch02: 215 pairs; numbers 0 unresolved; 14 anchors; align 215/215 med 3.25;
  content 0 displaced; entities 0; register within tolerance. 2 scene breaks
  (after body paras 55, 151).
- ch03: 178 pairs; numbers 0; 7 anchors; align 178/178 med 3.32; content 0;
  entities 0; register OK. 2 scene breaks (after 52, 133).
- ch04: 198 pairs; numbers 0; 4 anchors; align 198/198 med 3.14; content 0;
  entities 0; register OK. 2 scene breaks (after 65, 118).
- ch05: 172 pairs; numbers 0; 5 anchors; align 172/172 med 3.06; content 0;
  entities 0; register OK. 1 scene break (after 86).
- ch06: 212 pairs; numbers 0; 3 anchors; align 212/212 med 3.28; content 0;
  entities 0; register OK. 1 scene break (after 52).
- ch07: 189 pairs; numbers 0; 7 anchors; align 189/189 med 3.07; content 0;
  entities 0; register OK. 1 scene break (after 98).
- Build: build_reading_epub 7/71 chapters, 55 notes, 0 source notes.
  qa_epub PASS (78 documents, 55 refs/bodies/backlinks). epubcheck 5.1.0:
  0 fatals / 0 errors / 0 warnings.

Scene breaks were read from the raw XHTML (a run of two or more
`<p><br/></p>` inside the body), since the ingest collapses those blanks in
data/src; scripts/scene_map.py reports them and validated exactly against
ch01's known breaks (48, 115).

### Notes added: 40 (continuous numbering 16 to 55)

- ch02 (14): court nobility / Kujo / espionage; hatamoto and the Mikawa
  pedigree; koku and the kobushin-gumi; the Kogen Itto-ryu; the Tennen
  Rishin-ryu lineage (Kondo Kuranosuke, Shusai, the adoption of Katsuta); the
  Ryugo-ryu shin-cut; the sword (Yasushige / wazamono / shaku and sun); the
  "hidden surname" and commoners' surnames; the ryuha license grades
  (mokuroku / kaiden); the Edo dojo (Shieikan); the Kanto circuit officers;
  Inoue Genzaburo; Nagakura Shinpachi; Todo Heisuke.
- ch03 (7): meshimori-onna; chugen; Okita Soji; the Hachioji Thousand
  Guardsmen; iai; the Maniwa Nen-ryu; the Araki-ryu (with Oshima Shingoemon,
  d. 1779).
- ch04 (4): the Little Tengu of Chiba (Chiba Eijiro / Shusaku / the shin-cut
  counter); the waiwai-tenno and the Gozu Tenno talismans; the great Ansei
  earthquake; the expel-the-barbarian (joi) clamor.
- ch05 (5): the intendant system and the Egawa of Nirayama; the cho unit; the
  Taiheiki; the 1333 Battle of Bubaigawara; "a ground of highways" (Sunzi).
- ch06 (3): the Kusunoki and Koshu schools of military science; the okachi and
  Okita's Edo background; the Ikaho tablet affair.
- ch07 (7): the old sword-saints (Bokuden / Ittosai / Musashi); kigumi (the
  Tennen Rishin-ryu watchword); the three great dojo of Edo; Katsura Kogoro;
  Sakamoto Ryoma; Choshu; Harada Sanosuke.

First-appearance discipline held throughout. NOT re-noted (introduced earlier,
recurring here): the Shinsengumi (n1), the ri (n2), Fuchu / Rokusha Myojin /
Okunitama and its festival (glossary, n7), tenryo / shogunal domain (n12),
yobai night-crawling (n13), Sato Hikogoro and the nanushi (n6), the Tennen
Rishin-ryu name (n6, with its lineage newly noted in ch02), the Shinto
Munen-ryu (ch01), the traditional hours (n8), Ishida Powder (n10), the Senjubo
and married Shinshu clergy (glossary, n9), the swordsmith trade.

### Fact-check verdicts (real scholarship; never LLM-sourced)

- Shinsengumi captains introduced (Nagakura Shinpachi 1839-1915, Todo Heisuke
  1844-1867, Inoue Genzaburo 1829-1868, Okita Soji c.1842-1868, Harada
  Sanosuke 1840-1868): CORROBORATED, dates and roles per English/Japanese
  Wikipedia and Shinsengumi scholarship. Grokipedia results appeared in
  searches and were IGNORED per the LLM-source ban.
- Sword schools (Kogen Itto-ryu, founded 1776 by Henmi Tashiro, carried by
  Hiruma Yohachi d.1840; Ryugo-ryu of Okada Soemon with its shin-cut and
  naginata; Maniwa Nen-ryu of Kozuke; Araki-ryu): CORROBORATED (Japanese
  Wikipedia, kobudo sources).
- Hachioji Sennin Doshin: CORROBORATED as a real semi-agrarian shogunal guard
  force, largely ex-Takeda men of Kai, guarding the western approaches to Edo
  (Hachioji city site; Japanese Wikipedia).
- Battle of Bubaigawara: CORROBORATED, 1333, Nitta Yoshisada vs the Kamakura
  (Hojo) army, Miura's overnight reinforcement, the march on Kamakura, matching
  Shiba's account. Note flags that Shiba's "southern side" is a loose backward
  glance (the Northern/Southern Courts split came a few years later).
- Ikaho tablet affair (ch06): CORROBORATED as a real Chiba Shusaku vs Nen-ryu
  confrontation, but Shiba's particulars differ from the record, which dates it
  to 1823 (Bunsei 6, not the third year given) and names the Nen-ryu head as of
  the Higuchi family, not "Maniwa" (Shiba takes the surname from the school's
  seat). Translated Shiba faithfully; the discrepancy is stated in the note.
- The three great dojo of Edo (Genbukan/Chiba, Renpeikan/Saito Yakuro,
  Shigakukan/Momonoi Shunzo) and Katsura Kogoro as Renpeikan head student of
  Choshu: CORROBORATED (Japanese Wikipedia). The Ryoma-thrust-on-Katsura
  tournament anecdote is a popular tradition, told as such.

### Glossary rows added

75 rows across people/places/organizations/terms (see git for the full list),
each with attestation status. Principals flagged for the Principal Characters
page: Okita Soji (3), Inoue Genzaburo (4), Nagakura Shinpachi (5), Shichiri
Kennosuke (6, the recurring antagonist), Harada Sanosuke (7), Katsura Kogoro
(8). One rendering per referent enforced by check_content; two given-name keys
(半造 Hanzo, 周作 Shusaku) carry the short rendering used in the text, with the
full name in the pinyin field.

### Reading-authority corrections from the furigana

- 六車宗伯 = Rokusha Sohaku (not Muruma); chapter title corrected.
- 桃井春蔵 = Momonoi Shunzo (source ruby もものい, not Momoi).
- 猿田彦 rendered Sarutahiko (the attested deity name); the source rubies it
  さるだひこ (Sarudahiko), noted in the glossary.

### Digitization glitches

None found in the ch02 to ch07 bodies. The source remains clean commercial
digital text; the only mechanical transforms are the ingest's furigana
stripping and gaiji substitution from Step 0.

### Tooling changed this batch (see HANDOFF "do not revert")

- scripts/scene_map.py (NEW): reports scene breaks for a chapter by reading the
  raw data/src_epub XHTML (runs of two or more `<p><br/></p>` in the body),
  since the ingest collapses those blanks. Validated against ch01.
- scripts/reading_to_en.py (NEW): derives out/<id>_en.json from the authored
  out/<id>_reading.md (strips heading, drops ***, strips {j}), so the flat
  parity array can never drift from the display file. make_bilingual then
  cross-checks the count against data/src.
- scripts/check_chapter.sh (NEW): runs the per-chapter QC battery in one call.
- scripts/apparatus_merge.py (PATCH): glossary rows now REQUIRE a "section"
  field (people/places/organizations/terms) and are nested into it. The old
  flat g[zh]=row placed rows at the top level, which render_glossary reads as
  bogus one-entry sections and which broke the build; the 75 flat rows added
  earlier this batch were migrated into their sections and the flat keys
  removed. Future batches must set "section" on every glossary row.
- data/noise.txt: appended name/idiom numeral rules for this batch (Rokusha,
  Kujo, Mikawa, Hasshu, given-name numerals like Shinpachi/Yohachi/Genzaburo/
  Shingoemon/Kogoro/Yakuro/Rihachi/Jurozaemon, the teen-elision forms
  十二、三 / 十八、九 / 十四、五 / 十五、六, and time/idiom terms). Each is
  commented; no real quantity was noised.
- glossary.json: removed the single-kanji term key 石 (koku); it false-matched
  the 石 inside place names (Ishiwara, Ishida, Koishikawa). koku quantities are
  covered by check_numbers, so nothing is lost.

## B03 = ch08 to ch13 (桂小五郎 / 八王子討入り / スタスタ坊主 / 疫病神 / 浪士組 / 清河と芹沢)

Scope: chapters 8 through 13, end to end, run to completion. The arc closes the
Tama-country prologue and opens the political story: Katsura Kogorō outfences
Shichiri at the Edo dōjō and Toshizō conceives his class-hatred of the blessed
man; Toshizō raids the Hiruma hall at Hachiōji (the Sutasuta-monk night ambush)
and the school is shut; the Koishikawa measles-and-cholera epidemic ruins the
dōjō and drives the whole company to enlist in the shogunate's Rōshigumi;
Toshizō buys his sword and kills a night-duelist on the road out of Edo; and in
Kyoto, at the Mibu Shintokuji, Kiyokawa Hachirō reveals the corps's true
imperial purpose, whereupon Toshizō resolves to break away, kill Kiyokawa, and
found a new party, allying first with the violent Mito man Serizawa Kamo. The
core Shinsengumi is now assembling at Mibu.

### Checks (all green)

Per chapter: parity true by construction (make_bilingual refuses a count
mismatch), then verify_unit (parity + numbers with data/noise.txt + anchors),
check_align, check_content, qc_entities, check_apparatus, check_register --ref,
and an explicit tail verification against the source.

- ch08: 202 pairs; numbers 0; align 202/202 med 3.10; content 0 displaced;
  entities 0; register within tol (0.62x, little-dialogue noisy). 1 scene break
  (after body para 115). 5 notes.
- ch09: 178 pairs; numbers 0; align 178/178 med 3.00; content 0; entities 0;
  register 0.63x. 1 scene break (after 103). 4 notes.
- ch10: 168 pairs; numbers 0; align 168/168 med 3.04; content 0; entities 0;
  register 0.71x. 2 scene breaks (after 12, 50). 6 notes.
- ch11: 152 pairs; numbers 0; align 152/152 med 3.20; content 0; entities 0;
  register 0.43x (deliberately formal: Yamanami's stiffness, exposition). 1
  scene break (after 54). 11 notes.
- ch12: 187 pairs; numbers 0; align 187/187 med 3.13; content 0; entities 0;
  register 0.27x (formal speakers: the blind sword-dealer, the night-duelist;
  little-dialogue noisy). 1 scene break (after 73). 8 notes.
- ch13: 170 pairs; numbers 0; align 170/170 med 3.00; content 0; entities 0;
  register 0.36x (Kiyokawa's oratory, Yamanami; noisy). 1 scene break
  (after 32). 11 notes.
- Build: build_reading_epub 13/71 chapters, 100 notes, 0 source notes.
  qa_epub PASS (78 documents, 100 refs/bodies/backlinks all resolve).
  epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings.

Register note: check_register PASSED (no STILTED flag). The expository chapters
(ch11 to ch13) score low on the dialogue-contraction ratio, but every one is
flagged "little dialogue (noisy)" because it holds under 1200 speech-words, so
the metric is informational there. The low rates are character-driven, not
drift: Kiyokawa's set-piece oratory, Yamanami's bred-in stiffness, the courtly
old sword-dealer, and the formal challenge of the night-duelist are speakers
the register-drift references list as legitimately formal. Toshizō, Kondō,
Okita, Serizawa, and the Hachiōji meshimori-woman all keep the contracted
rough voice of the frozen reference.

Scene breaks were read from the raw XHTML via scripts/scene_map.py (a run of
two or more `<p><br/></p>` in the body).

### Notes added: 45 (continuous numbering 56 to 100)

- ch08 (5): the Kōbusho and formal match etiquette; the three guards
  (jōdan/chūdan/gedan); the "Tobari Fushigorō" ringer custom; Katsura "I would
  run" (the historical Runaway Kogorō, author-as-witness foreshadowing);
  Harada's belly-scar seppuku anecdote.
- ch09 (4): Idaten (the swift deva); the Day of the Ox in the dog-days
  (herb-gathering); dokudami; the Genki/Tenshō Warring-States eras.
- ch10 (6): the sutasuta/gannin proxy-pilgrim mendicant; the Hie (Sannō)
  deity; the Hijikata warrior pedigree (Ten Horsemen of Tama / Azuma Kagami /
  Bandō warriors / Odawara Hōjō); Ieyasu's 1590 Kantō entry (why Tama became
  shogunal farmland); the Aizu and Hakodate Wars (forward reference to
  Hijikata's death arc); Harada's Hizen Fujiwara Yoshihiro sword.
- ch11 (11): the Bunkyū era; the 1862 measles/cholera epidemic (with the Faroe
  fact-check); the Bukō Nenpyō / Saitō Gesshin; the Sakuradamon assassination
  of Ii Naosuke (1860); the Water Margin / Liangshan; Kiyokawa Hachirō; the
  Rōshigumi (its conception and significance); the rōjū Itakura Suō-no-kami;
  Saitō Hajime; Yamanami Keisuke (with his 1865 seppuku foreshadowed);
  Shiba's Zengakuren analogy (Tōdai/Waseda).
- ch12 (8): Matsudaira Kazusa-no-suke; Rai San'yō's Nihon Gaishi; Kondō's
  Kotetsu (the famous forgery, with fact-check); the Nosada / Izumi-no-kami
  Kanesada (with the fact-check that Hijikata's real blade was the 11th-gen
  Aizu Kanesada, not the Muromachi Nosada); the wazamono sharpness ranking;
  Ningen Mukotsu (Mori Nagayoshi's spear); tsujigiri; the Nakasendō route.
- ch13 (11): Mibu; the Suzaku Avenue; mibuna greens; the Tengu Party; Serizawa
  Kamo (with fact-check); Matsudaira Katamori and the Kyoto Protector; sonnō
  jōi; the Emperor Kōmei; Yamaoka Tetsutarō (the future Tesshū); Akechi
  Mitsuhide as byword for traitor; Kiyokawa's gambit and the birth of the
  Shinsengumi from the Rōshigumi split.

First-appearance discipline held. NOT re-noted (introduced earlier, recurring
here): the Shinsengumi (n1), the ri (n2), the traditional hours (n8, though
Shiba himself now uses the modern clock, e.g. "ten o'clock"), Ishida Powder
(n10), iai (ch03), the mokuroku/kaiden license grades (ch02), shaku/sun
(ch02), the Egawa/Nirayama intendant (ch05), jōi (ch04, expanded to sonnō jōi
in ch13), Kusunoki Masashige (ch06 glossary; his Nihon Gaishi romanticization
newly noted at ch12), the sword schools and the three great Edo dōjō (ch07),
Katsura/Harada/Nagakura/Tōdō/Inoue/Okita (ch02 to ch07; Katsura's evasiveness
and Harada's scar are new-aspect notes, not identity re-notes), the Kōgen
Ittō-ryū / Shintō Munen-ryū / Genbukan (glossary).

### Fact-check verdicts (real scholarship; never LLM-sourced)

- The Bunkyū-2 (1862) measles epidemic: CORROBORATED as real and catastrophic,
  the first outbreak in twenty-six years, sweeping Edo through the summer, with
  the Edo shichū hashika byōnin chōsho recording over 73,000 city deaths (higher
  estimates to ~240,000), and cholera running with it. Shiba's Bukō Nenpyō
  entries match. The Faroe-Islands origin is Shiba's dramatization: the
  celebrated Faroe measles epidemic studied by P. L. Panum was in 1846, not
  1862; noted as such. Sources: Panum (1846 Faroe study); Edo mortality records;
  environmental-history scholarship on the 1862 epidemic.
- Kondō's Kotetsu: CORROBORATED as almost certainly a forgery, by most accounts
  a Minamoto Kiyomaro blade carrying a faked Kotetsu signature; Saitō Hajime's
  later account has Kondō knowingly buying the fake and treasuring it. Note
  states this.
- Hijikata's Izumi-no-kami Kanesada: the surviving historical blade is by the
  11th-generation Aizu Kanesada, a bakumatsu smith (the line received the
  Izumi-no-kami title only in late 1863), acquired in Kyoto in connection with
  Matsudaira Katamori of Aizu. Shiba's scene of buying a Muromachi 2nd-gen Mino
  "Nosada" from a blind Asakusa dealer before leaving Edo is therefore
  novelistic invention; the note says so. Sources: records of the Hijikata
  Kanesada and the Aizu Kanesada line (Sesko; sword archives).
- Serizawa Kamo: CORROBORATED as a Mito rōnin of the Shindō Munen-ryū with
  Tengu-Party ties, co-commander of the founding Mibu corps, assassinated by the
  Kondō faction in 1863; his real name is disputed (Kimura/Shimomura Tsuguji),
  matching Shiba's 木村継次. Grokipedia surfaced in this search and was IGNORED
  per the LLM-source ban.
- Ii Naosuke / Sakuradamon (1860), Yamaoka Tesshū, Matsudaira Katamori as Kyoto
  Shugoshoku (1862), Kiyokawa Hachirō and the 1863 Rōshigumi, Yamanami's 1865
  seppuku, Saitō Hajime's dates, Emperor Kōmei's anti-foreign stance: all
  CORROBORATED against standard Japanese/English scholarship.

### Reading-authority corrections from the furigana

- 戸張節五郎 = Tobari Fushigorō (source ruby ふしごろう, an unusual reading of 節;
  the source's furigana is authoritative, as with Rokusha and Momonoi in B02).
- 山南 = Yamanami (source ruby やまなみ), settling the well-known Sannan/Yamanami
  reading question in favor of Yamanami.
- 容保 = Katamori; 芹沢鴨 = Serizawa Kamo; 新見錦 = Niimi Nishiki (all from the
  source furigana).
- CAUTION recorded: this source uses the author's EXPRESSIVE gikun furigana in
  places (将軍 rubied たいじゅ, 京 rubied ここ "here," 近藤 rubied せんせい
  "sensei"). These are semantic glosses, NOT phonetic readings, and must not be
  used to romanize. Only the name/word rubies are romanization authority.

### Digitization glitches

None found in the ch08 to ch13 bodies. The source remains clean commercial
digital text. The one image in ch12's source (part0014) is the class="gaiji"
glyph for 㝎 (the 之定/Nosada variant of 定), already substituted by the ingest
via data/gaiji_map.json; it is not an illustration. No dittography, stray
zero-width lines, or mojibake.

### Tooling changed this batch (see HANDOFF "do not revert")

- scripts/qc_entities.py (PATCH): now skips single-kanji glossary keys (zh forms
  of length < 2). A single-kanji name key cannot be matched as a whole entity by
  raw substring: 権 (the scout Gon) false-hits inside 権力 / 権威 / 政権, and 里
  (ri) inside 郷里, etc. This bit ch12 (3 phantom "Gon" misses) and would recur
  through the whole political half of the book, which is thick with 権/政権/幕権.
  check_content already skips zh of length < 2 for the same reason; qc_entities
  now matches that guard. The named referents (Gon, ri) stay in the glossary and
  on the glossary page; only the unreliable substring check is dropped for them.
- data/noise.txt: appended B03 name/idiom numeral rules, each commented:
  節五郎, 五分五分 (ch08); 八日市, 八幡, 八木 (ch09); 三、四十, 善四郎, 弥八郎,
  三左衛門 (ch10); 三十郎, 八郎 (ch11); 二合半, 千代田, 十字, 藤四郎, 十文字
  (ch12); 熊三郎 (ch13). No real quantity was noised.

### Glossary rows added: 34 (nested by section)

People (19): 山南敬助 Yamanami Keisuke (attested, principal 9), 芹沢鴨 Serizawa
Kamo (attested, principal 10), 斎藤一 Saitō Hajime (attested, principal 11),
清河八郎 Kiyokawa Hachirō, 松平上総介 Matsudaira Kazusa-no-suke (provisional),
松平忠敏 Matsudaira Tadatoshi, 山岡鉄太郎 Yamaoka Tetsutarō, 松平容保 Matsudaira
Katamori, 板倉周防守 Itakura Suō-no-kami, 新見錦 Niimi Nishiki, 平間重助 Hirama
Jūsuke (provisional), 野口健司 Noguchi Kenji, 平山五郎 Hirayama Gorō, 石坂周造
Ishizaka Shūzō, 池田徳太郎 Ikeda Tokutarō, 根岸友山 Negishi Yūzan, 八木源之丞
Yagi Gennojō, 頼山陽 Rai San'yō, 孝明天皇 the Emperor Kōmei. Places (5): 壬生
Mibu, 新徳寺 the Shintoku-ji, 中仙道 the Nakasendō, 会津 Aizu, 水戸 Mito.
Organizations (3): 浪士組 the Rōshigumi, 天狗党 the Tengu Party, 京都守護職 the
Kyoto Protector. Terms (7): 尊皇攘夷 sonnō jōi, 講武所 the Kōbusho, 辻斬り
tsujigiri, 鉄扇 iron war-fan, 公用方 liaison office, 和泉守兼定 Izumi-no-kami
Kanesada, 虎徹 Kotetsu. Principals flagged for the cast page: Yamanami (9),
Serizawa (10), Saitō Hajime (11). One rendering per referent enforced by
check_content; all 34 new names verified present in their source paragraphs.

## B04 = ch14 to ch18 (ついに誕生 / 四条大橋 / 高瀬川 / 祇園「山の尾」/ 士道)

The founding of the Shinsengumi and the purge of Serizawa. ch14 "Born at Last"
(the botched Kiyokawa assassination, the Aizu connection through Toshima Kihee,
and the granting of the name Shinsengumi); ch15 "Shijō Great Bridge" (money, the
Aizu stipend, and Toshizō's Western-modeled corps organization; ends on a
killing at the bridge); ch16 "The Takase River" (Toshizō and Okita hunt six
killers through Pontochō and Kiyamachi; a Kōgen Ittō-ryū man of Shichiri's
escapes); ch17 "The Yamanoo in Gion" (the Akazawa Morito murder, tracked to the
Serizawa faction; Toshima's warning to cut Serizawa down; Toshizō corners Niimi);
ch18 "The Warrior's Code" (Niimi's forced seppuku, the shidō argument, and the
night raid that kills Serizawa, Oume, and Hirayama).

### Checks (all green)

- verify_unit (parity + numbers --noise data/noise.txt + anchors), per chapter:
  ch14 213/213 pairs, 0 unresolved, 10 anchors ok.
  ch15 174/174 pairs, 0 unresolved, 8 anchors ok.
  ch16 218/218 pairs, 0 unresolved, 8 anchors ok.
  ch17 203/203 pairs, 0 unresolved, 9 anchors ok.
  ch18 185/185 pairs, 0 unresolved, 8 anchors ok.
- make_bilingual parity refused once and CAUGHT A REAL OMISSION: ch18 first came
  out 183 vs 185. Two source paragraphs had been dropped in a single dialogue
  seam — Toshizō's 「斬られたいか、新見錦…会津中将様から出ている」 and Niimi's
  「うぬっ」 (source lines 39-40). Restored verbatim, re-checked, tail re-read.
  This is exactly the rule-4 omission class; the parity gate did its job.
- check_align: all five 3.1 to 3.4 en/han median, no collapse/explosion runs.
- check_content: 0 displaced across all units (ch14 45, ch15 46, ch16 35,
  ch17 51, ch18 60 name-anchor occurrences, all in the paired paragraph).
- qc_entities: 0 misses per chapter (after fixing one ch18 slip — 旗本 had been
  rendered "bannermen"; corrected to the glossary's decided "hatamoto").
- check_apparatus: 0 failures / 0 warnings.
- check_register --ref reference/ch01_ref.md (em-dash /1k, ratio-of-ref,
  dialogue %, sentence length, notes, type-token): ch14 2.9, ch15 3.9, ch16 13.5,
  ch17 9.7, ch18 7.5 em-dashes/1k — all WITHIN TOLERANCE of the frozen ch01
  reference (12.7 baseline). ch16 runs highest (13.5) on the long two-man
  fight-and-banter, still in tolerance.
- Tail verified against the source for every chapter (rule 4): ch14 ends
  「事は、これからですよ」/ Serizawa's face; ch15 the fallen lantern and the man
  being cut down; ch16 Okita's shoulder shaking with a cough; ch17 Toshizō
  sliding the shōji open on Niimi; ch18 Noguchi's year-end seppuku and the
  faction annihilated.
- Whole-book: build_reading_epub 18/71 chapters, 143 notes; qa_epub PASS
  (143 references / 143 bodies / 143 backlinks, all links resolve);
  epubcheck 0 fatals / 0 errors / 0 warnings / 0 infos.

### Notes added: 43 (continuous numbering 101 to 143)

- ch14 (10): the war-fan motto 尽忠報国; 中将 "Middle Captain" (Katamori's court
  rank); 学習院 the court Gakushūin (not the peers' school); Sasaki Tadasaburō;
  the Akabanebashi/Azabu-Ichinohashi place discrepancy in Kiyokawa's killing;
  the Namamugi Incident; 新徴組; the naming of 新選組 (chronology telescoped);
  Bunkyū 3/3/13 = 2 May 1863; the "letter K" (き文字) circumlocution.
- ch15 (8): the Mibu-rō / mi-boro pun; 芋道場 "sweet-potato dōjō"; the ryō;
  Shimabara; the corps officer structure (jokin / kyokuchō / fukuchō / kansatsu)
  and Hijikata's deliberate vice-commander post; the Kōnoike house; the Ōshōroku
  (Hirosawa's genuine memoir); the shinai.
- ch16 (8): 雑掌 / 青侍 noble-house retainers; the goyōkiki and his jitte;
  Saru no Bunkichi and the 1862 tenchū terror; Shimada Sakon and Ugō Genba;
  the Shoshidai (vs the Protector); Okita's consumption; the Bushū barley-
  treading song; the Takase River (canal + domain mansions).
- ch17 (9): the Bon / Urabon festival; Rai San'yō's Honnō-ji poem and "the enemy
  is at Honnō-ji"; burei-uchi (killing for a slight); the Kiheitai; the Yamatoya
  arson (12 Aug 1863); the upright tea-stalk omen; the tayū; the hour of the
  Dragon; Horikawa Kunihiro.
- ch18 (8): kaishaku (the second); shidō (the warrior's code, the chapter's
  argument); shidō fukakugo; the Bandō warriors; the chūgen (Harada's origin);
  the "Sa"=左 wordplay for Sanosuke; the Serizawa assassination (30 Oct 1863,
  assassin roster disputed); the "hour of the Dragon" slip (source's own).

### NOT re-noted (already glossed/footnoted earlier; first-appearance discipline)

- mokuroku (noted ch02), koku (ch02), the Kyoto Protector / Matsudaira Katamori /
  公用方 liaison office / 鉄扇 iron war-fan / 尊皇攘夷 / 和泉守兼定 / 虎徹 Kotetsu /
  講武所 the Kōbusho (all glossed in B03), 天狗党 the Tengu Party, 甲源一刀流,
  神道無念流, 北辰一刀流, 天然理心流, hatamoto (glossed ch02), Rai San'yō
  (glossary), Shichiri Kennosuke, the Three Tama, the several ryū and guards.
  Recurrences rendered to the settled glossary forms, not re-annotated.

### Fact-check verdicts (real scholarship; never LLM-sourced; Grok ignored)

- Kiyokawa Hachirō's killing: CORROBORATED as event, place FOOTNOTED. Sasaki
  Tadasaburō's party cut him down on Bunkyū 3/4/13 (30 May 1863). Scholarship
  places the spot at Azabu Ichinohashi; Shiba writes Akabanebashi (the adjacent
  bridge, same Shiba-Azabu district). Discrepancy left visible and noted.
- Name "Shinsengumi": chronology TELESCOPED (noted). Standard dating puts the
  grant after the 8/18/1863 coup, with the grantor disputed between the Buke
  Tensō and Matsudaira Katamori; Shiba compresses it to the spring founding via
  Aizu. The Aizu patronage and the men are as given.
- Namamugi Incident: CORROBORATED. 14 Sept 1862; Richardson killed off Shimazu
  Hisamitsu's procession; led to the Aug 1863 bombardment of Kagoshima.
- Shimada Sakon / Saru no Bunkichi: CORROBORATED. Both killed in the 1862 tenchū
  wave (Shimada by Satsuma's Tanaka Shinbei in Kiyamachi; the informer Bunkichi
  by the Tosa loyalists, body exposed at the Sanjō riverbed).
- Yamatoya arson: CORROBORATED. Serizawa burned the silk-merchant Yamatoya
  Shōbei's storehouses on 12 Aug 1863, near the Palace, outraging the court.
- Serizawa assassination: CORROBORATED as event, assassin roster FLAGGED as
  disputed. Bunkyū 3/9/18 (30 Oct 1863) by the anti-Serizawa Kondō faction at
  the Yagi house; Oume killed with him. The exact assassins differ by source
  (Hijikata, Okita, Yamanami, Harada, Inoue all named in various accounts);
  Shiba's roster is one version, noted as such.

### Digitization glitches

- ch18, source line 168: 辰ノ下刻 ("lower hour of the Dragon," ~8-9 a.m.) sits
  inside a plainly nocturnal scene (日没後 "after sundown" the line before,
  午後十二時半 "half past midnight" a few lines later). Almost certainly a slip
  (likely 辰 for 戌, the evening Dog hour). Rendered faithfully as "late in the
  hour of the Dragon" with a footnote flagging the source's inconsistency; not
  silently corrected. This is the source's own error, not OCR.
- No dittography, stray U+200B lines, doubled headings, or mojibake in the
  ch14-ch18 bodies. The one gaiji glyph relevant here (兼㝎 / 之定) was handled
  in ch12; nothing new. Source remains clean commercial digital text.

### Tooling changed this batch (see HANDOFF "do not revert")

- scripts/check_numbers.py (PATCH, target-side only): spelled_numbers now reads
  "a/one hundred and <ten..nineteen>" (110-119) and "<one..nine> hundred and
  <teen>". The existing rules reached hundreds-plus-tens (120-990) but stopped
  short of the teens, so 百十 (110, in ch15's 百十数名 "a hundred and ten-odd
  men") had NO English word-form the check could read. The addition is
  target-side, so by the module's own invariant it can only ADD a number to the
  translation's set, never mask a dropped source quantity. Regression suite
  re-run: check_numbers pass-fixture OK, fail-fixture 5/5 drops detected. Fixes
  the gate rather than forcing a bare digit into the prose.
- data/noise.txt: appended B04 name/idiom numeral rules, each commented:
  唯三郎, 二条, 万、まちがい (ch14); 四条, 五郎 (ch15); 三条, 十手 (ch16);
  千本, 三本木 (ch17); 五体, 万能 (ch18). No real quantity was noised; real
  troop/koku/date figures are carried in the English word-forms.
- scripts/build_zh.py (NEW, mechanical): builds data/zh/<id>.txt from
  data/src/<file>.txt (title line "### <title>" then one body line per non-empty
  source paragraph, skipping the two header lines). A pure file-to-file copy, no
  authoring; formalizes the "mechanical build" the kickoff describes so data/zh
  can be regenerated deterministically.

### Glossary rows added: 25 (nested by section)

People (12): 外島機兵衛 Toshima Kihee (attested), 島津久光 Shimazu Hisamitsu,
佐々木唯三郎 Sasaki Tadasaburō, 九条尚忠 Kujō Hisatada, 島田左近 Shimada Sakon,
谷三十郎 Tani Sanjūrō, 広沢富次郎 Hirosawa Tomijirō, 久坂玄瑞 Kusaka Genzui,
山崎烝 Yamazaki Susumu, 赤沢守人 Akazawa Morito (all attested). Places (6):
先斗町 Pontochō, 木屋町 Kiyamachi, 高瀬川 the Takase River, 島原 Shimabara,
角屋 the Sumiya, 本能寺 the Honnō-ji. Organizations (3): 学習院 the Gakushūin,
新徴組 the Shinchōgumi, 所司代 the Shoshidai. Terms (6): 局長 commander (kyokuchō),
副長 vice-commander (fukuchō), 助勤 jokin, 監察 inspector (kansatsu), 鴻池 the
Kōnoike (org), 士道 the warrior's code (shidō). One rendering per referent
enforced by check_content; all capitalized proper-name rows verified present in
their source paragraphs (Pontochō, Kiyamachi, and the people forms rendered
verbatim where the full source string appears).

## B05 = ch19 to ch23 (再会 / 二帖半敷町の辻 / 局中法度書 / 池田屋 / 断章・池田屋)

Batch 5. All five chapters translated to the frozen ch01 register, annotated,
checked, and built into the cumulative EPUB. Notes 144 to 180 (37 this batch).
Continuous note number now 180. Every scripted gate green; qa_epub PASS;
epubcheck 0 fatals / 0 errors / 0 warnings / 0 infos.

### Chapters

- ch19 再会 / "Reunion" (215 source lines). Autumn 1863; Toshizō's secret haiku
  (pen-name Hōgyoku) surprised by Okita; the reunion with Osae in the honey-trap
  house off Fuyamachi. 1 scene break (after para 102, the love-haiku). 10 notes.
  register within tolerance (em-dash 2.7/1k; "little dialogue" flag).
- ch20 二帖半敷町の辻 / "The Crossroads at Nijōhanjiki-chō" (195 lines). The tryst
  goes hollow; Osae revealed as a loyalist go-between; the palanquin water-cask
  decoy at the Yoshikago; Shichiri Kennosuke steps out of the dark. 0 scene
  breaks. 4 notes. register within tolerance (em-dash 9.7/1k).
- ch21 局中法度書 / "The Code of the Corps" (180 lines). The Shichiri fight
  broken off; the rōnin-control edict; Yamanami kicked upstairs to general
  secretary (staff-not-line); the five-article Code drafted with Okita; the
  first enforcement, Sakai Hyōgo. 1 scene break (after para 53). 7 notes.
  register within tolerance (em-dash 11.3/1k after fixing one 3-dash list).
- ch22 池田屋 / "The Ikedaya" (171 lines). The surveillance of the Masuya;
  Kishibuchi's tip; Furutaka Shuntarō's arrest; the split of the force between
  the Ikedaya and the Tantora; Kondō's own letters to Shūsai quoted. 1 scene
  break (after para 49). 9 notes. register within tolerance (em-dash 8.1/1k).
- ch23 断章・池田屋 / "Ikedaya: A Coda" (133 lines). The documentary coda: the
  inn's plan, Kido's diary, the full loyalist roster, the raid blow by blow, the
  casualty tallies from Tamamushi Sadayū's Kanbu Tsūki. 1 scene break (after
  para 8). 7 notes. register within tolerance (em-dash 3.2/1k, documentary).

### Checks (every chapter, all green)

- Parity + verbatim quotation by construction (make_bilingual); verify_unit
  re-check clean for all five. Two parity misses were caught by make_bilingual
  and fixed: ch22 merged source lines 6-7 (the "picture afternoon" / "Gion
  festival near" pair); ch23 dropped line 29 (ということである) and merged the
  Matsuda Jūsuke lines 105-106. Re-read against source restored 171 and 133.
- check_numbers --noise: 0 unresolved all five. New noise rules added (each
  commented, never a real quantity): 三月亭, 為三郎 (ch19); 万事, 四つ手, 四つ路,
  七どん, 十数, 十七、八, 二帖半敷 (ch20); 無二 (ch21); 二階, 四郎兵衛, 何百日,
  万々, 六角, 四国屋 (ch22); 五吉郎, 新三郎 (ch23). Real quantities (koku, troop
  counts, the Ikedaya measurements, casualty figures, dates) all carried in the
  English word-forms.
- check_align, check_content: OK across all 23 units. One displacement caught
  and fixed: ch22 para 78 had dropped the source's (水戸) gloss on Kishibuchi's
  clan; restored "(Mito)".
- qc_entities: 0 misses. check_apparatus: 0 failures, 0 warnings.
- check_register --ref: all five within tolerance of the frozen ch01 reference.
- Tail verification against source: done explicitly for each chapter (rule 4).

### Fact-checks (verdict stated in the note)

- Hijikata's haiku: the pen-name Hōgyoku and the 41-verse Hōgyoku Hokku-shū
  (compiled spring 1863, held at the Hijikata museum in Hino) corroborated;
  grandfather Sangetsutei Sekiha, and the poets Natsume Seibi (1749-1817) and
  Matsubara-an Seifu (1732-1814, the Hachiōji woman poet) corroborated. Reading
  fixed: 松原庵 = Matsubara-an, not the draft's "Shōhōan" (Kotobank).
- Kujō Hisatada / Princess Kazunomiya kōbu-gattai marriage / his 1862 forced
  tonsure: corroborated.
- The Hōkyō-ji imperial convent and the Hōkō-ji Great Buddha (ch20): the
  institutions and geography are real; the safehouse-behind-the-Daibutsu is the
  novelist's device. Institutions corroborated.
- The five-article Code (ch21): PROVENANCE DEBATED. The name 局中法度書 and the
  five-article form come chiefly from Shimozawa Kan's Shinsengumi shimatsuki
  (1928); Nagakura's account has only four "interdictions"; no contemporary
  document survives. The discipline-by-seppuku it dramatizes is firmly attested.
  Note states the split verdict.
- Sakai Hyōgo's desertion and killing (ch21): attested in the traditional
  accounts, which place it in 1865 after Yamanami's seppuku; Shiba brings it
  forward as the code's first test. Timing is the novelist's; the killing real.
- Ikedaya Incident (ch22-23): date 元治元年6月5日 = 8 July 1864 corroborated;
  Furutaka Shuntarō / Masuya Kiemon, the plot, the small raid party, Kondō's
  quoted letters, the asagi dandara uniform and Hijikata's surviving hachigane
  all corroborated. Furutaka's confession: Shiba takes the minority line
  (roster seized, torture yielded nothing) against the famous torture-confession
  tradition; note states the dispute. Casualty counts vary across sources
  (7/8/9 dead, ~20-23 taken); Shiba's 7 dead / 23 taken kept, variance noted.
  (Grokipedia surfaced in a search and was IGNORED per rule 5.)

### Glossary rows added this batch: 48 (nested by section)

People (34): 隼人 Hayato, 為三郎 Tamesaburō, 三月亭石巴 Sangetsutei Sekiha,
夏目成美 Natsume Seibi, 松原庵星布 Matsubara-an Seifu (ch19); 家茂 Iemochi,
酒井兵庫 Sakai Hyōgo (ch21); 古高 Furutaka, 岸淵兵輔 Kishibuchi Heisuke, 四国屋
Shikokuya (Jūbei), 島田魁 Shimada Kai, 川島勝司 Kawashima Katsuji, 林信太郎
Hayashi Shintarō, 周平 Shūhei, 渡辺幸右衛門 Watanabe Kōemon, 利助 Risuke,
熊坂長範 Kumasaka Chōhan (ch22); 吉田稔麿 Yoshida Toshimaro, 宮部鼎蔵 Miyabe
Teizō, 松田重助 Matsuda Jūsuke, 北添佶麿 Kitazoe Yoshimaro, 望月亀弥太 Mochizuki
Kameyata, 野老山 Tokoroyama (Gokichirō), 大高又次郎 Ōtaka Matajirō, 玉虫左大夫
Tamamushi Sadayū, 惣兵衛 Sōbei, 奥沢新三郎 Okuzawa Shinzaburō, 安藤早太郎 Andō
Hayatarō, 新田革左衛門 Nitta Kakuzaemon, 山田信道 Yamada Nobumichi (ch23).
Places (7): 竹屋町 Takeyamachi, 二帖半敷町 Nijōhanjiki-chō, 仏光寺 the Bukkō-ji,
宝鏡寺 the Hōkyō-ji, 鴨川 the Kamo River, 室町 Muromachi, 大仏 the Great Buddha
(ch20); 本圀寺 the Honkoku-ji, 三条小橋 Sanjō-kobashi, 高麗橋 Kōraibashi (ch22).
Organizations (5): 芳駕籠 the Yoshikago (ch20); 枡屋 the Masuya, 茨木屋 the
Ibarakiya, 丹虎 the Tantora, 池田屋 the Ikedaya (ch22). Terms (2): 局中法度 the
Code of the Corps, 見廻組 the Mimawarigumi (ch21). Two entries carry a bare
surname en to satisfy check_content where the source shortens the name: 古高 ->
"Furutaka" (full "Furutaka Shuntarō" at first mention), 野老山 -> "Tokoroyama".
A bare-佐絵 row was tried and REMOVED: 佐絵 is a substring of お佐絵 (Osae, ch01-02)
and over-matched a prior chapter; the referent stays covered by お佐絵 -> Osae.

### "NOT re-noted" ledger (first-appearance discipline held)

Already noted in earlier batches, deliberately not re-noted this batch: Bunkyū
era-year (ch11/ch14); the Rokusha Myōjin / Ōkunitama shrine and miko
shrine-maidens (ch01); Ishida Powder (ch01, rendered verbatim); court noble
(kuge) / shodaibu / regent service (ch02); Shimabara and Gion pleasure quarters
(ch02/earlier); the Protector of Kyoto / Shoshidai and Revere-the-Emperor,
Expel-the-Barbarian (ch13); Toshizō's Izumi-no-kami Kanesada and the Kotetsu
smith (ch12, though ch23 adds the Ikedaya forgery-anecdote which says more);
Katsura Kogorō = Kido Takayoshi (ch07); the Tōkaidō (ch12); Aizu / Mibu / the
corps ranks and shidō (B04). New notes were placed only at genuine first
appearances.

### Digitization glitches / source oddities this batch

- None of substance. The source stays clean commercial digital text: no
  dittography, no stray U+200B lines, no doubled headings, no mojibake in the
  ch19-ch23 bodies. Expressive gikun furigana continue (将軍→たいじゅ, 京→ここ,
  近藤→せんせい and the like); treated as semantic glosses, never romanized.
- The source writes 玉虫左大夫 (ch23); standard scholarship writes 玉虫左太夫.
  Kept the source form, glossary note records the variant. Not corrected.
- 丹虎 is furigana'd たんとら (Tantora), not the "Tankō" one might guess; used the
  source's own reading.

## B06 = ch24 to ch28 (京師の乱 / 長州軍乱入 / 伊東甲子太郎 / 甲子太郎、京へ / 慶応元年正月)

Batch 6. All five chapters translated to the frozen ch01 register, annotated,
checked, and built into the cumulative EPUB. Notes 181 to 208 (28 this batch).
Continuous note number now 208. Every scripted gate green; qa_epub PASS (208
references / 208 bodies / 208 backlinks); epubcheck 0 fatals / 0 errors / 0
warnings / 0 infos. 28 of 71 chapters now translated.

### Chapters

- ch24 京師の乱 / "Turmoil in the Capital" (136 source lines). The Ikedaya
  aftermath: Shiba's argument that the affair hastened rather than delayed the
  Restoration; the Aizu liaison letter; Kondō declines the "senior yoriki" rank
  and plays the daimyō; the Chōshū residence empties toward the Tenryū-ji; the
  artillery-begging visit to Kurodani; Chōshū's expedition sails; the "king"
  (gyoku) shōgi metaphor; the Shinsengumi posted to the Hamaguri Gate. 1 scene
  break (after para 38). 7 notes. register within tolerance (em-dash 7.0/1k;
  "little dialogue" flag).
- ch25 長州軍乱入 / "The Chōshū Army Storms In" (165 lines). The Kinmon /
  Hamaguri Gate Incident: the armor-fitting and the "Makoto" banner; the
  Kanjinbashi posting; Toshizō reads the feint (Fushimi weak, Saga strong);
  Yamazaki's night ride at Fujinomori; Fukuhara's Fushimi wing beaten; Kunishi's
  Saga wing storms the palace; Kijima and Kusaka die; the Dondon-yaki fire; Maki
  Izumi's seventeen on Tennōzan. 1 scene break (after para 62). 5 notes.
  register within tolerance (em-dash 10.3/1k).
- ch26 伊東甲子太郎 / "Itō Kashitarō" (163 lines). Itō introduced: the Ono
  Keijirō authorial digression; Itō's Mito-radical, Hokushin Ittō-ryū
  provenance; Toshizō's dread of the school's topple-the-shogunate men; Tōdō's
  secret proposal to assassinate Kondō and make Itō captain; the kinchō
  sword-oath; Itō's cold reading of Toshizō. 2 scene breaks (after paras 54,
  82). 5 notes. register within tolerance (em-dash 11.0/1k).
- ch27 甲子太郎、京へ / "Kashitarō Comes to Kyoto" (174 lines). Itō meets Kondō
  in Edo; Kondō's boast of lobbying the rōjū and the bankrupt treasury (the
  secret French loan); the "eighty thousand mounted hatamoto" as straw dolls;
  Itō gathers his seven men (the roster with fates); Shinohara's theatrical
  warning; Itō divorces his wife on the nation's account; the party of eight
  enters Kyoto; Toshizō refuses to call on the newcomer. 2 scene breaks (after
  paras 78, 134). 5 notes. register within tolerance (em-dash 12.5/1k).
- ch28 慶応元年正月 / "New Year, First Year of Keiō" (178 lines). Kondō's
  swelling vanity after Edo; the Kiyamachi talk with Okita (Toshizō the
  "craftsman" who wants no rank, will help Kondō until Kondō quits the corps);
  the New Year photograph (hotogara) sent by Hitotsubashi Yoshinobu, Kondō
  powdered white by Ueno Hikoma; Itō's faction shunning the camera as a
  defilement; Yamanami drawn to Itō; ends "Yamanami Keisuke deserted." 1 scene
  break (after para 91). 6 notes. register within tolerance (em-dash 13.7/1k).

### Checks (every chapter, all green)

- Parity + verbatim quotation by construction (make_bilingual); verify_unit
  re-check clean for all five. THREE parity misses caught by make_bilingual and
  fixed by re-read against source: ch26 merged three seams (line 90 「平助が悩ん
  でいる」 into 91; line 98 と洩らした dropped; lines 142-143 そのあと、酒になった /
  席上、伊東はふと merged) restoring 163; ch27 dropped line 166 「なにがおかしい」
  restoring 174; ch28 dropped line 50 になるしかしかたがない restoring 178.
- check_numbers --noise: 0 unresolved all five. New noise rules (each commented,
  never a real quantity): 三々五々, 三田尻 (ch24); 五月人形, 弥十郎, 忠三郎 (ch25);
  三樹三郎 (ch26); 七子, 七五三之助, 二郎, 三村, 三田台町 (ch27). Real quantities
  (koku, troop counts, forty-thousand/thousand-odd, dates, ages, the eighty
  thousand hatamoto) all carried in the English word-forms. Two spelled-number
  forms adjusted so the parser reads them ("a bare hundred-odd" -> "a hundred and
  some"; "a good hundred" -> "a hundred or so"; decade band "thirties to fifties"
  -> "thirty to fifty").
- check_align, check_content: OK across all 28 units. Displacements caught and
  fixed: ch24 para 5 dropped the letter's (松平容保) gloss, restored "(Matsudaira
  Katamori's)"; ch24 para 61 rendered 福田理兵衛 to match the existing bare
  理兵衛->"Rihei" row (Fukuda Rihei); ch25 para 54 needed the decided 旗本
  ->"hatamoto"; ch28 paras 77/85 needed the decided 武州多摩->"Bushū Tama".
- qc_entities: 0 misses. check_apparatus: 0 failures, 0 warnings.
- check_register --ref: all five within tolerance of the frozen ch01 reference.
- Tail verification against source: done explicitly for each chapter (rule 4);
  the ch28 tail "Yamanami Keisuke deserted." verified against 山南敬助が脱走した。

### Fact-checks (verdict stated in the note)

- Kinmon / Hamaguri Gate Incident (ch25): the lunar date 元治元年7月19日 = 20 Aug
  1864 corroborated (布陣 on the 18th, fighting before 4 a.m. on the 19th). Kijima
  Matabee killed in battle (reversed his own spear); Kusaka Genzui and Terashima
  Chūzaburō seppuku at the Takatsukasa mansion; Fukuhara Echigo wounded; Kunishi
  Shinano escaped and was later made to die; Maki Izumi and party (17) seppuku on
  Tennōzan on the 21st — all corroborated. The Kyoto fire is the historical
  Dondon-yaki (~28,000 houses), corroborated; note states it.
- Itō Kashitarō provenance (ch26-27): born Suzuki Daizō in Hitachi-Shizuku;
  Shintō Munen-ryū at Mito then Hokushin Ittō-ryū under Itō Seiichi at Fukagawa
  Sagachō; married in and took the dōjō on Seiichi's death; took the name
  Kashitarō in the kinoe-ne (甲子) year, Genji 1; joined the Shinsengumi with
  brother Suzuki Mikisaburō and the men Shinohara, Kanō (Washio), Hattori,
  Utsumi, Nakanishi late 1864 — all corroborated. The Kōdai-ji split and the
  1867 Aburanokōji killing foreshadowed in the note.
- The secret French loan (ch27): the shogunate's approach to France (via
  Léon Roches) for war funds and Westernization, which foundered — corroborated;
  note states it.
- The Kondō photograph (ch28): Ueno Hikoma, Nagasaki photographer trained under
  Pompe van Meerdervoort; Matsumoto Ryōjun as Pompe's pupil, shogunal physician,
  later Surgeon-General and baron; Hitotsubashi Yoshinobu's fondness for
  photography — corroborated. Yamanami's desertion (2nd month Keiō 1) and forced
  seppuku with Okita as second — corroborated; note foreshadows it.
- (No Grok/Grokipedia sourced; a Grokipedia link surfaced in the Kinmon search
  and was IGNORED per rule 5.)

### Glossary rows added this batch: 39 (nested by section)

- People (33): Matsudaira Sadaaki, Jinbō Kuranosuke, Maki Izumi-no-kami,
  Fukuhara Echigo, Kijima Matabee, Kunishi Shinano, Fukuda Rihei (ch24); Takeda
  Kanryūsai, Yamazaki Susumu, Makita Sagami-no-kami Hirotaka, Toda Uneme-no-shō
  Ujiakira, Ohara Jinbee, Ōta Ichinoshin, Masuda Etchū, Kodama Minbu, Terashima
  Chūzaburō, Tsubaki Yajūrō (ch25); Itō Kashitarō, Ogata Shuntarō, Suzuki
  Mikisaburō (ch26); Shinohara Tainoshin, Kanō Michinosuke, Hattori Takeo, Sano
  Shimenosuke, Nakanishi Noboru, Utsumi Jirō, Matsumae Izu-no-kami (ch27);
  Hitotsubashi Yoshinobu, Ueno Hikoma, Matsumoto Ryōjun (ch28).
- Places (11): the Tenryū-ji, the Hamaguri Gate, Tennōzan, Kurodani, Mitajiri
  (ch24); the Gōō Shrine, the Sujikai Bridge, Fujinomori, the Takatsukasa
  mansion (ch25); the Kōshō-ji (ch27).
- Decided renderings kept verbatim: 旗本->"hatamoto", 武州多摩->"Bushū Tama",
  京都守護職->"the Kyoto Protector", 所司代->"the Shoshidai", 見廻組->"the
  Mimawarigumi", 総長->"general secretary", 公用方->"liaison office", 助勤
  ->"jokin". 蒔田 read Makita and 外島 read Toshima per the glossary/furigana.

### NOT re-noted (first-appearance discipline held)

- Already noted earlier and left un-renoted here: koku (B01); the Kyoto Protector
  / Shoshidai and Revere-the-Emperor-Expel-the-Barbarian (B03); hatamoto and
  jokin/vice-commander/inspector ranks (B03-B04); the era-year form and Genji/
  Keiō reign-names (earlier); the Tokaidō and Sanjō bridge (B03/B05); kinchō the
  sword-oath is NEW this batch (ch26) and noted once; the Tengu Party / Mito
  loyalism glossaried earlier, Takeda Kōunsai noted new (ch26); Kusaka Genzui,
  the Ikedaya, the Code of the Corps all glossaried/noted earlier.

### Digitization glitches / source oddities this batch

- None of substance. The source stays clean commercial digital text through
  ch24-ch28: no dittography, no stray U+200B lines, no doubled headings, no
  mojibake. Expressive gikun furigana continue (e.g. 将軍→たいじゅ); treated as
  semantic glosses, never romanized.
- 蒔田相模守広孝 is furigana'd まきた (Makita), not the "Maita" one often sees in
  English Shinsengumi sources; used the source's own reading, glossary note
  records the variant. 外島機兵衛 furigana とじま but the glossary's B04 decision
  "Toshima" kept for whole-book consistency (noted in the glossary tie-break).
