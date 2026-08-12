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
