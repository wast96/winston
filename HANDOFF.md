# HANDOFF — The Sword Roars in the West Wind

## Message to paste into the next chat

> Paste this VERBATIM to start Batch 6. It is the only bridge between
> conversations; HANDOFF/PROGRESS/book.json describe the state, but the pages
> are the voice, so read the last two pages of ch05's English first.

```
Sword Roars B06

Read CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. Work on branch claude/the-sword-roars (the canonical book
branch; if the harness starts you on a stray per-task branch, consolidate per
CLAUDE.md rule 2). Run ./setup.sh first.

Do Batch 6 = Chapter Six, "不是我，是风 / It Was Not Me, It Was the Wind"
(ch06), PDF 124-149, printed 109-134, end to end per the pipeline in CLAUDE.md.
Ten sections: ch06s01 一、代号"木匠" (PDF 125, printed 110), ch06s02 二、人间蒸发
(PDF 127, printed 112), ch06s03 三、快给巡捕房挂电话 (PDF 129, printed 114),
ch06s04 四、孟尝君风度 (PDF 131, printed 116), ch06s05 五、昨天晚上谁值班 (PDF 133,
printed 118), ch06s06 六、电灯闹鬼了 (PDF 134, printed 119), ch06s07 七、福利电器
公司 (PDF 137, printed 122), ch06s08 八、顺手拉开身后窗帘 (PDF 140, printed 125),
ch06s09 九、没有一人暴露是共产党员 (PDF 141, printed 126), ch06s10 十、告慰亲人，
明天再见 (PDF 142, printed 127). Simplified Chinese, horizontal; OCR chi_sim
--psm 6; crop --left 0.06 --right 0.95 --top 0.11 --bottom 0.955; offset is a
constant 15 (printed = pdf - 15), no plate drift through ch05, but READ each
opener's folio off the scan. This is a big chapter (26 pp., 10 sections); pace it.

BEFORE translating, read the final two pages of Chapter Five's English
(out/ch05_reading.md) so the voice carries over unbroken. Chapter One remains
the FROZEN register reference: run check_register.py --ref out/ch01_reading.md
on ch06 and record it (judge on the narratorial signals per
references/register-drift.md; the dialogue-contraction metric will move with how
dialogue-heavy the chapter runs, high or low, and is not itself drift).
Chapters One-Five's data/zh were hand-transcribed off the scans (OCR too noisy
on the proper names, assemble breaks on figure/opener pages); do the same for
ch06 where assemble misaligns, and keep parity exact. Cite printed folios in
notes, never PDF pages. Never invent bridging text: if OCR breaks mid-sentence
or a leaf is damaged, crop the scan and read the real continuation, or footnote
the gap. Verify every name, number and low-confidence span against a magnified
crop before writing. Consult authority.json and glossary.json for settled
renderings (esp. the Central Special Branch, the Red Squad, the Zhongtong, Zhou
Enlai, Chen Geng, Gu Shunzhang, the tingzijian, the concession streets). This
chapter runs a tradecraft/martyrdom thread (codename "Carpenter", the Welfare
Electric Company front, arrests, "not one exposed as a Communist"); expect fresh
tradecraft and material culture to note. Add ch06 to data/content_config.json
when you translate it, or the displacement check silently skips it.

Deliver the built EPUB attached in the chat, and paste the Batch 7 kickoff
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
  paragraphs), 27 footnotes, 5 figures, 75 new glossary rows; parity 66=66,
  numbers 0, align/content/entities clean, register within tolerance (dialogue
  metric HIGH, correct for a dialogue-rich chapter), qa_epub PASS (227 notes
  total), epubcheck 0/0. Details in PROGRESS.md.

## Tooling in place — DO NOT REVERT
- `scripts/indents.py`: furniture-band drop by y-position (`FURNITURE_TOP=0.11`,
  `FURNITURE_BOTTOM=0.955`). Folio + running head are one TOP band; no foot.
- `scripts/check_numbers.py`: arabic+万 combiner ("31万"=310,000) BEFORE the
  noise loop; matches English number-WORDS, ordinals, and MONTH NAMES.
- `build_reading_epub.py` alt-attribute escaping (fixed in B04): figure `alt`
  is emitted through `html.escape(..., quote=True)`. Keep it; still prefer
  single quotes in alt.
- `data/noise.txt`: this book's event-date names, numeral-bearing proper names,
  decade labels, idioms. B02-B05 blocks appended (B05: 四马路, 三马路, 朱葆三路,
  熊笑三, 零星, 几十万, 几千里). Extend per its header; longest literal first;
  comment every entry. B05's two 几-quantities are approximate hyperbole the
  digit parser cannot match in idiomatic English; the English carries the
  magnitude, so the noise entry cannot mask a real drop.
- `data/content_config.json`: docs+sources map for check_content; now covers
  ch01-ch05. ADD ch06 when you translate it, or the displacement check silently
  skips it.
- OCR crop for this book: `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955
  --lang chi_sim --psm 6`. Offset constant 15 (printed = pdf - 15).
- **Parity gotcha (confirmed B05):** in the hand-transcribed `data/zh/chNN.txt`,
  mark the chapter title `### ` (same prefix as the section heads), NOT `## `.
  `check_structure` strips only lines starting with the `###` prefix on the
  source side; a `## ` chapter line survives the filter and inflates the source
  count by one.
- **Glossary placement gotcha:** `apparatus_merge.py` writes glossary rows at the
  JSON TOP LEVEL; the builder's render_glossary chokes on a flat row. Add rows
  DIRECTLY into the people/organizations/places/terms sections with a
  re-read-verified one-shot script (deleted after use). Notes and figures go
  through apparatus_merge normally.
- **Glossary vs check consistency (B05 lesson):** set each new glossary row's
  `en` to the form you ACTUALLY render (short or long). `qc_entities` is lenient
  (accepts en / pinyin / first-or-last word), but `check_content` matches the
  full capitalised `en` string, so a row that says "Xiong Gengwu" while the text
  says "Gengwu" is flagged as displaced. When a decided term (e.g. laohuzao) is
  already in the glossary, RENDER the decided form; do not re-translate it.
- **figures.json `file` must be a BASENAME**; the builder prepends `data/figs/`
  and `images/`. Figure `before` anchors must fall in the FIRST ~80 chars of a
  paragraph; note anchors CANNOT sit on the `##`/`###` chapter-title line.
- **Set-off blocks:** displayed block quotations and dated diary/log entries get
  `{v}`; a document's signature and date can each be their own `{v}` line.
  Both zh and en must carry identical `{v}` lines.
- **Inline citation style:** the author's `（作者，年份）` source citations render
  inline as `(Author, YEAR)` right after the quoted material.

## Renderings settled through B05 (also in glossary.json / STYLE.local.md)
- 中央特科 = the Central Special Branch; 红队 / 打狗队 = the Red Squad / the
  dog-beating squad; 中统 = the Zhongtong; 中央特科一科 = the First (General
  Affairs) Section; 中央政治局 = the Central Politburo; 中央军委 = the Central
  Military Commission; 中央秘书处 = the Central Secretariat; 中组部 = the Central
  Organization Department.
- **B05 people (carry forward):** 熊瑾玎 = Xiong Jinding ("Boss Xiong"), 朱端绶 =
  Zhu Duanshou, 熊畅苏 = Xiong Changsu (their daughter, the chapter's witness);
  龚饮冰 = Gong Yinbing (his predecessor), 龚育之 = Gong Yuzhi; 熊笑三 = Xiong
  Xiaosan (Nationalist general, Xiong's estranged son); 南汉宸 = Nan Hanchen;
  洪扬生 = Hong Yangsheng; the child names 耕午 = Gengwu, 桑渝 = Sangyu, 骊午 =
  Liwu. Descendants and biographers by standard pinyin (all in glossary).
- **B05 places/terms:** 福兴字号 = the "Fuxing" firm; 云南路 = Yunnan Road (today
  Yunnan Middle Road); 天蟾舞台 = Tianchan Stage; 生黎医院 = Shengli Hospital;
  跑马厅 = the Racecourse; 湘鄂西 = West Hunan-Hubei; 洪湖 = Honghu; 陶乐春 =
  Taolechun. Streets: 巨籁达路 = Rue Ratard, 马斯南路 = Rue Massenet, 慎成里 =
  Shenchengli, 泰辰里 = Taichenli, 眉寿里 = Meishouli (里-compounds as -li);
  **康悌路 = Kangti Road** (French name uncertain, kept pinyin). Terms: 抄靶子 =
  frisking, 明矾水 = alum water, 红烧狮子头 = braised lion's-head meatballs, 伍豪 =
  Wuhao, 十里洋场 = the Ten-Li Foreign Settlement, 四人帮 = the Gang of Four,
  词牌 = tune-title. Reused unchanged: 老虎灶 = laohuzao (decided; ch03 gloss),
  石库门 = shikumen, 亭子间 = tingzijian, 蒲石路 = Rue Bourgeat.
- Concession streets (B04): 霞飞路 = Avenue Joffre; 蒲石路 = Rue Bourgeat; 云南路
  glosses render "(today X Road)". Uncertain French names kept as pinyin.
- Numbers: full value; the couple's death ages render "at the age of
  eighty-seven / eighty-six" (享年X岁 = died aged X, not "in his Xth year").

## Voice sheets (carry forward)
- **The author (Ye Xiaoshen):** warm, buttonholing popular-history narrator with
  a sardonic edge and open reverence for his subjects; heat in the verbs and
  rhythm, ration exclamation and rhetorical questions. In B05 he does sustained
  SOURCE-CRITICISM (weighing five memoir/biography accounts and debunking the
  romantic "found the house in the rain" story); keep that dry, skeptical edge.
- **Zhu Duanshou (B05):** a spirited, plain-spoken Hunan country girl, defiant
  and quick ("Let him dare be feudal, and I'll rise in revolt against him!");
  homegrown, self-deprecating, but sharp-eyed. Her autobiography voice is warm
  and direct.
- **Zhou Enlai:** in B05, WARM and big-brotherly, teasing and patient with Zhu
  Duanshou ("little sister"); keep this distinct from the burning 1930 martyr
  proclamation and the spent 1975 deathbed registers (both still stand).
- **Chen Geng (quoted diary/autobiography):** terse, military, plain.
- **Li Qiang / Ke Lin / Li Yimang / Dong Jianwu (quoted memoirs):** clipped and
  factual (Li Qiang); a doctor's dry precision (Ke Lin); brisk, wry (Li Yimang);
  careful, faintly self-aware (Dong Jianwu).
- **Gu Shunzhang:** the foil; written hot and contemptuous.
- (B01-B03 voice sheets for the Party leaders in committee, Li Zheshi, Luo
  Yinong, He Zhihua, etc. still stand for reruns.)

## Where the story stands
Chapters One-Two founded the Special Branch and drew the moral contrast; Chapter
Three ("Who Is Judas") was the first great betrayal (Luo Yinong); Chapter Four
("Bloodshed on Avenue Joffre") ran the double-agent thread (Bai Xin sold the
Jingyuanli meeting; Peng Pai and the others shot at Longhua; the Red Squad
killed Bai Xin). Chapter Five ("A Real Vault, a False Marriage") turned from the
traitor-hunt to the Party's own machinery: how Xiong Jinding and Zhu Duanshou,
in a marriage that began as cover, set up and guarded the "Fuxing" safe house on
Yunnan Road that doubled as the Politburo's meeting place (1928-1931), until Gu
Shunzhang's April 1931 defection forced it closed; and their whole life together,
to their deaths on the same calendar day 21 years apart. Chapter Six, "It Was
Not Me, It Was the Wind," turns to a tradecraft-and-martyrdom episode around the
codename "Carpenter" and the Welfare Electric Company front.

## Next-batch scope
B06 = ch06, PDF 124-149 (printed 109-134), ten sections ch06s01-s10 (openers at
PDF 125,127,129,131,133,134,137,140,141,142). A LARGE chapter (26 pp.); pace it.
Expect figures (eyeball every page; find_figures misses line art and dense
newsprint) and quoted material.

## Open traps / environment
- `data/zh/` is gitignored (copyright); a fresh checkout cannot regenerate the
  hand-transcribed sources. Use per-unit `check_structure --pairs`.
- `find_figures.py` misses dense-newsprint clippings and line-art diagrams;
  eyeball every page and hand-crop. When cropping a captioned photo, exclude the
  printed caption line (the builder renders the translator's caption).
- `tests/run_tests.py` "hook stands down on template stub" FAIL is benign (a
  real kickoff is present). Not a regression.
- `OMP_THREAD_LIMIT=1` mandatory for tesseract; verify `pgrep -c tesseract` = 0
  after OCR. epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (setup fetches).
- `authority.json` is updated on WHOLE-BOOK completion, not per batch; the
  B01-B05 decided renderings are in glossary.json and listed above.
- The Preface (ch00, PDF 6-15) is still UNTRANSLATED; it and the back matter
  (Works Cited, Afterword) fold into the final batches.
- Branch hygiene: the canonical branch is `claude/the-sword-roars`. The harness
  may start a session on a stray per-task branch; consolidate onto the canonical
  branch and delete the stray (local + remote) per CLAUDE.md rule 2. (B05
  started on a stray `claude/sword-roars-ch05-*`, which held no unique commits;
  consolidated and pruned.)
