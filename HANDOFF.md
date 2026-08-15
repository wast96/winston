# HANDOFF — The Sword Roars in the West Wind

## Message to paste into the next chat

> Paste this VERBATIM to start Batch 3. It is the only bridge between
> conversations; HANDOFF/PROGRESS/book.json describe the state, but the pages
> are the voice, so read the last two pages of ch02's English first.

```
Sword Roars B03

Read CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. Work on branch claude/the-sword-roars (the canonical book
branch; if the harness starts you on a stray per-task branch, consolidate per
CLAUDE.md rule 2). Run ./setup.sh first.

Do Batch 3 = Chapter Three, "谁是犹大 / Who Is Judas" (ch03), PDF 60-81,
printed 45-66, end to end per the pipeline in CLAUDE.md. Seven sections:
ch03s01 一、他们的手上有血 (PDF 61, printed 46), ch03s02 二、盛会难再 (PDF 62,
printed 47), ch03s03 三、半分钟都差不得 (PDF 66, printed 51), ch03s04
四、装成出殡救人 (PDF 68, printed 53), ch03s05 五、她要两本出国护照和巨额美金
(PDF 70, printed 55), ch03s06 六、爆竹声中的锄奸真相 (PDF 74, printed 59),
ch03s07 七、贺稚华到底想要什么 (PDF 78, printed 63). Simplified Chinese,
horizontal; OCR chi_sim --psm 6; crop --left 0.06 --right 0.95 --top 0.11
--bottom 0.955; offset is a constant 15 (printed = pdf - 15), no plate drift
so far, but READ each opener's folio off the scan.

BEFORE translating, read the final two pages of Chapter Two's English
(out/ch02_reading.md) so the voice carries over unbroken. Chapter One remains
the FROZEN register reference: run check_register.py --ref out/ch01_reading.md
on ch03 and record it (expect the dialogue metric to be more meaningful here,
this chapter has real scene dialogue). Chapters One and Two's data/zh were
hand-transcribed off the scans (OCR too noisy, assemble breaks on figure/opener
pages); do the same for ch03 where assemble misaligns, and keep parity exact.
Cite printed folios in notes, never PDF pages. Never invent bridging text: if
OCR breaks mid-sentence or a leaf is damaged, crop the scan and read the real
continuation, or footnote the gap. Verify every name, number and low-confidence
span against a magnified crop before writing. Consult authority.json and
glossary.json for settled renderings (esp. Gu Shunzhang, Zhou Enlai, the
Central Special Branch, the Red Squad, Chen Geng/Wang Yong, Xu Enzeng).

Deliver the built EPUB attached in the chat, and paste the Batch 4 kickoff
verbatim in the same reply.
```

## DONE (one line per batch; do not redo)
- Survey: structure, offsets, style contract, skeleton EPUB. (earlier session)
- **B01 = ch01 (voice gate):** full translation (165 paragraphs), 115 footnotes,
  12 figures, glossary seeded, all checks green, epubcheck clean, blind-critique
  loop run, held at and passed the human voice gate. Details in PROGRESS.md.
- **B02 = ch02:** full translation (56 paragraphs), 28 footnotes, 5 figures,
  14 new glossary rows; all checks green (parity 56=56, numbers 0, align/content
  OK, entities 0 misses, register within tolerance), qa_epub PASS, epubcheck
  0/0. Details in PROGRESS.md.

## Tooling in place — DO NOT REVERT
- `scripts/indents.py`: furniture-band drop by y-position (`FURNITURE_TOP=0.11`,
  `FURNITURE_BOTTOM=0.955`). Folio + running head are one TOP band; no foot.
- `scripts/check_numbers.py`: arabic+万 combiner ("31万"=310,000) BEFORE the
  noise loop. (Chinese-numeral+万 like 五十多万 is handled by a --noise entry,
  not the combiner.)
- `scripts/check_content.py`: `name_map` skips `_`-prefixed / non-dict keys.
- `data/noise.txt`: this book's event-date names, numeral-bearing proper names,
  decade labels, idioms. B02 appended a block (十足, 万能, 两肋, 五十多万, 万益,
  蒋三大). Extend per its header; longest literal first; comment every entry.
- OCR crop for this book: `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955
  --lang chi_sim --psm 6`. Offset constant 15 (printed = pdf - 15).
- **apparatus_merge.py gotcha:** it writes glossary rows at the JSON TOP LEVEL;
  MOVE them into the right section (people/organizations/places/terms) by hand
  after merging, or the builder's render_glossary throws on a flat row.
- **figures.json `file` must be a BASENAME** (e.g. `ch02-chen-yun.png`); the
  builder prepends `data/figs/` for the source and `images/` for the EPUB. A
  path prefix breaks qa_epub with a missing-image error. Figure `before` anchors
  must fall in the FIRST ~80 chars of a paragraph (paragraph-start), and note
  anchors CANNOT sit on the `##` chapter-title line (builder scans body
  paragraphs and `###` section headings only).

## Renderings settled B01-B02 (also in glossary.json / STYLE.local.md)
- 中央特科 = the Central Special Branch (short: the Special Branch); 红队/打狗队 =
  the Red Squad / the dog-beating squad; 化广奇 = Hua Guangqi; 黎明 = Liming
  ("the Dawn"); 王庸 = Wang Yong; 亭子间 = tingzijian; 摩登 = modern.
- Western scholars keep their own names: 魏斐德 = **Wakeman**; 维克托·乌索夫 =
  **Victor Usov**; 别尔津 = **Berzin**; **约翰·拜伦 = John Byron** and
  **罗伯特·帕克 = Robert Pack** (*The Claws of the Dragon*, 1992/1998).
- 侦察 in a security context = investigation/surveillance, not "reconnaissance".
- Numbers: full value ("310,000", "500,000"), never "wan"; 中午12时 = "twelve
  noon" (carry the 12).
- B02 additions (glossary): Zong Mengping, Kuang Yaming, **Shi Yanfen** (martyr;
  DISTINCT from **Shi Yaobin**, the Yixing county secretary), Chen Yun, Chen
  Duxiu, Peng Shuzhi, Luo Yinong, Zhao Shiyan, Wang Shouhua, Cai Mengjian,
  Xue Yue, Yang Zhihua (pen name **Du Ning**); Nanyang Brothers Tobacco Company;
  the Shanghai General Labor Union.

## Voice sheets (carry forward)
- **The author (Ye Xiaoshen):** warm, buttonholing popular-history narrator with
  a sardonic edge and open reverence for his subjects; keep the heat in the
  verbs and rhythm, ration exclamation and rhetorical questions. See the
  Voice-sharpening line in STYLE.local.
- **Chen Geng (quoted diary/autobiography):** terse, military, plain.
- **Dong Jianwu (quoted notes):** earnest, self-effacing, morally didactic.
- **Li Qiang (quoted letter):** precise, insistent, correcting the record.
- **Xu Enzeng (quoted):** cold, procedural, bureaucratic.
- **Dong Huifang (quoted):** warm, familial, concrete.
- **The 1927 Party leaders in committee** (Chen Duxiu, Luo Yinong, Zhao Shiyan,
  new in B02): clipped, procedural, decisive; meeting-record speech, lightly
  contracted, not banter (they are quasi-official utterances).
- **Kuang Yaming (quoted defiance):** plain, resolute, unbowed.
- **Gu Shunzhang:** the chapter's foil; the author writes him hot and
  contemptuous (gangster, "blood-and-iron"). Keep the temperature; the verdict
  is the author's, footnote where a factual claim is checkable.

## Where the story stands
Chapter One established the two sides and the founding of the Central Special
Branch. Chapter Two drew the moral contrast the whole book turns on: the
incorruptible underground heroes (Zong Mengping, Kuang Yaming, Shi Yanfen) set
against Gu Shunzhang the "lumpen proletarian," whose gangster instincts (not his
politics) foreshadow his 1931 treason. Chapter Three ("Who Is Judas") turns to
the hunt for a traitor: the killing of He Zhihua (贺稚华) and the Special
Branch's counter-espionage against informers. Expect real scene dialogue and
action (arrest/chase) — watch pronoun fog, keep the voice sheets current.

## Next-batch scope
B03 = ch03, PDF 60-81 (printed 45-66), seven sections ch03s01-s07 (openers at
PDF 61, 62, 66, 68, 70, 74, 78). A large chapter (22 pp.). Plan for figures
(eyeball every page; find_figures misses line art and dense newsprint).

## Open traps / environment
- `data/zh/` is gitignored (copyright); a fresh checkout cannot regenerate the
  hand-transcribed sources. `check_structure --config` therefore cannot run a
  whole-book parity pass on a clean checkout; use per-unit `--pairs`.
- `find_figures.py` misses dense-newsprint clippings and line-art diagrams;
  eyeball every page and hand-crop.
- `tests/run_tests.py` "hook stands down on template stub" FAIL is benign (a
  real kickoff is present). Not a regression.
- `OMP_THREAD_LIMIT=1` mandatory for tesseract; verify `pgrep -c tesseract` = 0
  after OCR. epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (setup fetches).
- `authority.json` is updated on WHOLE-BOOK completion, not per batch; the B02
  decided renderings are in glossary.json and listed above.
