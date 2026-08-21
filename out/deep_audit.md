# Deep audit — *China's Secret War* (final, B13)

Random-sample paranoid re-read of the translation against the verified Chinese
source, per CLAUDE.md check 10. Reported honestly, including the sample's
limits.

## Method

- **Frame.** Every paragraph with a regenerable Chinese scaffold: ch04&#8211;ch13
  (the resegment scripts rebuild their `data/zh/*.txt` deterministically). That
  is 2,314 true source paragraphs, the bulk of the body text.
- **Sample.** 81 paragraphs (3.5%), drawn with a fixed seed (`random.seed(20250821)`)
  so the draw is reproducible. Per-unit counts: ch04 3, ch05 13, ch06 17, ch07 10,
  ch08 7, ch09 8, ch10 6, ch11 13, ch12 4.
- **Test.** Each sampled pair read against its source for: dropped or altered
  numbers, names, dates, unit designations; omission; and the "invented
  precision" class (definiteness the source withholds). Numbers were also
  checked mechanically over the whole of ch04&#8211;ch13 by `verify_unit` /
  `check_numbers` (0 unresolved) and consistency by `check_reconcile` (exit 0).

## Coverage limit (stated honestly)

The Preface (ch00) and Chapters 1&#8211;3 (ch01&#8211;ch03) could **not** be
re-paired this session: ch00/ch01 have no wholesale resegment script, and the
ch02/ch03 scripts are in-place editors that need OCR inputs not present in a
fresh checkout. Those four units were verified in their own batches (B01&#8211;B04)
and are unchanged since; they are outside this final random draw. The 3.5%
figure is of the re-pairable frame, not of all 3,293 paragraphs.

## Findings

Two defects were observed, both in Chapter 8, and **both were corrected in this
batch** as part of the whole-book reconciliation (a known-wrong form must not
survive):

1. **西北公学 rendered "West China College" (Chapter 8, 5 occurrences).**
   西北 is "Northwest," not "West China" (华西); the same school is correctly
   rendered "Northwest College" in Chapters 2, 5, and 7. A geographic error and
   a cross-chapter inconsistency. Surfaced by sampled pair [45]; the whole book
   was then grepped and all five ch08 occurrences fixed to **"Northwest
   College."** (The reconciliation sweep did not catch it because ch02/ch03,
   where the correct form also appears, have no zh pairing this session.)

2. **冀南行署 rendered "Jinan Administrative Office" (Chapter 8, 1 occurrence).**
   Toneless pinyin for 冀南 (Jì-nán, "south Hebei") collides with 济南 (Jǐ-nán),
   the Shandong city; a reader would misread it. Surfaced by sampled pair [49];
   changed to the plainer, unambiguous **"South Hebei Administrative Office."**

The other 79 sampled paragraphs were faithful: numbers, names, dates, unit
designations, and set-piece quotations (Fu Zuoyi's open telegram, the TASS
statement, the Japanese Southern deployment table, the Rectification chronology,
the "paint a tiger" poem) all carried, with no invented precision found. All
four sampled Chapter 12 / 13 paragraphs (this batch's own new work) were clean.

## Observed rate

One substantive error and one romanization ambiguity in 81 sampled paragraphs.
Taking the clear error alone, that is **1 in 81 &#8776; 1.2%** at the paragraph
level. A sample of 81 with a single defect is consistent with a true
paragraph-level defect rate in the low single digits (a clean 81 would only have
proved a rate below about 3.6%); one defect found does not prove the rate is
higher than that, only that it is not zero. Both defects found were fixed, so the
shipped text is one pass cleaner than the sample measured.

## Residual uncertainties a reader should know

- **Provisional romanizations.** A handful of names survive only in Chinese
  transliteration and are marked provisional in the glossary and footnoted where
  they matter (e.g. the French attaché "Lei Meng," the Uyghur merchant "Aimaiti").
- **The 101-name public-security roster (Chapter 12).** Every name was crop-read
  from the scan and rendered in pinyin; a dense roster of rare given names is the
  single place most exposed to a mis-stroke, though all were checked against both
  OCR configs.
- **The interested-witness passages.** Where the author's partisan account meets
  the documentary record (the Suppression of Counterrevolutionaries, the Cultural
  Revolution purge of the security system, the "earliest counter-terror" and
  "safest country" claims), the text stays faithful to what he wrote and the
  footnotes carry the counter-record and the verdict.
- **Chapters 1&#8211;3 and the Preface** were not in this final random draw (see the
  coverage limit above).
