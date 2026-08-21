# Deep Audit — Chen Yangshan: Hero of the Secret War

Whole-book random-sample audit, run once at completion (Batch 10). Purpose: to
catch the error classes the per-chapter scripted gates cannot see, above all
**invented precision** (definiteness the source withholds) and subtle
mistranslation inside otherwise clean prose.

## Method

- **Population.** 1,256 body paragraphs across the 12 built units (headings and
  set-off markers excluded).
- **Sample.** 44 paragraphs (3.5%), drawn with a **fixed seed** (`random.seed(424242)`),
  distributed as: ch01 4, ch02 11, ch03 3, ch04 8, ch05 7, ch06 5, ch08 2,
  ch09 3, ch10 1. The sample list is archived alongside this file.
- **Two screens, then a hand read.**
  1. **Invented-precision grep** over the whole book for the classic tells
     (`for weeks/months/days`, `a dozen`, `dozens of`, `scores of`,
     `a handful of`, `several hundred/thousand`, `tall/young/old man`, etc.).
  2. **Hand read against the scan** for every sampled paragraph that could be
     pinned to a source page. Because `data/zh` is regenerated per batch and is
     gone on a fresh checkout, the paragraphs pinned with certainty were
     concentrated in the units whose source location is unambiguous
     (ch03 narrative, ch08 documents, ch09 chronology); these were read
     character-by-character against the page images. The remaining sampled
     paragraphs in ch01/ch02/ch04/ch05/ch06 were covered by the per-chapter
     gates (parity, numbers, content, entities, align, register — all green when
     each unit's zh was present) plus the whole-book grep screen.

## Findings

**Substantive errors found by the hand read: 0.**

Passages read character-by-character against the scan, all exact and faithful:

- **ch03, the "Three Questions for Kang Sheng" passage (PDF 110 / printed 99).**
  Narrative and quoted speech. The martyrs' answer ("There is nothing wrong in
  my past. If you say I made mistakes in my work, I don't deny it, but as for
  traitor, agent, Trotskyite, none of it touches me.") renders
  我历史上没有任何问题，要说工作上有错误，我不否认，至于叛徒、特务、托派，同我沾不上边
  exactly, with a natural dialogue contraction; the 1937 secret executions and
  the 1940 news reaching Chen Yangshan match line for line. The three names
  (Xiao Shouhuang, Ouyang Xin, He Changzhi) are rendered as printed.
- **ch08, the son's editorial footnote and both list documents (PDF 232-233 /
  printed 221-222).** The 36-item Memoir Outline (1. Back to Shanghai ... 36.
  Turning to new tasks) matches all 36 source items; Cheng Jianyu's note matches
  every item-range attribution (1-17, 18-19, 20-23, 24-30, 31-33, 34-36), the
  place list, and the 1989-summer lung-cancer death; all 13 household precepts
  match the source one for one, including 九 ("do not take up smoking or drinking
  at home" = 不能到家吸烟吃酒).
- **ch09, the chronology (PDF 234-237 / printed 223-226).** Every sampled
  year/age label matches (1928/22, 1931/25, 1935/29, 1936/30, 1940/34, 1941/35);
  the 1936, 1940, and 1941 entry bodies match the source clause for clause,
  including the wife's name (Zhang Suzhen), Baoji, and the exact office titles.

**Invented-precision grep:** the hits were all faithful renderings of source
quantities or of source-stated descriptions (checked in context), not supplied
definiteness. The book's genuinely vague quantities are rendered vague.

**Number/name integrity in the un-pinned narrative sample** rests on the
per-chapter `check_numbers` runs, which were 0-unresolved for every unit,
including the number-dense items in the sample (e.g. the forged "Wu Hao Notice"
in ch05: the 243 signatories and the February 15/16/19/20/21, 1932 dates all
survive, and the episode is corroborated in outline in the note).

## Cross-book reconciliation (check 12), reported here for completeness

- **Epithet drift: 0** compounds rendered more than one way.
- **One wrong form found and fixed:** 霞飞路 had been rendered "Route Joffre";
  the shelf agrees on **"Avenue Joffre"** (5 books, status *agreed*; the
  historically correct name). Corrected in the ch02 prose, the note anchor and
  body, and the glossary, then rebuilt and re-validated.
- **One homograph correctly kept separate:** 中原 is "Nakahara" here (a Japanese
  general's surname), not the shelf's "Central Plains"; not merged.
- **Three source variants preserved and footnoted, never harmonized:** the
  Xiao Shouhuang / Xiao Taihuang name (noted at the ch06 occurrence); the 1988
  letter printed twice (cross-referenced at the ch08 appendix); the rehabilitation
  timeline (1978 verdict quashed, residual "Right deviation" negated only in
  1983), consistent and noted in ch07.

## Honest confidence

Zero substantive errors across roughly twenty paragraph-equivalents read by hand
against the scan is **evidence of no systematic problem, not proof of a zero
error rate**: on a sample this size it is consistent with a true per-paragraph
error rate up to a few percent. It should be read together with the per-chapter
gates (which ran on the full text of every unit) and the reconciliation sweep,
not on its own.

## Residual uncertainties a reader should know about (see COMPLETION.md)

- **52 provisional romanizations** (out of 731 referents): minor bit-part names
  whose exact scan characters were doubtful; the build marks these, and the term
  ledger lists every one.
- **Source errors preserved as printed and footnoted** (never silently fixed):
  e.g. the 1912-for-1942 training date (ch04), Ma Hanshan / Ma Hansan (ch04),
  the "Tenth Central Committee" plenum that should read Eleventh (ch06), and the
  Xiao Shouhuang / Xiao Taihuang name variant.
