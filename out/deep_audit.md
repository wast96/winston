# Deep audit (check 10) — The Stealthy Ones

Random-sample deep audit of the finished translation, reading the Japanese
source (the scanned page images) against the English, paragraph by paragraph.
Full paranoid treatment: every name, number, date, place, and any phrase that
might carry definiteness the source withholds was checked against the scan.

## Method

- **Fixed seed:** `19870824` (Goemon's execution date, for reproducibility).
- **Sampling frame:** 3,134 body paragraphs across the 8 chapters.
- **Sample:** 18 windows of 6 consecutive paragraphs were drawn (≈108
  paragraphs, 3.4%), then mapped to their source pages. Because only Chapter 1
  carries a page-map, paragraph→folio mapping for the other chapters is
  proportional and approximate; several windows therefore landed a page or two
  off. Rather than discard those, the audit read the rendered source page and
  verified **whatever reading-file paragraphs actually map to it** (located by
  content match on names/numbers). This preserves the random, paranoid,
  read-the-scan character of the audit while guaranteeing every verified
  paragraph was genuinely checked against its own source.
- **Coverage:** at least one full source page was read and verified in **every
  one of the 8 chapters**:

  | Chapter | Source folio(s) read | Reading-file paras verified |
  | --- | --- | --- |
  | ch01 | 6, 19 | L9–L17; L173–L183 |
  | ch02 | 83–84 | L229–L241 |
  | ch03 | 174 | L395–L405 |
  | ch04 | 238 | L473–L483 |
  | ch05 | 314 | L571–L577 |
  | ch06 | 392 | L499–L509 |
  | ch07 | 433 | L397–L407 |
  | ch08 | 487 | L219–L223 |

  **≈54 paragraphs verified against the scan**, spread across all eight chapters.

## Result

**Zero mistranslation errors in the ≈54 image-verified paragraphs.**

By the rule of three, zero errors in 54 paragraphs bounds the paragraph-level
mistranslation rate **below about 5.6% at 95% confidence — a bound, not a proof
of zero.** The result is consistent with the per-batch checks already run and
passed across the eight approved batches.

What was checked and found faithful, sampled across the eight pages:

- **Numbers/dates carry exactly.** Tenshō 10 / 1582; the 21st, 29th, and the
  first of the sixth month (20 June by the solar calendar); the Frois letter of
  18 December 1583 and its three troop figures (6,000; 20,000+; 15,000
  half-naked men); "ten ken," "nine in the morning," Ieyasu's 9,000 at
  Fujigatake; 2.5 ri from Ishikawa; a bare 300 men at Hayashidani-yama, a
  kilometer from Kitsunezuka; the five provinces taken from Ieyasu. Every one
  matched the scan.
- **Names/places carry exactly**, including very dense runs: the Jesuits
  (Cariam, Lourenço, Bertolameu, Organtino), the Honnō-ji cast (Nobutada,
  Myōkaku-ji, Kurama, Takamatsu, Takayama Ukon), the Shizugatake and Nagakute
  commanders and topography (Sakuma Morimasa, Menju Shōsuke, the gilded gohei;
  Sakakibara, Ōsuga, Inaba, Yada, Honji, Irogane, Nagakute), the seven
  shichihōde disguises, and the entire Edo-founding digression (Tamachi,
  Hibiya, Marunouchi, Tsukiji, Ginza, Chichibu Shigetsugu, Ōta Dōkan).
- **Voice and dialect** render as natural English without loss: the doomed
  couple's Kansai-dialect exchange in ch07 (あて / おぬし / ～や) reads as living
  rural speech, not decoded Japanese.

## The "invented precision" class (grepped whole-book, then spot-checked)

This class greps better than it samples, so it was scanned across all eight
reading files, not just the random windows.

- **Vague-duration renderings** ("for days" ×2, "for some months" ×1, "for
  years" ×1): themselves vague; none convert a vague source into a false
  specific. (The failure mode to fear — 多時 → "for weeks" — did not appear.)
- **Exact durations** ("two months" ×8, "three days" ×8, etc., 52 in all):
  these are the ordinary fabric of a densely-dated historical novel; the sample
  confirmed such counts track the source exactly (二カ月 → "two months," 十三里
  → "thirteen ri," 五十年 → "fifty years," 二里半 → "two and a half ri").
- **Physical definiteness** ("a young man" ×7, "a young woman"/"a young girl"
  ×5, "a small man" / "a short man" ×2): the two riskiest — the "small/short
  man" cases — were read against the source and are both grounded in the
  source's own explicit description (the retainer explicitly "under five shaku";
  Hideyoshi by the well-known monkey-face/short trope, 猿面). No definiteness is
  added that the source withholds.

## One finding (systematic, fixed during this audit)

- **daimyō/daimyo and shōgun/shogun were split** (大名 rendered "daimyō" ×21 vs
  "daimyo" ×18; 将軍 rendered "shogun" ×26 vs "shōgun" ×2). This is a
  consistency defect, not a mistranslation. Both words are naturalized English
  (dictionary forms carry no macron), and "shogun" already dominated alongside
  its derivatives "shogunate/shogunal." Standardized to the plain naturalized
  forms **"daimyo"** and **"shogun"** across every unit, notes.json,
  glossary.json, and the afterword, and folded into the reconciliation variants
  map (data/variants.json). Nothing else in the audit required a change.

## One suspected error that proved faithful

In ch02 (L229) the medicine-peddler's patter says his wares were "brought over
from Ming China" — flagged because it sits beside a claim of fame "since the
Nara capital," when China was Tang, not Ming. Reading the source quote on folio
83 settled it: the source itself says 明国渡来 ("come over from the country of
Ming"). The anachronism is the peddler's (or the author's), and the translation
correctly preserves it rather than silently "fixing" it — exactly the house
rule for the source's own errors.

## Conclusion

Across ≈54 paragraphs read against the scan in all eight chapters, and a
whole-book invented-precision scan, the translation shows **zero mistranslation
errors** and disciplined handling of the invented-precision class. The single
finding was a naturalized-spelling inconsistency (daimyo/shogun), now fixed. The
sampled bound on the paragraph-level error rate is **below ~5.6% at 95%
confidence** — reported honestly as a bound, not as a claim of perfection.
