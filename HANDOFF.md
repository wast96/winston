# HANDOFF — The Gangs of Old Shanghai (旧上海的帮会)

The baton. A fresh session reads this and continues. **Voice gate PASSED** (B01).
ch03 is the FROZEN register reference: measure every later unit with
`check_register.py --ref out/ch03_reading.md`. The natural contemporary-English
voice of B01 is the standard for the whole book. Digits for specific quantities.

**B01 and B02 are COMPLETE. B03 has NOT been started.** Run B03 in a FRESH
session by pasting the kickoff below.

## Message to paste into the next chat

```
Gangs of Old Shanghai B03

Read CLAUDE.md, then HANDOFF.md, then book.json. Do batch B03 = ch07 (洪门历史初探,
A Preliminary Inquiry into the History of the Hongmen) + ch08 (我接触过的上海帮会人物,
Shanghai Gang Figures I Have Known), PDF 77–116, printed 68–107, end to end per
the pipeline. This scan defeats geometric indent detection, so assemble from the
fallback and HAND-BUILD the zh files to match the English 1:1 (see B01/B02); the
measured OCR crop is `--left 0.06 --right 0.91 --top 0.09 --bottom 0.89 --lang
chi_sim --psm 6`, folio cropped at the foot. BEFORE translating, read the final
two pages of ch06's English and skim ch05 — that natural voice is the frozen
reference; no stilted/period register, digits for specific quantities. CHECK
whether ch07/ch08 carry the author's OWN numbered footnotes at the page foot
(ch05 did, ch06 did not): if so, reproduce them as "Author's note." entries,
distinct from translator notes. ch07 is Hongmen (Red Gang / 洪门 / 天地会 /
三合会 / 哥老会) history — consult authority.json before romanizing and reuse the
B02 renderings (the Green Gang 青帮, the Hongmen, the Heaven and Earth Society
天地会, the Luo sect); ch08 is a first-person memoir of Shanghai gang figures, so
its cast will overlap B02's who's-who (Huang Jinrong, Du Yuesheng, Zhang Xiaolin,
Zhang Renkui, the three big bosses) — REUSE the glossary rows, do not re-romanize.
Keep 军统 as "the Juntong" (unsettled until B08). Cite printed folios; never
invent bridging text; verify names/numbers/low-confidence spans by eye against
the scan; do not pause for approval; deliver the EPUB in chat and paste the next
kickoff.
```

## What is DONE (do not redo)

- **B01 (ch01–ch04, printed 1–28):** front matter + the two workers'-movement
  memoirs (Zhu Xuefan, Wu Chengfang). 43 notes, 33 glossary rows.
- **B02 (ch05–ch06, printed 29–67):** Green Gang origins — Li Shiyu's archival
  study and Jiang Hao's memoir-study with a Shanghai gang who's-who. 77 notes
  (running total 120; ch05 reproduces the author's 57 source citations),
  +21 glossary rows (54 total). All checks green, qa_epub PASS, epubcheck 0/0.
  See PROGRESS.md for the per-check detail.

## Tooling in place (do NOT revert) — full list in PROGRESS.md

- ocr_crop `folio_present()` added; measured crop `--left 0.06 --right 0.91
  --top 0.09 --bottom 0.89 --lang chi_sim --psm 6` (the ch05 author footnotes
  at the page foot fell INSIDE this crop, so they OCR'd with the body).
- Geometric indent detection BYPASSED on this scan; assembly uses the fallback
  and zh files are HAND-BUILT to match the English 1:1.
- check_numbers: 〇 zero; `一一` compound-guard (B01). B02 added a general tael
  rule `(?<=[十百千万萬])两` and many name/place/idiom noise entries — see
  data/noise.txt (each commented).
- apparatus_merge: section-aware glossary merge (rows carry `section`).
- check_content: skips `_`-prefixed glossary keys.
- qc_entities: tolerant of a glossary row missing `pinyin` (B02).
- check_content needs a docs/sources config; `work/content_cfg.json` is the
  ch05/ch06 one (regenerate per batch, or add ch07/ch08 to it).

## Renderings settled B02 / carry-forward (reuse; in glossary.json)

- Green Gang lore: the Green Gang (青帮), the Hongmen (洪门), the Red Gang (红帮),
  the Green and Red Gangs (青红帮), the Heaven and Earth Society (天地会), the
  Luo sect (罗教/罗祖教), Patriarch Luo (罗祖; note only, not a glossary row),
  the Anqing Fellowship (安庆道友会), tongcao (通草, provisional), the incense
  hall (香堂), green skin (青皮), the grain(-tribute) transport (漕运).
- People: Li Shiyu (李世瑜), Jiang Hao (姜豪), the six patriarchs — Jin Youzi
  金幼孜, Luo Qing 罗清, Lu Kui 陆逵, Weng Yan 翁岩, Qian Jian 钱坚, Pan Qing 潘清
  — Wang Lun (王伦), Chen Shichang (陈世昌), Yang Hu (杨虎).
- Orgs: the Rong Society (荣社), the Wen Society (文社), the Loyal and Patriotic
  Army (忠义救国军). **the Juntong (军统) still shelf-UNSETTLED — decide at B08.**
- **Jin Tingsu (金廷荪)** — B01's rendering; reused (not "Jin Tingsun").
- **Three "Yi Societies"** all romanize alike: 毅社 (Zhu Xuefan, B01) / 逸社
  (Xu Yimin) / 怡社 (Sun Yixiang). Distinct bodies; footnoted once. Flag for
  the B10 reconciliation.
- The 24 generation-characters (青帮 seniority runs by generation, not age):
  清静道德文成佛法能仁智慧本来自性元(圆)明兴(行)理大通无(悟)学 — footnoted;
  Du Yuesheng was 悟/Wu, Huang Jinrong 通/Tong, Zhang Renkui 大/Da.

## Voice sheets

- **Narrators are the register.** B02 added two non-dialogue registers:
  LI SHIYU (ch05): a professional historian-folklorist; measured scholarly
  argument, Qing memorials quoted and dissected, his own citations at the foot;
  keep the classical quotes clear and faithful, never mock-antique. JIANG HAO
  (ch06): an initiated gang member writing a study; mostly expository, with a
  long biographical roster (one crisp paragraph per figure) and brief first-
  person memoir passages (the 1930 anti-Chiang episode). Both plain, unstilted.
- Dialogue voices still to be written when the first dialogue-heavy memoir
  arrives (a Huang/Du household memoir, B05+).

## Where the book stands

- The framing memoirs (B01) established how the Nationalist labour machine and
  the Communist underground each USED the gangs. B02 turns to the gangs' own
  history: the Green Gang's real origins among Qing grain-transport boatmen
  (Li Shiyu) and its legendary self-account and Shanghai cast (Jiang Hao).
  Next (B03) the book takes up the Hongmen's history and a memoirist's gallery
  of the Shanghai gang figures he knew, then moves to the big bosses.

## What is NEXT

- B03 = ch07–ch08, PDF 77–116, printed 68–107 (see the kickoff above).

## Open items for the read-through

- Gang genealogy in ch06 is legend (footnoted, cross-ref ch05). 24-char variant
  between the two studies (footnoted). 樊瑾成/樊瑾丞 same romanization; 曹志功/
  曹立功 left as printed. Provisional: tongcao romanization; Weiqing county
  (渭清县, ch06) as printed (possibly 渭源).

## Environment / traps state

- setup.sh green; tesseract chi_sim/chi_sim_vert/chi_tra/chi_tra_vert + eng;
  PaddleOCR absent (dual-tesseract substitute); epubcheck 5.1.0 at
  /tmp/epubcheck-5.1.0/epubcheck.jar (java present). OMP_THREAD_LIMIT=1.
- Watch short one-glyph closing lines (strip_folio can eat them).
- Stray per-task branch expected at each batch start; canonical branch is
  claude/gangs-of-old-shanghai (consolidate onto it, delete the stray).
