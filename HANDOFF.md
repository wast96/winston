# HANDOFF — The Sword Roars in the West Wind

## Message to paste into the next chat

> Paste this VERBATIM to start Batch 4. It is the only bridge between
> conversations; HANDOFF/PROGRESS/book.json describe the state, but the pages
> are the voice, so read the last two pages of ch03's English first.

```
Sword Roars B04

Read CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. Work on branch claude/the-sword-roars (the canonical book
branch; if the harness starts you on a stray per-task branch, consolidate per
CLAUDE.md rule 2).  Run ./setup.sh first.

Do Batch 4 = Chapter Four, "喋血霞飞路 / Bloodshed on Avenue Joffre" (ch04),
PDF 82-107, printed 67-92, end to end per the pipeline in CLAUDE.md. Seven
sections: ch04s01 一、捕人如像预知的一样 (PDF 83, printed 68), ch04s02
二、两面间谍 (PDF 87, printed 72), ch04s03 三、伏击枫林桥 (PDF 91, printed 76),
ch04s04 四、白鑫叛变 (PDF 94, printed 79), ch04s05 五、惊弓之鸟 (PDF 97, printed
82), ch04s06 六、皮夹里有一张车票 (PDF 99, printed 84), ch04s07 七、"将他老婆接来"
(PDF 101, printed 86). Simplified Chinese, horizontal; OCR chi_sim --psm 6;
crop --left 0.06 --right 0.95 --top 0.11 --bottom 0.955; offset is a constant 15
(printed = pdf - 15), no plate drift so far, but READ each opener's folio off
the scan.

BEFORE translating, read the final two pages of Chapter Three's English
(out/ch03_reading.md) so the voice carries over unbroken. Chapter One remains
the FROZEN register reference: run check_register.py --ref out/ch01_reading.md
on ch04 and record it. Chapters One-Three's data/zh were hand-transcribed off
the scans (OCR too noisy on the proper names, assemble breaks on figure/opener
pages); do the same for ch04 where assemble misaligns, and keep parity exact.
Cite printed folios in notes, never PDF pages. Never invent bridging text: if
OCR breaks mid-sentence or a leaf is damaged, crop the scan and read the real
continuation, or footnote the gap. Verify every name, number and low-confidence
span against a magnified crop before writing. Consult authority.json and
glossary.json for settled renderings (esp. Yang Dengying/Bao Junfu the double
agent, Chen Geng/Wang Yong, the Central Special Branch, the Red Squad, Zhou
Enlai, Gu Shunzhang, Xu Enzeng); ch04 is the double-agent chapter that
ch03's ending (杨登瀛/鲍君甫) sets up, and it turns on Bai Xin's (白鑫) betrayal.

Deliver the built EPUB attached in the chat, and paste the Batch 5 kickoff
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
  4 figures, 59 new glossary rows; parity 146=146, numbers 0, align/content/
  entities clean, register within tolerance, qa_epub PASS, epubcheck 0/0.
  Details in PROGRESS.md.

## Tooling in place — DO NOT REVERT
- `scripts/indents.py`: furniture-band drop by y-position (`FURNITURE_TOP=0.11`,
  `FURNITURE_BOTTOM=0.955`). Folio + running head are one TOP band; no foot.
- `scripts/check_numbers.py`: arabic+万 combiner ("31万"=310,000) BEFORE the
  noise loop. Matches English number-WORDS and ordinals (so spelled-out
  numbers count); a dropped count is a real flag, fix the English, never noise.
- `data/noise.txt`: this book's event-date names, numeral-bearing proper names,
  decade labels, idioms. B02 and B03 blocks appended (B03: 四川, 三教街, 化整为零,
  一百二十四, 推三阻四, 万籁, 万般, 第二天). Extend per its header; longest literal
  first; comment every entry.
- `data/content_config.json`: docs+sources map for check_content; now covers
  ch01+ch02+ch03. ADD ch04 when you translate it, or the displacement check
  silently skips ch04.
- OCR crop for this book: `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955
  --lang chi_sim --psm 6`. Offset constant 15 (printed = pdf - 15).
- **Glossary placement gotcha:** `apparatus_merge.py` writes glossary rows at the
  JSON TOP LEVEL; the builder's render_glossary chokes on a flat row. B03 added
  rows by writing them DIRECTLY into the people/organizations/places/terms
  sections with a re-read-verified one-shot script (deleted after use). Either
  path works; just never leave a flat top-level row. Notes and figures went
  through apparatus_merge normally (it validates anchors).
- **figures.json `file` must be a BASENAME** (e.g. `ch03-luo-yinong.png`); the
  builder prepends `data/figs/` for the source and `images/` for the EPUB. A
  path prefix breaks qa_epub. Figure `before` anchors must fall in the FIRST
  ~80 chars of a paragraph; note anchors CANNOT sit on the `##` chapter-title
  line (builder scans body paragraphs and `###` section headings only).
- **Inline citation style:** the author's `（作者，年份）` source citations are
  rendered inline as `(Author, YEAR)` right after the quoted material, per ch02.
  Do NOT drop them; check_numbers flags the missing year if you do.

## Renderings settled through B03 (also in glossary.json / STYLE.local.md)
- 中央特科 = the Central Special Branch; 组织局 = the Organization Bureau; 红队 /
  打狗队 = the Red Squad / the dog-beating squad; 东方大学 = the University of the
  Toilers of the East (KUTV); 布尔塞维克 = Bolshevik (the journal).
- 二房东 = second landlord; 拆白党 = confidence-man (chaibaidang); 买办 = comprador;
  老虎灶 = laohuzao; 会审公廨 = the Mixed Court; 白色恐怖 = the White Terror; 湘绣 =
  Xiang embroidery; 大世界 = the Great World; 哈同花园 = Hardoon Garden.
- Places: 龙华 = Longhua; 蒲石路 = Rue Bourgeat (today Changle Road); 静安寺路 =
  Bubbling Well Road (today Nanjing West Road). The author's `（今X路）` modern
  street glosses are rendered "(today X Road)".
- People new in B03: 李哲时 = **Li Zheshi** (= 李文宜 **Li Wenyi**, her later name);
  贺稚华 = **He Zhihua** (the traitor; scholarship writes 贺治华, same romanization);
  何家兴 = **He Jiaxing**; 罗亦农 = **Luo Yinong**; 郑超麟 = **Zheng Chaolin**;
  朱德 = **Zhu De**; 朱敏 = **Zhu Min**; 邓小平 = **Deng Xiaoping**; 苏兆征 = Su
  Zhaozheng; 项英 = Xiang Ying; 张国焘 = Zhang Guotao; 康生 = Kang Sheng; 张作霖 =
  Zhang Zuolin; 钱大钧 = Qian Dajun; **杨登瀛 = Yang Dengying (aka 鲍君甫 = Bao
  Junfu), the first double agent — CARRIES INTO ch04.** Western/other names keep
  the ch01-ch02 ledger.
- Numbers: full value ("310,000", "US$50,000"), never "wan"; 三千或五万 = "three
  thousand or fifty thousand"; carry counts (八人 "eight", 二楼 "second-floor").

## Voice sheets (carry forward)
- **The author (Ye Xiaoshen):** warm, buttonholing popular-history narrator with
  a sardonic edge and open reverence for his subjects; heat in the verbs and
  rhythm, ration exclamation and rhetorical questions. See STYLE.local.
- **Chen Geng (quoted diary/autobiography):** terse, military, plain.
- **Dong Jianwu / Li Qiang / Xu Enzeng / Dong Huifang (quoted):** as in B01-B02.
- **The 1927 Party leaders in committee** (Chen Duxiu, Luo Yinong, Zhao Shiyan):
  clipped, procedural, decisive; meeting-record speech, lightly contracted.
- **Gu Shunzhang:** the foil; written hot and contemptuous. Keep the temperature.
- **Li Zheshi (李哲时):** modest, self-doubting, honest; her grief is quiet and
  physical, never operatic. Her quoted self-talk is plain and humble.
- **Luo Yinong (罗亦农):** warm, direct, decisive; tender and unguarded in the
  courtship ("There is only you in my heart").
- **He Zhihua (贺稚华):** the chapter's traitor; glamorous, theatrical, cold,
  calculating. The author writes her with fascination and contempt ("burned like
  a ball of fire," "the heart of a viper"). Keep the heat; footnote the verdict.
- **He Jiaxing (何家兴):** weaker than his wife, anxious, dependent ("You're sure
  we'll be free and far away?").
- **Zheng Chaolin (quoted memoir):** precise, dry, scholarly, self-aware.
- **Zhang Guotao (quoted memoir):** measured, self-justifying, procedural.
- **Zhu De (1925 letter):** earnest, plain, resolute, lightly classical.
- **Zhu Min (quoted):** a wounded, proud daughter; unforgiving toward her mother,
  loyal to her father.
- **Deng Xiaoping (quoted via his daughter):** plain, urgent, vivid, colloquial.

## Where the story stands
Chapter One founded the Central Special Branch; Chapter Two drew the moral
contrast (incorruptible heroes vs Gu Shunzhang the lumpen-proletarian foil).
Chapter Three, "Who Is Judas," is the first great betrayal: He Zhihua and He
Jiaxing sell Luo Yinong to the concession police for passports and dollars; he
is shot at Longhua; the Special Branch's Red Squad kills He Jiaxing and blinds
He Zhihua in reprisal. The chapter ends by naming Yang Dengying (Bao Junfu) as
the Party's first double agent, recruited just after Luo's death. Chapter Four,
"Bloodshed on Avenue Joffre," runs the double-agent thread forward: the arrests
that came "as if foreknown," the double agent, the ambush at Fenglin Bridge, and
Bai Xin's (白鑫) betrayal. Expect more arrest/chase/ambush action (watch pronoun
fog) and quoted documents.

## Next-batch scope
B04 = ch04, PDF 82-107 (printed 67-92), seven sections ch04s01-s07 (openers at
PDF 83, 87, 91, 94, 97, 99, 101). A large chapter (26 pp.). Plan for figures
(eyeball every page; find_figures misses line art and dense newsprint).

## Open traps / environment
- `data/zh/` is gitignored (copyright); a fresh checkout cannot regenerate the
  hand-transcribed sources. `check_structure --config` therefore cannot run a
  whole-book parity pass on a clean checkout; use per-unit `--pairs`.
- `find_figures.py` misses dense-newsprint clippings and line-art diagrams;
  eyeball every page and hand-crop. B03 had 4 figures (2 portraits, 1 group
  photo, 1 street map); the chapter-opener montage is design furniture, not a
  captioned figure.
- `tests/run_tests.py` "hook stands down on template stub" FAIL is benign (a
  real kickoff is present). Not a regression.
- `OMP_THREAD_LIMIT=1` mandatory for tesseract; verify `pgrep -c tesseract` = 0
  after OCR. epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (setup fetches).
- `authority.json` is updated on WHOLE-BOOK completion, not per batch; the
  B01-B03 decided renderings are in glossary.json and listed above.
- Branch hygiene: the canonical branch is `claude/the-sword-roars`. The harness
  may start a session on a stray per-task branch; consolidate onto the canonical
  branch and delete the stray (local + remote) per CLAUDE.md rule 2.
