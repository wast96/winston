# HANDOFF — The Sword Roars in the West Wind

## Message to paste into the next chat

> Paste this VERBATIM to start Batch 5. It is the only bridge between
> conversations; HANDOFF/PROGRESS/book.json describe the state, but the pages
> are the voice, so read the last two pages of ch04's English first.

```
Sword Roars B05

Read CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. Work on branch claude/the-sword-roars (the canonical book
branch; if the harness starts you on a stray per-task branch, consolidate per
CLAUDE.md rule 2). Run ./setup.sh first.

Do Batch 5 = Chapter Five, "真金库，假夫妻 / A Real Vault, a False Marriage"
(ch05), PDF 108-123, printed 93-108, end to end per the pipeline in CLAUDE.md.
Three sections: ch05s01 一、党中央最机密的机关 (PDF 109, printed 94), ch05s02
二、爱吃红烧狮子头 (PDF 115, printed 100), ch05s03 三、三个良师益友 (PDF 120,
printed 105). Simplified Chinese, horizontal; OCR chi_sim --psm 6; crop --left
0.06 --right 0.95 --top 0.11 --bottom 0.955; offset is a constant 15 (printed =
pdf - 15), no plate drift through ch04, but READ each opener's folio off the
scan.

BEFORE translating, read the final two pages of Chapter Four's English
(out/ch04_reading.md) so the voice carries over unbroken. Chapter One remains
the FROZEN register reference: run check_register.py --ref out/ch01_reading.md
on ch05 and record it (expect the dialogue-contraction metric to be quiet on a
document-heavy chapter; judge on the narratorial signals, per
references/register-drift.md). Chapters One-Four's data/zh were hand-transcribed
off the scans (OCR too noisy on the proper names, assemble breaks on
figure/opener pages); do the same for ch05 where assemble misaligns, and keep
parity exact. Cite printed folios in notes, never PDF pages. Never invent
bridging text: if OCR breaks mid-sentence or a leaf is damaged, crop the scan
and read the real continuation, or footnote the gap. Verify every name, number
and low-confidence span against a magnified crop before writing. Consult
authority.json and glossary.json for settled renderings (esp. the Central
Special Branch, the Red Squad, Zhou Enlai, Chen Geng, Gu Shunzhang, the
tingzijian). This chapter turns to the Party's secret organs (a "vault" and a
"false marriage" guarding it); expect fresh material culture and tradecraft to
note. Add ch05 to data/content_config.json when you translate it, or the
displacement check silently skips it.

Deliver the built EPUB attached in the chat, and paste the Batch 6 kickoff
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
  24 footnotes, 10 figures, 62 new glossary rows; parity 131=131, numbers 0,
  align/content/entities clean, register within the reportage caveat, qa_epub
  PASS (200 notes total), epubcheck 0/0. Details in PROGRESS.md.

## Tooling in place — DO NOT REVERT
- `scripts/indents.py`: furniture-band drop by y-position (`FURNITURE_TOP=0.11`,
  `FURNITURE_BOTTOM=0.955`). Folio + running head are one TOP band; no foot.
- `scripts/check_numbers.py`: arabic+万 combiner ("31万"=310,000) BEFORE the
  noise loop; matches English number-WORDS, ordinals, and MONTH NAMES (so
  "December" reconciles with 12月, which makes the ch04 diary dates check clean).
- **`build_reading_epub.py` alt-attribute escaping (fixed in B04):** the figure
  `alt="%s"` is now emitted through `html.escape(..., quote=True)`, not the
  `quote=False` `esc()`. A literal double quote in alt text used to produce
  malformed XHTML and made qa_epub/epubcheck report the WHOLE chapter's ids as
  undefined; the fix is one line. Keep it, and still prefer single quotes in alt.
- `data/noise.txt`: this book's event-date names, numeral-bearing proper names,
  decade labels, idioms. B02-B04 blocks appended (B04: 百禄里, 五洲, 三民, 三轮车,
  八仙桥). Extend per its header; longest literal first; comment every entry.
- `data/content_config.json`: docs+sources map for check_content; now covers
  ch01-ch04. ADD ch05 when you translate it, or the displacement check silently
  skips it.
- OCR crop for this book: `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955
  --lang chi_sim --psm 6`. Offset constant 15 (printed = pdf - 15).
- **Glossary placement gotcha:** `apparatus_merge.py` writes glossary rows at the
  JSON TOP LEVEL; the builder's render_glossary chokes on a flat row. Add rows
  DIRECTLY into the people/organizations/places/terms sections with a
  re-read-verified one-shot script (deleted after use). Notes and figures go
  through apparatus_merge normally (it validates note anchors and figure specs).
- **figures.json `file` must be a BASENAME** (e.g. `ch04-an-e.png`); the builder
  prepends `data/figs/` for the source and `images/` for the EPUB. Figure
  `before` anchors must fall in the FIRST ~80 chars of a paragraph; note anchors
  CANNOT sit on the `##` chapter-title line (use a body-text occurrence).
- **Set-off blocks:** mark displayed block quotations and dated diary/log entries
  `{v}` (renders as an indented italic block); combine a diary date + entry on
  ONE line so each entry is one parity unit; keep a source's abridging "……" as
  its own `{v} ...` line. Both zh and en must carry identical `{v}` lines.
- **Inline citation style:** the author's `（作者，年份）` source citations render
  inline as `(Author, YEAR)` right after the quoted material; check_numbers flags
  the missing year if you drop one.

## Renderings settled through B04 (also in glossary.json / STYLE.local.md)
- 中央特科 = the Central Special Branch; 红队 / 打狗队 = the Red Squad / the
  dog-beating squad; 中统 = the Zhongtong; 调查科 = the Investigation Section;
  淞沪警备司令部 = the Songhu Garrison Command; 中央军委 = the Central Military
  Commission; 圣彼得堂 = St. Peter's Church; 怀恩堂 = Grace Church; 达生医院 =
  the Dasheng Hospital.
- Concession streets: 霞飞路 = Avenue Joffre (today Huaihai Middle Road); 蒲石路 =
  Rue Bourgeat (today Changle Road); 爱文义路 = Avenue Road; 戈登路 = Gordon Road;
  卡德路 = Cardan Road (today Shimen No. 2 Road); 同孚路 = Route Tunkadoo (today
  Shimen No. 1 Road); 金神父路 = Route Père Robert; 西摩路 = Seymour Road; 嵩山路 =
  Songshan Road; 新闸路 = Xinzha Road; 新闸邨 = Xinzha Village. The author's
  `（今X路）` glosses render "(today X Road)". Uncertain French names kept as
  pinyin (白尔部路 = Bai'erbu Road, 高恩路 = Gao'en Road).
- Places new in B04: 经远里 = Jingyuanli; 枫林桥 = Fenglin Bridge; 和合坊 =
  Hehefang; 秦城监狱 = Qincheng Prison; 龙华 = Longhua (from B03).
- People new in B04 (carry forward): **彭湃 = Peng Pai**, **杨殷 = Yang Yin**,
  颜昌颐 = Yan Changyi, 邢士贞 = Xing Shizhen, 张际春 = Zhang Jichun (the four
  martyrs + the survivor); **白鑫 = Bai Xin (the traitor)**; 范争波/范争洛 = Fan
  Zhengbo / Fan Zhengluo; **安娥 = An E** (real name 张式沅 Zhang Shiyuan);
  连德生 = Lian Desheng; **柯麟 = Ke Lin** (alias 柯达文 Ke Dawen); 贺诚 = He Cheng;
  李一氓 = Li Yimang; 杨剑虹 = Yang Jianhong; 陈立夫/陈果夫 = Chen Lifu / Chen
  Guofu; 张道藩 = Zhang Daofan; 黄金荣 = Huang Jinrong; 罗青长 = Luo Qingchang;
  赵子柏 = Zhao Zibai; 罗登贤 = Luo Dengxian; 徐锡根 = Xu Xigen; 赵容 = Zhao Rong
  (= Kang Sheng). **杨登瀛 = Yang Dengying (aka 鲍君甫 = Bao Junfu), 陈养山 = Chen
  Yangshan, 董健吾 = Dong Jianwu, 李强 = Li Qiang — all carried from earlier.**
  Western names: 达斯科·波波夫 = Dusko Popov ("Tricycle").
- Numbers: full value; carry counts (五位负责人 "five leaders"); the diary dates
  render "December 10, 1968" etc. (month names reconcile with 月 in check_numbers).

## Voice sheets (carry forward)
- **The author (Ye Xiaoshen):** warm, buttonholing popular-history narrator with
  a sardonic edge and open reverence for his subjects; heat in the verbs and
  rhythm, ration exclamation and rhetorical questions. See STYLE.local.
- **Chen Geng (quoted diary/autobiography):** terse, military, plain.
- **Zhou Enlai (quoted proclamation / deathbed):** in the 1930 martyr proclamation,
  formal, burning, decisive ("We must finish off the traitor Bai Xin!"); in the
  1975 deathbed scene, spent, tender, insistent about not forgetting old friends.
  Keep both registers; they are quoted documents, not casual speech.
- **Li Qiang (quoted diary):** the 1968-69 entries are clipped, factual, dated
  log prose; render plainly, no smoothing into narrative.
- **Ke Lin (quoted memoir):** measured, observant, a doctor's dry precision.
- **Li Yimang (quoted memoir):** brisk, first-person, a touch wry ("Old Ke took
  fright").
- **Dong Jianwu (quoted memoir):** careful, methodical, faintly self-aware; the
  cold smile of the disguised old man is the author's, not his.
- **Gu Shunzhang:** the foil; written hot and contemptuous (little of him here).
- **The 1927-29 Party leaders in committee:** clipped, procedural, decisive.
- (B03 voice sheets for Li Zheshi, Luo Yinong, He Zhihua, He Jiaxing, Zheng
  Chaolin, Zhang Guotao, Zhu De, Zhu Min, Deng Xiaoping still stand for reruns.)

## Where the story stands
Chapters One-Two founded the Special Branch and drew the moral contrast; Chapter
Three ("Who Is Judas") was the first great betrayal (Luo Yinong sold and shot).
Chapter Four ("Bloodshed on Avenue Joffre") runs the double-agent thread: Bai
Xin, the Military Commission secretary, sells the 24 Aug 1929 Jingyuanli meeting
to the Kuomintang, and Peng Pai, Yang Yin, Yan Changyi, and Xing Shizhen are shot
at Longhua; the Special Branch, working through the double agent Yang Dengying
and the doctor Ke Lin and the Red Pastor Dong Jianwu, tracks Bai Xin down and the
Red Squad kills him on Avenue Joffre (11 Nov 1929). The chapter closes on Zhou
Enlai still protecting Yang Dengying decades later, in Qincheng Prison. Chapter
Five, "A Real Vault, a False Marriage," turns from the hunt for traitors to the
Party's own secret machinery: its most secret organ, and a false-married couple
who guard it.

## Next-batch scope
B05 = ch05, PDF 108-123 (printed 93-108), three sections ch05s01-s03 (openers at
PDF 109, 115, 120). A medium chapter (16 pp.). Expect figures (eyeball every
page; find_figures misses line art and dense newsprint) and quoted documents.

## Open traps / environment
- `data/zh/` is gitignored (copyright); a fresh checkout cannot regenerate the
  hand-transcribed sources. `check_structure --config` therefore cannot run a
  whole-book parity pass on a clean checkout; use per-unit `--pairs`.
- `find_figures.py` misses dense-newsprint clippings and line-art diagrams;
  eyeball every page and hand-crop. B04 had 10 figures (6 portraits, a garrison
  photo, a full-page street map, a newspaper front page, a family photo); the
  faded full-page painting on pdf 107 is design furniture, not a captioned figure.
- `tests/run_tests.py` "hook stands down on template stub" FAIL is benign (a
  real kickoff is present). Not a regression.
- `OMP_THREAD_LIMIT=1` mandatory for tesseract; verify `pgrep -c tesseract` = 0
  after OCR. epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (setup fetches).
- `authority.json` is updated on WHOLE-BOOK completion, not per batch; the
  B01-B04 decided renderings are in glossary.json and listed above.
- The Preface (ch00, PDF 6-15) is still UNTRANSLATED; it and the back matter
  (Works Cited, Afterword) fold into the final batches.
- Branch hygiene: the canonical branch is `claude/the-sword-roars`. The harness
  may start a session on a stray per-task branch; consolidate onto the canonical
  branch and delete the stray (local + remote) per CLAUDE.md rule 2.
