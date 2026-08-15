# Deep audit — Burn, O Sword! (燃えよ剣)

Whole-book random-sample audit at completion (B15), QC check 9. The aim is an
honest error-rate statement for the finished translation, not a spot fix.

## Method

- **Pool.** Every source body paragraph across all 71 units, paired with its
  English (`out/<id>_en.json` against `data/zh/<id>.txt`). Total: **12,228
  paragraph pairs.**
- **Sample.** A random 4.0% drawn with a **fixed seed (1869)**, deterministic and
  reproducible: **489 paragraph pairs**, spread across all 71 units.
- **Read.** Each sampled pair was read Japanese-against-English for the error
  classes machines miss: fabrication (a fluent English sentence with no source
  warrant), omission (source content silently dropped), mistranslation, number/
  date/quantity errors, name-rendering drift, and register breaks.
- **Invented-precision sweep (100% coverage, mechanical).** In addition to the
  per-chapter `check_numbers.py` (which verifies every *source* number survives
  into the English), a whole-book reverse scan was run for the "invented
  precision" class: any Arabic number in the English whose paragraph has no
  numeral in the source. Across all 71 units it returned **one** hit, and that
  one is a false positive ("Genji 1" for 元治元年, where 元 = "first year" is the
  numeral). No invented precision anywhere in the book.

## Findings

- **Errors found in the 489-pair sample: 0.**
  - Numbers and quantities: correct throughout (e.g. 三千人近く → "close on three
    thousand," 五十万石 → "five hundred thousand koku," 二十四斤 → "twenty-four
    kin," 十七日か十八日 → "the seventeenth or the eighteenth," 四斤山砲 …
    弾丸は千メートル以上 → "the shell flew more than a thousand meters").
  - Dates: era-year form kept and correct (元治元年十二月一日, 慶応元年二月二十一日,
    嘉永六年六月三日 → "the third day of the sixth month of Kaei 6," etc.).
  - Names: one settled rendering per referent, matching the glossary (Hijikata
    Toshizō, Kondō Isami, Okita Sōji, Shichiri Kennosuke, Kōga Magodayū, Nakajima
    Saburōsuke, Ōtori Keisuke, Enomoto Takeaki, Oyuki, …).
  - No fabrication and no omission were observed in any sampled paragraph,
    including the long single-pass paragraphs (the ch24 Aizu dispatch, the ch53
    monument passage, the ch64 Kōtetsu description) whose tails were read in full.
  - Register held to the frozen ch01 reference; the essay back matter reads in
    the essayist's own voice, as intended (exempt from dialogue-contraction
    expectations).

## Honest error-rate statement

Zero errors were found in a fixed-seed random sample of 489 paragraphs (4.0% of
the book). This does **not** prove the book is error-free. By the statistical
"rule of three," zero defects in n = 489 bounds the true paragraph-level error
rate at roughly **3/489 ≈ 0.6%** at about 95% confidence — i.e. the audit is
consistent with an error rate below ~0.6%, not with zero. The mechanical checks
that run at 100% coverage (parity by construction, source-number survival,
reverse invented-precision, entity survival, content/displacement, apparatus
anchors) found no defect in the finished text either, save the two documented
standing items that are not errors: the ch52 `check_content` substring
false-flag (近藤勇平 ⊃ 近藤勇), and the article-only "unused glossary form" miss on
茨木屋 "the Ibarakiya" (the form does occur, ch22).

_Sample regenerable: seed 1869, 4% of the 12,228-pair pool; see the B15 record in
PROGRESS.md._
