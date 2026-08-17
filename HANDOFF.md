# HANDOFF — Chen Yangshan: Hero of the Secret War (秘战英雄陈养山)

The baton. A fresh session reads this and starts immediately. It is the ARCHIVE
of the kickoff, not its delivery: every batch ends with the block below PASTED
VERBATIM INTO THE CHAT beside the attached EPUB.

Batch 7 (Chapter 5, ch05, PDF 172–204, printed 161–193) is COMPLETE: translated,
annotated, built, all gates green (parity 180=180, apparatus 0/0, content aligned,
entities 0, numbers 0, align OK, register within tolerance; qa_epub PASS, epubcheck
0/0/0). Chapter 5 is now COMPLETE. The block below is the Batch 8 kickoff, ready to
paste.

## Message to paste into the next chat

```
Chen Yangshan B08

Read, in order: CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. This is the survey-approved biography 秘战英雄陈养山 (Yao Huafei,
2018); modern SIMPLIFIED Chinese, horizontal, clean typeface. Source is
source.pdf (image-only); run ./setup.sh first. Offset: printed = pdf - 11
(constant). Chapter 1 is the FROZEN register reference
(check_register.py --ref out/ch01_reading.md). Chapters 1, 2, 3, 4 and 5 are done.

Do Batch 8 = Chapter 6 (ch06, all four sections), PDF 205-224, printed 194-213,
end to end per the CLAUDE.md pipeline:
  - NEW unit ch06 (its own out/ch06_reading.md + data/zh/ch06.txt), four "###"
    section headings with the English titles from book.json:
    1 = 一、司法部案，忍辱负重20年 (PDF 206; printed 195);
    2 = 二、宁夏十年，混乱年代显本色 (PDF 210; printed 199);
    3 = 三、彻底平反，终盼深山出太阳 (PDF 213; printed 202);
    4 = 四、发挥余热，鞠躬尽瘁为人民 (PDF 215; printed 204).
    Chapter 6 opens at PDF 205; the chapter-opener recto carries a photo above the
    heading -- SKIP it (per ch01-ch05). CHECK the top of PDF 206 and each section
    opener for lead paragraphs. Chapter 7 (Appendix I) opens at PDF 225. 20 pp.
  - ADD ch06 to data/check_config.json AND make a scoped data/check_config.ch06.json
    (copy the ch05 one). data/zh/*.txt are gitignored and gone on a fresh checkout;
    ch01-05 zh will NOT be present -- run the parity/number/content/align/entity
    checks with the ch06-scoped config; build/qa/epubcheck/register run on the whole
    cumulative EPUB; check_apparatus validates anchors against the whole notes.json.
  - BEFORE translating, read the final two pages of out/ch05_reading.md (the Li
    Kenong death close and the two 1961 letters) and STYLE.local.md. Chapter 6 is
    the persecution years: the 1958 "司法部反党集团" frame-up, twenty years of
    disgrace, ten years exiled in Ningxia through the Cultural Revolution, full
    rehabilitation, and the last working years. Chen Yangshan's plain, steady,
    uncomplaining voice; keep the author's indignation in the facts, not adjectives.
    The 1958 case and the Ningxia posting were SET UP at the end of Chapter 5
    (ch05 s4 anecdote four + note on the "anti-Party clique" case) -- cross-reference,
    do not re-explain from scratch.
  - render 205-224; OCR with the SAME crop as ch01-ch05 (do-not-revert list below):
    ocr_crop.py --lang chi_sim --psm 6 --left 0.045 --right 0.985 --top 0.08
    --running-head "秘战英雄陈养山", RECTO (PDF even) --bottom 0.945, VERSO (PDF odd)
    --bottom 0.915, run per-page so the parity-correct bottom applies. The per-page
    loop and ocr_dual exceed a 120s foreground timeout -- run them in the background
    or in page-range chunks; verify pgrep -c tesseract is 0 after.
  - WATCH THE SILENT OCR-LOSS (CONFIRMED every batch, incl. B07 p200: dropped
    "我贺龙" off a quoted line-end): tesseract drops an isolated paragraph-final SHORT
    line, AND a long single-paragraph tail can be dropped in the English on a first
    pass. VERIFY EVERY PAGE BOTTOM and every long paragraph's final sentences against
    the scan and restore them. data/zh is hand-assembled from corrected OCR + scans,
    one source paragraph per line. Keep portrait bio-boxes and photo captions OUT of
    data/zh (they are figure captions, into figures.json) so parity stays 1:1.
    Crop-verify EVERY name/number (verify_names.py --auto shows the dual-OCR
    disagreements; crop systematic mangles by eye).
  - eyeball EVERY page for figures; find_figures.py matches photographs but MISSES
    line art/calligraphy and flags the chapter-opener photo (SKIP it) - verify each
    by eye, crop clean images to data/figs/ (name p0NNN-f1.png; crop OUT the caption
    AND any bio-box text and wraparound body text -- portrait crops on this book
    routinely need y1 pulled up to exclude the caption line). Photo/portrait captions
    go in figures.json (translated; who's-who labels are the source's, caption prose
    is yours). FIGURE ALT MUST CONTAIN NO STRAIGHT DOUBLE QUOTES (they break
    alt="..." -> epubcheck fatal); use single/curly quotes. A figure `before` anchor
    must be a substring of the FIRST ~80 chars of its paragraph (the builder refuses
    a longer one).
  - Write English one paragraph per source line, mirror {v}/{p}/### /#### markers in
    BOTH data/zh/ch06.txt and out/ch06_reading.md. Set-off documents (letters,
    telegrams, quoted written accounts, verdicts) are {v} lines, one per source line
    incl. greeting/signature/date; verse/couplets are {p}. Use PLAIN ASCII in the
    reading file (straight quotes, literal em dash — ONLY for genuine interruption or
    a bracketed aside; the builder curls quotes and makes ... an ellipsis at render,
    but does NOT make em dashes from --). NO dashed-in appositive glosses. Consult
    authority.json + glossary.json before romanising; ONE rendering per referent
    (the whole ch01-05 cast is decided -- He Long, Chen Yangshan, Li Kenong, Zhou
    Enlai, Kang Sheng, Peng Zhen, Luo Ruiqing, etc.). PUT THE DECIDED FULL NAME ONCE
    PER PARAGRAPH the referent appears in (check_content is strict; pronouns/short
    forms carry the rest). Do NOT add a glossary row whose English collides with a
    common word (B07: 斗争 as the newspaper "Struggle" collided with 斗争 "struggle"
    everywhere -- footnote such a title instead of glossing it). Cite PRINTED folios
    in notes. Never invent bridging text; verify the final paragraphs.
  - Footnotes via apparatus_merge.py (glossary rows carry a "section" field; status
    must be attested/provisional/decided ONLY). HIGH NOTE DENSITY is a standing
    commissioner directive (STYLE.local.md): gloss every named person/place/
    institution/event/period-term a non-specialist might not know, at first
    appearance, each note saying more than the name. grep notes.json + out/ch0[1-5]_
    reading.md BEFORE re-noting a recurring subject (density TAPERS; Li Kenong, the
    Ministries of Public Security and Justice, the Central Investigation Department,
    the Cultural Revolution, the Gang of Four, the "anti-Party clique" case, Ningxia,
    Peng Zhen etc. are already noted). Fact-check the claims; verdict in the note.
  - verify_unit.py ch06, check_structure.py/check_content.py --config
    data/check_config.ch06.json, make_bilingual.py ch06 then qc_entities.py
    out/ch06_bilingual.md, check_numbers.py out/ch06_bilingual.md --noise
    data/noise.txt, check_align.py ch06, check_apparatus.py, check_register.py
    out/ch06_reading.md --ref out/ch01_reading.md. Build the cumulative EPUB,
    qa_epub.py green, epubcheck (/tmp/epubcheck-5.1.0/epubcheck.jar) 0/0.
  - Record everything in PROGRESS.md. Run to completion; do not pause for approval
    mid-batch.

Deliver the EPUB in chat AND paste the next kickoff verbatim in a fenced block.
All work on branch claude/chen-yangshan.
```

## What is DONE (do not redo)

- **Survey session:** full structure in book.json (6 chapters / 29 sections + 3
  appendices + references + afterword + series foreword); metadata; STYLE.md
  composed; skeleton EPUB.
- **B01 = Chapter 1** (ch01, PDF 12-37): 141 paragraphs, 73 footnotes. Voice-gate
  approved and FROZEN as the register reference.
- **B02 = Chapter 2, sections 1-3** (PDF 39-68). **B03 = Chapter 2, sections 4-5**
  (PDF 69-92): ch02 complete.
- **B04 = Chapter 3** (ch03, PDF 93-115): 125 paragraphs, 62 footnotes.
- **B05 = Chapter 4, sections 1-4** (PDF 117-146). **B06 = Chapter 4, sections 5-8**
  (PDF 147-171): ch04 complete (245 paras, 75 notes).
- **B07 = Chapter 5** (ch05, PDF 172-204, printed 161-193): 180 body paras (incl.
  23 `{v}` + 1 `{p}`), 47 footnotes (book-wide 387), 101 new glossary rows (677
  referents), 17 figures. The post-1949 years: the Xi'an takeover and first national
  public security conference; the Nanjing years and the Huang Kai interrogation (the
  Wu Hao forgery saga, told as a set-piece with two block-quoted 启事 and Qin Jie's
  written account); the deep Li Kenong friendship and the 1961 Shanghai materials
  trip; principle and frugality (seven "anecdotes" + the 13-point deathbed testament);
  two appended 1961 letters. All gates green; qa PASS; epubcheck 0/0/0.

## Tooling in place (DO NOT REVERT)

- **OCR crop** (measured for this book): `ocr_crop.py --lang chi_sim --psm 6
  --left 0.045 --right 0.985 --top 0.08 --running-head "秘战英雄陈养山"`, recto/
  verso split bottom: RECTO (PDF even) `--bottom 0.945`, VERSO (PDF odd)
  `--bottom 0.915`, run per-page in a loop (background it or chunk it). ocr_dual.py
  for the disagreement filter. indents.py/assemble.py UNUSED (data/zh is
  hand-assembled from corrected OCR + scans).
- `apparatus_merge.py`: glossary merges into SECTIONS via a `"section"` field on
  each row; `status` MUST be attested/provisional/decided. figures.json `file` is a
  BARE filename (p0NNN-f1.png); a figure `before` anchor must be a substring of the
  FIRST ~80 chars of its paragraph or the build refuses.
- `check_content` STRICT: the decided full glossary name must appear once in each
  paragraph the source names the referent (short forms/pronouns fail it). Do NOT
  glossary a title/word whose English collides with a common word (B07: dropped the
  `斗争` "Struggle" newspaper row; footnoted instead).
- `build_reading_epub.sec_nav`: the EPUB nav omits pending (untranslated) sections.
  Chapters 1-5 fully translated; ch06-ch11 stay pending.
- **data/zh gitignored, regeneration protocol.** `data/zh/*.txt` do NOT survive a
  fresh checkout. Run parity/number/content/align/entity with the UNIT-SCOPED config
  (`data/check_config.ch06.json`, copy the ch05 one); build/qa/epubcheck/register on
  the WHOLE cumulative EPUB; check_apparatus against the whole notes.json.
- **{v}/{p}/### /#### mirroring:** data/zh/<id>.txt and out/<id>_reading.md are
  hand-assembled STRUCTURALLY IDENTICAL line-for-line. Headings are skipped by the
  parity check; `{v}`/`{p}` prefixes are stripped before comparison.
- `data/noise.txt`: B07 added 8 rules (二三十年代, 20多岁, 四马路, 千头万绪, 百忙,
  百出, 一则/二则, 丁老二). All carried in English prose; none are quantities.
- setup.sh regression "hook stands down on template stub: FAIL" is BENIGN (the
  fixture expects a placeholder HANDOFF; ours is real). All translation checkers pass.

## Renderings settled B07 / carry-forward

- Decided NEW in B07 (feed to authority.json at completion): Huang Xueyu, Sun Miantian,
  Ding Lao'er, Yao Huanwen, Wang Jinxiang, Jiang Peng, Di Fei, Liu Yong, Chen Long,
  Xu Jianguo, Li Shiying, Zhou Xing, Luo Ruiqing, Chen Yi, Wu Kejian, Liang Guobin,
  Wang Fan, Yang Fan, Zhang Suzhen (Chen's wife), Hai Yu, Gan Lu, Ma Jingzheng, Huang
  Gengfu, Huang Kai, Yang Pao'an, Luo Qiyuan, Chen Hua, Deng Yanda, Qin Jie, Lian
  Chengyi, Zhang Chong, Wu Hao (=Zhou Enlai alias), Zhou Shaoshan (=Zhou Enlai alias),
  Xiang Zhongfa, Lu Futan, Tan Zhongyu, Chen Congying, Yang Xiuzhen, Zhou Huinian,
  Zhang Yuexia, Bo Gu (=Qin Bangxian), Zhang Wentian, Li Zhusheng, Tao Xingzhi, Shi
  Liangcai, Huang Mulan, Chen Zhigao, Ba He (provisional, French lawyer), Jiang Qing,
  Wang Yaqiao, Zhang Guotao, Tan Zhengwen, Pan Fang, Xu Qiang, Zhao Ying (Li Kenong's
  wife), Liang Hanbing, Nie Yuansu, Han Yangshan, Lü Ming (provisional), Li Bai (the
  radio martyr, NOT the poet), Kong Xiangxi (=H. H. Kung), Ke Qingshi, Li Delai, Qin
  Dong, Li Zheng, Mu Xin, Song Qingling, Chen Chang, Chen Kehan, Wang Shiying, Chen
  Jianyu, Zhao Hongfei, Yu Shengzhang, Wu Jusheng, Shi Liang, Yang Shangkun, An Ziwen,
  Tong Xiaopeng, Wang Ruofei, Ye Ting, Deng Fa, Zhang Dehan (provisional), Lei
  Rongtian (provisional), Yang Qiqing, Cai Shunli, Liu Fuzhi. Orgs/places/terms: the
  Ministry of Public Security, the Ministry of Justice, the Central Investigation
  Department, the Six Nations Hotel, the Metropole Hotel, the Shen Bao, the Xinwen
  Bao, the Awakening (觉悟), the Chinese Soviet Republic, the Comintern's Far Eastern
  Bureau, the State Political Security Bureau, the Longhua Martyrs' Cemetery, the
  Chinese Peasants' and Workers' Democratic Party, the Supreme People's Procuratorate,
  the Central Commission for Discipline Inspection, the North China Administrative
  Committee, the All-China Federation of Trade Unions, the Rescue Campaign, the
  Campaign to Suppress Counter-Revolutionaries, the Three-Antis, the War to Resist
  America and Aid Korea, Panmunjom, the Eighth National Congress. (斗争 "Struggle"
  deliberately NOT glossaried — footnoted only.)
- Source errors rendered as printed + footnoted (do NOT "fix"): 西安部门 misprint for
  公安 (printed 165); 堂兄 (×2) / 妻兄 (×1) for the same Huzhou relative (printed 189/190);
  事务所法 garbled law-office letterhead (printed 172).
- Crop-verified source oddities (NOT OCR): 一网打尽陈养山党中央机关 (printed 176);
  为寻陈养山出路 (printed 179) — the author over-inserts the subject's name.

## Voice sheets (consult at every dialogue scene)

- **Chen Yangshan** (subject). Earnest, modest, understated; plain and sincere,
  deflects credit. First-person report passages plain, no ornament. In the
  persecution chapter (ch06) keep him steady and uncomplaining; the indignation is
  the author's, carried in the facts.
- **Li Kenong** (Chen's intelligence chief; CENTRAL to Chapter 5). Senior, precise,
  warm to Chen; brief practical instructions; unassuming about himself ("what I know
  is still not enough"); the donkey-and-load saying ("The body doesn't matter. We're
  pack donkeys... carry what you can"). The chief who trusts his people and keeps the
  rules strictly himself.
- **He Long** (Chen's chief in the Jin-Sui chapter; reappears in ch05 s4 anecdote 1).
  Blunt, earthy, proud, short concrete declaratives; "In Shanghai in 1927 he saved my
  life — my, He Long's, life... Your looking down on him is looking down on me."
- **Zhou Enlai.** Measured, strategic, courteous; principled directives quietly.
- **Kang Sheng** (ch03 villain; ch05 the wrongful jailing of Xu Qiang). Cold,
  sinuous, dangerous; controlled, not cartoonish.
- **Chen Geng** (ch01-02). Warm, bold, decisive; a soldier's ease.

## Where the book stands

- Chapters 1-5 COMPLETE. Chapter 5 closes the "up" arc: Chen at the height of his
  service (public security chief in Xi'an, Shanghai, Nanjing; North China; the
  Ministry of Justice), the Li Kenong friendship, and his frugal integrity. It plants
  the 1958 "司法部反党集团" case and the Ningxia posting that Chapter 6 (the "down"
  arc: persecution and rehabilitation) will tell in full.
- B08 = Chapter 6 "A Loyal Heart Revealed in a Time of Injustice."

## What is NEXT

- B08 = Chapter 6 (ch06, PDF 205-224, printed 194-213, four sections). NEW unit.
  Add ch06 to both check configs. B09 = front + back matter (foreword + appendices
  I-III + references); B10 = afterword + whole-book close (reconcile, cover, term
  ledger, deep audit, COMPLETION.md, commit final EPUB).

## Open traps / environment state

- Offset printed = pdf - 11 (constant). Front matter runs a SECOND folio sequence.
  Chapter-opener rectos carry a photo above the heading (SKIP it). PDF p243 is an
  Anna's Archive metadata leaf.
- OMP_THREAD_LIMIT=1 for tesseract; kill the process GROUP; pgrep -c tesseract=0.
  The per-page ocr loop and ocr_dual.py exceed a 120s foreground timeout on a full
  chapter -- background them or chunk the range.
- Reading files are PLAIN ASCII (straight quotes, literal em dash only for real
  interruption or a bracketed aside; NO dashed appositive glosses). Note bodies:
  numeric character references only (&#8211; &#8212; &#160; &#8220; &#8221;), never
  named entities; <i> is allowed. Note ANCHORS must be verbatim ASCII substrings of
  the reading file (straight quotes, not &quot;).
- check_content is STRICT (full name once per paragraph). Do not glossary a
  title/word whose English form collides with a common word.
- A long single paragraph's TAIL, and an isolated short final line at a page bottom,
  can be silently dropped by OCR (B05, B06, B07). Verify against the scan.
- Figure alt: NO straight double quotes. figures.json `file` is a BARE filename; the
  `before` anchor must be within the first ~80 chars of its paragraph. Crop OUT
  captions AND bio-box text (portrait crops routinely need y1 pulled up). find_figures
  MISSES line art/calligraphy.
- epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup if the
  container is fresh).
