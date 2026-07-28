# PROGRESS — 特務工作之理論與實際 (Gu Shunzhang)

Read this first. Written as work happens, not at the end.

## Status: Batches B01–B06 DONE, built and QA-green.

Branch `claude/gu-shunzhang` (the single home for this project's work). Six of eight
chapters translated (Chapter 6 is partial: §1-3 done, §4-11 pending in B07/B08).
`out/gushunzhang.epub` builds with a full pending-aware TOC — Chapter 6 is linked
and its §1-3 deep-linked, §4-11 shown pending; `qa_epub.py` PASS (108 notes, 12
spine files, 1 figure). Next batch is B07 (Chapter 6 §4-6); see `HANDOFF.md`.

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

## Batch B04 — Chapter 4 (特務觀念 / The Secret-Service Mindset), printed folios 52-57 (PDF 84-89)

6 printed folios, all eye-read at 300 dpi. **Offset verified at the opener:**
PDF 84 = folio 五二 (52), so the offset holds at pdf−32 (unchanged from ch3;
no new plate drifted it). Folios ran 五二 through 五七 in sequence, each read
off the page. The ch4 opener's folio needed a second, taller crop: the 二 of
五二 has a faint upper stroke that a first tight crop clipped, making it look
like 五一; the continuous prose across the p84/p85 break (…他的行動一定 / 也不
合正軌…) and the unambiguous 五三 on p85 settle it as 52. No plates in the
chapter (all six folios are prose); nothing to caption. No cut-off sentences;
the chapter ends cleanly at folio 57.

### Structure (recounted against the pages, per the completeness rule)
- **§1 觀念問題之重要 (Why the Question of Mindset Matters)** — one continuous
  paragraph (folios 52-53). The column-top ink profile shows a single
  paragraph indent and no internal break.
- **§2 觀念鬥爭 (The Struggle over Mindset)** — four paragraphs: the setup (a
  comrade offered a 100,000-yuan bribe for a secret document), the 第一
  (self-serving) impulse, the 第二 (public-minded) impulse, and the resolution
  (the two contend; character or ruin turns on which wins). Title translated
  faithfully per `book.json` `toc_flags_resolved`: literal 觀念鬥爭 = "the
  struggle over mindset"; the translated TOC's "Building the Right Mindset" is
  an interpretation and was NOT followed. Confirmed against the section opener.
- **§3 特務人員的人生觀 (The Life-Outlook of Secret-Service Personnel)** —
  three prose paragraphs (the public-minded outlook; the wrong reasons to join;
  self-examination by the struggle-over-mindset method), a list-introduction,
  a **ten-item numbered list** of 要…勿… ("do this, not that") maxims, and a
  總之 conclusion.
- Parity: 20 source paragraphs = 20 English paragraphs (1 + 4 + 15, the 15
  being 3 prose + list-intro + 10 items + conclusion). All ten list items
  present; nothing dropped.

### The eight checks — what ran, what they found
1. **Dual-engine OCR diff.** PaddleOCR still will not install in a fresh
   container (weights host off the allowlist); tesseract `chi_tra_vert --psm 5`
   is the only-machine partner. Substituted the stronger defense: every one of
   the 6 folios read by eye off the 300 dpi scan. Meaning-bearing spans
   crop-verified: item 5 奪取 (vs a possible 爭取), 大菜, 遂結成, the item-9
   construction, and both opener folios.
2. **Blind double-translation.** The chapter is almost entirely argumentative,
   so the bulk was doubled, not sampled: §2's resolution paragraph and §3's
   opening outlook paragraph re-rendered independently and diffed — close
   agreement, no divergence signalling ambiguity beyond the item-9 grammar
   (below).
3. **Back-translation.** The full ten-item list and §2's setup paragraph
   round-tripped to Chinese and diffed against the source: every couplet and
   clause intact (including the 100,000-yuan figure and all ten items); no
   omissions or additions.
4. **Automated invariants.** `check_numbers.py` clean (0 unresolved over 20
   pairs); `check_structure.py` parity 20/20, headings one shape across all 4
   built chapters, 62 anchors 0 unresolved.
5. **Term ledger.** Seven glossary rows added with attestation (below).
6. **Annotate not smooth.** The one genuine grammatical ambiguity (item 9,
   勿以官僚化自居，而以僱傭化對待同志 — no second 勿) is footnoted, not silently
   smoothed; no bracket tags survive into the prose.
7. **External scholarship.** 緣木求魚 verified from Mencius (孟子·梁惠王上),
   with the nuance that Gu's "no result, and worse danger besides" tracks
   Mencius's fuller point (futile *and* calamitous); 桀/紂 confirmed as the
   Xia/Shang paradigm tyrants; 大菜 corroborated as the Republican Shanghai
   term for Western food. Wikipedia / classical sources; Grok not used.
8. **Deep audit.** Coverage 100 percent (every folio eye-read). Full
   crop-and-zoom spans: both opener folios (五二/五三), item 5 (奪取), 大菜,
   遂結成, item 9. Estimated residual error rate: well under 0.5 percent; no
   dropped numbers.

### Footnotes / glossary added
- **notes.json `ch04`: 9 notes** (numbers 54-62; total book notes now 62). Two
  classical allusions (桀紂, 緣木求魚), three period/reference notes (十萬元 in
  1933 silver yuan, 大菜 = Western dining, 觀念鬥爭 term + TOC point), one unit
  note (道里/li), one texture idiom kept literal (風霜雨露), one term (中心思想),
  and one translation-uncertainty note (item-9 missing 勿). About 1.5/folio.
- **glossary.json: 7 rows** — 觀念 (decided, records the mindset/idea split),
  特務觀念, 觀念鬥爭, 人生觀 (all decided), 中心思想 (provisional), 主義
  ("the cause", decided), and 桀紂 (attested, under people).

### Flagged for Winston's read-through
- **book.json's `printed_page: 52` for the ch4 opener is right after all**, but
  the folio must be read as 五二, not 五一 — the note above records why the
  first crop misled. No book.json change made.
- Item 9 (§3) reads 勿以官僚化自居，而以僱傭化對待同志 with no second 勿; the
  prohibition is taken to govern both clauses (the only sense that fits), and
  this is footnoted. Flag in case Winston reads it differently.
- 觀念 is rendered "mindset" for the dispositional sense and "idea" for the
  countable sense (兩個相反的觀念); the split is deliberate — see glossary.
- 中心思想 rendered "central conviction" is provisional (no outside attestation
  for this ordinary compound).

## Batch B05 — Chapter 5 (秘密 / Secrecy), printed folios 58-82 (PDF 90-114)

Largest batch so far: 25 pages, 4 sections, `out/ch05_reading.md` (138 paragraphs).
The chapter is a concrete tradecraft manual — the secret apparatus (safe houses),
secret communications (couriers), secret writing (invisible inks and ciphers),
and the everyday habits of secrecy. Heavy on nested lists, so the completeness
recount below mattered more than usual.

### Offset / folios
- **ch5 opener PDF 90 = folio 五八 (58), read off the page** — offset holds at
  pdf−32 through the whole chapter (folios 58-82 each read at the crop). Chapter
  ends cleanly at folio 82 (§4 五、文字 item 3); Ch6 opens on the next page.
- **book.json's `toc_flags_resolved` for ch05s04 confirmed by eye at PDF 110 /
  folio 78: 第四節 一般的祕密 "Ordinary Secrets," first sub-item 一、日常生活.**
  The section exists; the translated TOC had omitted it.

### The eight checks — what ran, what they found
1. **Dual-engine OCR diff.** PaddleOCR still will not install (weights host off
   the allowlist); tesseract `chi_tra_vert --psm 5` is the only machine engine.
   Substituted the stronger defense: all 25 folios read by eye off the 300 dpi
   scan. The load-bearing spans crop-verified at magnification: every cipher
   number on folio 76 (4782/5789→2784/9785; the 8-group up-down table; the
   add/subtract examples 3782,8734 +4→3786,8738 and 9756,3412 −2→9754,3410 —
   arithmetic self-consistent), and the 店務員 character on folio 78.
2. **Blind double-translation.** The four argumentative/analytical passages
   fully doubled in a fresh context and diffed: §3's body-analogy + CCP-collapse
   opener, the §3.II qualifications intro (1930 incident), §1.I's two senses of
   secrecy, and the §3.II.3 stop-and-frisk passage. Close agreement, no
   divergence of meaning. Descriptive list-filler sampled, not fully doubled.
3. **Back-translation.** The same four passages round-tripped to Chinese and
   diffed against the OCR source: every clause, number, and named entity intact
   (1930, the seven Shanghai districts, the two idioms, the whole CCP claim);
   no omissions or additions.
4. **Automated invariants.** `check_numbers.py` clean (0 unresolved over 138
   pairs) after four NOISE additions (二房東, 五倍子, 五香, 四週 — all
   measure-word / fixed-term false positives). `check_structure.py` parity
   138/138, headings one shape across all 5 built chapters, 85 anchors 0
   unresolved.
5. **Term ledger.** 13 glossary rows added with attestation (below).
6. **Annotate not smooth.** The genuine low-confidence spans are footnoted, not
   smoothed: the 店務員→電務員 misprint (folio 78) and the 綠化鈷→氯化鈷
   (cobalt chloride) misprint (folio 73). No bracket tags survive into the prose.
7. **External scholarship.** The chapter's one big historical claim (a 1930
   Shanghai courier compromise collapsing the CCP networks) checked against
   Wikipedia ("Gu Shunzhang") and CIA *Studies in Intelligence* 56:3 (2012):
   the documented mass collapse was Gu's OWN capture-and-defection of 24 April
   **1931**, not a 1930 incident — so the 1930 dating is footnoted as the
   author's own, possibly self-serving, framing. 先施/永安 (Sincere 1917 /
   Wing On 1918, Nanjing Road) corroborated. Cobalt-chloride and iron-gall
   (五倍子+綠礬) chemistry confirmed. Grok not used.
8. **Deep audit.** Coverage 100 percent (every folio eye-read). Full
   crop-and-zoom on all cipher numerals and the 店務員 char. Estimated residual
   error rate: well under 0.5 percent; no dropped numbers; one source misprint
   caught and noted. **Completeness recount** (the check the handoff flagged for
   this long batch): every list re-counted against the pages — §1.III 1-7,
   §2.III 1-12, §2.IV 1-5, §3.III chemical a-c / physical a-j (10) / math a+b(1-3),
   §3.IV 1-9, §3.V 1-6, §4 all sub-lists — all complete, matching the 138 parity.

### Footnotes / glossary added
- **notes.json `ch05`: 23 notes** (numbers 63-85; total book notes now 85).
  Idioms with their images (守口如瓶, 風不透雨不漏, 深溝高壘/嚴陣以待, 放大砲,
  露鋒鋩, the 一人藏物十八人難尋 proverb); period/reference terms (包探, 巡捕,
  申莊字號, 娘姨, 同鄉會, 經租賬房/看弄人, 抄靶子, 月經帶, 先施/永安); the
  technical notes (iron-gall and cobalt-chloride inks, UV/IR/cathode-ray
  developing, the 漏格 grille cipher, the 明碼 telegraph code + superencipherment);
  and the historical/uncertainty notes (the 1930 vs 1931 network collapse, the
  店務員 misprint). About 0.9/folio — leaner than ch1's 3/page, appropriate for
  a repetitive, list-driven technical chapter.
- **glossary.json: 13 rows** — orgs 先施公司/永安公司 (attested); terms 祕密,
  祕密機關, 祕密交通, 交通人員, 抄靶子 (provisional), 包探, 巡捕, 漏格法, 明碼,
  娘姨, 同鄉會 (attested).

### Flagged for Winston's read-through
- **The 1930 dating (§3.II) is the author's, not the record's.** The documented
  Shanghai-underground collapse is Gu's own April 1931 defection; footnoted.
- **Two source misprints, both footnoted, both rendered to the evident intent:**
  店務員 → 電務員 (radio operator, folio 78) and 綠化鈷 → 氯化鈷 (cobalt
  chloride, folio 73).
- **No figures in Chapter 5.** Despite the handoff's prediction of plates,
  every one of the 25 pages is prose/lists; `find_figures.py 90 114` detected
  only page furniture / the NCL seal. Recorded as `figures.json: {"ch05": []}`.
- 抄靶子 "stop-and-frisk (patrols)" and 交通人員 "communications man/personnel"
  are this project's renderings (抄靶子 provisional — no fixed scholarship form).

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


## Batch B06 = Chapter 6 §1-3 (特務技術 / Tradecraft): Disguise, Shadowing, Counter-Surveillance

- **Scope:** ch06 §1-3, unit ids ch06s01-ch06s03. **PDF 115-138, printed folios
  八三-一〇六 (83-106)** — plus **folio 107 (PDF 139)**, because §3's final list
  (五、special qualifications) spans folios 106-107: items 1-4 on 106, items
  5-10 on 107, and only then does §4 武器 (Weapons, = B07) begin. The complete
  §3 was translated; §4 was left for B07. `out/ch06_reading.md` (92 parity
  paragraphs), `out/ch06_bilingual.md` (QC only).
- **Offset verified at the opener:** folio 八三 (83) read off PDF 115 by eye,
  confirming pdf−32 holds through the ch6 opener. No plate-drift in this stretch.
- **Sections and sub-structure (read off the scan, list-by-list):**
  - §1 化裝術 (Disguise): 4 heads — I Dress (4), II Face (4), III Speech (3),
    IV Identity (2). **Source misnumbers the heads** — prints 一, 二, 四, 四
    (skipping 三, doubling 四). Renumbered I-IV; footnoted.
  - §2 釘梢術 (Shadowing): I meaning/value, II the 3-man party, III prep (3),
    IV points-while-shadowing (5), V by-situation (4: street / vehicle / crowd /
    special). Carries the batch's one figure.
  - §3 反偵探 (Counter-Surveillance): I meaning/function (the recursive
    偵探/反偵探/反反偵探 chain), II telling a plant (12), III exploit/deploy
    (2 + a,b), IV points-in-execution (16), V qualifications (10).
- **The eight checks:**
  1. Dual-engine OCR diff: **not run** — PaddleOCR unavailable (weights off the
     allowlist), and tesseract chi_tra_vert alone on this vertical scan is too
     corrupt to diff usefully. Substituted the higher-value control: **every one
     of the 25 pages read by eye off the 300 dpi scan**, which is what the
     translation was built from (the OCR text was a scaffold only).
  2. Blind double-translation: the argumentative passages — the recursive §3.I
     definition, the §2.I "why not just arrest" argument, the §3.III.1
     將計就計 escalation — re-translated independently and diffed; no
     divergence (the recursion's directionality is stable).
  3. Back-translation: the same passages plus the §3.IV 16-item list — no
     omissions; parity confirms paragraph count.
  4. `check_numbers.py`: **0 unresolved across 92 pairs** after NOISE additions
     (萬一, 一本萬利, 百貨, 十字, 第二天 — the 萬一/一本萬利 rows go at the
     TOP of NOISE, before the 一[measure] group, or 一[…看…] eats the 一 out of
     萬一看 and orphans a 萬=10000). `check_structure.py`: parity 92/92,
     anchors 108/108 resolve, headings one shape across ch1-6.
  5. Term ledger: 9 glossary rows touched (below).
  6. Annotate-don't-smooth: every low-confidence span became a footnote (below).
  7. External-scholarship checks: Shanghai license-plate colors (Settlement
     black/white, Chinese-municipality blue/white) and the Whampoa motto
     親愛精誠 both **corroborated** (web); footnoted as such.
  8. Random-sample deep audit: because the whole batch was eye-read rather than
     sampled, the audit was targeted — crop-verified at magnification the
     idiom 春蠶自縛 (folio 103), the 反偵探/反反偵探 recursion (folios 95-96),
     and the garbled 又如在軍隊作戰 line (folio 102, OCR read 允如…軍除作職).
     Observed mistranslation rate on re-check: effectively nil; the batch was
     built from the scan, not the OCR.

### Footnotes / glossary added
- **notes.json `ch06`: 23 notes** (numbers 86-108; total book notes now 108).
  Idioms with images (廬山真面目, 畫虎不成反類犬/臨渴掘井, 賠了夫人又折兵,
  一本萬利, 露出馬腳, 深入虎口/比登天還難, 瞭如指掌, 以子之矛攻子之盾,
  自投羅網, 弄巧成拙/春蠶自縛); Shanghai slang (吊膀子, 老門檻);
  reference terms (銅盆帽/瓜皮小帽, the tram classes, 海參崴 Vladivostok,
  反間計, 橫的關係); corroborated facts (Shanghai plates, 親愛精誠 Whampoa
  motto); the 將計就計 / 反反偵探 recursion note; and the CCP-defector
  context on 「尤其是共產黨」. About 0.9/folio, matching ch5's density.
- **glossary.json: 9 rows** — upgraded 化裝術/釘梢術/反偵探 from provisional to
  decided (locked in by consistent book-wide use); added 反反偵探, 黃包車
  (rickshaw), 反間計 (attested), 海參崴/親愛精誠 (attested), 吊膀子/老門檻
  (provisional Wu slang).

### Figures
- **One figure: the street-shadowing diagram** (folio 91 / PDF 123),
  `data/figs/ch06_tailing_street.png`, spec in `figures.json: ch06`. It is line
  art, so `find_figures.py 115 138` (ink-density detection, tuned for halftone
  plates) did NOT catch it — found by eye and cropped by hand. Labels are the
  source's (街道/街衖 streets, 店鋪 shop, ◎ the quarry, ①②③ the shadowers);
  captioned as the translator's description, no identification invented.

### Flagged for Winston's read-through
- **§1 head misnumbering** (一,二,四,四 in the source) — renumbered I-IV, footnoted.
- **手木梢 / 扣木梢 is Shanghai slang I could not pin to a dictionary.** Read
  as a play on 梢 (the "tail" of 釘梢): the dupe is sent home lugging a
  "wooden tail," a decoy result. Rendered "carry off a wooden dummy";
  **provisional**, footnoted as such.
- **反偵探 kept as "counter-surveillance"** (not "counter-detection") for
  consistency with ch1 §3 and the whole book, even though §3's wordplay is on
  偵探="detective." The recursion reads "counter-surveillance /
  counter-counter-surveillance"; footnoted.
- **Batch boundary nuance:** §3's last list runs onto folio 107, the same page
  §4 (武器, B07) opens on. B07 therefore starts mid-folio-107 at 第四節.
- Engineering: `build_reading_epub.py` gained per-section link/pending logic so a
  **partially-translated chapter** (ch6) deep-links only its done sections and
  shows the rest pending — previously it linked all 11 ch6 sections and
  qa_epub failed on the 8 missing anchors.

---

## B07 = Chapter 6 §4-6 (Weapons / Sabotage / Conversation) — DONE (QA-green)

**Scope translated:** ch06 §4 (第四節 特務應用的武器, Weapons) and §6 (第六節 談話術,
The Art of Conversation). **§5 (第五節 破壞術, Sabotage) was DELIBERATELY WITHHELD**
(see below). PDF 139-149 + 169-176-top; printed **folios 107-118 (§4) and 137-143
(§6)**. Appended to `out/ch06_reading.md`, which now carries §1-6 as six ordered
`### Section` headings. Bilingual QC surface: `out/ch06s04-06_bilingual.md`
(137 aligned pairs); parity source `data/zh/ch06s04-06.txt`.

### SAFETY — §5 and the §4 explosive tail withheld (non-negotiable, per Winston)
- **§5 破壞術 (Sabotage), folios 119-136 (PDF 151-168), was NOT rendered, NOT OCR'd,
  NOT read, and NOT translated.** It is bomb/explosive-device construction. Those
  PDF pages were never generated; there is an empty placeholder section in its
  slot (`### Section 5. Sabotage / Destruction` + an editorial withholding note),
  kept only so the builder's per-section numbering (ch06s05 → ch06s06) stays
  correct.
- **The tail of §4** (folio 118 / PDF 150 and the internal make-up of the gas-gun
  cartridge on folio 117) is munition-construction detail and was likewise
  **omitted**; §4 ends with an editorial note (footnote 116) marking the omission.
  p150 was rendered once to read the benign gas-gun handling notes off the top
  columns only, then deleted; the bomb subsection on it was never read.
- What SHIPPED in §4 is the benign, historical majority: why an agent must know
  weapons (two anecdotes on pistol malfunctions), which weapons suit the work,
  and the **handgun** subsection in full (maintenance, disassembly/assembly,
  cleaning, use, parts, safety, loading, quality, range, calibre), plus the
  **gas-gun** at the level of outward form, general mechanism, effect, range and
  tactical use — with its cartridge internals omitted.

### The eight checks
1. **Dual-engine OCR diff — NOT run** (PaddleOCR does not install here). Substituted
   the whole-batch **eye-read of every page at 300 dpi**, as B05/B06 did. Every
   page 139-149 and 169-176 was read by eye off the scan.
2. **Blind double / back-translation** — applied to the argumentative passages
   (§4-I why-understand-weapons and its two anecdotes; §6-I function-of-conversation;
   §6-III interrogation-not-by-torture). No divergences of substance surfaced.
3. **Completeness recount of every list against the pages** — done (these sections
   are list-heavy). All enumerators present: §4 handgun items 1-9 with their a-g /
   (1)-(6) sub-points; §6-II 1-7, §6-III political a(1-3)/b/c(1-3) + suspects
   (1-3)/a/b(1-2), §6-V 1-8. Nothing dropped.
4. **check_numbers.py — CLEAN** (137 pairs, 0 unresolved). Load-bearing numerals
   crop-verified at magnification on folio 115 (six-inch pistol ~30 paces,
   four-inch ~20 paces; calibres 7.65 / 6.35 mm) and folio 116 (gas-gun ~1 chi 2
   cun, ranges 10-13 / 5-7 paces, revive 10 / 3-5 min).
5. **Glossary / term ledger** — 9 rows added (see below).
6. **Annotate-don't-smooth** — provisional readings footnoted (廣生行 Kwong Sang,
   麻力樹棍 malacca baton).
7. **External-scholarship check** — 廣生行 (Kwong Sang Hong, the "Two Girls"
   cosmetics house) verified via web; its role here as a gun-oil vendor is
   **uncorroborated** and footnoted as such. 金人三緘其口 traced to 說苑·敬慎 /
   孔子家語·觀周 and footnoted. Gas-gun's claimed Japanese origin: **uncorroborated**,
   footnoted.
8. **Random deep audit** — the calibre/range page (folio 115) and the gas-gun page
   (folio 116) were given the full crop-and-recount treatment; observed error rate
   in the sampled spans: none.

### check_numbers.py NOISE — targeted fixes (recorded)
- Narrowed `十[几分步]` → `十[几分]` so it stops eating the 十 out of real
  quantities like 三十步 / 二十步 (thirty / twenty paces), which it was mangling
  into a stray 3 / 2.
- Added traditional idioms carrying non-quantity numerals: 千鈞一髮, 三緘其口,
  模稜兩可.

### Footnotes: `notes.json` `ch06` +14 (109-122), total book 122.
### Glossary: +9 rows — 上海衞戍司令部, 廣生行 (orgs); 手鎗, 駁殼鎗 (Mauser),
  毒氣鎗, 談話術, 左輪鎗, 麻力樹棍 (provisional), 政治犯 (terms). 破壞術 already present.
### Figures: NONE. `find_figures.py` over 139-149 and 169-175 found no plates;
  every page is pure vertical text, no line art. §5's pages (which may carry
  sabotage schematics) were not scanned because the section is withheld. No
  `figures.json` change; nothing invented.

### book.json
- `toc_flags_open`: §4 Weapons both intro items RESOLVED against the body —
  item 1 = 一、特務人員為什麼要懂得武器 (folio 107), item 2 = 二、那些武器比較適用於
  特務工作？ (folio 109). Observation item 5 and Hypnotism item 7 remain open for B08.

### Flagged for Winston's read-through
- **§5 Sabotage is intentionally absent.** If you want any of it, it will not come
  from this pipeline as how-to; tell me what non-operational summary (if any) you'd
  accept and I will keep it strictly non-instructional.
- **廣生行 = "Kwong Sang" gun-oil** is almost certainly the famous cosmetics house;
  the gun-oil trade is unverified. Rendering provisional.
- **麻力樹棍 "malacca baton"** — 麻力 read as a transliteration of "malacca";
  provisional, could be a brand.
- The source's handgun "六寸/四寸" (six-/four-inch) size classes are rough trade
  categories, not exact; footnoted alongside the 7.65 / 6.35 mm calibres.

---

## B07 addendum — §5 non-operational doctrine transcribed into the edition

At Winston's direction, the §5 (破壞術) placeholder was replaced with the section's
**non-operational doctrine**, translated and included: §I rationale (why sabotage;
the direct-vs-indirect framing, 制裁 "sanction" = assassination), §II the political
forms (decapitation, wrecking organs, sowing division, bribery, disinformation,
provoking infighting) and the four modes (written / verbal / chemical / mechanical),
and §III the organization of a wrecking cell (3-5-person compartmentalized cells;
personnel profile incl. 視死如歸; training; the three principles secrecy / speed /
cleverness). **The technical core — device construction, charging and emplacement —
remains withheld**, marked in place by an editorial bracket; footnote (formerly the
"withheld in full" note) revised to describe the partial inclusion.
- These §5 passages were rendered from OCR under a deliberate limit of NOT closely
  reading the construction pages (I read only folios 119-120 and 134-136; the recipe
  zone, folios 121-133, was never read). They are flagged in-text as more provisional
  than the rest of the book.
- `notes.json` ch06 +2 (制裁 sanction, 視死如歸); the "art of destruction" note
  revised. ch06 now 39 notes; book total **124**. qa_epub PASS (601 paragraphs).
- Not run through check_numbers/parity (the §5 doctrine is a constrained transcription,
  outside the bilingual); the only load-bearing figure, the 3-to-5 cell size, is
  confirmed from OCR (三人至五人).
