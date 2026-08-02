# HANDOFF — The Whistling Wind (风萧萧) by Xu Xu

State: Batch B09 (ch42 through ch45: Chapters 42 to 45) is COMPLETE, checked, and
committed. The cumulative EPUB `out/The Whistling Wind.epub` has 46 of 60 chapters
translated (ch00 through ch45); the other 14 still link to their skeleton outlines
and the TOC stays fully navigable. Next up: Batch B10 = ch46 through ch48
(Chapters 46 to 48).

## Message to paste into the next chat

```
Whistling Wind B10 — Chapters 46 to 48 (ch46 through ch48).

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Then do Batch B10 = units ch46 through ch48
(Chapters 46 to 48 of the novel; ~17,009 source chars) end to end, following the
per-batch pipeline in CLAUDE.md.

Concretely:
- The ingest is regenerable but NOT committed (data/src/ is gitignored). If
  data/src/ is missing in a fresh checkout, run scripts/ingest_epub.py source.epub
  once to repopulate it before you start.
- Read the batch's source text from data/src/ for each unit (ch46 =
  50_chapter48.txt, ch47 = 51_chapter49.txt, ch48 = 52_chapter50.txt). Quote the
  source VERBATIM in the bilingual QC file; do not re-type or paraphrase it. The
  fastest safe way is the batch helper scripts/_zip_bilingual.py: author an
  English-only file (one paragraph per line, in order), and it pairs your English
  with the VERBATIM source paragraphs copied from data/src (stripping the UTF-8 BOM
  and the two duplicated chapter-numeral heading lines the source repeats), erroring
  if the paragraph counts differ. Then confirm with the whitespace-stripped char
  comparison of the joined '>' blockquotes vs the joined source paragraphs (used
  every batch).
- B10 is the theft operation and the ball (narrative, not diary): ch46 the night
  before, the phone call from Bai Ping, and going to the masked ball; ch47 opens
  INSIDE the safe-room after the theft — the narrator under the desk, another
  intruder at the safe, a bomb in the safe — then the climb back down; ch48 opens
  with the 5 o'clock unmasking ("three more dances," 撤掉面具), Miko, and Mei Yingzi
  ("你看到蓝尾蛇了吗？" — 蓝尾蛇 "blue-tailed snake" is a code name; decide a rendering
  and, if it recurs, a glossary row/first-appearance note). Watch for a new
  Japanese name in ch48 (朝村登水子 "朝村登水子的真面目" — give it a plausible Japanese
  reading and a glossary row). The diary convention is a ch42 thing and does not
  recur here, but if any diary extract reappears use the ch42 scheme (note 64):
  each entry a self-contained double-quoted paragraph; lone 「──」 → a lone "—"
  paragraph, lone 「……」 → "…"; fused 「──X」 → "—X", 「X──」 → "X—"; the narrator's
  「──...──」 block-fences around his "My note:" glosses.
- Translate to the register in CLAUDE.md: clean, flowing English narrative prose
  in the book's own first-person voice; all apparatus lives in the notes, never
  inline. Never invent bridging text and never silently drop material; if a
  passage is genuinely ambiguous or the source is cut/corrupt, footnote it and
  leave it visible. Render the recurring source digitization glitches to plain
  sense (and list them in PROGRESS), footnoting only genuine reading uncertainty.
- Author one aligned bilingual QC file out/<id>_bilingual.md per unit (a first
  line "## H2 Chapter N" for the title, then, for each source paragraph, a "> "
  blockquote line followed by one English paragraph; skip the duplicated
  chapter-number heading lines the source repeats; a lone source "──" divider
  line is rendered as a lone "—" paragraph, and verse is kept line-by-line).
  Generate the reading text and parity source with scripts/split_bilingual.py
  (pass the source chapter heading as the third argument, e.g. "四十六"). WATCH the
  paragraph count: _zip_bilingual.py errors on a mismatch — if it does, one English
  line has merged two source paragraphs (a common slip on tag-less dialogue where a
  paragraph ends with a colon "说：" and the quote is a separate source paragraph; in
  B08 ch39 a whole letter paragraph was dropped and caught only by the count). ALSO
  watch for source dittography and multi-speaker paragraphs (B08 ch40 had two source
  paragraphs each carrying two or three speakers' quotes in one paragraph — render all
  the quotes of one source paragraph on the one English line; ch44 in B09 had 「自然。」
  「真的？」, two speakers, on one line).
- Run the checks and record them in PROGRESS.md: check_numbers.py --noise
  data/noise.txt on each bilingual file; check_structure.py --config over the batch
  (build a small {docs,sources,notes,variants} config over the translated units, as
  B09 did in scratch/b09_check.json; scratch/ is gitignored, so regenerate it — and
  in the variants map put ONLY wrong forms in each value list, NEVER the canonical
  itself, or every correct occurrence is flagged as drift). Blind double translation
  on the analytical/lyrical passages, sampled on plain narration; round-trip back-
  translation as an omission check; a 3 to 5 percent random deep audit with the
  observed error rate reported. Extend data/noise.txt whenever the number check flags
  a non-quantity numeral (write down what and why).
- Number-check notes: the built-in NOISE strips clock times AND whole-hour "点钟"
  times; B07 added 两/兩 to those top clock/duration char classes, so 两点四十分 /
  两点钟 / 两分钟 strip whole (before the built-in 十分 "=very" can eat the "十分" out
  of "四十分"). The bare-一 measure patterns AND the two 一-idiom patterns all carry a
  negative lookbehind, so compound numbers like 十一个 / 十一点钟 / 十一日 / 十一时
  survive (B04). B06 added, at the TOP block, r"[一二三四五六七八九]十多" (mirroring the
  existing 四十几): the built-in r"[十几幾]多" was eating the "十多" out of 五十多
  ("fifty-odd") and orphaning a 五 read as 5. WORD_NUM already carries first/second/
  third...tenth AND the day-of-month/century ordinals "eleventh" (11), "twelfth" (12),
  "thirteenth" (13, B09), "seventeenth" (17), "twentieth" (20), "twenty-third" (23),
  and MONTHS maps january..december to 1..12, so "the twelfth of March" accounts for
  三月十二日 (B09); add the next such ordinal the same way (B09 added twelfth/thirteenth
  for the masked-ball dates). NOTE clock caveat: "点半" (half past) and "时" times are
  NOT stripped by the 点钟/点X分 patterns (they need 钟 or X分), so 十二点半 → 12,
  五时半 → 5, 十一时三刻 → 11 survive as bare numerals and must appear in the English
  ("half past twelve", "half-past-five", "eleven forty-five"); B09 added
  r"[一二三四五六七八九十]刻" so the 三刻 in 十一时三刻 strips and 十一时 → 11 survives whole.
  Prefer noise/prose fixes over editing the script (a spelled "three hundred and forty"
  parses to 3/40/300, so write such figures as digits; write 十来个 as "ten or so", not
  "a dozen or so", and 十来步 as "ten steps or so", so the source 10 survives). Proportion
  idioms 四分/八分/六分/二分 ("four parts in ten" etc., B09 ch45) are NOT stripped and
  render literally as "four parts... eight... six... two". LIVE GOTCHAS: the bare-一
  measure rule strips "一次" out of the idiom 一次两次 and orphans the 两 (B05) — reword the
  English to carry the count; likewise 第二个人 / 第二方面 / 两个人 must be reworded so the
  第二/两 survives ("a second person", "in the second place", "the two of us"), not "no one
  else / on the other / together" (B09 ch42/ch43). Reduplicated count-idioms like 两两三三
  ("in twos and threes", B06) are noise, not quantities. Tenths fractions (十分之七, and the
  B09 十分之一/十分之九) are stripped by the built-in fraction pattern and NOT re-verified, so
  render them faithfully yourself; clock times, durations, positional years (一九四一年), 里
  speeds, bow angles, and the arm-elevation degrees (六十七八度 etc., B09) likewise are not
  re-verified. data/noise.txt already carries: 两样, 十足, 光芒万丈, a numeral+丈 pattern
  (丈 -> feet), the 四十二四十三 artifact; the B04 additions (二房东 / 飘零 / 二○号 /
  [一二三四五]更 / 六角 / 大千世界); the B05 additions 两[手膝] / 连三接四 / 零碎; the B06
  additions 万物 / 两两三三 / 畸零 / 万国; the B07 additions 凋零 / 四顾 / 万岁 / 百般; the
  B08 additions 四肢 / 四望 / 万念; and the B09 additions 千种 ("a thousand kinds"), 三五牌
  (State Express 555), 十字 ("cross" the shape), and [一二三四五六七八九十]刻 (quarter-hour).
- Footnotes into notes.json (about 3 per chapter-equivalent; anchors must be verbatim
  substrings of the English prose, matched BEFORE markup - use ASCII apostrophes/quotes
  and the exact capitalisation of the prose; XHTML bodies use NUMERIC character
  references, never named entities - escape every non-ASCII codepoint to &#dec;, reuse
  that pattern). Numbering is continuous and assigned by the builder, so just append to
  each unit's list; B09 ended at note 69. Recurring subjects already have their note at
  first appearance in B01-B09 (Stephen, Bai Ping, Mei Yingzi, Helen, Mrs. Manfield,
  Mrs. Stephen, Dr. Philip, Ah Mei, Jimi the cat, the Solitary Island, the Paramount,
  Renji Hospital, the narrator's name Xu, the Arcadia, West Lake landmarks, Geling, the
  National Academy of Art, Mario Paci, Jessfield Park, DD's Café, Route Prosper Paris,
  Tao Yuanming, the Palace of the Moon, Wu Zetian / the Western Empress Dowager, the
  Pacific war outbreak, the Pudong internment, the July 7 Incident, Sai Jinhua, Shitao,
  Hongkou, the Benner Inn, the Standford, the Fuyuan native bank, the Hailin Broadcasting
  Station, the narrator's alias Chen Ji, the International Cemetery, Isadora Duncan, the
  "true gold fears no fire" proverb, the Great World, Jiangwan, the Greater East Asia
  Co-Prosperity Sphere, the heroine of Ghost Love, the 小鹿乱撞 "little deer" idiom, Flaubert,
  Qingdao, Stoyevsky, and the B09 references: the diary presentation (note 64), Mei Yingzi
  as the diary's remembered speaker (note 65), State Express 555 / Lucky Strike (note 66),
  the interior / Free China (note 67), Korea a Japanese colony since 1910 / Miko (note 68),
  and quinine / the suicide pills (note 69)), so do NOT re-note them; footnote only
  genuinely new refs.
- Glossary discipline: glossary.json (120 term rows) already fixes the whole cast and
  the Shanghai/Hangzhou/Qingdao geography, dance halls, restaurants, the cheongsam
  (旗袍), and the B09 additions (国泰 the Cathay cinema, chez Rovere restaurant), on top
  of the whole earlier set (Ah Mei 阿美, Jimi 吉迷, Dr. Gaolang 高朗 / Gaoye Road 高叶路,
  Honsa Jiro 本佐次郎, Umetake 梅武, Colonel Arita 有田大佐, Miko 米可, the Standford,
  Chen Ji 陈寂, Beiping 北平, Qingdao 青岛, Stoyevsky 史托亦夫斯基, the Hailin Broadcasting
  Station, the Racecourse, the International Cemetery, Jing'an Temple, Malang Road, the
  Great World, Jiangwan 江湾, the Kaidi Restaurant 凯第饭店, the White Palace 白宫舞厅,
  Greater East Asia 大东亚). REUSE those exact renderings; add a new row for every new
  proper noun / place / org / term with status (attested / provisional / decided) and
  attestation, deciding the one rendering before you romanize it. Fact-check any
  historical/real-world reference against real scholarship (Wikipedia / Baidu Baike /
  academic), never LLM-generated sources (never Grok/Grokipedia), and say corroborated /
  uncorroborated / contradicted.
- Rebuild the cumulative EPUB: python3 scripts/build_reading_epub.py
  "out/The Whistling Wind.epub" (the TOC stays pending-aware). Run
  python3 scripts/qa_epub.py "out/The Whistling Wind.epub" until green.
- Commit on the one working branch claude/the-whistling-wind. Rewrite HANDOFF.md
  so its first section is the paste-ready kickoff for Batch B11 = ch49 through ch52.
- Cite chapters, never page numbers. Do not pause for approval mid-batch.
- Deliver out/The Whistling Wind.epub to me as an attached file in the chat.
```

## Project facts a fresh session needs

- Deliverable filename: `out/The Whistling Wind.epub`. Working branch:
  `claude/the-whistling-wind` (one branch only; do not spin off others). If a
  session opens you on a different branch, move the work onto this one and delete
  the stray branch, per CLAUDE.md rule 2. (B01-B09 were each started on a stray
  branch and consolidated here; the stray branch is then deleted, local and
  remote.)
- Structure (see book.json): ch00 = About the Author (front matter);
  ch01..ch58 = the novel's 58 numbered chapters (源 一..五十八); ch59 =
  Impressions of Xu Xu (appendix). Units have no sub-sections.
- Pipeline artifacts that persist across batches: glossary.json (120 term rows),
  notes.json (69 notes so far), data/noise.txt (project number-check noise),
  scripts/_zip_bilingual.py (the batch helper), scripts/check_numbers.py (its
  1-idiom and measure patterns carry negative lookbehinds so date/time compounds
  survive; the top clock/duration classes include 两/兩; WORD_NUM carries the
  ordinals incl. twelfth/thirteenth; MONTHS maps month names to 1..12; see the B05
  一次两次 gotcha above), data/src/ (all source text, regenerated by the ingest;
  gitignored), data/zh/ (parity source, regenerated per unit by split_bilingual.py),
  scratch/ (gitignored; put the check_structure config here, e.g. b09_check.json).
- Deferred source material to handle later, NOT dropped: `chapter61.html`
  (edition/imprint note) becomes the translated Colophon on the LAST batch via
  back_matter.json; `coverpage.html` abstract and `chapter1.html` (source TOC)
  are intentionally not body chapters (recorded in book.json `_source_note`).
- Title note (in the translator's note already): 风萧萧 echoes 风萧萧兮易水寒,
  the parting song for the assassin Jing Ke; keep that note of doomed sacrifice
  audible.

## Batch plan (approved)

| Batch | Units | Chars | Status |
|---|---|---|---|
| B01 | ch00 to ch08 | 18,512 | DONE |
| B02 | ch09 to ch14 | 19,469 | DONE |
| B03 | ch15 to ch17 | 16,230 | DONE |
| B04 | ch18 to ch21 | 19,962 | DONE |
| B05 | ch22 to ch25 | 18,788 | DONE |
| B06 | ch26 to ch31 | 20,716 | DONE |
| B07 | ch32 to ch36 | 18,411 | DONE |
| B08 | ch37 to ch41 | 17,945 | DONE |
| B09 | ch42 to ch45 | 14,344 | DONE |
| B10 | ch46 to ch48 | 17,009 | next |
| B11 | ch49 to ch52 | 17,733 | |
| B12 | ch53 to ch57 | 20,620 | |
| B13 | ch58 to ch59 | 15,635 | (last: back matter + whole-book QA) |
