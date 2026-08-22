# Deep audit — Nameless Heroes (英雄无名), whole-book random sample

Written on the completion batch (B36). This is the manual read for the error
classes the scripted checks cannot see: subtle mistranslation, invented
precision, register slips, and quiet omission or displacement inside an
otherwise-plausible paragraph. The scripted checks already cover the whole
population for the machine-detectable classes (paragraph parity and verbatim
quotation by construction; numeric invariants; entity survival; alignment and
content displacement), so this audit is deliberately aimed at what those miss.

## Method

- **Population:** 6,160 translated body paragraphs across 43 units (the whole book).
- **Sample:** 45 paragraph pairs (0.7%), drawn by `random.sample` under a fixed
  seed (`random.seed(43)`, the batch number) so the draw is reproducible. The
  draw spanned 18 chapters across all four Parts (ch06–ch09, ch15, ch16, ch22,
  ch24–ch26, ch28, ch33–ch37, ch39, ch40), including narrative, quoted-document,
  contributed-account, and folk-custom paragraphs.
- **Procedure:** each Chinese source paragraph was read against its English
  paragraph in full, checking for (1) omission, (2) fabricated/added content,
  (3) invented precision (a number, date, name, or specific made sharper than the
  source), (4) mistranslation, (5) displacement (text belonging to a neighbor).
- The 0.7% manual sample is below the 3–5% aspiration for a hand read; it is
  reported honestly as such. It sits on top of, not instead of, the whole-book
  scripted coverage described above.

## What the sample showed

- **44 of 45 pairs: faithful and complete.** Names, Republican-year dates
  (rendered literally, e.g. 二十一年 → "In 1932", 六十九年版 → "the sixty-ninth
  year" edition), counts (六十余案 → "more than sixty cases"; 平均为五天一件 →
  "one every five days"), transliterated proper nouns (Chung Hua Jih Pao, Ta
  Kung Pao, Weldon Dance Hall, No. 76), classical idiom (张冠李戴 → "mistaken
  names"; 雷大雨小、头重脚轻 → "great thunder and small rain, top-heavy"), the
  garbled Japanese source line at ch26 §, and the nested-quote handling of the
  Li Mingqiu / Lin Biao / Tao Zhu dialogue (ch35) all render correctly. A
  digitization glitch caught in passing — 愚原路 for 愚园路 — is correctly read as
  Yuyuan Road. No omission, fabrication, invented precision, or displacement was
  found in these 44.

- **1 of 45: a minor title imprecision, corrected in this batch.** ch07 rendered
  何部长（军分会代委员长）— "Minister He (acting **chairman** of the Military
  Branch [Council])" — as "acting **deputy** chairman of the Military Branch."
  The referent (He Yingqin heading the Beiping Branch of the Military Affairs
  Commission) was correct and no fact was distorted; the single unwarranted word
  "deputy" (代委员长 = *acting chairman*, not *deputy*) has been fixed to "acting
  chairman of the Military Branch Council."

## Error-rate statement (honest)

Zero **substantive** errors (omission / fabrication / invented precision /
displacement) were found in the 45-pair sample; the one flag was a title
nuance, now corrected. By the rule of three, zero errors in 45 independent
draws bounds the true substantive-error rate at roughly **below 6–7%** at 95%
confidence — it does **not** prove zero. This manual result is consistent with,
and additional to, the whole-book scripted checks, which pass across all 43
units (parity 6,160/6,160; numbers 0 unresolved; content displacement limited
to the documented homograph/substring false positives; register within
tolerance of the frozen reference).

## Standing "invented precision" grep

A grep of the class most prone to invention (bare numerals, "exactly", "precisely",
sharpened dates) surfaced no target-only precision absent from the source in the
sample; Republican years and counts trace to a source numeral in every case the
scripted `check_numbers` pass resolves (0 unresolved book-wide with the project
noise rules).
