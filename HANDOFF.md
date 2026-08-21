# HANDOFF: The Sword Roars in the West Wind

## Message to paste into the next chat

> Paste this VERBATIM to start the next batch. It is the only bridge between
> conversations; HANDOFF/PROGRESS/book.json describe the state, but the pages
> are the voice, so read the last two pages of ch12's English (and ch01, the
> frozen register reference) before drafting ch13.

```
Sword Roars B15 Chapter Thirteen

Read CLAUDE.md, then HANDOFF.md, then book.json, then STYLE.md and
STYLE.local.md. In STYLE.local.md the top section "THE REGISTER REBASELINE
(B09 commissioner review)" and the "Footnote apparatus" and "Apparatus policy"
sections are the frozen reference for all further work. Work on branch
claude/the-sword-roars (the canonical book branch; if the harness starts you on
a stray per-task branch, consolidate per CLAUDE.md rule 2 and delete the stray,
local and remote). Run ./setup.sh first.

STATE: B14 is done. Chapter Twelve ("A Purge in the Red-Light District," ch12, PDF
264-283, printed 249-268, 139 paragraphs, 7 sections) is drafted end to end against
the frozen doc: hand-transcribed off the 300-DPI images (OCR too noisy on the names),
rendered in ch08-ch11's sardonic source-criticism register — Ma Shaowu's killing at the
Little Garden, Ding Ling's abduction and the "License Plate 1469" (the author sets
Smedley's and Ding Ling's partisan memoirs against the contemporary press and finds them
wrong on points), the Xiong Guohua traitor case and the Renji Hospital hit, the taking of
the crack shot Kuang Hui'an, and the martyr set-piece of the four Red Squad men garrotted
at Nanjing in 1935. 15 footnotes (book total 366), 2 hand-cropped figures, 75 new glossary
rows, ch12 added to data/content_config.json. Decided the numbered Shanghai avenues as
pinyin per the glossary/gazetteer: 四马路 = Sima Road (today Fuzhou Road, NEW gazetteer),
三马路 = Sanma Road; 巨籁达路 Rue Ratard already gazetteered. Two tooling patches (DO NOT
REVERT): qc_entities.py grew the same HOMOGRAPHS={"严重"} stoplist as check_content (B13);
data/noise.txt got a B14 idiom/name block. All checks green: parity 139=139, numbers 0
unresolved, content/entities clean, qa_epub PASS, epubcheck 0/0/0/0, register within
tolerance of ch01 (no stilted flag). See PROGRESS.md "B14" for the "NOT re-noted" list, the
settled renderings, and two open ch01-ch09-sweep items.

This batch's job: DRAFT CHAPTER THIRTEEN (ch13, "Twin Lotus on One Stem," 第十三章 并蒂莲,
PDF 284-307, printed 269-292, 5 sections: s1 一、派沈琬去 "Send Shen Wan" PDF 285, s2 二、挺进师
"The Vanguard Column" PDF 289, s3 三、按住蒋介石的脉搏 "A Finger on Chiang Kai-shek's Pulse"
PDF 293, s4 四、失联 "Contact Lost" PDF 298, s5 五、开张吃三年 "One Job Feeds You Three Years"
PDF 302) end to end against the frozen doc. Offset a constant 15 (printed = pdf - 15); read
each opener's folio off the scan. Re-render and re-OCR (data/png and data/zh are gitignored,
gone on a fresh checkout): render.py 284 307 --dpi 300, then ocr_crop.py 284 307 --left 0.06
--right 0.95 --top 0.11 --bottom 0.955 --lang chi_sim --psm 6. OCR is TOO NOISY on the proper
names, so HAND-TRANSCRIBE data/zh/ch13.txt off the 300-DPI page images directly
(data/png/p####.png), one paragraph per line, chapter title and section heads as ###
(the B08/B11/B12/B13/B14 method; OCR is a cross-check, not the source). The chapter divider
(PDF 284) and any washed-out full-page painting are design furniture, not captioned figures;
eyeball every page for real photos/line art and hand-crop any (exclude the printed caption,
translator's caption with source-label provenance, real alt text). Numerals in unit/place
designations are load-bearing — crop-verify them. Add ch13 to data/content_config.json.

BEFORE translating, read the final two pages of ch12's English (the voice). Read
the zh against the en on every line; change register, never meaning; invent
nothing (CLAUDE.md rule 4; verify the TAIL of the unit explicitly against the
scan). Cite printed folios, never PDF pages. Then footnotes at reader-model
density (consult the "NOT re-noted" lists in PROGRESS; grep notes.json before
adding); glossary rows straight into the sectioned ledger (en ASCII only),
consulting authority.json first; flag any NEW recurring institutional term
recurring:true and any NEW concession street gazetteer:true+today. Run
check_structure --pairs (SOURCE first: data/zh/ch13.txt out/ch13_reading.md),
verify_unit, make_bilingual + qc_entities, check_align, check_content --config
data/content_config.json, apparatus_merge + check_apparatus, and check_register
--ref out/ch01_reading.md (informational). Rebuild, run qa_epub and epubcheck (jar
at /tmp/epubcheck-5.1.0/epubcheck.jar).

Do it end to end; do not pause for approval. Deliver the rebuilt EPUB attached in
the chat, and paste the next kickoff verbatim in the same reply.
```

## DONE (one line per batch; do not redo)
- Survey: structure, offsets, style contract, skeleton EPUB. (earlier session)
- **B01 = ch01 (voice gate):** 165 paragraphs, blind-critique loop, human gate.
- **B02 = ch02:** 56. **B03 = ch03:** 146. **B04 = ch04:** 131. **B05 = ch05:** 66.
  **B06 = ch06:** 165. **B07 = ch07:** 99. **B08 = ch08:** 252.
- **B09 review:** register-rebaseline style doc + itemized corrections ch01-ch08.
- **B09 continuation:** register de-archaizing pass over ch01-ch08; dates
  month-day-year book-wide.
- **B10:** two builder features (Glossary of Recurring Terms + Street Gazetteer);
  footnote placement sweep; ch01 thinned; ch07/ch08 backfilled; spine-test pass; 290 notes.
- **B11 = ch09:** "The Riddle of Xiang Zhongfa's Disappearance," 194 paragraphs, 9
  sections; 27 notes (book 317), 5 figures, 95 glossary rows, 善钟路 -> gazetteer.
- **B12 = ch10:** "Opening a Shop, Doing Trade," 39 paragraphs, 2 sections; 15 notes
  (book 332), 3 figures, 101 glossary rows; 华润 = "Huarun" (glossed China Resources).
- **B13 = ch11:** "The Wild Swan," 82 paragraphs, 3 sections, PDF 248-263. Hand-transcribed;
  ch08-ch10 source-criticism register; 19 notes (book 351), 3 figures, 108 glossary rows;
  薛华立路 -> gazetteer; check_content HOMOGRAPHS patch (严重).
- **B14 (this batch) = ch12:** "A Purge in the Red-Light District," 139 paragraphs, 7
  sections, PDF 264-283. Hand-transcribed; ch08-ch11 source-criticism register; 15 notes
  (book 366), 2 figures, 75 glossary rows; 四马路 -> Sima Road (gazetteer); qc_entities
  HOMOGRAPHS patch (严重, mirrors check_content). All checks green, epubcheck 0/0/0/0,
  register no stilted flag. See PROGRESS.md "B14". ch13-ch15, the Preface, and back matter
  remain.

## Tooling in place (DO NOT REVERT)
- **build_reading_epub.py:** `render_recurring` (Glossary of Recurring Terms),
  `render_gazetteer` (Street Gazetteer), `_walk_flagged`, `.gaz` CSS; both back-matter
  pages wired into spine/nav/ncx and rendered only when their data exists.
- **check_content.py:** `AUTHOR` set (author self-naming) AND `HOMOGRAPHS` set (B13):
  严重 = the ch10 courier "Yan Zhong" but also the adjective "severe"; excluded from the
  content name-map.
- **qc_entities.py (B14):** the SAME `HOMOGRAPHS = {"严重"}` stoplist, for the identical
  reason (as an entity key it flagged every 极其严重 / 白色恐怖最严重). Keep the two lists in sync.
- Register-pass drivers: `edits/chNN_edits.md` + `scripts/apply_edits.py`;
  `scripts/anchor_check.py`. Scratchpad helpers from B10 (not committed).
- `scripts/indents.py`: furniture-band drop (FURNITURE_TOP=0.11, BOTTOM=0.955).
- `scripts/check_numbers.py`: arabic+万 combiner before the noise loop.
- `data/noise.txt` carries B02-B14 blocks (longest literal first); the B14 block adds
  万目睽睽, 成千上万, 百发百中, 十恶不赦, 万世, 二妹, 四溅 (四马路/三马路 street-name numerals
  were already present).
- `data/content_config.json`: docs+sources map for check_content, ch01-ch12.
  ADD ch13 when you translate it.
- OCR crop for this book: `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955
  --lang chi_sim --psm 6`. Offset constant 15 (printed = pdf - 15).
- **Transcription method (B08, confirmed again B14):** OCR is too noisy on the proper
  names; READ the 300-DPI page images (data/png/p####.png) directly and transcribe,
  cropping tight regions only for ambiguous names/numbers.
- **Parity gotcha:** in `data/zh/chNN.txt` mark the chapter title `### ` (like section
  heads), NOT `## `. English side: chapter title `## `, section heads `### `. AND run
  check_structure --pairs with the SOURCE file FIRST: `data/zh/chNN.txt
  out/chNN_reading.md`.
- **Glossary placement gotcha:** glossary.json is a DICT keyed by hanzi under
  people/organizations/places/terms. Add rows directly into the sub-objects with a
  re-read-verified one-shot (NOT via apparatus_merge's glossary path). `en` must be ASCII;
  curly punctuation only in note bodies (numeric char refs). (Four pre-existing non-ASCII
  `en` rows from earlier batches — Xiao Chunü, the Donghua/Donghai Café, Rue de Sieyès —
  are left as-is; builds pass with them.)
- **check_content full-name-vs-surname trap:** a glossary `en` of "Agnes Smedley" fails
  when the body uses only "Smedley"; set the glossary `en` to the SHORT form actually used
  in the prose (Smedley), so the substring test passes. Same care for any street/institution
  glossed one way but written another (e.g. "Moscow Sun Yat-sen University" not "Moscow's").
- **VERY high-frequency recurring names with pronoun runs, and name/common-word
  homographs, stay OUT of the entity glossary** (or go in the HOMOGRAPHS stoplist in BOTH
  check_content and qc_entities). Aliases with non-ASCII pinyin (e.g. 吕克勤 "Lü Keqin") are
  kept in the prose but left OUT of the checked glossary.
- **figures.json `file` is a BASENAME**; builder prepends `data/figs/`. `before` anchors
  fall in the FIRST ~80 chars of a paragraph, cannot sit on a heading.
- **Washed-out full-page divider/illustration pages** are design furniture, NOT captioned
  figures (exclude them; ch12's are p0264 the divider and p0283 a faint group painting).
- Set-off block quotes render `{v}`; verse `{p}`; dateline `{d}`; `check_structure.py`
  strips markers before parity. ch10-ch12 used ZERO markers — cited memoir/document passages
  read cleanly as normal paragraphs with a "(Name, year)" attribution or a colon lead-in.

## Apparatus state after B14 (frozen doc = STYLE.local top sections)
- 366 notes (ch09 +27, ch10 +15, ch11 +19, ch12 +15). Densities taper as the book's
  furniture gets covered; ch12 runs reference-dense in s1-s3 (the whole Ding Ling / Civil
  Rights League / Smedley cast is new) and light in s4-s7 (the traitor-hunt is Special
  Branch furniture already covered). A modest new-note count is healthy.
- The Glossary of Recurring Terms and Street Gazetteer carry the recurring furniture and
  the concession streets; gloss such terms ONCE at first appearance and let the back matter
  carry the rest. When drafting ch13, flag any NEW recurring institutional term
  `recurring:true` and any NEW concession street `gazetteer:true`+`today`.
- Marker placement: put a marker at the end of the clause/sentence that holds the referent,
  never mid-phrase (right after a complete referent noun-phrase is fine).

## Renderings settled (also in glossary.json / STYLE.local.md)
- Consistency canon (verified clean): Center (not Centre), the Politburo, the White Terror,
  the Xujiahui Observatory, Lazily Seeking Old Dreams (italic), fused lane names, the ten-li
  foreign quarter, presiding pastor. Dates month-day-year. Spelling: AMERICAN.
- 中央特科 the Central Special Branch (handle: the Special Branch); 红队 / 打狗队 the Red
  Squad / the dog-beating squad (打狗团 the dog-beating corps, a source variant); 中统 the
  Zhongtong; 华润 Huarun (China Resources).
- **Numbered Shanghai avenues = pinyin (glossary/gazetteer, ch05/ch06):** 四马路 Sima Road
  (today Fuzhou Road), 三马路 Sanma Road (today Hankou Road). ch09 para 163 has the ONE
  outlier "Fourth Avenue" -> fix to "Sima Road" in the end-of-book sweep.
- B14 additions: 马绍武 Ma Shaowu; 丁玲 Ding Ling; 冯达 Feng Da; 杨杏佛 Yang Xingfo; 史沫特莱
  Smedley (glossary en "Smedley"); 熊国华 Xiong Guohua; 邝惠安 Kuang Hui'an (龚昌荣, "老广东");
  孟华亭 Meng Huating; 陈同生 Chen Tongsheng; 经盛鸿 Jing Shenghong; 盛忠亮 Sheng Zhongliang
  (盛岳 Sheng Yue); 牛兰 Noulens. Institutions: the China League for the Protection of Civil
  Rights; the Blue Shirts Society (recurring); the Academia Sinica; the CCP Shanghai Central
  Bureau (recurring). Newspapers: 时事新报 the China Times, 大公报 L'Impartial, 申报 the Shen Bao,
  独立评论 the Independent Critic, 北斗 the Big Dipper. Streets: 四马路 Sima Road (gazetteer).
- Consult authority.json before romanizing (Sun Yat-sen, Du Yuesheng, Deng Yanda, Guo Moruo,
  Feng Xuefeng, Wang Jingwei, Song Qingling, Lu Xun, Yang Xingfo all confirmed shelf-wide).

## Voice sheets (carry forward)
- **The author (Ye Xiaoshen):** warm, buttonholing popular-history narrator with a sardonic
  edge; heat in the verbs and rhythm, ration exclamation and rhetorical questions; sustained
  source-criticism as running skeptical argument in plain English, sources' own wrong words
  kept, verdict in the note; first person kept where he places himself as interviewer/reader
  of the archive ("I could not find the sheet of Commercial News..."). His SARDONIC framing
  of partisan memoirs (Smedley's 1469 vs the real plates; Ding Ling misremembering the
  street) is his voice — preserve it, verdict in the note; do not iron it flat.
- **Martyr set-pieces run at full temperature, verdict in the note.** ch12 closed on the
  chaplain's "men greater than Christ"; ch13 ("Twin Lotus on One Stem") turns to the Shen
  Wan / vanguard-column / lost-contact story — watch for the same interested-witness heat.
- **Zhou Enlai** warm and big-brotherly; **Gu Shunzhang** the foil, hot and contemptuous;
  **Xu Enzeng / KMT memoirists** officialese, self-regarding, self-exculpating (his memoir
  supplies half of ch12's narration); **Party leaders / descendants / martyrs' cellmates
  in interview** clipped, factual, contracted (Chen Tongsheng's prison dialogue in ch12).

## Where the story stands
Chapters One-Twelve are drafted. Chapter Eleven recovered Yang Du; Chapter Twelve, "A Purge
in the Red-Light District," returned to the Special Branch's counter-traitor killings — Ma
Shaowu at the Little Garden, the Ding Ling abduction and the civil-rights campaign around it,
the Xiong Guohua case and the Renji Hospital hit, the crack shot Kuang Hui'an, and the four
Red Squad men garrotted at Nanjing in 1935. Chapter Thirteen, "Twin Lotus on One Stem" (ch13,
PDF 284-307), is next: five sections (派沈琬去 "Send Shen Wan," 挺进师 "The Vanguard Column,"
按住蒋介石的脉搏 "A Finger on Chiang Kai-shek's Pulse," 失联 "Contact Lost," 开张吃三年 "One Job
Feeds You Three Years"). Read the ch08-ch12 source-criticism voice sheet forward.

## Open traps / environment
- `data/zh/` and `data/png/` are gitignored; a fresh checkout has neither. ch13 drafting
  needs both (render + hand-transcribe from source.pdf, which IS tracked). The tracked
  deliverables (out/chNN_reading.md, notes/glossary/figures, the built EPUB) are complete.
- Cross-check note AND figure anchors before any re-voicing edit (scripts/anchor_check.py).
  A broken figure `before` anchor fails the build.
- `OMP_THREAD_LIMIT=1` mandatory for tesseract; `pgrep -c tesseract` = 0 after OCR.
  epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar (setup fetches).
- `authority.json` is updated on WHOLE-BOOK completion, not per batch.
- **ch01-ch09 cleanup-sweep worklist (do at the end, not mid-batch):** (1) ch01 Yang Du
  note birth year "1875" -> "1874" (the book's Cihai entry, ch11); (2) ch09 para 163
  "Fourth Avenue" -> "Sima Road" for 四马路 (the one numbered-avenue outlier).
- Still UNTRANSLATED: ch13-ch15, the Preface (ch00, PDF 6-15), and back matter (Works Cited
  ch16, Afterword ch17). They fold into later batches.
- Branch hygiene: canonical branch is `claude/the-sword-roars`. B14 started on a stray
  `claude/exciting-maxwell-2v9540` (identical commit; local canonical was stale at an
  ancestor); reset canonical to origin, consolidated, stray pruned local and remote.
