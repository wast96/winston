# HANDOFF — The Autobiography of Huang Mulan — COMPLETION REPORT

The commissioned scope is COMPLETE. This is no longer a batch baton; it is the
final report. B09 (ch39-ch43, the appendices) was the last batch, and with it the
whole commissioned scope — front matter, chapters 1-21, and the five appendices —
is translated, annotated, built, and QA-green. Chapters 22-38 remain pending
skeleton pages by instruction.

## What was delivered

The deliverable is `out/The Autobiography of Huang Mulan.epub`: an annotated English
translation of 《黄慕兰自传》 (Encyclopedia of China Publishing House, 2016 reissue).
Every build ships a full, hyperlinked table of contents nested part -> chapter ->
appendix; translated chapters show their content, and the out-of-scope chapters
22-38 link to skeleton outline pages that state their source size.

Final whole-book state (qa_epub.py PASS): 105 files, 50 documents, 44 reading
documents, 555 paragraphs; 89 note references / 89 bodies / 89 backlinks, numbering
continuous and sequential in reading order; all internal links resolve.

## Final counts

- Chapters translated: 27 of 44 — ch00 (front matter), ch01-ch21 (Parts One-Three,
  through "Cast into Prison Together"), and ch39-ch43 (the five appendices).
- Chapters intentionally pending (skeleton pages): ch22-ch38 (Parts Four-Five), out
  of the commissioned scope.
- Footnotes: 89 total (translator's; the source carries none of its own — its four
  editorial endnotes, ch05[1]/ch08[2]/ch11[3][4], are rendered as the source's own
  notes). B09 added notes 75-89.
- Glossary rows: 438 people / 112 organizations / 100 places / 26 terms (676 total),
  one rendering per referent, statuses attested / provisional / decided.
- Figures: 49 placed across ch01-ch21 (reusing images in the range 00002-00052,
  with skips). The five appendices carry no images. Next free basename: 00053.
- Part poems: the five 临江仙 ci are folded as epigraphs at the head of each part's
  first chapter; three (Parts One-Three, ch01/ch05/ch13) are in scope and shipped.
  Parts Four-Five open at ch22/ch32 (out of scope), so their poems are not yet placed.
- Batches: B01-B09, all recorded in PROGRESS.md; source in scope ≈ 146,824 CJK chars.

## Open read-through flags (carried forward for the commissioner)

Faithfully-rendered source slips, all kept visible and footnoted (never silently
corrected):
- ch15: the 救国会 (National Salvation Association) founding YEAR — memoir 1931,
  scholarship 31 May 1936 (day/month right, year five years early).
- ch15: Father Rao / Jacquinot's arm — memoir "German shellfire in WWI"; in fact a
  1914 fireworks accident at Xujiahui.
- ch17: "Chairman Ho Chi Minh" met at Haiphong in 1939 — anachronistic (name/title
  and location do not fit the record).
- ch18: Chen Di as captain of the warship Zhongshan — unverified, on the memoir's
  authority alone.
- ch20: the "fourteen base areas" figure — non-canonical (the citable 1945 count is
  nineteen Liberated Areas).
- ch21: 周夔龙/Zhou Kuilong — almost certainly a slip for the attested 周伟龙/Zhou
  Weilong; and the Ye Ting-carried-wounded-Chiang anecdote — unverified.
- ch41 (new): the appendix gives Liu Shaowen's original name as 刘自章/Liu Zizhang;
  standard references attest 刘国章/Liu Guozhang (one-character difference).
- ch42 (new): the granddaughter's closing quotation cites "Professor Dena Gutman"
  (德纳·古特曼) of Stanford and a book "A New Culture, a New Stage" (Stanford UP,
  1997) — the author and title could not be traced in any catalog or scholarly
  record and appear spurious. Rendered as she quotes it, footnoted with the caveat.
- ch43 (new): the "Monument to the Nameless Heroes standing in Tiananmen Square" —
  the Tiananmen Square monument is the 人民英雄纪念碑 (Monument to the People's
  Heroes); the dedicated 无名英雄 monument is at Xishan, unveiled Dec 2013 (a decade
  after this 2003 text).

Minor discrepancies left as written and NOT footnoted (low stakes): ch40's CYL
entry dated 秋/autumn 1926 (scholarship: June 1926); 俞楼 credited to Zeng Guofan
(ch12); Chen Fu "propaganda head" vs secretary-general (ch07/08); Guan Xiangying
"deputy" vs full political commissar (ch10). The People's Daily citation behind
Appendix III (罗青长/柴成文, 10 Jun 1996) is plausible but was not independently
verifiable; treated as the appendix's own attribution.

Provisional renderings to upgrade if a source turns up (glossary flags them): 巴和
/"Baho" (ch11); 许宝/"Xu Bao" (ch14); the two 每日译报 English publisher names
(ch16); and the B09 one-off names flagged provisional — Li Lantian, Yang Shuhui,
Liu Zizhang (appendix form), Chen Hongxin, Ye Bingnan, Qian Lin, Hongshen, Liang
Yunfu, Tong Xingkan, Shen Yingying, and Dena Gutman (unverified). If any is fixed,
change glossary.json AND grep every built unit for the old form and rebuild.

## Things the commissioner should know

- Scope is partial BY INSTRUCTION. ch22-ch38 (Parts Four and Five: from "Reviving
  Tongyi" through "The Deep Bond of Kin," her post-1949 life, the Qincheng years,
  rehabilitation, and old age) are NOT translated and stand as skeleton pages. If
  those are ever commissioned, the machinery is ready: extend gen_bilingual_b02.py's
  DROP/POEM maps (Part Four opens at ch22, Part Five at ch32 — each needs its 临江仙
  folded in), reuse the checks and noise list, continue note numbering from 89, and
  keep to the single branch claude/huang-mulan. Batch target 21,000 source chars.
- The build is driven entirely by book.json. Reading text lives in out/<id>_reading.md
  (the correction surface); notes.json / glossary.json / figures.json / back_matter.json
  are the apparatus. data/src/, data/src_epub/, data/figs/manifest.json, out/*.epub and
  out/*_bilingual.md are gitignored and rebuild from source.epub (run
  scripts/ingest_epub.py source.epub, and pip install pillow for interior figures).
- Corrections workflow (CLAUDE.md): the commissioner files corrections in
  CORRECTIONS.md; global corrections cascade via a glossary/style change plus a
  grep-driven edit across ALL built units, then rebuild + full QA; each corrections
  pass appends a dated entry to CHANGELOG.md.
- The deliverable filename is exactly `out/The Autobiography of Huang Mulan.epub`
  (with spaces). It is presented in chat as an attached file, in addition to being
  committed.
