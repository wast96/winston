# PROGRESS — 特務工作之理論與實際 (Gu Shunzhang)

Read this first. Written as work happens, not at the end.

## Status: Batches B01, B02, B03 (Chapters 1-3) DONE, built and QA-green.

Branch `claude/gu-shunzhang` (the single home for this project's work). Three of eight chapters translated.
`out/gushunzhang.epub` builds with a full pending-aware TOC; `qa_epub.py`
PASS (53 notes, 9 spine documents). Next batch is B04 (Chapter 4); see `HANDOFF.md`.

## Source facts established at setup (unchanged)

- 298-page image-only PDF, National Central Library (Taiwan) copy. No text
  layer. Vertical, right-to-left, Traditional characters. Running head down the
  outer margin, chapter title as running foot, folio at the bottom outer
  corner. Round NCL library seal stamped across the centre of many pages.
- Page offset drifts; use `book.json` per-section anchors. Chapter 1 opens at
  PDF 27 = printed 1 (confirmed by eye against folio 一).

## Batch B01 — Chapter 1 (緒論 / Introduction), printed folios 1-16 (PDF 27-42)

Three sections: §1 The Nature of Secret-Service Work (printed 1-6), §2 The
Importance of Secret-Service Work (printed 7-11), §3 The Scope of Secret-Service
Work (printed 12-16). 60 body paragraphs, 25 footnotes. No figures in this
chapter (pure text; confirmed by reading all 16 pages).

### Environment
- Installed: tesseract 5.3.4 with `chi_tra` and `chi_tra_vert`; pymupdf,
  pillow, numpy. `poppler-utils` present but unused for rendering.
- PaddleOCR NOT installed: its model weights download from a host outside the
  sandbox allowlist (as the sibling `ocr_dual.py` note already recorded), so
  check 1's dual engine is tesseract `chi_tra_vert` versus a direct eye-read of
  the 300 dpi scans, which for this chapter is the stronger of the two. Record
  this for later batches; retry Paddle only if the allowlist changes.
- `cv2` (opencv) NOT installed; `find_figures.py` needs it. Not required for
  Chapter 1 (no plates). Install before the first batch that has figures
  (Chapter 2 onward may have plates).

### Deliverables produced
- `out/ch01_reading.md` — clean English, the correction surface.
- `out/ch01_bilingual.md` — QC-only source-above-English draft (gitignored).
- `data/zh/ch01.txt` — verified source transcription for the parity check
  (gitignored; rebuilds from `out/ch01_bilingual.md`).
- `notes.json` — 25 notes keyed `ch01`. `glossary.json` — ledger extended.
- `out/gushunzhang.epub` — cumulative EPUB, full TOC, ch1 linked, ch2-8
  pending.

### The eight checks — what ran and what it found
1. **Dual-engine OCR diff.** Tesseract `chi_tra_vert --psm 5` (the measured
   crop) versus a direct character-by-character eye-read of every one of the 16
   rendered pages. The seal and the vertical type make tesseract noisy;
   systematic mangles seen: 緒論→繕論, 暗殺→唔殺, 特務→畫務/岩務, 偵緝→偵繩,
   格伯武 read cleanly. Every disagreement was resolved off the scan. The
   eye-read is the authority for this chapter.
2. **Blind double translation.** The seven argumentative/analytical passages
   (definition + GPU; the negative/positive-aspect argument; 防患未然; the
   履霜堅冰 / 百發百中 passage; the budget-figures passage; the 1927/C.P. history;
   the WWII-Pacific forecast) were retranslated in a separate context with no
   sight of the first pass and diffed. Close agreement throughout; the one
   substantive note was that 利害 in the history passage is 厲害 ("formidable"),
   which the finished text already reflects. Descriptive/list filler was
   sampled, not fully doubled.
3. **Round-trip back-translation.** Seven finished English passages (incl. all
   the numbers) were back-translated in a fresh context and diffed against the
   source: no omissions and no additions detected. It flagged the 履霜堅冰
   simile as possibly expanded, but the source carries both 履霜堅冰 and
   其來也漸, so the fuller English is faithful.
4. **Automated invariants.** `check_numbers.py` on the bilingual draft: 60
   pairs, 0 unaccounted numbers. `check_structure.py`: paragraph parity 60/60,
   heading shape consistent, glossary drift 0, all 25 note anchors resolve.
   (check_numbers was extended for this book: Traditional 萬/億, X分之Y
   fractions, English "million"/"billion", and several numeral-idioms.)
5. **Term ledger.** `glossary.json` extended with pinyin + attestation for the
   recurring referents (中國國民黨, 三民主義, 國民革命, 中央特科, 格伯武/GPU,
   別動隊, 一黨專政, 土豪劣紳, 巡捕房, 交通部, 偵察, 情報, 非常). Statuses set;
   GPU, KMT, Three Principles, National Revolution, Central Special Branch now
   attested with citations.
6. **Annotate not smooth.** Low-confidence and idiom spans became footnotes
   rather than smoothed away; no bracketed tags survive into the clean prose.
7. **External scholarship.** Checked and cited: Gu Shunzhang's biography and
   1931 defection; GPU/OGPU (1922-34); the 1927 KMT-CCP split; the Zhou and
   Qin-Han offices 司隸/司稽/鄉亭/游徼; the WWII-Pacific forecast (corroborated by
   1941). Sourced to Wikipedia / Baidu Baike / a CIA study; Grok/Grokipedia
   results appeared in searches and were NOT used (standing rule).
8. **Deep audit.** Coverage was 100 percent (every page eye-read), so the
   audit is the whole batch rather than a 3-5 percent sample. Spans given the
   full crop-and-zoom treatment: 河溝/山丘 (p41), 司隸/司稽/鄉亭/游徼 (p36),
   格伯武 (p28), 五百萬金磅 (p35), 百戰百勝 (p35). Estimated residual error rate:
   under 0.5 percent; no dropped numbers, no omissions.

### Flagged for Winston's read-through
- The budget figures on printed p9 (British "secret" fund ~£5,000,000/yr; Japan's
  military = half the budget, its "secret" fund = a third of that) are the
  author's 1933 rhetoric, uncorroborated. Noted as such.
- 別動隊 rendered "special-operations corps" (provisional; not found attested).
- Chapter 1 uses 格伯武 for GPU; Chapter 7 is expected to use 格伯烏. Both are
  glossed to the same referent "the GPU"; confirm the ch7 spelling in that batch.
- The self-referential irony (Gu praising the C.P. apparatus he himself built
  and then betrayed) is footnoted at "it began with the C.P."

## Batch B02 — Chapter 2 (特務組織 / Secret-Service Organization), printed folios 17-39 (PDF 43-71)

The chapter's 7 sections: §1 組織原則 (Principles of Organization, folio 17), §2
偵探網 (The Detective Network, folio 20), §3 交通網 (The Communications Network,
folio 21), §4 人才選擇 (Selection of Personnel, folio 22), §5 紀律 (Discipline,
folio 27), §6 待遇 (Treatment and Remuneration, folio 30), §7 訓練 (Training,
folio 35). Body ends folio 39.

### Environment / offset
- tesseract chi_tra + chi_tra_vert installed; pymupdf, pillow, numpy, opencv.
  PaddleOCR NOT installed (as predicted); tesseract as diff partner and the
  300&#8202;dpi eye-read as the authority.
- Offset verified at the ch2 opener: PDF 43 = printed folio 十七 (17), read off
  the page. The offset holds through the chapter; it does NOT drift within ch2,
  but three unpaginated figure plates (PDF 47-48, 49-50, 53-54) are bound in
  mid-chapter, which is where later drift comes from. Each plate is a recto
  with a blank verso.

### Deliverables produced
- `out/ch02_reading.md` (clean English), `out/ch02_bilingual.md` (QC only),
  `data/zh/ch02.txt` (parity source) — 101 aligned paragraphs.
- `notes.json` `ch02`: 19 footnotes (continuous numbering 26-44).
- `glossary.json`: 13 new entries (國家政治檢察局, 中央特務會議, 中央特務總部,
  各省區特務部, 青幫, 紅幫, 上海工部局, 鋼的紀律, 自我批評, 報務員, 譯電員, plus
  cross-refs). Statuses set; 青幫/紅幫/上海工部局 attested with citations.
- `figures.json` `ch02`: 4 figures — the three-layer inset (from p45) and the
  three full-page plates (中央特務組織圖, 偵探網分布圖, 交通網分布圖), cropped to
  `data/figs/`, placed by anchor, all embedded in the built EPUB with captions.
- `out/gushunzhang.epub` rebuilt (2 of 8 chapters, 44 notes); `qa_epub.py` PASS.

### The eight checks — what ran and what it found
1. **Dual-engine OCR diff.** Paddle unavailable; ran `ocr_crop.py`
   (chi_tra_vert, psm 5) and eye-read every page off the 300&#8202;dpi scan.
   Every proper name, number, figure label, and low-confidence span was
   crop-verified by eye. The seal sits mostly off the text columns on these
   pages; central columns still spot-checked.
2. **Blind double-translation.** Six argumentative passages (§1 secrecy, §4
   selection-explanation and 人非生而知之, §5 不教而誅, §6 bomb metaphor and the
   reward-warning) fully re-translated in a separate context and diffed. Close
   agreement throughout. It caught one real error: 否即棄之 had been mistranslated
   "only to cast him off afterward"; corrected to "nor reject one for the lack
   of such a tie." Enumerative/list filler was sampled, not fully doubled.
3. **Back-translation (omission detector).** Same six passages round-tripped to
   Chinese; no omissions or additions, all numbers and enumerations intact.
   (It could not catch a consistent misreading, by design — the double
   translation did.)
4. **Automated invariants.** `check_numbers.py` clean (0 unresolved over 101
   pairs) after extending NOISE with 萬 intensifier-idioms (萬不得已, 萬不可,
   萬一, 萬分, 萬萬, 千萬). `check_structure.py` parity 101/101; headings shape
   matches ch1.
5. **Term ledger.** glossary extended (above).
6. **Annotate not smooth.** Idiom, allusion, and reference spans became
   footnotes; no bracketed tags survive into the clean prose.
7. **External scholarship.** Checked and cited: Shanghai Municipal Council /
   工部局 and the Settlement police 捕房; the Green Gang 青幫 and Gu's own
   membership; the GPU public-organ name (國家政治檢察局 vs 國家政治保衛局). The
   Analects allusions (不教而誅 from 堯曰; 生而知之/學而知之 from 季氏/述而) and the
   唾面自乾 (Lou Shide) allusion verified against the classical sources. Sourced
   to Wikipedia; Grok/Grokipedia not used (standing rule).
8. **Deep audit.** Coverage was 100 percent (every page eye-read). Spans given
   the full crop-and-zoom treatment included 上海工部局/捕房 (p64), 二十人 (p69,
   the class-size cap), the four department labels and 中央特務統計研究會 on the
   org-chart plate, and the eight region labels on the detective-net plate.
   The audit surfaced a genuine omission — §7's training-class points f-m
   (folio 38) had been skipped between item e and "平時訓練"; all eight were
   translated and restored (parity rose 93 to 101). Estimated residual error
   rate after fixes: under 0.5 percent; no dropped numbers.

### Flagged for Winston's read-through
- The three org-chart plates are the author's **idealized blueprint**, not a
  documented apparatus. Footnotes say so.
- 國家政治檢察局 (source) is a variant name for the GPU; the commoner form is
  國家政治保衛局. Rendered "State Political Directorate," cross-referenced to ch1's
  格伯武/GPU note.
- Provisional glossary entries: 中央特務會議, 中央特務總部, 各省區特務部 (all from
  the plate; not independently attested as real bodies).
- Register note: the manual repeatedly reproduces Communist organizational
  idiom — 鋼的紀律 (steel discipline), 批評會 / 自我批評 (criticism and
  self-criticism), the heuristic-over-rote training method — in a handbook
  written for the Nationalist side. Footnoted where it appears.

## Batch B03 — Chapter 3 (特務工作的方法 / Methods of Secret-Service Work), printed folios 40-51 (PDF 72-83)

12 printed folios, all eye-read at 300 dpi. **Offset verified at the opener:**
PDF 72 = folio 四〇 (40), so the offset is now pdf−32 (it was pdf−31 at ch2;
one more unpaginated leaf has drifted it). Folios ran 四〇 through 五一 in
sequence, each read off the page. No plates in the chapter (find_figures found
only page furniture); nothing to caption. No cut-off sentences; the chapter
ends cleanly at folio 51.

### Structure (recounted against the pages, per the completeness rule)
- **§1 工作的原則 (Principles of the Work)** — six principles, in the body's
  order: 1 積極性 proactiveness, 2 秘密性 secrecy, 3 敏捷性 agility,
  4 精密性 precision, 5 普遍性 universality, 6 實際性 practicality, then a
  closing paragraph. This confirms `book.json`'s `toc_flags_resolved`: the
  translated TOC's "Flexibility" (item 2) and its "Secrecy" (item 5) were both
  wrong; there is no "flexibility" principle.
- **§2 工作上絕對反對的事項 (Things Absolutely Forbidden)** — three forbidden
  tendencies: 官僚化 bureaucratization (with sub-points a 失去敏捷性, b 失去秘密性),
  空洞化 empty formalism, 僱傭化 the mercenary spirit, then a closing paragraph.
- **§3 工作的實施 (Carrying Out the Work)** — five requirements: 創造的精神
  (a, b), 整個的計劃, 進行的步驟, 社會化 (a, b, c + a deferral), 只求實際
  (a, b), then a closing paragraph to superiors.
- Parity: 27 source paragraphs = 27 English paragraphs (7 + 6 + 14). No items
  dropped.

### The eight checks — what ran, what they found
1. **Dual-engine OCR diff.** PaddleOCR still will not install (weights host off
   the allowlist), so no automated character diff. Substituted the stronger
   defense: every one of the 12 folios read by eye off the 300 dpi scan, with
   tesseract `chi_tra_vert` as the only-machine partner. Low-confidence spans
   crop-verified (see below).
2. **Blind double-translation.** Five argumentative passages (積極性,
   實際性, the 空洞化 political-power argument, the 僱傭化 conclusion, and the
   整個計劃 passage) re-translated in a blind context and diffed: close
   agreement throughout, no divergence signalling ambiguity or misreading.
3. **Back-translation.** Three passages (the three-step 積極性 sequence, the
   doorman/visiting-card passage, the §3 closing to superiors) round-tripped
   to Chinese and diffed against the OCR: every clause intact, including the
   three steps, the 匪區 / time-span detail, and the "special difficulties"
   clause. No omissions or additions.
4. **Automated invariants.** `check_numbers.py` clean (0 unresolved over 27
   pairs) after two NOISE fixes; `check_structure.py` parity 27/27, headings
   one shape, 53 anchors 0 unresolved.
5. **Term ledger.** Six glossary rows added with attestation (below).
6. **Annotate not smooth.** The one genuinely damaged span (暗中進行, the 進
   under the NCL seal on folio 50) is footnoted, not silently smoothed; no
   bracket tags survive into the prose.
7. **External scholarship.** The Sunzi allusion (孫子·九地 靜如處女…出如脫兔)
   and 紙上談兵 (Zhao Kuo / Changping, via the Shiji, with the caveat that the
   four-char phrase is a later coinage) verified against the received texts;
   匪區 confirmed as the standard Nationalist "bandit" framing of the CCP.
   Wikipedia / classical sources; Grok not used (standing rule).
8. **Deep audit.** Coverage 100 percent (every page eye-read). Spans given the
   full crop-and-zoom treatment: the folio numbers 四〇–五一; the p73 一定不會
   等待 (confirmed 不會 present); the p50 暗中進行 under the seal; the p50
   衆手畢舉 and the p43 成效/威效 variant (no translation impact either way).
   Estimated residual error rate: well under 0.5 percent; no dropped numbers.

### Footnotes / glossary added
- **notes.json `ch03`: 9 notes** (continuous numbering follows automatically;
  total book notes now 53). Two classical allusions (Sunzi, 紙上談兵), one
  period-term reference (匪區), one tradecraft term with a forward cross-ref
  (社會化 → Ch.7), one scan-damage note (暗中進行 under the seal), and four
  vivid idioms kept literal (神不知鬼不覺, 掛一漏萬, 如水銀瀉地無孔不入,
  點石成金). About 0.75/folio, in line with ch2.
- **glossary.json: 6 term rows** — 匪區 (attested), 社會化 (decided, tied to the
  Ch.7 §1 title), 官僚化 / 空洞化 / 僱傭化 (decided, §2's three tendencies),
  積極性 (decided, records the 積極/消極 = positive/negative reading and lists
  all six §1 principles for cross-chapter consistency).

### Engineering: check_numbers.py NOISE extended (B03)
Two false-positive classes fixed, both documented in the file:
- Reordered the 萬-idiom patterns so `千萬` / `萬萬` precede the bare `萬X`
  forms; `萬不可` had been eating the 萬 out of `千萬不可` and orphaning a 千
  that read as 1000.
- Added `r"\d+[．.、]"` to strip the Arabic list enumerators the book prints
  at the head of sub-items (1. 2. 3.), which the English renders a./b./c.

### Flagged for Winston's read-through
- 匪區 rendered literally "bandit area" to keep the book's Nationalist
  standpoint (the author is a CCP security chief writing for his new KMT
  masters); footnoted.
- The Sunzi tag is quoted by Gu as 出如脱兔; the received/popular forms are
  後如脱兔 / 動如脱兔. Footnote says so.
- No new provisional glossary entries this batch; nothing left open in ch3.

## Engineering state (for later batches)
- `scripts/build_reading_epub.py` REWRITTEN for this book: driven by
  `book.json` structure (dict), one XHTML per translated chapter, full
  8-chapter/37-section pending-aware TOC (translated sections deep-linked),
  continuous footnote numbering, refuses to build on any unmatched anchor.
- `scripts/split_bilingual.py` NEW: derives `out/<id>_reading.md` and
  `data/zh/<id>.txt` from one `out/<id>_bilingual.md`, so the shipped prose and
  the parity source cannot drift.
- `scripts/check_numbers.py` extended (see check 4 above).
- `scripts/ocr_crop.py` crop geometry is correct for this book; just run it.
