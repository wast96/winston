# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch12); rebuilt, qa green.
- LOCAL: fixed a dropped clause in ch03 section 2.
-->

## 2026-08-03 — review pass (tire-kicking audit of the finished book)

Full six-part accuracy/readability/apparatus audit of all 60 units (source vs.
reading text, paragraph by paragraph, every footnote checked). No HIGH-severity
problems found anywhere: no invented content, no meaning-flips, no dropped
clauses, no wrong numbers/names/dates; footnotes all factually sound. The
following consolidated corrections were applied; rebuilt, qa_epub green,
paragraph parity re-confirmed on every touched unit.

- GLOBAL: unified the recurring epithet 杏仁色 (Mei Yingzi's teeth) to
  "almond-tinted" throughout. It had drifted three ways — "almond-tinted"
  (ch08/09/15), "almond-coloured"/"almond-colored" (ch18/22/40/52, with a
  British/American spelling split), and "almond-white" (ch47/48). Now 10/10
  read "almond-tinted". (ch15 keeps its source-justified "glistening white"
  from 润白.) Files: out/ch18, ch22, ch40, ch47, ch48, ch52 _reading.md.
- GLOBAL: aligned the novel title 江湖行 to its decided/attested glossary form
  "River of Fury" (Frederik Green). The text had drifted to "Rovings" (ch00)
  and romanized "Jianghu xing" (ch59); both now read "River of Fury", matching
  glossary.json. Files: out/ch00, ch59 _reading.md.
- LOCAL ch21: "a bundle of oppression and contradiction" -> "anguish"
  (苦闷 = inner anguish, not external subjugation).
- LOCAL ch19: "He is browner ... on you" -> "You've grown browner ..." — the
  source line 人黑了…於你 is addressed to the narrator throughout; fixed the
  stray third person.
- LOCAL ch18: attributed the protest "It is an insult to us!" to the narrator
  ("...I said."), which the source's two-speaker line left ambiguous and made
  it read as Mei Yingzi contradicting her own next line.

Files touched: out/ch00, ch18, ch19, ch21, ch22, ch40, ch47, ch48, ch52,
ch59 _reading.md; CHANGELOG.md.
