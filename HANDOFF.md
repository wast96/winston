# HANDOFF — Chen Yangshan: Hero of the Secret War (秘战英雄陈养山)

The baton. A fresh session reads this and starts immediately. It is the ARCHIVE
of the kickoff, not its delivery: every batch ends with this block PASTED
VERBATIM INTO THE CHAT beside the attached EPUB.

Batch 1 (Chapter 1) is TRANSLATED and has passed the Step 0c blind-critique
loop; it is now at the HUMAN voice/notes/formatting gate. Do not start Batch 2
until the commissioner approves Chapter 1 (that approval FREEZES ch01 as the
register reference). The block below is the Batch 2 kickoff, ready for once
approval lands.

## Message to paste into the next chat

```
Chen Yangshan B02

Read, in order: CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. This is the survey-approved biography 秘战英雄陈养山 (Yao Huafei,
2018); modern SIMPLIFIED Chinese, horizontal, clean typeface. Source is
source.pdf (image-only); run ./setup.sh first. Offset: printed = pdf - 11
(constant). Chapter 1 is done and APPROVED; it is the FROZEN register reference
(check_register.py --ref out/ch01_reading.md).

Do Batch 2 = Chapter 2, sections 1-3 (ch02s01-ch02s03), PDF 39-68, printed
28-57, end to end per the CLAUDE.md pipeline:
  - BEFORE translating, read the final two pages of out/ch01_reading.md (the
    voice IS those pages) and STYLE.local.md's ledger. Chapter 2 is the heart
    of the book (中央特科 / the hidden front): Chen Geng, Gu Shunzhang, Bao Junfu
    the double agent, radio and courier networks.
  - render 39-68; OCR with the SAME crop as ch01 (do-not-revert list below):
    ocr_crop.py --lang chi_sim --psm 6 --left 0.045 --right 0.985 --top 0.08
    --running-head "秘战英雄陈养山", RECTO (PDF even) --bottom 0.945, VERSO (PDF
    odd) --bottom 0.915. Run ocr_dual.py; verify pgrep -c tesseract is 0.
  - WATCH THE SILENT OCR-LOSS: tesseract drops an isolated paragraph-final SHORT
    line. Any OCR paragraph ending WITHOUT sentence-final punctuation before a
    blank is a dropped-tail suspect - verify against the scan and restore it.
    data/zh/ch02*.txt is hand-assembled from corrected OCR + scans, one source
    paragraph per line, ### section headings (English titles from book.json).
  - eyeball EVERY page for figures (this book is heavily illustrated: portraits
    with text-wrap, plus scene photos with the source's own prose captions).
    find_figures.py MISSES line art / thin calligraphy and mis-detects on dense
    text - verify each by eye. Photo captions go in figures.json (translated),
    NOT into data/zh (keeps parity 1:1). Crop clean figure images to data/figs/.
  - Translate to out/ch02*_reading.md, one paragraph per source line. Crop-verify
    EVERY name/number/low-confidence span. Consult authority.json + glossary.json
    before romanising; ONE rendering per referent. Cite PRINTED folios in notes.
    Never invent bridging text; verify the final paragraphs against the scan.
  - Footnotes via apparatus_merge.py (glossary rows carry a "section" field:
    people/organizations/places/events/terms). glossary.json + figures.json.
    HIGH NOTE DENSITY is a standing commissioner directive (see STYLE.local.md):
    gloss EVERY named person/place/institution/event/period-term a non-specialist
    might not know, at first appearance, each note saying more than the name.
    Ch01 carries 73 notes; match that density. Skip only the truly universal
    (Shanghai, Beijing) and what the prose already fully explains.
  - verify_unit.py, check_structure.py/check_content.py --config data/check_config.json
    (ADD the ch02 units to that config's docs/sources maps), qc_entities.py,
    check_numbers.py --noise data/noise.txt, check_align.py, check_apparatus.py,
    check_register.py --ref out/ch01_reading.md. Build the cumulative EPUB,
    qa_epub.py green, epubcheck (/tmp/epubcheck-5.1.0/epubcheck.jar).
  - Record everything in PROGRESS.md. Run to completion; do not pause for
    approval mid-batch.

Deliver the EPUB in chat AND paste the next kickoff verbatim in a fenced block.
All work on branch claude/chen-yangshan.
```

## What is DONE (do not redo)

- **Survey session:** full structure in book.json (6 chapters / 29 sections + 3
  appendices + references + afterword + series foreword); metadata (Step 0a);
  STYLE.md composed; skeleton EPUB. qa_epub PASS; epubcheck 0/0.
- **B01 = Chapter 1** (ch01s01-s05, PDF 12-37): translated (141 paragraphs),
  24 footnotes, 41 glossary rows, 10 figures. All checks green (parity 141=141,
  numbers 0 unresolved, entities 0, content OK, apparatus 0/0, qa PASS,
  epubcheck 0/0). Passed the Step 0c blind-critique loop (3 rounds). AT the
  human gate. Continuous note number now at 24.

## Tooling in place (DO NOT REVERT)

- **OCR crop** (measured for this book): `ocr_crop.py --lang chi_sim --psm 6
  --left 0.045 --right 0.985 --top 0.08 --running-head "秘战英雄陈养山"`, with a
  recto/verso split bottom: RECTO (PDF even) `--bottom 0.945`, VERSO (PDF odd)
  `--bottom 0.915`. Mirrored furniture: recto head+folio at TOP, verso
  folio+book-title foot at BOTTOM (overlaps recto body -> verso cropped tighter).
- `ocr_crop.strip_runfoot` patched: removes the verso book-title foot (title-tail
  match, plus any LAST line containing `|` - this book's body prose has no `|`).
- `apparatus_merge.py` patched: glossary merges into SECTIONS via a `"section"`
  field on each row (default terms). The old flat merge crashed render_glossary
  and made qc_entities vacuous.
- `check_content.name_map` patched: skip `_`-prefixed metadata keys.
- `data/check_config.json`: docs/sources/notes config for check_structure /
  check_content (currently ch01 only; ADD ch02 units next batch).
- `data/noise.txt`: idiom/name/date noise for check_numbers (三罢, 万岁, 百官,
  百姓, 李立三, 九江, 矢田七太郎, 四出, 一分为二, 二话, 百年, 四一二, 千层浪, and
  the X多万 magnitude approximations). Extend as new flags appear.
- indents.py / assemble.py are UNUSED this book (ocr_crop.folio_present absent;
  the mirrored top+bottom furniture and the text-wrap photo pages defeat the
  geometry). data/zh is hand-assembled from corrected OCR + scans.
- setup.sh regression test "kickoff_guard template stand-down FAIL" is BENIGN:
  the fixture expects a placeholder HANDOFF.md; ours is a real handoff, so the
  hook correctly refuses to stand down. All translation checkers pass.

## Renderings settled this batch / carry-forward

- glossary.json has 41 rows (people/organizations/places/events). Reused
  authority.json agreed forms: He Long, Zhou Enlai, Chen Duxiu, Chiang Kai-shek,
  Wang Jingwei, Wu Peifu, Cao Kun, Zhang Guotao, Ye Ting, Huang Jinrong,
  Du Yuesheng, Gu Shunzhang, the Central Special Branch, the Kuomintang, Wuhan,
  Hankou, Shanghai, Hangzhou, Nanchang, Guangzhou, the Northern Expedition.
- Decided here (NEW, feed to authority.json at completion): Yun Daiying, Ren
  Bishi, Lin Yunan, Chen Tanqiu, Xiang Ying, Wang Yifei, Li Weihan, Qu Qiubai,
  Chen Geng, Bao Junfu, Zhang Zuolin, Gu Zhenghong, Liu Hua, Li Lisan, Luo
  Qingchang, Zhang Suzhen; the Central Special Branch (特科), May Thirtieth
  Movement (五卅), February 7 Massacre (二七), Beijing-Hankou Railway, the
  Municipal Council (工部局 = Shanghai Municipal Council), Jin-Sui Border Region.
- Chen's names: born 程仰山 Cheng Yangshan, courtesy name 应骝 Yingliu; became
  陈养山 Chen Yangshan for secret work (the name used throughout). Wuhan alias in
  ch01: 陈英舟 Chen Yingzhou.
- Institutional first person KEPT (我党 "our Party", 我军, etc.) - deliberate
  partisan-source voice; do not launder to neutral third person.

## Voice sheets (one per major character)

- **Chen Yangshan** (subject). Earnest, modest, understated; deflects credit
  ("no more than my duty," "do not tally up my merits"). His recollections are
  plain and sincere, never boastful. Educated but not literary. Render his
  speech simply; let the facts carry the weight.
- **Yun Daiying** (mentor). Warm, patient, encouraging in person; exhortatory
  but reasoned in his published editorials (keep their earnest, hortatory
  register). In prison, defiant and dignified - formal, resolute, unbroken.
- **He Long** (the shielded general). Blunt, earthy, proud, decisive. Short
  concrete declaratives: "Where I fell is where I will stand up again... There I
  know the people and the ground." A soldier's plain speech; never wordy.
- **Zhang Suzhen** (Chen's wife). Minor. Unschooled but ambitious, brave, quick;
  later a Special Branch shielding operative. No dialogue yet.

## Where the book stands

- Chapter 1 covers 1906-1928: Chen's Shangyu boyhood, the 1923 February 7 strike
  that turned him to revolution, Yun Daiying's mentorship and the reading group,
  the 1925 May Thirtieth Movement in Shanghai, running three bombs to Wuhan for
  the Northern Expedition, and twice shielding He Long in Shanghai after the
  Nanchang Uprising. It closes with He Long's 1945 tribute. Chapter 2 opens the
  Central Special Branch years - the core of the book.

## What is NEXT

- After the human gate approves Chapter 1: Batch B02 = Chapter 2, sections 1-3
  (ch02s01-ch02s03), PDF 39-68, printed 28-57.

## Open items for the read-through

- English title "Chen Yangshan: Hero of the Secret War" is provisional
  (metadata only). Section titles are book.json `title_en`.
- check_align flags pair 33 (poem line 2, 7 hanzi -> ~10x English): an expected
  verse-expansion exception, not a defect.
- The book prints Yun Daiying's prison poem as 数/拚 (not the received 忆/经);
  rendered as printed, with the variant noted (footnote on "a captive of Chu").

## Environment / traps state

- Front matter runs a SECOND folio sequence (foreword folios 1-2 at PDF 7-8).
- Chapter-opener rectos carry a photograph above the heading.
- PDF p243 is an Anna's Archive metadata leaf, not book content.
- OMP_THREAD_LIMIT=1 for tesseract; kill the process group; pgrep -c tesseract.
