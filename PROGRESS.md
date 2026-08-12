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
