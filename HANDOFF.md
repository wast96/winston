# HANDOFF — The Autobiography of Huang Mulan

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Huang Mulan B06 — ch15-ch16 (Ch 15. Resistance and National Salvation; Ch 16. Struggle on the Solitary Island). No part poem in this batch (Part Three runs ch13-ch21).

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then book.json, then HANDOFF.md. We are translating The Autobiography of Huang Mulan (黄慕兰自传) into an annotated English EPUB per CLAUDE.md. Work only on branch claude/huang-mulan; build the deliverable at out/The Autobiography of Huang Mulan.epub and present it in chat as an attached file.

Scope reminder (approved): translate ONLY the front matter (ch00), chapters 1-21 (ch01-ch21), and the appendices (ch39-ch43). Chapters 22-38 are out of scope and MUST stay as pending skeleton pages; do not translate or delete them. Batch target is 21,000 source chars max.

B01 (ch00-ch03), B02 (ch04-ch06), B03 (ch07-ch09), B04 (ch10-ch11) and B05 (ch12-ch14) are DONE and committed (see PROGRESS.md). Do Batch B06 = ch15-ch16 (Ch 15. Resistance and National Salvation; Ch 16. Struggle on the Solitary Island), end to end:
1. Regenerate the extracted source if data/src/ is absent (it is gitignored): run scripts/ingest_epub.py source.epub. Read the batch's source from data/src/ (ch15=22_index-split-020.txt, ch16=23_index-split-021.txt). Translate to the register in CLAUDE.md, faithfully and in full. Quote the source VERBATIM in the bilingual QC file: write out/<id>_en.txt (one English paragraph per line, first line = English chapter title), then reuse scripts/gen_bilingual_b02.py (add ch15/ch16 to its DROP map with the 1-indexed NON-EMPTY line numbers of the header + title + any caption-only lines). It interleaves verbatim source with your English and asserts paragraph parity. Never invent bridging text; if a passage is genuinely ambiguous or the source is cut, footnote it and leave it visible. (B03's parity check caught an invented recap paragraph in ch09 this way -- trust the check.)
2. NO part poem in B06 (Part Three's 临江仙 was already folded into ch13 in B05). Parts remaining: Part Four opens at ch22 and Part Five at ch32, both OUT of scope.
3. Watch for spliced-in image captions (a caption, sometimes an inscription + 说明, dropped mid-paragraph): rejoin the narrative from its verbatim halves, route the photo to figures.json, and put any inscription/说明 in a footnote. Caption-only lines go to figures.json, not the reading text. Cross-check images per chapter with `grep -o 'images/[0-9]*\.jpg' data/src_epub/index_split_0NN.html`; basenames map to data/figs/. ch15 (index_split_020) carries images 00037-00041; ch16 (index_split_021) carries 00042-00044. (B05 used 00022-00030 and 00032-00036; the Part-Three divider image 00031 was uncaptioned and skipped.)
4. Author out/<id>_bilingual.md per unit (source blockquote line tagged "> ", English beneath; chapter title tagged "## H2 <English title>"). Generate reading + parity with scripts/split_bilingual.py, then run scripts/check_numbers.py out/<id>_bilingual.md --noise data/noise.txt and scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md until both are clean. Extend data/noise.txt (source-side name/idiom numerals) and, if a spelled ordinal is missed, WORD_NUM in check_numbers.py, when a flag is a non-quantity; carry every real quantity. NB from B05: the target-side check only counts "a hundred"/"a thousand"/"one thousand"/"N thousand" -- if you write "the hundred days"/"the thousand dollars" the number reads as dropped, so write "a hundred"/"the one thousand". "108" as digits reads as 108; "One Hundred and Eight" reads as 100+8. check_numbers strips thousands separators, so write big numbers with commas as normal.
5. Blind double-translation and back-translation on the argumentative/literary passages (use subagents in fresh context); fact-check names/dates/events against real scholarship (Wikipedia, Baidu Baike, academic sources; never Grok/Grokipedia or any AI-written source). Say corroborated / uncorroborated / contradicted in PROGRESS.md.
6. Add ~3 footnotes per chapter-equivalent to notes.json (keyed by unit id; XHTML bodies with NUMERIC character references; anchors must be verbatim substrings of the English reading prose -- mind that anchors spanning a straight quote need the exact "...,"" punctuation; recurring subjects get their note at FIRST appearance in the book). Extend glossary.json (one rendering per referent; reuse ALL prior decisions -- Kuomintang, Sun Yat-sen, Chiang Kai-shek, Whampoa, Zhou Enlai, Chen Duxiu, He Chang, Chen Tanqiu, Rao Shushi, Guan Xiangying, Pan Hannian, Chen Geng, Chen Zhigao, Chen Qishou/Jieqing, Xiang Zhongfa, Gu Shunzhang, Kang Sheng, Dong Zhujun, Liu Bochui, Lin Gengbai, Shen Junru, Liu Yazi, He Xiangning, Song Qingling, A Ying, Xu Jiqing, the Tongyi Company, the Southern Society, the author's name rows 黄彰定/慕兰/定慧, etc.). Place any images via figures.json (reuse images already in data/figs/).
7. Rebuild with scripts/build_reading_epub.py "out/The Autobiography of Huang Mulan.epub" (TOC stays fully linked; ch22-38 remain pending), run scripts/qa_epub.py until green.
8. Commit, present the EPUB to me directly as an attached file in this chat (not a git link), update PROGRESS.md, and rewrite HANDOFF.md whose first section is the ready-to-paste kickoff message for the NEXT batch (B07 = ch17-ch19), beginning with the label line "Huang Mulan B07".

Cite chapters and sections, never page numbers. Do not pause for approval mid-batch; run the whole batch and report back when it is built and QA-green, and paste the B07 kickoff message at the end of your reply.
```

Every batch kickoff message (here and in every future HANDOFF) MUST begin with a
label line "Huang Mulan B<nn>" naming the batch and its chapter scope, then a
blank line, then the standard "Read CLAUDE.md in full..." instructions.

## What is DONE (do not redo)

- Step 0 (ingest + survey): source ingested (53 spine docs, 105 images,
  254,900 chars). book.json is the logical structure; skeleton EPUB with a fully
  hyperlinked TOC; metadata wired for Kindle/Apple Books; qa_epub PASS.
- B01 = ch00-ch03. 19,695 source chars. Part One 临江仙 folded into ch01. 11
  footnotes. All checks green. See PROGRESS.md.
- B02 = ch04-ch06. 19,567 source chars. Part Two 临江仙 folded into ch05. 9
  footnotes (20 total), incl. the source's OWN endnote in ch05 (Wan Xiyan death
  discrepancy). ~37 glossary rows, 5 figures. All checks green.
- B03 = ch07-ch09. 18,809 source chars. No part poem. 10 footnotes (30 total),
  incl. the source's OWN endnote in ch08. ~57 glossary rows, 3 figures. ch09
  title corrected to "Head of the Rescue Department". All checks green.
- B04 = ch10-ch11. 11,004 source chars. No part poem, NO images. 9 footnotes (39
  total), incl. the source's OWN TWO endnotes in ch11. ~47 glossary rows. Blind
  double-translation + back-translation + fact-check done. Build + qa_epub PASS.
- B05 = ch12-ch14 (In Seclusion by West Lake; The Voice of Justice; The Tongyi
  Company). 18,752 source chars. Part Three 临江仙 (抗日救亡) folded into ch13.
  ch12 IS index_split_016.html, whose trailing 【注释】 block (the ch05/ch08/ch11
  endnotes) was DROPPED, not translated as ch12 body. 10 footnotes (49 total; ch12
  40-43, ch13 44-46, ch14 47-49). ~112 glossary rows added (totals 219 people / 47
  orgs / 38 places / 12 terms). 14 figures (ch12 00022-00030, ch13 00032-00036; the
  uncaptioned Part-Three divider image 00031 skipped; ch14 none). Blind
  double-translation + back-translation + fact-check done (俞楼/Zeng-Guofan funding
  CONTRADICTED and footnoted; He Chang rank/death, 郑毓秀, 高志航, 七君子, Tongyi
  resumption all corroborated; the A Ying manuscript-custody claim flagged as the
  author's own testimony). Build + qa_epub PASS (89 files, 15 of 44 chapters,
  322 paragraphs). Committed.

## What is NEXT

- B06 = ch15-ch16 (see kickoff above; no part poem). Then B07 ch17-ch19, B08
  ch20-ch21, B09 ch39-ch43 (appendices). See book.json "batches".

## Reusable machinery (saves time)

- scripts/gen_bilingual_b02.py IS the bilingual generator: a DROP map of
  {unit: (src_file, {1-indexed NON-EMPTY lines to drop = header, title,
  captions})}, plus a POEM map for part-opening chapters. IMPORTANT: the DROP
  indices are 1-indexed over the file's NON-EMPTY lines (blank lines skipped) --
  enumerate with `python3 -c "print([l for l in open(f) if l.strip()])"` for true
  indices. B05 added ch12 (drop header+title+9 captions+the 5 trailing 注释 lines),
  ch13 (header+title+5 captions; POEM keeps [3,4,5] of 19_index-split-017.txt), and
  ch14 (header+title only, no images).
- Finding caption line numbers: caption-only lines in data/src are image captions
  (person-bio lines like "柳亚子（1887~1958），...", 原图片说明 lines, 右起/左起… name
  rosters, or a standalone photo caption). A two-line caption (title line + a
  左起/前排 roster line) is ONE image: drop both, fold the roster into the figure
  caption. Cross-check images per chapter with
  `grep -o 'images/[0-9]*\.jpg' data/src_epub/index_split_0NN.html`; basenames map
  straight to data/figs/. Used so far: B01 00002-00012, B02 00013-00018, B03
  00019-00021, B04 none, B05 00022-00030 + 00032-00036 (00031 skipped).
- The SOURCE'S OWN endnotes: some chapters carry a bracketed [n] linking (via a
  filepos anchor) to a 【注释】 block that lives in index_split_016.html = ch12.
  ALL FOUR are now handled and rendered as the source's own notes: ch05 [1] (Wan
  Xiyan), ch08 [2] (Wan Xixian), ch11 [3]/[4] (伍豪启事 quote). The 注释 block itself
  (ch12 source lines 45-49) is DROPPED from ch12 body. No in-scope chapter after
  ch12 is expected to carry a source endnote, but grep each unit's HTML for
  `<sup`/`filepos` to be sure.
- data/noise.txt strips this book's recurring non-quantity numerals. B05 added
  陈振九 (name), 千千 (千千万万 residue after the generic 万万 strip -> 2000), 六军
  (imperial-army set term), 四川 (北四川路), 五金 (五金公司 hardware). check_numbers.py
  strips thousands separators (_decomma), so write grouped figures with commas.
- check_numbers target-side gotchas (learned in B05): it counts "a hundred" /
  "a thousand" / "one thousand" / "N thousand" / "N hundred" / teens+"hundred" /
  "ten thousand" / "N million" -- but NOT a bare "the hundred"/"the thousand". If
  a real quantity trips this, reword to "a hundred"/"one thousand", or (for a set
  number like 一百零八) write the digits "108". Only add to noise when the numeral
  is genuinely NOT a quantity.

## Open items / read-through flags

- book.json author_note still calls Huang Dinghui the "birth name"; the source and
  scholarship make 黄彰定 (Zhangding) the birth/school name, 慕兰 the 1926 name,
  定慧 a 1932 name (per ch12). Translation and glossary are correct; the metadata
  line is worth tidying in a later pass (does not affect the reading text).
- Allusive/subject titles still to footnote when reached: 面谒周公 (ch20, 周公 =
  Zhou Enlai; the 周公/Lord Zhou honorific is footnoted at its first appearance in
  ch11, cross-referenced forward to the ch20 title).
- Faithfully-rendered source slips kept visible (not silently corrected): the
  memoir calls Chen Fu the Northern Bureau "propaganda head" (scholarship:
  secretary-general); Tan Yankai's headship of the Yuelu Academy is unverified;
  the memoir calls Guan Xiangying "deputy political commissar of the Second Front
  Red Army" (he was the FULL commissar). 俞楼's construction is credited to Zeng
  Guofan's money (scholarship: student subscription + Peng Yulin; Zeng died 1872) --
  footnoted in ch12. All left as the author wrote them.
- 民社党 (ch14): the memoir's abbreviation for what, in the mid-1930s, was the China
  National Socialist Party (国家社会党) of Zhang Junmai / Zhang Dongsun; the two
  merged into the Democratic Socialist Party (民社党) only in 1946. Rendered
  "National Socialist Party" (glossary keyed 民社党, with the naming explained).
- 巴和 (the French lawyer, ch11): rendered "Baho" (provisional); French original
  unverified. If a source turns up the real name, update the glossary AND grep every
  built unit for "Baho" and rebuild.
- 许宝 (ch14): the source gives the nephew's name as just 许宝 (Xu Bao); it may be
  truncated. Rendered "Xu Bao", flagged provisional in the glossary.

## State / traps

- Scope is PARTIAL by instruction: ch00, ch01-ch21, ch39-ch43 only. ch22-ch38
  stay as pending skeleton pages (the build handles this; do not delete them).
- Part poems: Part One at ch01, Part Two at ch05, Part Three at ch13 (all DONE).
  Part Four opens at ch22 and Part Five at ch32, both out of scope.
- Note anchors go in BEFORE markup substitution (the builder inserts them and
  REFUSES on an unmatched anchor). XHTML note bodies use NUMERIC character
  references, never named entities. Numbering is continuous and builder-assigned
  in reading order (49 notes through ch14; ch12 = 40-43, ch13 = 44-46, ch14 = 47-49).
- Figure "before" anchors must be a substring within the FIRST 80 characters of a
  paragraph line, or the builder silently skips the figure. A two-line photo caption
  (title + roster) is ONE figure. Verify placement by grepping the built .xhtml for
  the image basename.
- Deliverable filename is exactly out/The Autobiography of Huang Mulan.epub (with
  spaces). data/src/, data/src_epub/, data/figs/, out/*.epub are gitignored and
  rebuild from source.epub; commit the JSON, the reading/bilingual/en md, the
  generator + check scripts, PROGRESS/HANDOFF, data/zh, data/noise.txt.
- Work on ONE branch: claude/huang-mulan (per CLAUDE.md rule 2). If a session starts
  you on a stray branch, consolidate onto the working branch and delete the stray
  (local + remote). Pillow needed for interior figures (pip install pillow on a fresh
  container) -- B05 had 14 figures, so it was installed.
