# HANDOFF — The Sword Roars in the West Wind

## Message to paste into the next chat

> Paste this VERBATIM to start Batch 7. It is the only bridge between
> conversations; HANDOFF/PROGRESS/book.json describe the state, but the pages
> are the voice, so read the last two pages of ch06's English first.

```
Sword Roars B07

Read CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. Work on branch claude/the-sword-roars (the canonical book
branch; if the harness starts you on a stray per-task branch, consolidate per
CLAUDE.md rule 2). Run ./setup.sh first.

Do Batch 7 = Chapter Seven, "大隐隐于市 / The Great Hermit Hides in the City"
(ch07), PDF 150-171, printed 135-156, end to end per the pipeline in CLAUDE.md.
Seven sections: ch07s01 一、全国苏维埃区域代表大会 (PDF 151, printed 136),
ch07s02 二、神秘医院 (PDF 153, printed 138), ch07s03 三、以子之矛，攻子之盾
(PDF 158, printed 143), ch07s04 四、多重保险 (PDF 160, printed 145), ch07s05
五、分批进场，一律不准外出 (PDF 164, printed 149), ch07s06 六、唱起《国际歌》
(PDF 166, printed 151), ch07s07 七、真相只有一个 (PDF 168, printed 153).
Simplified Chinese, horizontal; OCR chi_sim --psm 6; crop --left 0.06 --right
0.95 --top 0.11 --bottom 0.955; offset is a constant 15 (printed = pdf - 15),
no plate drift through ch06, but READ each opener's folio off the scan.

BEFORE translating, read the final two pages of Chapter Six's English
(out/ch06_reading.md) so the voice carries over unbroken. Chapter One remains
the FROZEN register reference: run check_register.py --ref out/ch01_reading.md
on ch07 and record it (judge on the narratorial signals per
references/register-drift.md; the dialogue-contraction metric moves with how
dialogue-heavy the chapter runs, and is not itself drift). Chapters One-Six's
data/zh were hand-transcribed off the scans (OCR too noisy on the proper names,
assemble breaks on figure/opener pages); do the same for ch07 where assemble
misaligns, and keep parity exact. In the hand-transcribed data/zh/ch07.txt mark
the chapter title with ### (same prefix as the section heads), NOT ##. Cite
printed folios in notes, never PDF pages. Never invent bridging text: if OCR
breaks mid-sentence or a leaf is damaged, crop the scan and read the real
continuation, or footnote the gap. Verify every name, number and low-confidence
span against a magnified crop before writing. Consult authority.json and
glossary.json for settled renderings (esp. the Central Special Branch, the Red
Squad, the Zhongtong, the Party Affairs Investigation Section, Zhou Enlai, Gu
Shunzhang, Chen Geng, the concession streets, and the radio thread from ch06:
Li Qiang, Zhang Shenchuan, the Hao cipher). This chapter runs a hidden-hospital
/ national-Soviet-congress thread ("the Great Hermit hides in the city", the
secret hospital, "his own spear against his own shield", singing the
Internationale); expect fresh institutions and material culture to note. Add
ch07 to data/content_config.json when you translate it, or the displacement
check silently skips it.

Deliver the built EPUB attached in the chat, and paste the Batch 8 kickoff
verbatim in the same reply.
```

## DONE (one line per batch; do not redo)
- Survey: structure, offsets, style contract, skeleton EPUB. (earlier session)
- **B01 = ch01 (voice gate):** full translation (165 paragraphs), 115 footnotes,
  12 figures, glossary seeded, all checks green, epubcheck clean, blind-critique
  loop run, held at and passed the human voice gate. Details in PROGRESS.md.
- **B02 = ch02:** full translation (56 paragraphs), 28 footnotes, 5 figures,
  14 new glossary rows; all checks green, qa_epub PASS, epubcheck 0/0.
- **B03 = ch03 "Who Is Judas":** full translation (146 paragraphs), 33 footnotes,
  4 figures, 59 new glossary rows; all checks green, qa_epub PASS, epubcheck 0/0.
- **B04 = ch04 "Bloodshed on Avenue Joffre":** full translation (131 paragraphs),
  24 footnotes, 10 figures, 62 new glossary rows; all checks green, qa_epub
  PASS (200 notes total), epubcheck 0/0.
- **B05 = ch05 "A Real Vault, a False Marriage":** full translation (66
  paragraphs), 27 footnotes, 5 figures, 75 new glossary rows; all checks green,
  qa_epub PASS (227 notes total), epubcheck 0/0.
- **B06 = ch06 "It Was Not Me, It Was the Wind":** full translation (165
  paragraphs, 3 {v} block quotes), 28 footnotes, 3 figures, ~120 new glossary
  rows; parity 165=165, numbers 0, align/content/entities clean, anchors 28/28,
  register within tolerance (dialogue metric high, correct for a dialogue-rich
  chapter), qa_epub PASS (255 notes total), epubcheck 0/0. Details in PROGRESS.md.

## Tooling in place — DO NOT REVERT
- `scripts/indents.py`: furniture-band drop by y-position (`FURNITURE_TOP=0.11`,
  `FURNITURE_BOTTOM=0.955`). Folio + running head are one TOP band; no foot.
- `scripts/check_numbers.py`: arabic+万 combiner ("31万"=310,000) BEFORE the
  noise loop; matches English number-WORDS, ordinals, and MONTH NAMES.
- `build_reading_epub.py` alt-attribute escaping (fixed in B04): figure `alt`
  is emitted through `html.escape(..., quote=True)`. Keep it; prefer single
  quotes in alt.
- `data/noise.txt`: this book's event-date names, numeral-bearing proper names,
  decade labels, idioms. B02-B06 blocks appended. B06 block: 四成里, 曾三, 零陵,
  万航渡路 (romanized names with a numeral); 零敲碎打, 零配件, 零件, 十字路口,
  六神无主, 千刀万剐, 千斤重担, 烽火万里, 百姓 (idioms; the English carries the
  magnitude in words); 四一二 (the "4-12" event date-name). Extend per its
  header; longest literal first; comment every entry. Each entry strips a SOURCE
  numeral carrying no cardinal quantity, so none can mask a real drop.
- `data/content_config.json`: docs+sources map for check_content; now covers
  ch01-ch06. ADD ch07 when you translate it, or the displacement check silently
  skips it. Run check_content with `--config data/content_config.json`.
- OCR crop for this book: `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955
  --lang chi_sim --psm 6`. Offset constant 15 (printed = pdf - 15).
- **Parity gotcha (confirmed B05/B06):** in the hand-transcribed
  `data/zh/chNN.txt`, mark the chapter title `### ` (same prefix as the section
  heads), NOT `## `. `check_structure` strips only lines starting with the `###`
  prefix on the source side; a `## ` chapter line survives and inflates the
  source count by one. On the English side (`out/chNN_reading.md`) the chapter
  title is `## ` and section heads `### `; both are stripped there.
- **Set-off block quotes:** displayed/indented block quotations get the `{v}`
  marker at the START of the line, in BOTH zh and en; `check_structure` strips
  the prefix before parity, so `{v}` lines still count one-for-one. Inline
  quotations (with quote marks, not indented) are ordinary paragraphs, no marker.
- **Glossary placement gotcha:** `apparatus_merge.py` writes glossary rows at the
  JSON TOP LEVEL; the builder's render_glossary chokes on a flat row. Add rows
  DIRECTLY into the people/organizations/places/terms sections with a
  re-read-verified one-shot script (deleted after use). Notes and figures go
  through apparatus_merge normally.
- **Glossary vs check consistency (B05/B06 lesson):** set each new glossary row's
  `en` to the form you ACTUALLY render. `qc_entities` is lenient (en / pinyin /
  first-or-last word), but `check_content` matches the full capitalised `en`, so
  a row that says "Xiong Gengwu" while the text says "Gengwu" is flagged as
  displaced. Render a DECIDED term in its decided form; do not re-translate it.
- **figures.json `file` must be a BASENAME**; the builder prepends `data/figs/`
  and `images/`. Figure `before` anchors must fall in the FIRST ~80 chars of a
  paragraph AND the anchor STRING itself must be short enough to sit within that
  window (B06: a 95-char anchor failed the build; shortened to a 40-char prefix).
  Note anchors CANNOT sit on the `##`/`###` chapter-title line.
- **Number-check "keep the counted numeral" rule (STYLE.local, applied B06):**
  when the source counts a NAMED group (两/三/四/十七 + 人/同志/etc. with the
  members named), keep the numeral in English rather than letting the names
  carry it: 六大 = "Sixth Congress" (not "the congress"), 四人 = "four in all",
  两人 = "the two of them", 十七人 = "seventeen ... among them". The names do
  not carry the count for the reader OR for check_numbers.
- **Inline citation style:** the author's `（作者，年份）` source citations render
  inline as `(Author, YEAR)` right after the quoted material.

## Renderings settled through B06 (also in glossary.json / STYLE.local.md)
- 中央特科 = the Central Special Branch; 红队 / 打狗队 = the Red Squad / the
  dog-beating squad; 中统 = the Zhongtong; 党务调查科 = the Party Affairs
  Investigation Section (KMT Central Organization Dept, Zhongtong's forerunner);
  中央特科第四科/三科 = the Fourth / Third Section.
- **B06 radio thread (carry forward):** 涂作潮 = Tu Zuochao (codename
  "Carpenter"); 李强 = Li Qiang (Fourth Section chief, radio); 张沈川 = Zhang
  Shenchuan (built the first secret station); 苏刚达 = Su Gangda (real name 任玑
  Ren Ji); 蔡叔厚 = Cai Shuhou; 夏衍 = Xia Yan; 恽代英 = Yun Daiying; 豪密 = the
  Hao cipher; 木匠 = "Carpenter"; 风语者 = windtalker.
- **B06 concession streets:** 迈尔西爱路 = Route Cardinal Mercier; 亚尔培路 =
  Avenue du Roi Albert; 极司非而路 = Jessfield Road (今万航渡路 Wanhangdu Road);
  大西路 = Great Western Road; 福煦路 = Avenue Foch; 古拔路 = Route Voisin; 赫德路
  = Hart Road; 康脑脱路 = Connaught Road; 有恒路 = Youheng Road; 三马路 = Sanma
  Road. Uncertain French names NOT invented; Chinese-named roads kept pinyin.
  Reused: 巨籁达路 = Rue Ratard, 西摩路 = Seymour Road.
- **B05 people (still current):** 熊瑾玎 = Xiong Jinding, 朱端绶 = Zhu Duanshou,
  熊畅苏 = Xiong Changsu; 巨籁达路 = Rue Ratard, 云南路 = Yunnan Road; 老虎灶 =
  laohuzao, 石库门 = shikumen, 亭子间 = tingzijian.
- Concession streets (B04): 霞飞路 = Avenue Joffre; 蒲石路 = Rue Bourgeat.
- Numbers: full value; death ages render "at the age of X" (享年X岁 = died aged X).

## Voice sheets (carry forward)
- **The author (Ye Xiaoshen):** warm, buttonholing popular-history narrator with
  a sardonic edge and open reverence for his subjects; heat in the verbs and
  rhythm, ration exclamation and rhetorical questions. He does sustained
  SOURCE-CRITICISM (in B06 he corrects the received "Jessfield Road" address of
  the first station, and weighs the Xiong-Zhu marriage accounts in B05); keep
  that dry, skeptical edge.
- **B06 registers established:** the tradecraft narrative (the raid, the painter's
  ruse) runs quick and wry; the martyrdom close (the prison, Yun Daiying's poem,
  the deaths of Shen Kanfu / Mai Jianping / Xie Xiaokang / Zhang Qingfu) runs
  grave and full-temperature, footnoting the verdict, never laundering the
  framing. Su Gangda's prison voice is dry, defiant, and quick-witted (the
  thought-assessment-chief exchange). Zhang Sengbao (Zhang Shenchuan's daughter,
  the witness) is warm and plain.
- **Zhou Enlai:** warm and big-brotherly with juniors (teasing Li Qiang, "the
  best man for it"); distinct from the martyr-proclamation and deathbed
  registers of earlier chapters. **Chen Geng / Li Qiang / quoted memoirists:**
  clipped and factual. **Gu Shunzhang:** the foil, written hot and contemptuous
  (in B06 he quibbles and scapegoats Yang Zhishui after the raid).
- (B01-B05 voice sheets for the Party leaders in committee, Li Zheshi, Luo
  Yinong, He Zhihua, the Xiong-Zhu couple, etc. still stand for reruns.)

## Where the story stands
Chapters One-Two founded the Special Branch and drew the moral contrast; Chapter
Three ("Who Is Judas") ran the first great betrayal (Luo Yinong); Chapter Four
("Bloodshed on Avenue Joffre") ran the double-agent thread (Bai Xin); Chapter
Five ("A Real Vault, a False Marriage") turned to the Party's own machinery (the
Xiong-Zhu safe house on Yunnan Road). Chapter Six ("It Was Not Me, It Was the
Wind") is the radio-and-martyrdom chapter: how Li Qiang and Zhang Shenchuan
built the Party's first wireless station and codes (the Hao cipher), trained
operators under the Welfare Electric Company cover on Rue Ratard, and how Gu
Shunzhang's insistence on massing the trainees led to the December 1930 raid,
the arrests, the prison deaths, and (through the trainees' iron discipline)
"not one exposed as a Communist." Chapter Seven, "The Great Hermit Hides in the
City," turns to the National Congress of Soviet Areas and a secret hospital.

## Next-batch scope
B07 = ch07, PDF 150-171 (printed 135-156), seven sections ch07s01-s07 (openers
at PDF 151,153,158,160,164,166,168). Expect figures (eyeball every page;
find_figures misses line art and dense newsprint) and quoted memoir material.

## Open traps / environment
- `data/zh/` is gitignored (copyright); a fresh checkout cannot regenerate the
  hand-transcribed sources. Use per-unit `check_structure --pairs`.
- `find_figures.py` misses dense-newsprint clippings and line-art diagrams;
  eyeball every page and hand-crop. When cropping a captioned photo, exclude the
  printed caption line (the builder renders the translator's caption). Washed-out
  full-page chapter-divider illustrations (e.g. p0124, p0149) are design
  furniture, not captioned figures.
- `tests/run_tests.py` "hook stands down on template stub" FAIL is benign (a
  real kickoff is present). Not a regression. setup.sh prints "CHECKER
  REGRESSION TESTS FAILED" for this one line only; ignore it.
- `OMP_THREAD_LIMIT=1` mandatory for tesseract; verify `pgrep -c tesseract` = 0
  after OCR. epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (setup fetches).
- `authority.json` is updated on WHOLE-BOOK completion, not per batch; the
  B01-B06 decided renderings are in glossary.json and listed above.
- The Preface (ch00, PDF 6-15) is still UNTRANSLATED; it and the back matter
  (Works Cited ch16, Afterword ch17) fold into the final batches.
- Branch hygiene: the canonical branch is `claude/the-sword-roars`. The harness
  may start a session on a stray per-task branch; consolidate onto the canonical
  branch and delete the stray (local + remote) per CLAUDE.md rule 2. (B06 started
  on a stray `claude/sword-roars-ch06-*`, which held no unique commits;
  consolidated and pruned.)
