# HANDOFF — The Gangs of Old Shanghai (旧上海的帮会)

The baton. A fresh session reads this and continues. **Voice gate PASSED** (B01).
ch03 is the FROZEN register reference: measure every later unit with
`check_register.py --ref out/ch03_reading.md`. The natural contemporary-English
voice of B01 is the standard for the whole book. Digits for specific quantities.

**B01, B02, and B03 are COMPLETE. B04 has NOT been started.** Run B04 in a FRESH
session by pasting the kickoff below.

## Message to paste into the next chat

```
Gangs of Old Shanghai B04

Read CLAUDE.md, then HANDOFF.md, then book.json. Do batch B04 = ch09 (张仁奎与仁社,
Zhang Renkui and the Ren Society) + ch10 (我的老师袁寒云, My Teacher Yuan Hanyun) +
ch11 (先父徐朗西生平事略, A Brief Life of My Late Father Xu Langxi) + ch12 (黄金荣事略,
A Brief Account of Huang Jinrong), PDF 117–146, printed 108–137, end to end per the
pipeline. This scan defeats geometric indent detection, so assemble from the fallback
and HAND-BUILD the zh files to match the English 1:1 (see B01–B03); the measured OCR
crop is `--left 0.06 --right 0.91 --top 0.09 --bottom 0.89 --lang chi_sim --psm 6`,
folio cropped at the foot. BEFORE translating, read the final two pages of ch08's
English and skim ch06 — that natural voice is the frozen reference; no stilted/period
register, digits for specific quantities. CHECK whether ch09–ch12 carry the author's
OWN numbered footnotes at the page foot (ch05 did; ch06–ch08 did not): if so,
reproduce them as "Author's note." entries, distinct from translator notes. These are
biographical/memoir pieces on the older generation and the first Huang Jinrong life:
the cast overlaps B02/B03 heavily — Huang Jinrong (黄金荣), Du Yuesheng (杜月笙),
Zhang Xiaolin (张啸林), Zhang Renkui (张仁奎, subject of ch09; his body is the Ren
Society 仁社), Xu Langxi (徐朗西, subject of ch11, by his son), the Green Gang (青帮),
the Hongmen (洪门) — REUSE the glossary rows, do not re-romanize. New principals to
add: 袁寒云 (Yuan Hanyun = 袁克文, son of Yuan Shikai 袁世凯, a "Da"-generation Green
Gang celebrity and Yuan Hanyun's pupil is the ch10 author). Consult authority.json
before romanizing any new name. Keep 军统 as "the Juntong" (unsettled until B08). Cite
printed folios; never invent bridging text; verify names/numbers/low-confidence spans
by eye against the scan (esp. dates, dollar/tael amounts, and Zhang Renkui's Ren
Society roster); do not pause for approval; deliver the EPUB in chat and paste the next
kickoff.
```

## What is DONE (do not redo)

- **B01 (ch01–ch04, printed 1–28):** front matter + the two workers'-movement
  memoirs (Zhu Xuefan, Wu Chengfang). 43 notes, 33 glossary rows.
- **B02 (ch05–ch06, printed 29–67):** Green Gang origins — Li Shiyu's archival
  study and Jiang Hao's memoir-study. 77 notes (ch05 reproduces the author's 57
  source citations), +21 glossary rows.
- **B03 (ch07–ch08, printed 68–107):** the Hongmen's history (Jiang Hao) and a
  French Concession detective's gallery of Shanghai gang figures (Xue Gengshen).
  40 notes (running total 160), +41 glossary rows (95 total). All checks green,
  qa_epub PASS, epubcheck 0/0. See PROGRESS.md for the per-check detail.

## Tooling in place (do NOT revert) — full list in PROGRESS.md

- OCR crop `--left 0.06 --right 0.91 --top 0.09 --bottom 0.89 --lang chi_sim
  --psm 6`, folio at the foot. Geometric indent detection BYPASSED on this scan;
  zh files are HAND-BUILT to match the English 1:1.
- check_content needs a docs/sources config; `work/content_cfg.json` and
  `work/structure_cfg.json` were regenerated to cover ch01–ch08. ADD ch09–ch12
  to both next batch (or regenerate).
- data/noise.txt has grown per batch; every entry is commented. B03 added a CJK
  list-enumerator rule `（[一二…十]）` for the source's （一）（二）… sub-heads,
  plus many name/place/lodge/idiom numerals. Do NOT remove; extend as needed.
- No script logic changes in B03.

## Renderings settled / carry-forward (reuse; in glossary.json)

- **Secret-society lexicon (B02–B03):** the Green Gang (青帮), the Hongmen (洪门),
  the Red Gang (红帮), the Green and Red Gangs (青红帮), the Heaven and Earth
  Society (天地会), the Three Harmonies Society (三合会, = the Triads), the Elder
  Brothers Society (哥老会), the Chee Kung Tong (致公堂), the Small Sword Society
  (小刀会), the Hanliu (汉留, provisional), the Luo sect (罗教), the incense hall
  (香堂). Orgs: the Ren Society (仁社), the Rong Society (荣社), the Wen Society
  (文社), the Yi Society (毅/逸/怡社, three distinct bodies), the Wusheng Mountain
  (五圣山), the Hongxing Association (洪兴协会), the Loyal and Patriotic Army
  (忠义救国军). **the Juntong (军统) still shelf-UNSETTLED — decide at B08.**
- **Cast (reuse, do not re-romanize):** Huang Jinrong, Du Yuesheng, Zhang Xiaolin,
  Zhang Renkui, Dai Li, Yang Hu, Chen Shichang, Jin Tingsu (金廷荪, NOT Tingsun),
  Jiang Hao, Li Shiyu; B03 added Xue Gengshen (薛耕莘), Xu Langxi (徐朗西), Wang
  Yucheng (汪禹丞), Xiang Songpo, Zheng Ziliang, Yu Qiaqing, Cheng Ziqing, Jin
  Jiuling, Gu Zhuxuan, Chang Yuqing, Lu Liankui, Wei Tingrong, Lu Lanchun, Chen
  Qimei, Sun Yat-sen, Huang Xing, Song Jiaoren, Situ Meitang, Zheng Chenggong
  (Koxinga), Chen Jinnan, Hong Ying, Kawashima Yoshiko.
- **Three "Yi Societies"** all romanize alike (毅/逸/怡社); footnoted once (ch06).
  Flag for the B10 reconciliation.
- The 24 generation-characters and the "Da/Tong/Wu" ranks are footnoted at ch05.

## Voice sheets

- **Narrators are the register.** JIANG HAO (ch06–ch07): an initiated gang member
  writing a study — plain expository prose, long biographical rosters (one crisp
  paragraph per figure), brief first-person memoir passages; never mock-antique,
  keep the classical/legendary material clear and faithful. XUE GENGSHEN (ch08):
  a career detective's memoir — precise, worldly, faintly ironic; sustained
  first-person narration with two dialogue registers (Huang Jinrong: boastful,
  colloquial, self-important, uses contractions; the narrator's own official
  speech: measured and diplomatic). His anecdotes are told as an insider's; where
  a claim is his alone, the note says so.
- Dialogue-heavy household memoirs (Huang/Du) begin in B05; write their voice
  sheets there.

## Where the book stands

- B01 established how the Nationalist labour machine and the Communist underground
  each USED the gangs; B02 gave the Green Gang's real and legendary origins; B03
  added the Hongmen's own (legendary) history and a detective's panorama of the
  Shanghai underworld — the three big bosses, the concession police, the opium,
  gambling, trafficking and smuggling rackets, and the wartime traitor-gangs.
  Next (B04) the book turns to individual lives: Zhang Renkui and the Ren Society,
  the celebrity Yuan Hanyun, Xu Langxi, and the first full life of Huang Jinrong.

## What is NEXT

- B04 = ch09–ch12, PDF 117–146, printed 108–137 (see the kickoff above).

## Open items for the read-through

- B03 provisional/left-as-printed (for B10 reconciliation): the Hanliu
  romanization; the ch07 mountain-lodge founder names (many single-appearance,
  OCR-corrected but unattested); 荩忠山, 福建霞宁县 (faint readings); 和丛亮
  (又名徐为彬) and 杨庆/杨庆山 in the ch07 Juntong committee (garbled); 赵志游
  (ch08, ≠ Du's disciple 赵志英); 张法党 (Zhang Xiaolin's son). Earlier open items
  (ch06 genealogy legend, 24-char variants, 樊瑾成/丞, tongcao, 渭清县) still stand.

## Environment / traps state

- setup.sh green; tesseract chi_sim/chi_sim_vert/chi_tra/chi_tra_vert + eng;
  PaddleOCR absent (dual-tesseract substitute); epubcheck 5.1.0 at
  /tmp/epubcheck-5.1.0/epubcheck.jar (java present). OMP_THREAD_LIMIT=1.
- `tests/run_tests.py` reports one FAIL — "hook stands down on template stub."
  This is EXPECTED for a mid-flight book: that test asserts the Stop hook stands
  down when HANDOFF.md holds the template *placeholder* kickoff, but our HANDOFF
  holds a real B04 kickoff, so the hook correctly BLOCKS a kickoff-less wrap-up
  instead. The two enforcing paths ("blocks kickoff-less", "passes compliant")
  both PASS. Do NOT "fix" the hook — it would break the real Stop-hook guard.
- Stray per-task branch expected at each batch start; canonical branch is
  claude/gangs-of-old-shanghai (consolidate onto it, delete the stray).
