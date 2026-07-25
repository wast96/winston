# PROGRESS — 军统内幕 / Inside the Juntong

Working state. Updated as each unit lands.

## The book

Shen Zui (沈醉), 军统内幕, 3rd ed., Zhongguo Wenshi Chubanshe, Beijing 2001,
ISBN 978-7-5034-0755-0. 521-page image-only scan, no text layer, no bookmarks.
515 pages of book text, ~338,000 Han characters by OCR count (the CIP page
claims 418,000 字, which counts punctuation and front matter).

A memoir, not a narrative history: twenty-one free-standing chapters, most of
them written between 1962 and 1966 for the CPPCC's *Selected Historical
Materials* and collected here. The author was a Juntong major-general.

## Verified structure

- **Two page-number sequences.** Main text: printed = PDF − 19. Front matter
  (概况, 前言, 目录): printed = PDF − 5, running 1–14. Confirmed by eye on the
  magnified footers of PDF 200/250/450 → 181/231/431, and cross-checked against
  a dozen page references in the book's own contents pages. The front-matter
  sequence is why the first offset measurement (PDF − 5, taken on page 10) was
  wrong for the body of the book; anything citing pages before this was settled
  would have been off by fourteen.
- The scan's contents pages (PDF 16–19) exist but are **incomplete** — they
  omit several chapters they nonetheless paginate. The authoritative map is
  `data/structure.json`, recovered from heading geometry and confirmed against
  the contents pages where those do list an entry.
- 25 units: 2 front matter, 21 chapters, 2 back matter. See `book.json`.
- One chapter was missing from the geometric pass and found by probing the gap:
  保密局内幕 (Inside the Bureau of Secrets Preservation), printed 392.
- PDF 521 is the Anna's Archive provenance page.

## Pipeline state

Rendered: all 520 pages at 300 dpi. OCR'd: all 515 text pages. Both complete;
the per-chapter work from here is assemble → verify → translate → check.

## Environment findings worth keeping

- **`OMP_THREAD_LIMIT=1` on tesseract is mandatory.** Without it three
  concurrent processes each pinned a core at 130% and did not finish a single
  page in ten minutes — twice, once through a Python thread pool and once
  through xargs. Tesseract's OpenMP threads busy-wait; twelve of them on four
  cores starve each other rather than sharing. Pinned, with `xargs -P 4`, a
  page costs 0.93s and the whole book OCRs in about six minutes. This cost
  roughly an hour to diagnose and is the single most expensive trap here.
- Killing a stalled run **orphans the tesseract children**, which keep
  spinning and slow everything afterwards. Kill by PID and verify with
  `pgrep -c tesseract`.
- Blank lines in the OCR output are the **only** paragraph signal the file
  carries — tesseract drops the source's two-space indent. The first OCR pass
  filtered them as noise and had to be redone.
- Page folios cannot be cropped away: the last body line reaches 0.9117 of
  page height on some pages while the folio starts at 0.8890 on others, so the
  bands overlap globally. Filtered by shape in `ocr_crop.py:strip_folio`.

## Register baseline — NEEDS WINSTON'S SIGN-OFF

There is no approved reference chapter for this book yet, and the skill's whole
per-chapter drift check is measured against one. `fm01_gaikuang` is proposed as
that baseline: institutional prose, first person, plain and documentary, period
political idiom preserved rather than neutralised.

**This is the one thing worth reading before the rest of the book is
translated**, because everything after it is measured against it. If the voice
is wrong, it is wrong once here and twenty-four times later.

Specific choices made in it, all reversible:
- 军统 glossed once in full, then "the Juntong" throughout — the book's own usage.
- 重庆 as "Chungking", the period English form, not "Chongqing".
- 委员长 as "the Generalissimo".
- 臭招牌 kept literal as "stinking signboard", with a note on the register.
- Chapter title 军统概况 as "An Outline of the Juntong".

## Register baseline: the dialogue half is NOT yet set

`fm01_gaikuang` works as the baseline for the expository voice, but it contains
no dialogue at all, so its dialogue-contraction rate is 0.0/1k and measuring
anything against it is measuring nothing: the ratio comes out 1.00x whatever
the chapter does. The preface reads 13.2/1k against it and the check reports
"within tolerance," which is true and uninformative.

The dialogue baseline has to be reset from the first unit that has real
dialogue. Until then, treat the contraction column as unmeasured rather than
passing. The "shall" share is the usable signal in the meantime: it caught one
line in the preface where Zhou Enlai's warm, plain send-off had been given a
formal "I shall," which is exactly the drift the check exists for, and it is
now "I'll."

## Per-unit log

### fm01_gaikuang (军统概况 / An Outline of the Juntong) — DONE

- PDF 6–9, front-matter printed 1–4. 18 source paragraphs, 18 translated.
- **13 name mangles caught by crop verification**, every one of them a
  plausible-looking valid word rather than obvious garbage — the defect class
  the dual-OCR disagreement filter cannot see, because both psm configurations
  make the same mistake on the same glyphs:
  郑锡鹿→郑锡麟, 岂料→酆悌, 潘估强→潘佑强, 印开基→邱开基, 候志明→侯志明,
  徐因曾→徐恩曾, 贺友组→贺耀组, 钱大钓→钱大钧, 林幸→林蔚, 玫珈山→珞珈山,
  番戒委员会→惩戒委员会, 一九八年→一九八〇年, and 张国琳→**张国焘**.
  The last is the one that mattered: Zhang Guotao, a founder of the Chinese
  Communist Party, running a Juntong research office — OCR had turned him into
  a nobody, and nothing but the scan would have caught it.
- Checks: parity 18/18, anchors 12/12 resolve, headings consistent, numbers
  0 unresolved across 18 pairs.
- Notes: 12 (3.0 per printed page).
- Glossary: +32 entries (75 total).
- **Three real tool bugs found and fixed**, all of which would have produced
  false confidence rather than noise:
  1. `check_structure.check_parity` dropped a source line as the "chapter
     title" even when the title had already been removed as a heading, biasing
     every parity count by one — in the direction that hides a dropped
     paragraph, which is the defect the check exists to find.
  2. `check_numbers.cn_to_int` could not read 百/千/万, so 一千四百 fell apart
     into a stray 四 and reported a dropped number that was not dropped.
  3. A NOISE entry (`[一二三]十`) ate the first half of 二十九 and left a bare
     九 behind — the exact prefix-eating trap the script's own comment warns
     about, recurring with a different pair.

### fm02_qianyan (前言 / Preface) - DONE

- PDF 10-15, front-matter printed 5-10. 15 source paragraphs, 15 translated.
- Crop verification caught five more source errors, two of which the numeric
  check had already flagged from the other direction: 十和年 for 十八年
  (eighteen years) and 十别总理 for 辞别总理 (took leave of the Premier), both
  of which left a stray 十 that read as a dropped "10"; plus 黄效先生 for
  黄雍先生 (Huang Yong, a CPPCC member and one of the original Ten-Man Team),
  郑锡记 for 郑锡麟, and 周因来 for 周恩来.
- Checks: parity 15/15, anchors 14/14, numbers 0 unresolved, register within
  tolerance (but see the baseline caveat above).
- Notes: 14 (2.3 per printed page).
- EPUB built and QA PASS: 2 documents, 33 paragraphs, 26 notes, all references,
  bodies and backlinks matching.

### Two more tool fixes this unit

- `qa_epub.py` identified chapter documents by matching `prologue|chNN` in the
  filename, so it reported "0 documents, 0 paragraphs" for a spine made of
  front matter and did not notice it had measured nothing. It now derives
  content documents from the spine by excluding the known apparatus documents,
  so a unit named anything at all is still checked. This is the last gate
  before a build ships and it must not depend on a naming convention it does
  not itself enforce.
- `check_numbers.py`: a noise pattern beginning with a numeral could eat the
  TAIL of a longer numeral (一日 fired inside 二十一日 and left 二十, reported
  as a dropped "20"). All such patterns are now guarded with a lookbehind.
  Also added "a million" to the English reader.

### New in the pipeline: a correction ledger

`data/ocr_fixes.json` plus `scripts/apply_fixes.py`. Crop verification is the
most expensive step here and its results were the most perishable: `data/txt/`
and `data/zh/` are untracked, so a fresh checkout re-runs OCR and quietly
reinstates every mangle already paid for - 张国焘 reverts to 张国琳. Every
verified reading is now recorded with the page it was checked on and why, and
replayed by script. 18 entries so far.

### ch03 (抗战时期军统特务在重庆的罪行 / Juntong Crimes in Chungking during the War of Resistance) - TRANSLATED, notes pending

- PDF 91-149, printed 72-130. 193 source paragraphs, 193 translated. 11 sections.
- **619 crop-verified OCR corrections**, by far the largest ledger of any unit so
  far. Names OCR had turned into non-names and the scan restored: 郭寄峤,
  张简斋, 陈逊斋, 肖茂如, 胡藻, 曹万道, 廖承志, 史良, 曹禺, 孔祥熙 (mangled
  five distinct ways), 孔令俊, 宋希濂, 唐毅, 酆裕昆, 魏大铭, 王瓒绪, 刘耀,
  蒲岗, 何成濬, 张炎元, 胡天秋, 韦贤, 王兴国, 曾泽, 祝宗梁, 周伯勋, 周景敦,
  刘之盘, 刘廷根, 邹陆夫, 陈昌熙, 龚仙舫, 任建鹏, 王芃生, 林可胜, 贝祖诒,
  谷正纲, 葛天璇, 陈韵娜, 陈雯, and 张国焘 twice more.
- Places restored: 红岩村, 渣滓洞, 白公馆, 鹅公岩, 寸滩, 海棠溪, 机房街,
  枣子岚垭, 赣江街.
- Checks: parity 193/193, alignment OK across every pair, register within
  tolerance of the ch01 reference, numeric check 6 residual flags, all
  adjudicated (see below).

### ch03 numeric adjudication - 27 flags, 0 real omissions

Every flag was one of four classes, none of them a dropped quantity:
- numerals inside NAMES (许忠五, 曹万道, 廖越万, 王四心, 三斗坪);
- numerals inside PLACE names (两湖会馆, 两路口, 万寿宫, 一品场);
- numerals inside IDIOMS (漏洞百出, 成千上万, 不三不四, 劲头十足, 百般,
  十有八九, 七折八扣, 数以百计);
- real numbers correctly translated that the checker could not read in English
  ("a hundred thousand dollars" for 十万元, "between a hundred and seventy and
  a hundred and eighty" for 一百七八十, "two or three hundred" for 二三百).

The classes are now in `data/noise.txt` and the parser reads "a hundred
thousand". The exercise was still worth it: it caught ONE real loss. The source
counts characters - 望龙门 is 三个字, 望龙门的 is 四个字 - and the translation
had flattened both to "the words". Restored as "the three characters" and
"those four characters".

### FOR WINSTON'S READ-THROUGH, ch03

- The book prints 卫成总司令部 throughout for what is unmistakably the
  重庆卫戍总司令部, the Chungking Garrison Command. 卫成 is not a word. Twelve
  occurrences, all reading 成 in the scan. Preserved as printed and to be noted,
  not silently corrected. JBIG2 glyph substitution and a printing error are both
  live possibilities and I cannot tell them apart at this resolution.
- 助桀为虐 where the common form is 助纣为虐. Crop-verified as printed.
- 王固盘 where scholarship gives 王固磐. Preserved as printed.
- 黄角垭 where the commoner form is 黄桷垭. Preserved as printed.
- Two passages need notes more than most: the hotel waiter's cry "Is Mr. Wang
  Sixin at home?", which is the character 憲 taken apart into 王/四/心 as a
  warning that the military police are at the door; and the action group the
  operatives themselves nicknamed the 锦衣卫 after the Ming secret police.
- The prison ladder - 小学 / 中学 / 大学 for the corps detention house,
  Baigongguan and the Xifeng camp - is the author's own reported usage.

### FOR WINSTON'S READ-THROUGH, fm01

- The scholarship pass is **not yet run** for this unit. The twelve notes rest
  on general knowledge of the period and are written to be checkable; claims
  that need external verification (the Lixingshe founding roster, Feng Ti's
  execution, the Dai Hill crash site) are flagged as such in the note text
  rather than asserted flatly. Per the skill's cost model, research is batched
  across several chapters rather than run per chapter — that pass is pending.
- The book prints 戴山 for the hill Dai Li's aircraft struck, where other
  sources give 岱山. Preserved as printed and noted; not silently corrected.

### ch01 (军统培训特务的内幕 / Inside the Juntong's Training of Agents) - DONE

- PDF 20-47, printed 1-28. 97 source paragraphs, 92 translated (declared -5:
  see the song appendix below). 5 sections.
- Crop verification caught 13 more source errors, including **the author's own
  name**: 沈醉 was OCR'd 沈醇 in the one paragraph where he lists himself among
  the staff. Also 王尝五→王崇五, 薪镇南/菏镇南→蒋镇南, 严杰/严你→严燮 (the
  student beaten to death in a training bout), 喜铭易→袁铭鼎, and 正是需要二部
  →正是需要干部.
- Checks: parity OK with the declared exception, anchors 45/45, numbers
  0 unresolved across 92 pairs, headings consistent, register within tolerance.
- Notes: 45, i.e. 1.6 per printed page, against 3.0 in fm01 and 2.3 in fm02.
  Deliberately not padded: a third of this chapter is personnel rosters -
  ninety-odd names of company commanders and platoon leaders - which need no
  glossing and would not be improved by it. The density is where the material
  earns it, and this is the justification on record.
- Glossary: +42 entries (117 total).
- EPUB rebuilt: 3 documents, 125 paragraphs, 71 notes, qa_epub PASS.

### THE SONG APPENDIX - a decision Winston should confirm

The chapter ends its second section by printing the full lyric of the class
song, which became the Juntong's own anthem. That lyric is characterised in one
editorial block rather than set out line by line; the two lines Shen Zui himself
singles out, and on which his whole argument rests - the leader's safety before
the state's territory - are quoted in the body where he makes the point. The
departure is declared in `book.json` as a parity exception with a written
reason, printed on every run of the structural check, and the QC file folds the
same run so the numeric check stays aligned. Say if you want the lyric rendered
in full instead; it is four lines of conventional period exhortation and
nothing in the argument turns on it.

### The numeric check earned its keep this chapter

17 flags on first run, all adjudicated: 3 were OCR errors in the source, TWO
WERE REAL OMISSIONS IN MY TRANSLATION - a dropped "four rounds" from Tao
Yishan's mahjong remark, and a dropped "two" from "the two specialities of
telecommunications and accounting" - and the other 12 were names containing
numerals (王崇五, 王百刚, 周万尝) and period idioms. Fixes made:
- English ordinals now resolve, so 十六兵团 as "Sixteenth Army Group" and
  第二十六军 as "Twenty-Sixth Army" stop reading as dropped unit numbers. Unit
  numbers are load-bearing and must not be silenced as noise.
- Project noise moved to `data/noise.txt` and applied BEFORE the built-in list,
  not after. The generic 两[三边] was eating the front of the project's 两三百
  and leaving a bare 百 - the same prefix-eating trap as inside NOISE, one
  level up.

### ch02 (抗战前军统特务在上海的罪恶活动) - TRANSLATED, checks incomplete

- PDF 48-90, printed 29-71. 117 source paragraphs, 117 translated, parity OK.
- 30 source OCR errors recorded and replayed, including six separate manglings
  of one name (吴乃宪) and four of another (程慕熙). Crop-verified: 唐腴庐,
  车耀先, 邹韬奋, 高巩白, 吴乃宪. The Cui Wanqiu passage - Zhang Chunqiao
  writing as Di Ke against Lu Xun, and Lan Ping at Cui's house - reads as
  printed; it is the most historically loaded claim in the chapter and it was
  checked against the scan rather than trusted to OCR.
- STILL TO DO on this chapter: the numeric check has 46 flags outstanding,
  unadjudicated (the count rose with the corrected segmentation, which
  restored text the folio bug had removed). On ch01 the same first pass was 17 flags of which two were
  real omissions in the translation, so these must be worked through, not
  waved past. Notes not yet written. Not yet built into the EPUB.

## A pipeline defect that cost the afternoon, and what it changed

`strip_folio` decided whether a page's last line was the printed page number
by looking at the TEXT: short, at most one Han character, dot-delimited. That
rule deleted a real line - a paragraph whose final line was 写。 - and with it
the paragraph break that followed, silently merging two paragraphs of the
book. It was found only because chapter 2's parity came out one over and the
scan was consulted to see why.

Silent deletion of text is the worst defect this pipeline can produce after
invented text, so the guess was replaced by a measurement: a folio sits below
a gap 1.35x the leading and is a few glyphs wide against a full measure.
Sampled over the book it finds a folio on 71 of 72 pages, and where it is
unsure it KEEPS the line, which is the right direction to fail in.

Restoring those lines then exposed a second problem. The short-last-line rule
for paragraph ends is right inside a page and wrong at the foot of one, since
a page's final line is short whenever the text block ends there. So paragraph
segmentation now uses the printed INDENT, measured off the page image by
`scripts/indents.py` - the mark the typesetter actually made. Two things had
to be got right for it to work, and both were got wrong first:
- the flush-left margin is measured GLOBALLY rather than per page, because
  twenty-odd lines are too few to locate it and a skewed page produces a
  second cluster;
- it is measured SEPARATELY for recto and verso, because the gutter mirrors.
  A single margin sat between the two and read one side as all-indented.
- at the top of a page the indent is not trusted at all; there the previous
  page's short last line decides.

Chapter 2's source came out at 117 paragraphs under this scheme - the exact
count the translation had independently reached from reading the scan, after
the earlier segmentation said 116. That agreement is the reason to believe it.

### CONSEQUENCE FOR THE THREE FINISHED UNITS - work outstanding

fm01, fm02 and ch01 were translated against the OLD segmentation, which was
missing the lines the folio bug had eaten. Their prose is unaffected and every
other check on them still passes, but their paragraph COUNTS no longer match
the corrected source: fm01 19 against 18, fm02 18 against 15, ch01 95 against
92. In each case the book splits a paragraph where the translation runs two
together. The fix is to insert paragraph breaks at those points - checking
each against the scan, not against the count - and to recompute ch01's
declared song-appendix exception, which was written against the old numbering.
This is bookkeeping, not retranslation, but it is not done.

## SEGMENTATION: RESOLVED, and the root cause

The previous session recorded that this had not converged and warned against
tuning thresholds. Following that note, the detector was validated against the
pages themselves before anything else was touched -- and it was exact: six
indents of six on one sample page, three of three on another, no false
positives. The detector was never the problem.

THE ROOT CAUSE was that the indent was being measured off the page image in
one pass and the text produced in another, then matched BY LINE INDEX.
Tesseract's line grouping is not the printed line banding -- it merges and
splits lines of its own accord -- so the two disagreed on 140 of 515 pages,
and each disagreement slid every paragraph mark below it one line out of
place. That, not any threshold, is what made the counts wander for hours.

THE FIX: take the indent from the same tesseract pass that produces the text.
`--psm 6 txt tsv` yields a bounding box per word and so a left edge per OCR
line, and the reference margin is the mode of the line starts on that page.
Same pass, same lines, no alignment step to get wrong. Misaligned pages went
from 140 to 0. No global margin, no recto/verso calibration, no page-top
special case, no short-line fallback -- all of those were scaffolding for a
problem that no longer exists.

Two further defects fell out of it:
- Folio-derived pseudo-headings. `find_headings` had recorded two page numbers
  as section titles ('.5，' and '到'); assemble was injecting them into the
  source as '### ' lines, which both split a paragraph mid-sentence and put
  junk in the text. Dropped: a heading has at least two Han characters.
- Every break is still gated on sentence-final punctuation, which is what
  makes the result safe by construction rather than merely correct today.

RECONCILIATION DONE. All four translated units now match the corrected source
exactly: fm01 18/18, fm02 16/16, ch01 91/91, ch02 115/115. The adjustments
were paragraph joins and one split in the ENGLISH, plus removal of ch01's
song-appendix parity exception, which was an artefact of the old segmentation
-- the book sets that lyric as a single paragraph, which is how the
translation renders it. No prose was rewritten. There are now no parity
exceptions anywhere in the book.

## THE FOLIO FILTER WAS STILL DELETING TEXT, AND IT REACHED CHAPTERS 1-4

Found while assembling chapter 3, by chasing a single stray character. The
source read "...与处相等的室、人。" where 人 made no sense. The scan showed the
book prints a whole line there that the OCR did not have:

    区、组，还有几个委员会，内勤达到一千多人，外勤增至五万多

A line carrying two of the Juntong's strength figures, silently gone.

THE MECHANISM. `strip_folio` popped a page's last OCR line whenever
`folio_present` said the page had a printed folio. But `folio_present`
profiled the WHOLE page while the text it judged came from the CROPPED image.
Where the crop bottom (0.905) fell above the folio, the crop had already
removed the page number, tesseract's output ended on real prose, and the pop
deleted that prose. In chapter 3 the folio falls outside the crop on 24 of 59
pages: 41% of pages lost their last line.

WHY NOTHING CAUGHT IT. A line deleted from the middle of a paragraph changes
no paragraph count, so parity passed. The previous session's reconciliation
("all four translated units now match the corrected source exactly") was
matching the translation against an already-damaged source. Two derived
artifacts agreeing with each other, again.

THE FIX. Deletion now requires the geometric AND the textual signal to agree,
and where they disagree the line is KEPT. Neither signal is sound alone: the
geometry is what ate the line above, and the text-only rule is what once ate
写。. A full folio carries digits; a folio the crop clipped keeps its dot
delimiters, and Chinese typesetting forbids a line opening on sentence-final
punctuation, so a short line starting with 。 is not prose either.

REJECTED: widening the crop to 0.970 to swallow the folio whole. It does fix
the folio, and body text (max 0.9173) and folios (from 0.8868) genuinely
overlap so no crop line separates them -- but a taller image regroups psm 6's
lines, which broke heading matching (chapter 4's title merged into its first
paragraph) and moved settled paragraph counts. Reverted to 0.905.

CONSEQUENCE FOR THE FINISHED UNITS - now resolved. Corrected source counts
came out fm01 18, fm02 16, ch01 93, ch02 116, ch04 20, against translations
of 18/16/92/115/19. Every shortfall was a paragraph BOUNDARY, not lost prose:
the eaten line carried the indent that marked the break, so two paragraphs ran
together. `reflow.py` re-laid ch01, ch02 and ch04 onto the corrected
boundaries. No prose was rewritten and none was found missing.

State after the repair: parity OK on all five units, and check_align reports
no pair straying from the median on any of them.

## A TRUNCATION BUG IN MY OWN READING, AND WHAT CAUGHT IT

Reading assembled source with `cut -c1-700` to keep chunks manageable. `cut -c`
counts BYTES, not characters, so on UTF-8 Chinese the window was really about
233 characters. Twenty-one of chapter 3's first 96 paragraphs were translated
only as far as that cut, losing the second half of each -- including the whole
middle of the Inspectorate's staffing paragraph (the three recalled deputy
inspectors-general), the wireless-registration and interception passage, the
Kong Lingjun confrontation, Liao Gongshao's traitor relations, and the entire
close of the chapter's detective-brigade section.

Nothing in the prose showed it: every truncated paragraph ended on a complete
English sentence. `check_align.py` caught it, because the ratio of English
characters to Han characters collapsed on exactly those pairs. That check was
written for a different failure (source and translation slipping past one
another) and found this one for free. It is the reason to keep ratio checks
even when parity passes.

All twenty-one repaired against the full source, with the OCR in the recovered
tails crop-verified like the rest. ch03 now reports "alignment OK: no pair
strays more than 2.2x from the median" across all 96 translated paragraphs.

Reading the source in fixed-size chunks is now done by paragraph index in
Python, never by `cut`.

## THE SENTENCE-END GATE DID NOT KNOW ASCII PUNCTUATION

`assemble.py` gates every proposed paragraph break on the text ending in
sentence-final punctuation, with SENT_END = "。！？…" -- all fullwidth. But
tesseract reads the printed ！ and ？ as ASCII "!" and "?" often enough that
the gate refused real breaks: six across the book, each welding two source
paragraphs into one. The typesetter's own indent said "new paragraph" and was
overruled by a punctuation list that did not contain the mark on the page.

Found while translating ch03 p133, where "...真是不知道怎么办才好!" ran
straight into the start of the counter-espionage section. The indent flag for
that line was True; the break was suppressed anyway.

Fixed by admitting the ASCII forms (they are the same marks) and the colon.
The colon is safe here because a break still requires the measured indent as
well, so a false split would need a colon and a typesetter's indent together;
it recovers the ordinary enumerating case, "...分述于下:" followed by an
indented list entry.

Consequence: ch02 source 116 -> 119, ch03 source 190 -> 193. ch02's finished
English re-laid onto the corrected boundaries with reflow.py and passes parity
and alignment at 119/119. ch03's in-progress English split by hand at the two
points that fall inside the translated range, verified by matching content
markers independently in the Chinese and the English.

## Wake-up routines

Four routines fire into this session on the hour, offset to give a roughly
15-minute cadence (the server enforces a one-hour minimum per routine, so the
cadence is built from four of them rather than one quarter-hourly schedule):

  trig_01S5CvzyS3eJ8WNftAfreQrJ  resume (:00)   0 0-23 * * *
  trig_01WDHR8F56isWhzk1hutP53i  resume (:15)   15 * * * *
  trig_01SHb5gLz8MuUSVGqrSbmwdq  resume (:30)   30 * * * *
  trig_01YPE2vMy3oZtsVWjCsTTBVv  resume (:45)   45 * * * *

ALL FOUR must be deleted once every unit is done and qa_epub passes. They
store no MCP connectors, so the sessions they wake cannot delete them: that
has to happen from a session holding the tool, or from the routines UI.

## Pending decisions

- **Chapter 1 contains an appendix printing the full lyrics of the training
  class song** (附录:班歌歌词全文, printed p.40). Intention is to characterise
  and summarise it — what it says, what register it is in, what it tells you
  about the institution — rather than set out a complete lyric translation.
  Say if you want it rendered in full instead.
- Note numbering runs continuously across the book (decided; implemented in
  neither builder nor QA yet — the builder is the next engineering task).

## Next steps, in order

1. Generalise `build_reading_epub.py` and `qa_epub.py` from the previous
   project's chapter-1 shape to this book's 25 units, with the anchor gate that
   refuses to build on an unmatched anchor.
2. fm02_qianyan (前言), PDF 10–15 — source already assembled.
3. Chapters 1–21 in order, per the pipeline in CLAUDE.md.
4. Batched scholarship pass, covering several chapters at a time.
5. Final sweep per the skill: re-run every script, register across the whole
   spine, historical pattern analysis, random-sample deep audit.
