# HANDOFF — The Sword Roars in the West Wind

## Message to paste into the next chat

> Paste this to start Batch 2 **after** you have approved the Chapter One voice
> gate (voice / note density / formatting). If you want changes to Chapter One
> first, tell me here instead and I will revise before B02.

```
Sword Roars B02

Read CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. Work on branch claude/the-sword-roars (the canonical book
branch; if the harness starts you on a stray per-task branch, consolidate per
CLAUDE.md rule 2). Run ./setup.sh first.

Do Batch 2 = Chapter Two, "清者自清，浊者自浊 / The Clean Stay Clean, the Foul
Stay Foul" (ch02), PDF 50-59, printed 35-44, end to end per the pipeline in
CLAUDE.md. Two sections: ch02s01 一、英雄阳刚 (PDF 51, printed 36) and ch02s02
二、流氓无产者 (PDF 55, printed 40). Simplified Chinese, horizontal; OCR chi_sim
--psm 6; crop --left 0.06 --right 0.95 --top 0.11 --bottom 0.955; offset is a
constant 15 (printed = pdf - 15), no plate drift — but read each opener's folio
off the scan.

BEFORE translating, read the final two pages of Chapter One's English
(out/ch01_reading.md) so the voice carries over unbroken; Chapter One is the
FROZEN register reference — run check_register.py --ref out/ch01_reading.md on
ch02 and record it. Chapter One's data/zh was hand-transcribed off the scans
(OCR too noisy, assemble breaks on figure/opener pages); do the same for ch02
where the pipeline's assemble misaligns, and keep parity exact. Cite printed
folios in notes, never PDF pages. Never invent bridging text: if OCR breaks
mid-sentence or a leaf is damaged, crop the scan and read the real
continuation, or footnote the gap. Verify every name, number and low-confidence
span against a magnified crop before writing. Consult authority.json and
glossary.json for settled renderings.

Deliver the built EPUB attached in the chat, and paste the Batch 3 kickoff
verbatim in the same reply.
```

## DONE (one line per batch; do not redo)
- Survey: structure, offsets, style contract, skeleton EPUB. (earlier session)
- **B01 = ch01 (voice gate):** full translation (165 paragraphs), 52 footnotes,
  12 figures, glossary seeded, all checks green, epubcheck clean, blind-critique
  loop run. Held at the human voice gate. Details in PROGRESS.md.

## Tooling in place — DO NOT REVERT
- `scripts/indents.py`: furniture-band drop by y-position (`FURNITURE_TOP=0.11`,
  `FURNITURE_BOTTOM=0.955`), no more `ocr_crop.folio_present`. This book's folio
  + running head sit in one TOP band; there is no running foot.
- `scripts/check_numbers.py`: arabic+万 combiner ("31万"=310,000) BEFORE the
  noise loop (fixes the `\d+[．.、]` list-marker rule eating a decimal like 2.6万).
- `scripts/check_content.py`: `name_map` skips `_`-prefixed / non-dict glossary
  keys.
- `data/noise.txt`: this book's event-date names, numeral-bearing proper names,
  decade labels, and idioms. Extend per its header; longest literal first.
- OCR crop for this book: `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955
  --lang chi_sim --psm 6`.

## Renderings settled this batch (also in glossary.json / STYLE.local.md)
- 中央特科 = the Central Special Branch (short: the Special Branch); 红队/打狗队 =
  the Red Squad / the dog-beating squad; 化广奇 = Hua Guangqi; 黎明 = Liming
  ("the Dawn"); 王庸 = Wang Yong; 亭子间 = tingzijian; 摩登 = modern.
- Western scholars keep their own names: 魏斐德 = **Wakeman** (not Wei Feide);
  维克托·乌索夫 = **Victor Usov**; 别尔津 = **Berzin**.
- 侦察 in a security context = investigation/surveillance, not "reconnaissance"
  (keep reconnaissance for Chen Geng's 1943 battlefield 侦察).
- Numbers: full value ("310,000"), never "31 wan"; mixed arabic+万 handled in
  check_numbers.

## Voice sheets (carry forward; this chapter is mostly quoted documents, not scene dialogue)
- **The author (Ye Xiaoshen):** warm, buttonholing popular-history narrator with
  a sardonic edge and open reverence for his subjects; keep the heat in the
  verbs and rhythm, ration exclamation and rhetorical questions. See the
  Voice-sharpening line in STYLE.local.
- **Chen Geng (quoted diary/autobiography):** terse, military, plain; short
  declaratives, no ornament.
- **Dong Jianwu (quoted notes):** earnest, self-effacing, morally didactic.
- **Li Qiang (quoted letter):** precise, insistent, correcting the record.
- **Xu Enzeng (quoted):** cold, procedural, bureaucratic.
- **Dong Huifang (quoted):** warm, familial, concrete.

## Where the story stands
Chapter One establishes the two sides and the origin of the Central Special
Branch: Gu Shunzhang the magician-spymaster; Chen Geng (Wang Yong) the
intelligence chief; Zhou Enlai the founder; the "Red Pastor" Dong Jianwu; the
White Terror of 1927 that drove the Party underground; the founding meetings of
Nov 1927; the deep pre-history through Mei Baoji and Mei Gongbin; and the
workers' pickets / "dog-beating squad" that became the Red Squad. Chapter Two
turns to the character of these men ("A Hero's Mettle," "The Lumpen
Proletariat").

## Next-batch scope
B02 = ch02, PDF 50-59 (printed 35-44), sections ch02s01 (PDF 51) and ch02s02
(PDF 55). Light chapter (10 pp.).

## Open traps / environment
- `data/zh/` is gitignored (copyright); the hand-transcription approach means a
  fresh checkout cannot regenerate it from OCR. Raised at the gate.
- `find_figures.py` misses dense-newsprint clippings and line-art diagrams;
  eyeball every page and hand-crop (as done for the Shen Bao ads and the org
  chart in ch01).
- `tests/run_tests.py` "hook stands down on template stub" FAIL is benign (real
  kickoff present). Not a regression.
- `OMP_THREAD_LIMIT=1` mandatory for tesseract; verify `pgrep -c tesseract` = 0
  after OCR.
