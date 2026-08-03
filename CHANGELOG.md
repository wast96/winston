# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch12); rebuilt, qa green.
- LOCAL: fixed a dropped clause in ch03 section 2.
-->

## 2026-08-03 — Whole-book review pass ("kick the tires")

A full accuracy and rendering review of all 27 translated units, run as a
paragraph-by-paragraph bilingual comparison plus a cross-cutting consistency
audit, with every finding verified against the source before applying.

Accuracy fixes (~60): wrong referents corrected (the revolutionary bond was
with Xiyan, not the author, ch05; Chen made the call to Xiao Cao, ch10; the
gift in the old master's name, ch10; the railway union as publicist, ch03;
grandmother's natal family, ch01); dropped clauses restored ("But you had no
such thought," ch06; the Analects tag, ch06; "heroically," ch01; "rich in the
stuff of legend," ch43); unsupported additions removed ("or since," ch01;
"reactionaries" inside a quoted label, ch18; "by marriage," ch21); term slips
fixed (jingli registrar not "assistant salt commissioner," ch01; muyou aide,
ch09; nephews not cousins, ch09; mourning banner, ch11; fetters not
"instruments of torture," ch21; 字-counts rendered "characters" not "words,"
ch40/ch43; "golden rice bowl," ch01); "Mr. Song Qingling" and "Mr. Huang"
misgenderings removed (ch20/ch43); romanization typos fixed (He Shisi, Bei
Songsheng) with glossary cascade; ch21 retitled "Wrongfully Imprisoned
Together" (冤狱); ch43 retitled "Editors' Postscript."

Readability fixes (~80): calques recast (breast/narrow-minded, hand over
hand, refugee-visits, "trick his money," "disband refugees," 奇兵, 你中有我,
对内/对外, 肚量, garden-path and dangling constructions throughout); inline
glosses added where a native reader was lost (wild pheasants, Eight
Characters, tubaozi/Earth Leopard, Fragrant Harbor pun, tanhua, Qin Hui, Song
Jiang and the 108 Generals, Premier = Sun Yat-sen).

Consistency cascades: Kuomintang/National Government unified (ch12/13/17/18/
42 had drifted to "Nationalist"); one rendering each for 救国会, 银联 (Banking
Union), 文联 (Cultural Federation), 民社党 (now Democratic Socialist Party,
footnoted), News Daily, Songhu War, Solitary Island, Grand Secretary Chen,
Earth Leopard, Elder Sister/Elder Madame, Party Central, Yangtze,
Zhuzhou–Pingxiang Railway, police station, white areas/White Terror, Fuxing
Middle Road, Route Lafayette; US spelling and DMY dates normalized (ch08-21);
book/periodical titles italicized from ch07 on, matching ch00-06.

Apparatus: 18 garbled CJK characters in note bodies corrected (the heredoc
trap); 9 notes added (April Twelfth moved to first appearance; new notes on
the Mukden Incident, Noulens couple, Southern Anhui Incident, lady Zhuge, Huo
Qubing, Democratic Socialist Party, a Wuchang emendation, an internal source
contradiction, a garbled congress designation) — 98 notes total; ambiguous
note anchors pinned; the translator's note no longer denies the source's four
editorial endnotes; glossary display bug fixed (298 double-escaped entities);
glossary rows added/corrected. Builder: display-layer curly typography
(unifies the straight/curly split between batches), note markers after
punctuation, TOC size-spans only on pending chapters, zh-Hans lang tags,
refuse-on-unplaced-figure guard.

QA: verbatim-source sync, paragraph parity 27/27, check_numbers 0 unresolved
on all units, qa_epub PASS (105 files, 98 notes, all links resolve).
