# HANDOFF — The Autobiography of Huang Mulan

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Huang Mulan B08 — ch20-ch21 (Ch 20. An Audience with Zhou Enlai; Ch 21. Cast into Prison Together). No part poem in this batch (Part Three runs ch13-ch21; Part Four opens at ch22, out of scope).

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then book.json, then HANDOFF.md. We are translating The Autobiography of Huang Mulan (黄慕兰自传) into an annotated English EPUB per CLAUDE.md. Work only on branch claude/huang-mulan; build the deliverable at out/The Autobiography of Huang Mulan.epub and present it in chat as an attached file.

Scope reminder (approved): translate ONLY the front matter (ch00), chapters 1-21 (ch01-ch21), and the appendices (ch39-ch43). Chapters 22-38 are out of scope and MUST stay as pending skeleton pages; do not translate or delete them. Batch target is 21,000 source chars max.

B01 (ch00-ch03), B02 (ch04-ch06), B03 (ch07-ch09), B04 (ch10-ch11), B05 (ch12-ch14), B06 (ch15-ch16) and B07 (ch17-ch19) are DONE and committed (see PROGRESS.md). Do Batch B08 = ch20-ch21 (Ch 20. An Audience with Zhou Enlai; Ch 21. Cast into Prison Together), end to end:
1. Regenerate the extracted source if data/src/ is absent (it is gitignored): run scripts/ingest_epub.py source.epub, and pip install pillow if figures are placed. Read the batch's source from data/src/ (ch20=27_index-split-025.txt, ch21=28_index-split-026.txt). Translate to the register in CLAUDE.md, faithfully and in full. Quote the source VERBATIM in the bilingual QC file: write out/<id>_en.txt (one English paragraph per line, first line = English chapter title), then reuse scripts/gen_bilingual_b02.py (add ch20/ch21 to its DROP map with the 1-indexed NON-EMPTY line numbers of the header + title + any caption-only/inscription/roster lines). It interleaves verbatim source with your English and asserts paragraph parity. Enumerate non-empty lines with `python3 -c "lines=[l for l in open(f) if l.strip()]; [print(i,l[:60]) for i,l in enumerate(lines,1)]"`. Never invent bridging text; if a passage is genuinely ambiguous or the source is cut, footnote it and leave it visible.
2. NO part poem in B08. Part Four opens at ch22 and Part Five at ch32, both OUT of scope.
3. Watch for spliced-in image captions (a caption, sometimes an inscription + 说明, dropped mid-paragraph): rejoin the narrative from its verbatim halves, route the photo to figures.json, and put any inscription/说明 in a footnote. Caption-only lines and roster lines (左起/前排…) go to figures.json, not the reading text. Cross-check images per chapter with `grep -o 'images/[0-9]*\.jpg' data/src_epub/index_split_0NN.html`; basenames map to data/figs/. ch20 = index_split_025, ch21 = index_split_026. Next free figure basename after B07 is 00051 (B07 used 00045-00050); verify per chapter with the grep.
4. Author out/<id>_bilingual.md per unit (source blockquote line tagged "> ", English beneath; chapter title tagged "## H2 <English title>"). Generate reading + parity with scripts/split_bilingual.py, then run scripts/check_numbers.py out/<id>_bilingual.md --noise data/noise.txt and scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md until both are clean. Extend data/noise.txt (source-side name/idiom numerals) and, if a spelled ordinal is missed, WORD_NUM in check_numbers.py, when a flag is a non-quantity; carry every real quantity. NB: check_numbers' spelled_numbers DOES count cardinal tens and tens-ones ("forty-five"->45, "fifty"->50, "twenty"->20, "over fifty"->50), so those spell out naturally; only tens-ones ORDINALS ("twenty-ninth","forty-fifth") and day-ordinals (21st/22nd/25th) need digits. It strips thousands separators, so write big numbers with commas as normal. Note 面谒周公 (ch20 title, 周公 = Zhou Enlai): the 周公/Lord Zhou honorific is already footnoted at ch11; footnote or cross-reference the ch20 title.
5. Blind double-translation and back-translation on the argumentative/literary passages (use subagents in fresh context); fact-check names/dates/events against real scholarship (Wikipedia, Baidu Baike, academic sources; never Grok/Grokipedia or any AI-written source). Say corroborated / uncorroborated / contradicted in PROGRESS.md.
6. Add ~3 footnotes per chapter-equivalent to notes.json (keyed by unit id; XHTML bodies with NUMERIC character references; anchors must be verbatim substrings of the English reading prose -- mind that anchors spanning a straight/curly quote need the exact punctuation; recurring subjects get their note at FIRST appearance in the book). Extend glossary.json (one rendering per referent; reuse ALL prior decisions -- Kuomintang, Sun Yat-sen, Chiang Kai-shek, Zhou Enlai, He Xiangning, Song Qingling, Liu Shaowen, Pan Hannian, Chen Zhigao, A Ying, Chen Ce/Chan Chak, Deng Xianyu, Gu Jiatang, the Central Relief Commission, the East River guerrillas, Qujiang/Shaoguan, the Tuesday Dining Club, the author's name rows 黄彰定/慕兰/定慧, etc.). Place any images via figures.json (reuse images already in data/figs/).
7. Rebuild with scripts/build_reading_epub.py "out/The Autobiography of Huang Mulan.epub" (TOC stays fully linked; ch22-38 remain pending), run scripts/qa_epub.py until green.
8. Commit, present the EPUB to me directly as an attached file in this chat (not a git link), update PROGRESS.md, and rewrite HANDOFF.md whose first section is the ready-to-paste kickoff message for the NEXT batch (B09 = ch39-ch43, the appendices -- the LAST batch), beginning with the label line "Huang Mulan B09".

Cite chapters and sections, never page numbers. Do not pause for approval mid-batch; run the whole batch and report back when it is built and QA-green, and paste the B09 kickoff message at the end of your reply.
```

Every batch kickoff message (here and in every future HANDOFF) MUST begin with a
label line "Huang Mulan B<nn>" naming the batch and its chapter scope, then a
blank line, then the standard "Read CLAUDE.md in full..." instructions.

## What is DONE (do not redo)

- Step 0 (ingest + survey): source ingested (53 spine docs, 105 images,
  254,900 chars). book.json is the logical structure; skeleton EPUB with a fully
  hyperlinked TOC; metadata wired for Kindle/Apple Books; qa_epub PASS.
- B01 = ch00-ch03. 19,695 source chars. Part One 临江仙 folded into ch01. 11
  footnotes. All checks green.
- B02 = ch04-ch06. 19,567 source chars. Part Two 临江仙 folded into ch05. 9
  footnotes (20 total), incl. the source's OWN endnote in ch05. All green.
- B03 = ch07-ch09. 18,809 source chars. No part poem. 10 footnotes (30 total),
  incl. the source's OWN endnote in ch08. All green.
- B04 = ch10-ch11. 11,004 source chars. No part poem, NO images. 9 footnotes (39
  total), incl. the source's OWN TWO endnotes in ch11. All green.
- B05 = ch12-ch14. 18,752 source chars. Part Three 临江仙 folded into ch13. ch12's
  trailing 【注释】 block DROPPED. 10 footnotes (49 total). 14 figures (00022-00030,
  00032-00036; 00031 skipped). All green.
- B06 = ch15-ch16. 17,874 source chars. No part poem. 7 footnotes (56 total; ch15
  50-53, ch16 54-56). 8 figures (00037-00044). The 救国会 founding YEAR is wrong in
  the memoir (says 1931; scholarship 1936) -- footnoted; Father Rao's arm lost in a
  1914 accident not WWI shellfire -- footnoted. All green.
- B07 = ch17-ch19 (Moving to Hong Kong; Thirty Days a Refugee; A Righteous Rescue
  of the Worthies). 16,085 source chars. No part poem. 10 footnotes (66 total; ch17
  57-59, ch18 60-62, ch19 63-66). 115 glossary rows added (totals 395 people / 100
  orgs / 83 places / 18 terms). 6 figures (00045-00049 ch17, 00050 ch19; ch18 has
  none). Blind back-translation + fact-check done: fixed a 3-vs-2-person referent
  slip (国母孙夫人和廖夫人 = Madame Sun the Mother of the Nation, and Madame Liao);
  the memoir's "Chairman Ho Chi Minh met at Haiphong in 1939" is anachronistic
  (name/title c.1940-45, he was inland in Guangxi/Yunnan) -- footnoted; Chen Di as
  captain of the warship Zhongshan is unverified in scholarship -- footnoted; all
  other names/dates/events corroborated (China Defence League 14 Jun 1938, Chan
  Chak's escape, Yang Huimin's flag-swim, the Great Rescue ~800, Lin Gengbai d.
  19 Dec 1941 aged 45, Qu Yingguang). Build + qa_epub PASS (103 files, 20 of 44
  chapters, 413 paragraphs). Committed.

## What is NEXT

- B08 = ch20-ch21 (see kickoff above; no part poem). Then B09 = ch39-ch43
  (appendices) is the LAST batch. See book.json "batches".

## Reusable machinery (saves time)

- scripts/gen_bilingual_b02.py IS the bilingual generator: a DROP map of
  {unit: (src_file, {1-indexed NON-EMPTY lines to drop = header, title,
  captions, rosters, inscriptions})}, plus a POEM map for part-opening chapters.
  The DROP indices are 1-indexed over the file's NON-EMPTY lines (blank lines
  skipped) -- enumerate with
  `python3 -c "lines=[l for l in open(f) if l.strip()]; [print(i,l[:50]) for i,l in enumerate(lines,1)]"`.
  B07 added ch17 (drop 1,2,8,14,19,21,22,25), ch18 (drop 1,2 -- no images), ch19
  (drop 1,2,4,5). B08 has no part poem, so POEM is untouched.
- Finding caption/inscription line numbers: caption-only lines in data/src are
  image captions (photo-caption lines, 原图片说明/封面照片说明 lines, 左起/前排/后排…
  rosters, person-bio lines) or an author's inscription (X为此照题诗云…). A two-line
  photo (title + roster) is ONE image: drop both, fold the roster into the figure
  caption. An inscription goes to a FOOTNOTE, not figures.json. Some source captions
  are MIRROR-REVERSED (printed backwards, e.g. ch15/31) -- decode before translating.
  Cross-check per chapter with `grep -o 'images/[0-9]*\.jpg' data/src_epub/index_split_0NN.html`;
  basenames map straight to data/figs/. Verify placement by grepping the built .xhtml
  for the image basename (the builder silently skips a figure whose "before" anchor is
  not within the FIRST ~80 chars of a reading paragraph -- so prefer an anchor from the
  START of the paragraph, ideally with no apostrophe). Used so far: B01 00002-00012,
  B02 00013-00018, B03 00019-00021, B04 none, B05 00022-00030 + 00032-00036 (00031
  skipped), B06 00037-00044, B07 00045-00050. Next free: 00051.
- The SOURCE'S OWN endnotes: all four (ch05 [1], ch08 [2], ch11 [3]/[4]) are handled
  and live in ch12's DROPPED 【注释】 block. No in-scope chapter after ch12 has been
  found to carry a source endnote (ch15-ch19 checked: only the chapter-title
  `<h2 id="filepos...">`), but grep each unit's HTML for `<sup`/`filepos` to be sure.
- data/noise.txt strips this book's recurring non-quantity numerals. B07 added 九龙/
  九龍, 满七/滿七, 四邻/四鄰, 千恩万谢/千恩萬謝, 四行, 文六, 万国/萬國. check_numbers.py
  NOISE line 78 was widened from [幾几] to [幾几數数] so 数百万/数千万 strip WHOLE
  (else 数百 is eaten and a stray 万 reads as 10000). Longest-literal-first; do NOT
  re-sort the NOISE list.
- check_numbers target-side facts (verified by reading the script): spelled_numbers
  DOES count cardinal tens ("fifty"->50) and cardinal tens-ones ("forty-five"->45),
  and "over/past <tens>" ("over fifty"->50), and "a hundred"/"a thousand"/"one
  thousand"/"N thousand"/"N hundred"/teens+"hundred"/"ten thousand"/"N million". It
  does NOT count tens-ones ORDINALS ("twenty-ninth","forty-fifth" give only the tens)
  or plural tens ("sixties"/"seventies" -- use the singular "sixty or seventy" to
  register 60/70), nor teen+thousand ("fifteen thousand" gives only 15). For those,
  and for day-ordinals (21st/22nd/25th), write the digits. _decomma strips thousands
  separators, so write grouped figures with commas.

## Open items / read-through flags

- book.json author_note still calls Huang Dinghui the "birth name"; the source and
  scholarship make 黄彰定 (Zhangding) the birth/school name, 慕兰 the 1926 name,
  定慧 a 1932 name (per ch12). Translation and glossary are correct; the metadata
  line is worth tidying in a later pass (does not affect the reading text).
- The ch20 title 面谒周公 (周公 = Zhou Enlai): the 周公/Lord Zhou honorific is
  footnoted at its first appearance in ch11; footnote or cross-reference the ch20
  title when reached.
- Faithfully-rendered source slips kept visible (not silently corrected): the 救国会
  founding YEAR (memoir 1931, scholarship 1936; ch15, footnoted); Father Rao's arm
  lost in a 1914 accident not WWI (ch15, footnoted); the memoir's "Chairman Ho Chi
  Minh"/Haiphong 1939 meeting (ch17, footnoted as anachronistic); Chen Di as captain
  of the Zhongshan (ch18, footnoted as unverified); 俞楼's construction credited to
  Zeng Guofan (ch12); Chen Fu "propaganda head" vs secretary-general; Guan Xiangying
  "deputy" vs full political commissar. All left as the author wrote.
- Provisional renderings to upgrade if a source turns up: 巴和/"Baho" (ch11); 许宝/
  "Xu Bao" (ch14); the two 每日译报 publishers "Fees" and "Bonner" (孙特士·斐士/拿门·
  鲍纳, ch16, English names unverified); 张曼怡/"Zhang Manyi" (ch16); and B07's minor
  one-off names flagged "provisional" in glossary.json (梅总领事/consul-general Mei
  was rendered descriptively; Li Zhifu, Pan Xiao'e, Qin Liankui, Zhang Duhe, Xu
  Caichen, Shi Weici, Zhu Wenyang, Li Tongcun, Zhao Letian, Luo Jianbing, Gao Boshi,
  Zhang Haoran, Zhao Tianmin, Chen Erxin, Huang Cheng). If any is fixed, update
  glossary.json AND grep every built unit for the old form and rebuild.

## State / traps

- Scope is PARTIAL by instruction: ch00, ch01-ch21, ch39-ch43 only. ch22-ch38
  stay as pending skeleton pages (the build handles this; do not delete them).
- Part poems: Part One at ch01, Part Two at ch05, Part Three at ch13 (all DONE).
  Part Four opens at ch22 and Part Five at ch32, both out of scope.
- Note anchors go in BEFORE markup substitution (the builder inserts them and
  REFUSES on an unmatched anchor). XHTML note bodies use NUMERIC character
  references, never named entities. Numbering is continuous and builder-assigned
  in reading order (66 notes through ch19; ch17 = 57-59, ch18 = 60-62, ch19 = 63-66).
- Figure "before" anchors must be a substring within the FIRST ~80 characters of a
  paragraph line, or the builder silently skips the figure. Prefer an anchor from the
  paragraph start with no apostrophe. A two-line photo caption (title + roster) is ONE
  figure. Verify placement by grepping the built .xhtml for the image basename.
- Deliverable filename is exactly out/The Autobiography of Huang Mulan.epub (with
  spaces). data/src/, data/src_epub/, data/figs/, out/*.epub are gitignored and
  rebuild from source.epub; commit the JSON, the reading/bilingual/en md, the
  generator + check scripts, PROGRESS/HANDOFF, data/zh, data/noise.txt.
- Work on ONE branch: claude/huang-mulan (per CLAUDE.md rule 2). If a session starts
  you on a stray per-session branch, consolidate onto claude/huang-mulan and delete
  the stray (local + remote). B07 did exactly this. Pillow is needed for interior
  figures (pip install pillow on a fresh container).
