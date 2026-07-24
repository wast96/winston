# PROGRESS

Working state for the full-book run. Updated as each chapter lands.

## Environment notes

- tesseract 5.3.4 with chi_sim and chi_sim_vert. PyMuPDF renders (poppler cannot, JBIG2).
- PaddleOCR: pip install fails in this environment (PyYAML/debian conflict, then no usable wheel).
  Dual OCR therefore uses tesseract psm6 vs psm4 diff, exactly as ch1 did. Disagreement spans
  get magnified-crop adjudication before translation.
- GitHub push access: BLOCKED at session start. Both the git proxy and the API report the app
  token has read-only contents permission on wast96/winston. Work is committed locally on
  branch claude/chinas-king-assassins-folder-anmqi5; push retried at every commit point.
  Winston: grant the Claude GitHub App write access to wast96/winston to let pushes through.

## Verified structure

- PDF page = printed page + 10. Verified: PDF 37 opens ch2 at printed 27; PDF 11 is printed 1 (小引).
- TOC runs PDF 6-9 (not 6-8; ch15's entry is on PDF 9).
- PDF 336 is the Anna's Archive provenance page, not book text. Book text ends printed 325 (PDF 335).

## Chapter map (printed pages / PDF pages)

| # | Title (as OCR'd, cleaned) | Printed | PDF |
|---|---|---|---|
| 小引 | 蒋介石、戴笠、王亚樵 | 1-8 | 11-18 |
| 1 | 首次刺杀出师不利 (DONE, reference/) | 9-26 | 19-36 |
| 2 | 谋杀蒋介石的第一次预演 | 27-42 | 37-52 |
| 3 | 诛杀赵铁桥 | 43-56 | 53-66 |
| 4 | 挫败上海三大亨 | 57-80 | 67-90 |
| 5 | 庐山大刺杀 | 81-108 | 91-118 |
| 6 | 两场因由各异的谋杀，同时发生在上海北火车站 | 109-136 | 119-146 |
| 7 | 宋案扑朔迷离，申城再起风波 | 137-152 | 147-162 |
| 8 | 谋刺日酋白川 | 153-176 | 163-186 |
| 9 | 枪口曾瞄准"国联"代表李顿 | 177-200 | 187-210 |
| 10 | 王亚樵走麦城 | 201-218 | 211-228 |
| 11 | 辗转粤闽 | 219-238 | 229-248 |
| 12 | 杀手与情人 | 239-258 | 249-268 |
| 13 | 孙凤鸣行刺前后 | 259-280 | 269-290 |
| 14 | 蛰影(?)困香江 (title glyphs rough; re-verify at ch14) | 281-298 | 291-308 |
| 15 | 梧州，一代枭雄的人生终点 | 299-325 | 309-335 |

Uncertain TOC readings to re-verify against chapter openers when reached: ch14 title
(OCR gave 投影蛋恒/秽影恒屋困香江, likely 蛰影 or similar), ch14 section 47 subject
(戴笠遗书 vs other), ch8 section 30 (朝鲜义士 name, likely 金九 Kim Gu).

## Per-chapter log

### Prologue (小引) - pending
### Ch 2-15 - pending

## Checks status (Winston's 8)

1. Dual OCR + char diff: tesseract psm6/psm4 (paddle unavailable), flags adjudicated by crop. ACTIVE per chapter.
2. Blind double translation: fresh-context second pass per chapter, diffed. ACTIVE per chapter.
3. Back-translation omission check: per chapter. ACTIVE.
4. Invariants: extended script, every chapter. ACTIVE.
5. Term ledger: builds through the run, rendered at end. PENDING.
6. Annotate not smooth: literal pass with LOW-CONF tags kept per chapter (out/chNN_literal.md), uncertainty notes in apparatus. ACTIVE.
7. Scholarship consistency: per-note web checks + end pass. ACTIVE/PENDING.
8. Random-sample deep audit: end of run. PENDING.
