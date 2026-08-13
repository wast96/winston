# Deep Audit — The Gangs of Old Shanghai

**Method.** A whole-book random-sample audit, run once at completion (check 10 of
the QC contract). From the 1,196 source-paired paragraphs across the 27 running-prose
units (the two appendices, ch27's charter and ch28's described member-roll, are not
paragraph-parallel and are excluded), a fixed-seed sample was drawn
(`random.seed(54)`, 3.5% = **42 paragraphs**) and each pair read source-against-English
under full paranoid treatment, looking for: fabricated or bridged text; dropped names,
numbers, or clauses; invented precision (definiteness the source withholds); mistranslation;
and register drift. The sample spans 23 of the 28 chapters, weighted by length (ch15,
the longest, drew 7; the Gu Zhuxuan batch drew 1).

**Reproducing the sample.** `random.seed(54)`, sample 42 of the 1,196 parallel
paragraphs enumerated in reading order over `data/zh/ch*.txt` × `out/ch*_reading.md`.

## Findings

**Substantive fidelity errors: 0 of 42.**

Not one sampled paragraph carried a fabrication, a dropped proper name, a dropped or
altered number, or a mistranslation of consequence. This held across the hardest cases
in the sample — the name-dense list paragraphs (S21, a run of nineteen hoodlums with
their epithets and businesses; S36, the nineteen founding Heng Society directors; S2,
the Dagong News Agency roster; S12, the five-fold Ren Society census; S40, the Linji
Timber Firm with its dozen names), the long narrative set-pieces (S16, Chiang Kai-shek's
kowtow to Huang Jinrong; S31, the arrest of Du's son; S41, the eighty-twenty opium
negotiation), and the classical-register quotations (S5, the Qing memorial on the
"Wujiang uproar"; S9, the Hongmen altar tablets). Numbers were carried faithfully
throughout (150-odd *li*, nearly sixty *mu*, 20,000 silver yuan, 400,000 yuan, more than
6,000 guests, more than two thousand disciples, twenty men counted at the incense hall).

**Minor observations (not counted as errors):**

- S28 (ch15 ¶144): 上海市参议会 is rendered "the Shanghai Municipal Council." The
  reading is defensible (参议会 is a council/assembly, here the postwar elected city
  assembly), but the same English phrase is the conventional name of the International
  Settlement's 工部局, the Shanghai Municipal Council; context (a 1947 KMT-era birthday)
  disambiguates, and no SMC reference stands near it, so this is a clarity note, not a
  fidelity fault.
- Currency: 元 is rendered now "yuan," now "dollars," by context (e.g. S3 "a few
  thousand dollars," S24 "from one yuan to a hundred"). Both are in period use for the
  Chinese dollar/yuan; the variation is stylistic, not a value error.

## Rate

Zero errors in 42 independently sampled paragraphs does not prove a zero error rate; by
the rule of three it places the true substantive-error rate below about **7% at 95%
confidence** (3/42). What it does establish positively is that the book's recurring
failure modes for this genre — a dropped name in a long enumeration, a number silently
changed, a fluent invented bridge over an OCR gap — did not appear anywhere in a 3.5%
paranoid read. The per-chapter scripted gates (parity, numeric invariants, entity
survival, content displacement, register) that ran on every unit as it was translated
are the reason: the classes this audit hunts are the classes those gates already close,
and the audit finds the residue, which here is nil.

## Residual uncertainties a reader should know

- The OCR layer, not the translation, is the floor on accuracy for rare proper names.
  Every name in the running prose was crop-verified against the page image where the two
  OCR engines disagreed; but the **1934 member roll (Appendix II)** is a list of 324
  personal names that could not be verified one by one to that standard, and is therefore
  given as a described appendix with a fourteen-entry verified sample rather than a full
  romanized transcription. See the appendix's own note.
- Where two contributors disagree on a fact (Gu Zhuxuan's given name, his gang master,
  and his rank in the Zhabei corps differ between ch25 and ch26; ch22 and ch23 disagree
  on Zhang Xiaolin's birthplace), both are rendered as printed and the discrepancy
  footnoted, never silently reconciled.
- A handful of the book's own claims are uncorroborated or contradicted by outside
  scholarship; each such note says so in its verdict.
