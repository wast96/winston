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

### Prologue (小引) - DONE (all checks signed off)

- Printed 1-8, PDF 11-18. 54 source paragraphs, all eight pages eye-verified
  against the scan (full-page magnified views), not trusted to OCR.
- Verified readings worth knowing: the book itself prints Ji'e Alley No. 54
  (printed p5) and No. 45 (printed p6) for the same courtyard; documented
  address is No. 53. Preserved as printed, noted. 洪武街51号, 贺衷寒, 1916,
  张啸林, 熊心虎胆, 娘希匹 all crop-confirmed.
- Figures: 3 (printed 2, 4, 7), captions read from the vertical margin text:
  蒋介石与戴笠 / 北伐时期的蒋介石 / 令蒋介石寝食不安的王亚樵.
- Checks: dual OCR flags adjudicated by eye against the scan. Blind double
  translation: pass B by a fresh-context agent, 54/54 paragraphs, mean
  string similarity 0.485, all top divergences reviewed = stylistic only,
  zero meaning conflicts. Invariants: 0 unresolved (NOISE list extended;
  bare-一 suppressed as chronic false positive, documented in script).
  Entities: 5 flags, all natural pronominalization, adjudicated OK.
  Back-translation omission check: PASS. 54/54 paragraphs, mean length
  ratio 1.02, one flag (para 32) adjudicated as checker-side expansion of
  "unnoticed"; zero omissions, zero additions detected.
- Literal pass with the polished layer beside it: out/prologue_literal.md
  vs out/prologue_reading.md. Bilingual audit: out/prologue_bilingual.md.
- Notes: 21 (2.6/printed page). Scholarship checks run via web: Feng
  Yuxiang/Yan Xishan absent from the April 18 1927 ceremony (photo lineup
  CONTRADICTED); Three Great Policies not in Sun's testament (attribution
  CONTESTED, stated in note); Ji'e Alley 53 documented (book's 54/45 noted);
  Ten-Man Team = 1928 Liaison Group retrojected (chronology CONTRADICTED,
  noted); Wang-Dai sworn-brother tie attested, car-crash rescue
  UNCORROBORATED (noted); April 1927 warrant UNCORROBORATED (noted).
- Glossary: +5 people, +2 orgs, +3 places, +6 terms.
- Build: QA PASS, 2 documents (prologue + ch1), 79 refs/bodies/backlinks.
- For Winston's read-through: the 校长="Commandant" and 委座="the
  Generalissimo" conventions are mine; the anachronism notes lean on them.
  娘希匹 rendered "God damn his mother" (force kept, Ningbo lost, noted).

### Ch 2 (谋杀蒋介石的第一次预演) - checks in flight

- Printed 27-42, PDF 37-52. 94 source paragraphs; all 16 pages eye-verified
  against magnified scans; idiom spans crop-verified (真空做一回人, the
  inverted 站着生/跪着死 maxim).
- Figures: 3 (printed 30, 31, 32). The p30 group photo's margin caption
  identifies the March 10, 1927 KMT Third Plenum photo with a full name
  roster (incl. Soong Ching-ling, T.V. Soong, Dong Biwu, Mao Zedong);
  translated in full.
- Scholarship: chapter compresses 1929-30 events into a March-1928 frame.
  Wang Leping assassination documented Feb 18, 1930 (office, 314 Route
  Cardinal Mercier; book stages an Avenue Joffre car ambush Feb 17) -
  CORROBORATED/REDATED, staging differs. Fang Zhenwu: chairman May 1929,
  telegram-summons arrest Sept 1929, Tangshan in irons, freed post-Mukden -
  the book's arrest scene matches the record to the prop list, moved back
  a year and a half. Shi Yousan Dec 1929 Pukou revolt = likely seed of his
  "crushed force." Zhao Tieqiao (1886-1930) attested, shot 24 July 1930 at
  the China Merchants gate; popular tradition names ch1's Wang Ganting and
  Niu Anru among shooters and gives the informer motive the book uses.
  Zhou Fengqi note: Dai Li's first master, shot by Juntong 1938. Peng
  Jianguo/Fourth Brigade UNCORROBORATED (provisional). Whampoa 6th class
  cavalry CORROBORATED (1926, book says 1925).
- Notes: 33 (2.1/printed page; dialogue-heavy chapter). Glossary: +26
  people/orgs/places/terms (incl. Soong conventional forms for the caption
  roster). Invariants 0/94 after NOISE growth (九哥, 石友三's 三, ordinals).
  Entity check caught 4 real drops (attribution, agent, two names) - fixed;
  remaining 18 flags adjudicated as pronominalization.
- Build: QA PASS, 3 documents, 112 refs/bodies/backlinks.
- Blind double translation: DONE. Pass B by a fresh-context agent, 94/94
  paragraphs, mean string similarity 0.331 (lower than the prologue's 0.485
  because this chapter is dialogue-heavy, where two translators diverge in
  wording far more than in narration). All 8 most-divergent paragraphs
  reviewed line by line: every one is a stylistic difference, zero meaning
  conflicts, zero [UNCLEAR] flags raised by pass B. Pass B independently
  reached the same reading on every load-bearing point.
- Back-translation omission check: STILL RUNNING at handoff (agent writing
  data/qc/ch02_backzh.txt). To finish: diff its 94 lines against
  data/zh/ch02.txt by CJK length ratio + SequenceMatcher, same script as
  the prologue used; flag ratio <0.72 or >1.40 or sim <0.35, adjudicate.

### Ch 3 (诛杀赵铁桥) - translated; A/B + round-trip in flight at handoff

- Printed 43-56, PDF 53-66. 98 source paragraphs; all 14 pages eye-verified
  against magnified scans.
- Figures: NONE. The only ink-density hit in the range (p0057-f1) is the
  recurring recto margin medallion, i.e. page furniture, confirmed by eye
  across all 14 page views. figures.json["ch03"] = [] deliberately.
- Scholarship (the strongest corroboration in the book so far): Li Guojie
  (1881-1939), Li Hongzhang's eldest grandson and China Merchants board
  chairman from 1924, DID hire Wang Yaqiao to kill Zhao Tieqiao, and Zhao
  WAS shot dead at the company gate on 24 July 1930 - date, place and two
  named shooters (Wang Ganting, Niu Anru) all match the record. The
  chapter's spine is history. Aftermath the book omits, added as a note:
  Chiang's commission (T.V. Soong, Yu Feipeng, Wu Tiecheng) traced it to
  Li Guojie, who drew 8 years; Li was himself shot by Dai Li's service in
  Feb 1939. UNCORROBORATED: the Jiang'an ship as the fee (payment itself
  is documented, the vessel is not); Zhao's American finance degree (his
  documented education was in Japan) - noted as the author's furnishing.
- Notes: 31 (2.2/printed page). Glossary: +17.
- Uncertain readings flagged in notes, not smoothed: 脑拿牌 car marque
  (glyphs certain, make unidentifiable - kept as "Naona"); the book prints
  刘德山 here vs 刘德才 elsewhere for the same man (kept as printed, noted).
- Invariants 0/98 after further NOISE growth. Entity check caught 6 real
  drops - fixed; remaining 20 adjudicated as pronominalization.
- Build: QA PASS, 4 documents, 139 refs/bodies/backlinks.
- Blind pass B: STILL RUNNING at handoff (agent writing
  data/qc/ch03_passB.md, 98 paragraphs). Back-translation not yet launched.

### Ch 4 (挫败上海三大亨) - prep only
- Printed 57-80, PDF 67-90 (24 pages, the longest chapter so far).
- Rendered + OCR'd (data/txt/p0067-p0090.txt) and page thumbnails written to
  data/verify/. NOT yet eye-verified, NOT translated.
- Next step: read the OCR, then eye-verify all 24 page views against it
  before writing a word of translation.

### Ch 5-15 - pending

## Resuming this run

The per-chapter loop, in order:
1. render.py / ocr_crop.py / find_figures.py over the chapter's PDF range
2. read data/txt/*.txt, then READ EVERY PAGE THUMBNAIL in data/verify/ and
   correct the OCR against it by eye; write the corrected source to
   data/zh/chNN.txt (one paragraph per line, "### " for section heads)
3. launch the blind pass-B agent (see the prompts used for ch2/ch3 - they
   specify: never open out/, follow glossary.json, one paragraph per source
   paragraph, write to data/qc/chNN_passB.md)
4. write out/chNN_literal.md (literal, [LOW-CONF] tags kept) then
   out/chNN_reading.md (polished, same paragraph count as source)
5. build out/chNN_bilingual.md; run check_invariants.py and qc_entities.py;
   fix real drops, adjudicate the rest
6. diff pass B; launch and diff the back-translation
7. web-check every historical claim; write notes into notes.json under the
   chapter key, new names into glossary.json with status
8. figures.json entry (or [] with a reason); build_reading_epub.py; qa_epub.py
9. update PROGRESS.md, commit, push

Note numbering is CONTINUOUS across the book and is assigned at build time
by reading order, so notes.json order within a chapter does not matter.

## Checks status (Winston's 8)

1. Dual OCR + char diff: tesseract psm6/psm4 (paddle unavailable), flags adjudicated by crop. ACTIVE per chapter.
2. Blind double translation: fresh-context second pass per chapter, diffed. ACTIVE per chapter.
3. Back-translation omission check: per chapter. ACTIVE.
4. Invariants: extended script, every chapter. ACTIVE.
5. Term ledger: builds through the run, rendered at end. PENDING.
6. Annotate not smooth: literal pass with LOW-CONF tags kept per chapter (out/chNN_literal.md), uncertainty notes in apparatus. ACTIVE.
7. Scholarship consistency: per-note web checks + end pass. ACTIVE/PENDING.
8. Random-sample deep audit: end of run. PENDING.
