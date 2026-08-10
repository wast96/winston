# HANDOFF — The Gangs of Old Shanghai (旧上海的帮会)

The baton. A fresh session reads this and continues. **Voice gate PASSED** (B01).
ch03 is the FROZEN register reference: measure every later unit with
`check_register.py --ref out/ch03_reading.md`. The natural contemporary-English
voice of B01 is the standard for the whole book. Digits for specific quantities.

**B01, B02, B03 and B04 are COMPLETE. B05 has NOT been started.** Run B05 in a
FRESH session by pasting the kickoff below.

## Message to paste into the next chat

```
Gangs of Old Shanghai B05

Read CLAUDE.md, then HANDOFF.md, then book.json. Do batch B05 = ch13 (我当黄金荣管家的
见闻, What I Saw as Huang Jinrong's Steward) + ch14 (我所知道的黄金荣, The Huang Jinrong
I Knew), PDF 147–203, printed 138–194, end to end per the pipeline. These are the two
long household memoirs of Huang Jinrong: ch13 by a steward, ch14 by an insider —
DIALOGUE-HEAVY, with Huang's own boastful, colloquial, self-important speech (he uses
contractions; the narrators are more measured). This is where the household-memoir
voice begins; WRITE VOICE SHEETS for Huang Jinrong and the narrators as they appear,
and calibrate dialogue contractions UP from the cultured-reminiscence level of ch10 —
Huang should sound like a swaggering gang boss, not a scholar. This scan defeats
geometric indent detection, so assemble from the fallback and HAND-BUILD the zh files
to match the English 1:1 (see B01–B04); the measured OCR crop is `--left 0.06
--right 0.91 --top 0.09 --bottom 0.89 --lang chi_sim --psm 6`, folio cropped at the
foot; chapter-opening pages carry a large top margin, so the title/byline sit around
y≈0.2 of the page — crop there, not at the very top. CHECK each chapter's page feet for
the author's OWN numbered footnotes (ch05 and ch12 had them; ch09–ch11 did not): if so,
reproduce them as "Author's note." / "Editors' note." entries. Cast overlaps B04
heavily — Huang Jinrong (黄金荣), Du Yuesheng (杜月笙), Zhang Xiaolin (张啸林), the three
big bosses, the Sanxin Company (三鑫公司), the Rong Society (荣社), Lu Lanchun (露兰春),
Gao Xinbao (高鑫宝), the April 12 coup, Wang Shouhua (汪寿华) — REUSE the glossary rows
(178 of them now), do not re-romanize; consult authority.json before romanizing any new
name. Keep 军统 as "the Juntong" (unsettled until B08); 宋子文 = "T. V. Soong", 孔祥熙 =
"H. H. Kung", 晶报 = "The Crystal" (decided in B04). Cite printed folios; never invent
bridging text; verify names/numbers/low-confidence spans by eye against the scan (esp.
dates, dollar/tael amounts, the household roster, and Lu Lanchun's story); NEVER give
two notes anchors that END at the same point (a suffix-collision inverts the numbering);
do not pause for approval; deliver the EPUB in chat and paste the next kickoff.
```

## What is DONE (do not redo)

- **B01 (ch01–ch04, printed 1–28):** front matter + the two workers'-movement
  memoirs (Zhu Xuefan, Wu Chengfang). 43 notes, 33 glossary rows.
- **B02 (ch05–ch06, printed 29–67):** Green Gang origins — Li Shiyu's archival
  study and Jiang Hao's memoir-study. 77 notes, +21 glossary rows.
- **B03 (ch07–ch08, printed 68–107):** the Hongmen's history (Jiang Hao) and a
  French Concession detective's gallery of Shanghai gang figures (Xue Gengshen).
  40 notes (running total 160), +41 glossary rows (95 total).
- **B04 (ch09–ch12, printed 108–137):** older-generation lives — Zhang Renkui and
  the Ren Society, Yuan Hanyun (Yuan Kewen), Xu Langxi (by his son), and the first
  full life of Huang Jinrong. 54 notes (running total **214**), +83 glossary rows
  (**178 total**). Bylines: ch09 unbylined; ch10 Chen Timin; ch11 Xu Xiaogeng (set
  down by Yang Shi); ch12 pen-name "Xiang Bo" (reprinted from a ROC-history series,
  with one editors' note ①). All checks green, qa_epub PASS, epubcheck 0/0. See
  PROGRESS.md for the per-check detail and the crop-verification list.

## Tooling in place (do NOT revert) — full list in PROGRESS.md

- OCR crop `--left 0.06 --right 0.91 --top 0.09 --bottom 0.89 --lang chi_sim
  --psm 6`, folio at the foot. Geometric indent detection BYPASSED; zh files are
  HAND-BUILT to match the English 1:1. Chapter-opening titles/bylines sit ~y0.2.
- `work/structure_cfg.json` and `work/content_cfg.json` cover ch01–ch12 (regenerate
  or extend for ch13–ch14 next batch; heading_depth 1). work/ is gitignored.
- `data/noise.txt` has grown every batch; every entry is commented, longest-literal
  first. B04 added 23 entries and RELOCATED `一二八五` above the `一二八` (Jan-28)
  rule. Do NOT remove; extend as needed.
- No script logic changes in B04.

## Renderings settled / carry-forward (reuse; in glossary.json, 178 rows)

- **Decided cross-shelf forms:** 宋子文 = "T. V. Soong", 孔祥熙 = "H. H. Kung", 晶报 =
  "The Crystal", 戴传贤 = "Dai Chuanxian" (= Dai Jitao, noted). **the Juntong (军统)
  still shelf-UNSETTLED — decide at B08.**
- **B04 principals/cast (reuse, do not re-romanize):** Yuan Hanyun (袁寒云 = Yuan Kewen
  袁克文), Yuan Shikai, Yuan Keding, Yuan Jialiu; Chen Timin; Zhang Jian, Zhang Cha,
  Xu Baoshan, Feng Guozhang, Qi Xieyuan, Lu Yongxiang, He Fenglin, Li Chun, Chen
  Guangfu, Qian Xinzhi, Xu Jingren, Ge Guangting, Han Fuju, Song Zheyuan, Jiang
  Dingwen, Zhu Shaoliang, Zuo Zongtang, Zhang Zhuping, Zhang Xiaoruo, Zhao Zichao,
  Zhao Dan, H. H. Kung, T. V. Soong, Wang Shouhua, Chiang Kai-shek; Duan Qirui, Mei
  Lanfang, Zhang Zongchang, Chu Yupu, Xu Shiying, Li Jinbiao, Bu Zhangwu, Yu Daxiong,
  Qian Jiechen, Pu Yingxian, Empress Dowager Longyu; Xu Xiaogeng, Zheng Bichen,
  Toyama Mitsuru, Miyazaki Torazo, Tang Jiyao, Chen Shufan, Yao Yijia, Xu Yongchang,
  Yu Youren, Li Yuanhong, Dai Chuanxian, Zhou Fohai, Wang Yachen, Hu Zhenjia; Huang
  Bingquan, Fan Erdi, Zhou Yinren, Bai Chongxi, Chen Qun, Wang Bailing, Hao Pengju,
  Ding Mocun, Mei Siping, Li Changjiang, Gong Tianjian, Wang Wenkui, Li Zhiqing,
  Huang Yuantao. Orgs: the Sanxin Company (三鑫公司), the China Mutual Progress Society
  (中华共进会), The Crystal (晶报), Yuyun Mountain (峪云山); the Great World (大世界).
- **Source inconsistency kept as printed:** Zhang Renkui's hao is 锦湖 (Jinhu) in
  ch08/ch09 but 镜湖 (Jinghu) in ch12; rendered as printed, footnoted at ch12.

## Voice sheets

- **Narrators are the register.** JIANG HAO (ch06–ch07); XUE GENGSHEN (ch08): see
  earlier handoffs. YUAN HANYUN (ch10): cultured, relaxed, faintly ironic aristocrat-
  aesthete — opium-couch ease, literary allusion, gang-kinship banter; contractions in
  speech but NOT street-colloquial (2.8/1k). CHEN TIMIN (ch10 narrator): deferential,
  precise, self-deprecating.
- **Household memoirs (Huang/Du) begin at B05.** Write Huang Jinrong's voice sheet
  there: boastful, colloquial, self-important, contraction-heavy — the swaggering
  gang-boss register, DISTINCT from and higher-contraction than Yuan Hanyun's cultured
  reminiscence. Give each narrator (steward, insider) a two-line spec at first scene.

## Where the book stands

- B01–B03: the labour machine and the underground each USED the gangs; the Green
  Gang's and Hongmen's real and legendary origins; a detective's panorama of the
  Shanghai underworld. B04 turned to individual lives of the older generation and gave
  the first full, hostile biography of Huang Jinrong. Next (B05) the book stays with
  Huang Jinrong, seen up close from inside his household — the steward's and the
  insider's memoirs (ch13–ch14), the most dialogue-rich chapters yet.

## What is NEXT

- B05 = ch13–ch14, PDF 147–203, printed 138–194 (see the kickoff above).

## Open items for the read-through (carried forward + B04)

- B04 provisional / left-as-printed (for B10 reconciliation): single-appearance
  Nantong names (蒋暇堂, 韩奉持, 赵汉生, 许泽初, 赵鸿祠), 盛昇颐; 黄伯炮, 俞佩文, 浦应仙,
  吴桐渊, the seal 上第二子; 徐晓耕, 郑弼臣, 张国威, the 峪云山 romanization, 中华艺术
  专科学校 (sources give 新华艺专), recorder 杨×实; 樊尔谛, 龚天健, 王文奎, 鲁锦臣,
  邱子善, 李志清, 黄源焘, the puppet county/army roster, and the bandit nicknames 太保
  阿书 / 猪猡阿美. Zhang Renkui's 锦湖/镜湖 hao split (flag for check_reconcile).
- Earlier open items (B03 Hanliu romanization, ch07 lodge-founder names, 荩忠山, 和丛亮,
  杨庆山, 赵志游, 张法党; B02 ch06 genealogy legend, 24-char variants, 樊瑾成/丞, tongcao,
  渭清县) still stand.

## Environment / traps state

- setup.sh green; tesseract chi_sim/chi_sim_vert/chi_tra/chi_tra_vert + eng;
  PaddleOCR absent (dual-tesseract substitute); epubcheck 5.1.0 at
  /tmp/epubcheck-5.1.0/epubcheck.jar (java present). OMP_THREAD_LIMIT=1.
- `tests/run_tests.py` reports one FAIL — "hook stands down on template stub." This is
  EXPECTED for a mid-flight book (HANDOFF holds a real B05 kickoff, so the Stop hook
  correctly BLOCKS a kickoff-less wrap-up); the two enforcing paths both PASS. Do NOT
  "fix" the hook.
- Stray per-task branch expected at each batch start; canonical branch is
  claude/gangs-of-old-shanghai (consolidate onto it, delete the stray).
- qa_epub numbering trap (B04): never give two notes anchors that END at the same
  character; a suffix-collision inverts the marker numbering.
