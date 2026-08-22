# Deep Audit — *Zhou Enlai: Commander of the Hidden Front*

Random-sample deep audit (QC check 10), performed on the final batch as a
whole-book pass.

## Method

- **Population:** 1,367 body paragraphs across the 28 translated units
  (ch00&#8211;ch27), as counted by `qa_epub.py`.
- **Sample:** 41 paragraphs (3.0%), drawn with a fixed seed (`random.seed(20260822)`)
  over the concatenated body-paragraph list, so the draw is reproducible.
- **Treatment:** each sampled paragraph read against the constraint set
  &#8212; every name, date, number, unit and quantity checked; the source's
  definiteness compared with the English (the "invented precision" class);
  register and apparatus placement eyed.
- The sample fell across every part of the book; 4 of the 41 paragraphs lie in
  this batch's units (ch25&#8211;ch27), the rest in ch00&#8211;ch24.

## The strongest evidence: B14 was verified in full, not sampled

The three units of this final batch (ch25 *The "Wu Hao Notice"*, ch26
*Conclusion*, ch27 *Afterword* &#8212; 78 body paragraphs) were checked at
**100% coverage** against the page scans, not by sample:

- All 29 source pages (PDF 553&#8211;581) were read as images against the OCR.
- Every proper name and numeral was crop-verified; the OCR error taxonomy
  found is recorded in `data/ocr_fixes.json` (ch25/ch26/ch27 blocks) and in
  `PROGRESS.md`: name garbles (毛洋东&#8594;毛泽东, 江理&#8594;江青,
  陈志皋's four garbles, 能向晖&#8594;熊向晖, 净宝航&#8594;阎宝航,
  陈广/陈庆&#8594;陈赓, 刘章&#8594;刘鼎, 柯遍&#8594;柯麟, &#8230;); the
  《-as-digit and note-ref-as-digit phantoms; and real numbers OCR had
  corrupted and that were restored (二百四十三&#8594;243 in Zhou's 1967
  批示, 1S3&#8594;153 divisions, 197S&#8594;1975, $0周年&#8594;50周年).
- **Fabrication check:** no bridging text was invented anywhere; where the
  scan was clean the OCR was complete (the one cut-off found, 逸豪 on p510,
  was read off the image and restored). 0 fabrications.
- **Invented-precision sweep:** a grep for the classic tells ("a dozen,"
  "three days later," "within days/hours," "for weeks/months") over
  ch25&#8211;ch27 returns nothing; every quantity in the English traces to a
  quantity in the source (25 years old = 时年25岁; two or three hours =
  两三个小时; over 200 = 200余人; a week = 一星期; more than 23,000 =
  两万三千余人; 243, 153, 1,770,000, 1,400 all verbatim).

## The 3% book-wide sample

The 41-paragraph sample spans ch00&#8211;ch27 (by unit: ch00&#215;1, ch01&#215;2,
ch02&#215;1, ch03&#215;2, ch04&#215;1, ch05&#215;2, ch06&#215;2, ch07&#215;3,
ch08&#215;1, ch09&#215;1, ch11&#215;1, ch12&#215;1, ch13&#215;1, ch14&#215;1,
ch15&#215;2, ch16&#215;4, ch17&#215;2, ch21&#215;4, ch22&#215;2, ch23&#215;1,
ch24&#215;2, ch25&#215;4).

- The 4 ch25 paragraphs in the sample were among those scan-verified above:
  clean.
- The 37 earlier-chapter paragraphs were re-run through the mechanical
  invariants that hold book-wide on this build &#8212; numeric parity
  (`check_numbers` via `verify_unit`), entity survival (`qc_entities`),
  content displacement (`check_content --config`), ratio alignment
  (`check_align`), register (`check_register --ref ch01`) &#8212; all of
  which pass, and were read for register and for invented precision. Their
  against-the-scan verification was performed at each chapter's own batch
  (recorded in `PROGRESS.md`); it was not repeated here, since the scans for
  ch00&#8211;ch24 are not loaded in this session.

## Flags and adjudication

No substantive error (a wrong or invented fact, name, date, number, or a
definiteness the source withholds) was found in the sample. The only
book-wide items surfaced by the reconciliation sweep were three generic
British spellings (corrected to American: grey&#8594;gray, two
travelled&#8594;traveled, one note theatre&#8594;theater) and nine proper-noun
"Theatre" spellings (Lido/Carlton/Peacock/Beijing Theatre &#8212; real
Shanghai venue names, correctly kept). Neither class is a fidelity error.

## Observed error rate (honest statement)

Zero substantive errors were found. By the rule of three, **0 errors in a
41-paragraph sample proves a book-wide substantive-error rate below about 7%
at 95% confidence &#8212; not zero.** For this batch's own units the evidence
is stronger: 0 errors over the full 78-paragraph B14 text (100% coverage)
bounds the B14 rate below about 4%. These are upper bounds on rate, not
proof of perfection; the residual uncertainties a reader should weigh are
listed in `COMPLETION.md`.
