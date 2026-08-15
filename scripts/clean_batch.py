#!/usr/bin/env python3
"""Derive data/zh/<id>.txt (the parity source) VERBATIM from data/src/<file>.

The machine copies the source, never the translator: this reads the ingested
source lines and applies only structural, per-unit transformations that are
declared explicitly below and verified against the source afterwards:

  drop     leading lines that are page furniture or heading markup
           (the running-header '英雄无名-陈恭澍', the chapter <h1>/<h2>).
  merges   source <p> pairs split mid-phrase (the first ends on a comma or
           mid-word, last char not terminal); joined with no separator.
  glued    a sub-heading the digitization glued onto the END of a paragraph's
           <p>; split off and emitted as its own '### ' heading line AFTER the
           paragraph it was stuck to (it introduces the next section).
  standal  a sub-heading the source kept as its own <p> but with no heading
           markup; emitted as a '### ' heading line in place of the paragraph.

Output: '### <zh chapter title>' then, in order, the body source paragraphs
(one per line) with '### <zh sub-heading>' lines interleaved. check_align and
verify_unit strip every '#'-prefixed line, so the headings are apparatus, not
paragraphs, and parity is measured on the prose alone.

VERIFICATION (printed, and a hard failure): the concatenation of every emitted
line's raw characters, in order, must equal the concatenation of the kept
source <p> lines. That proves nothing was added, dropped, or mistyped.

Usage: clean_batch.py            (rebuilds every configured unit)
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Per-unit structural spec. Line numbers are 1-based into data/src/<file>.
UNITS = {
    "ch01": {
        "file": "02_index-split-000.txt",
        "title": "「英雄无名」卷前",
        "drop": 3,            # header + <h1>卷前 + <h2>构想
        "merges": [], "glued": {}, "standalone": [],
    },
    "ch02": {
        "file": "03_index-split-000-0001.txt",
        "title": "「北国锄奸」介绍",
        "drop": 2,            # header + <h2>
        "merges": [(5, 6)],   # 「滦 / 榆游击队」 split mid-word
        "glued": {}, "standalone": [],
    },
    "ch03": {
        "file": "04_index-split-000-0002.txt",
        "title": "「河内辱命」介绍",
        "drop": 2,
        "merges": [], "glued": {}, "standalone": [],
    },
    "ch04": {
        "file": "05_index-split-000-0003.txt",
        "title": "「百战声威」介绍",
        "drop": 2,
        "merges": [(29, 30)],  # 「国民党特务」， / 这不但说明了...
        "glued": {11: "另外两部书",
                  19: "我对「特务工作」的看法",
                  35: "为什么要「制裁」"},
        "standalone": [50, 62],  # 中国模式的「特工」 ; 为无名英雄留历史纪录
    },
    "ch05": {
        "file": "06_index-split-000-0004.txt",
        "title": "北国锄奸",
        "drop": 2,
        "merges": [], "glued": {}, "standalone": [],
    },
    "ch06": {
        "file": "07_index-split-000-0005.txt",
        "title": "第一节 任重道远 勇往直前",
        "drop": 2,             # running header + <h2> section title
        # extractor splits: a line broken mid-phrase into the next <p>
        "merges": [(101, 102), (173, 174), (202, 203), (221, 222),
                   (230, 231)],
        # sub-section headings the digitization glued onto a paragraph's tail
        "glued": {72: "二 吸收入「军会」与征召受「特训」",
                  145: "三 负有秘密任务的领班人",
                  194: "四 蒙然不知的遇上了国际大间谍",
                  280: "五 情报活动中的政治运用"},
        "standalone": [3],     # 一 学友小聚初识戴雨农
    },
    "ch07": {
        "file": "08_index-split-000-0006.txt",
        "title": "第二节 一鸣惊人 不同凡响",
        "drop": 2,             # running header + <h2> section title
        # one extractor split: 「...这表示有了 / 新的情况。」 broken mid-phrase
        "merges": [(199, 200)],
        # ch07's four sub-headings are each their own <p> (no glued tails)
        "glued": {},
        "standalone": [3, 90, 194, 288],
    },
    "ch08": {
        "file": "09_index-split-000-0007.txt",
        "title": "第三节 盘根错节 李代桃僵",
        "drop": 2,             # running header + <h2> section title
        # six extractor splits (mid-phrase / mid-word continuations). NOTE:
        # (402,403) is NOT a merge — L402 (第三点) trails off in a source cut
        # ("其原由，在") and L403 is the next bullet (第四点); left visible +
        # footnoted. The ；/： enumerated bullet lists are deliberate <p>.
        "merges": [(95, 96), (117, 118), (129, 130), (150, 151),
                   (308, 309), (376, 377)],
        # 一 is standalone; 二–六 are glued to the tail of a preceding <p>
        "glued": {112: "二 苗而未秀 早折了栋梁材",
                  206: "三 搜寻吉某的踪迹 总算有了着落",
                  250: "四 这就是一般所常道的 临机应变",
                  328: "五 失之毫厘与乎收之桑榆",
                  394: "六 原是个魔鬼附身命中带煞的人"},
        "standalone": [3],     # 一 煽扬赤焰的叛国者皆曰可杀
    },
    "ch09": {
        "file": "10_index-split-000-0008.txt",
        "title": "第四节 急功躁进铸成大错",
        "drop": 2,             # running header + <h2> section title
        # extractor splits (mid-phrase continuations). (89,90,91) is a THREE-
        # fragment chain: "...事件的发生，" / "...还可以" / "使用...对付他。".
        # The many ：-ended lines introduce a quote/example as a DELIBERATE
        # separate <p> and are NOT merged. L54 ("且看石友三...下作行为") is a
        # short colon-less lead-in <p>, kept whole (not merged into the dated
        # L55). L164 ends with a stray opening 「 that belongs to L165's
        # paragraph (a misplaced-bracket digitization glitch); the two stay
        # separate <p> and the bracket is left where the source has it so raw
        # characters are conserved.
        "merges": [(30, 31), (89, 90), (90, 91), (127, 128), (161, 162)],
        # 一 is standalone; 二 三 五 四 六 are glued to a preceding <p> tail.
        # NOTE the SOURCE prints sections 四 and 五 OUT OF SEQUENCE: the <p>
        # labelled 五 (L183) physically precedes the one labelled 四 (L242),
        # confirmed by byte order in the source XHTML. Preserved verbatim in
        # printed order and footnoted in the translation (rule 4).
        "glued": {52: "二 枪击与毒杀两者之间的取舍",
                  115: "三 过甚操切所造成的惨痛后果",
                  183: "五 不敢面对现实作了一次边塞流亡",
                  242: "四 处置失当步调与进退失据",
                  282: "六 像石友三这种人自然不会有好下场"},
        "standalone": [3],     # 一 争取到对方的亲信作为内应
    },
    "ch10": {
        "file": "11_index-split-000-0009.txt",
        "title": "「河内汪案始末」自序",
        # drop=3: running header + <h1>「河内辱命」 (the Part Two banner, handled
        # by book.json's `part` field) + <h3>「河内汪案始末」自序 (the chapter title,
        # re-emitted from `title`). This preface carries NO sub-headings.
        "drop": 3,
        "merges": [], "glued": {}, "standalone": [],
    },
    "ch11": {
        "file": "12_index-split-000-0010.txt",
        "title": "第一章 浴血杀敌奋勇抗战",
        "drop": 2,             # running header + <h2> chapter title
        # one extractor split: L90 ("...二十九日汪氏艳") continues mid-word into
        # L91 ("电后，...") — 艳|电. The 「艳电」 document is a THREE-<p> quoted block
        # (lead-in ends ：, salutation ends ：, then the body); those ：-ended <p>
        # are DELIBERATE separate paragraphs and are NOT merged.
        "merges": [(90, 91)],
        # this chapter's sub-headings are couplet-style titles with NO number
        # prefix: L3 stands alone; L52's heading is glued to a paragraph's tail.
        "glued": {52: "只限于行踪监视与活动侦察"},
        "standalone": [3],     # 一道急急令飞渡万里关山
    },
    "ch12": {
        "file": "13_index-split-000-0011.txt",
        "title": "第二章 人心叵测别有肺肠",
        "drop": 2,             # running header + <h2> chapter title
        # three extractor splits (mid-phrase / mid-word continuations):
        # L42 (以分析的|方法), L94 (不敢遽|下判断), L124 (黯然|握别), and L131
        # (笔者相信「用五」|先生 — the name 「用五」先生 split across the closing 」, a
        # mid-phrase split the "」 is terminal" heuristic hides). The many ：-ended
        # lines lead into the two long quoted documents (Konoe's third statement,
        # Chiang's 9000-word address) as DELIBERATE separate <p> and are NOT
        # merged. The chapter body ends with a "(本章完)" marker at L133, after
        # which the source prints a 5-<p> reflective coda (L134-138) kept whole.
        "merges": [(42, 43), (94, 95), (124, 125), (131, 132)],
        # this chapter's sub-headings are numbered-in-parens (一)/(二)/(三):
        # L3 stands alone; (二) and (三) are glued to a preceding <p>'s tail.
        "glued": {33: "(二)明澈透底的揭露了敌国阴谋",
                  69: "(三)绝对不会有那种不可思议的事"},
        "standalone": [3],     # (一)尚未察觉汪氏已与敌国 暗通款曲
    },
    "ch13": {
        "file": "14_index-split-000-0012.txt",
        "title": "第三章 波诡云谲 风雨欲来",
        "drop": 2,             # running header + <h2> chapter title
        # The 279 source <p> expand to exactly 283 body lines via 4 <br/> (proven
        # p-by-p against the source XHTML, zero mismatches). Two <br/> paragraphs:
        #  - L157/158 (a two-sentence prose pair inside one <p>), chained into the
        #    L156-158 merge below;
        #  - L172-175, a four-line 律诗 inside one <p> — kept as four body lines and
        #    rendered as verse ({p}) in the reading.md.
        # SIX mid-phrase splits where the SOURCE itself broke one sentence across two
        # <p> (a digitization artifact, faithfully reproduced by the extractor):
        #    L61/62 (专事国际情报|由王芄生...); L156/157/158 (...「身死为天下所僇笑」。这样|
        #    可悲的结局...|汪如九原有知... — a THREE-fragment chain, the <br/> pair folded
        #    in); L162/163 (胡涂的事，天|下最不可思议... — 天|下 split mid-word); L202/203
        #    (才逼他走|上极端... — 走|上极端 mid-word); L228/229 (见客的时候，|礼貌十足...).
        # The many ：-ended lead-ins to quoted verse/documents, and the ；-ended verse
        # lines and two ；-ended prose <p> (L246, L255), are DELIBERATE separate <p>
        # and are NOT merged. The chapter body ends with a "(本章完)" marker at L132
        # (cf. ch12), after which the source appends a long biographical essay on
        # Wang Jingwei whose (一)-(五) sub-heading numbering RESTARTS independently of
        # the chapter's own (一)-(四) — a faithful source structure, kept verbatim.
        "merges": [(61, 62), (156, 157), (157, 158),
                   (162, 163), (202, 203), (228, 229)],
        # every sub-heading is its own <p> (all standalone; no glued tails). Two
        # numbered-in-parens series — (一)-(四) for the operational narrative, then
        # (一)-(五) for the appended Wang essay — plus an inner enumerated list
        # 一、-六、 inside the essay's section (三) (rendered #### in the reading.md).
        "glued": {},
        "standalone": [3, 36, 68, 94,          # (一)-(四) operational narrative
                       136, 161, 194, 215, 232,  # (一)-(五) Wang essay
                       198, 200, 204, 206, 208, 210],  # 一、-六、 inner list
    },
    "ch14": {
        "file": "15_index-split-000-0013.txt",
        "title": "第四章 三面受敌 一往无前",
        "drop": 2,             # running header + <h2> chapter title
        # A very short bridge chapter: 6 <p> = one couplet-style sub-heading
        # (L3, no number prefix, cf. ch11) + five body paragraphs (L4-8). No
        # <br/>, no images, no set-off formatting; all five body lines end on a
        # terminal char (。/！), so there are NO extractor mid-phrase splits.
        "merges": [], "glued": {},
        "standalone": [3],     # 壁垒坚强迎接多方面的挑战
    },
    "ch15": {
        "file": "16_index-split-000-0014.txt",
        "title": "第五章 博浪一击 误中副车",
        "drop": 2,             # running header + <h2> chapter title
        # 235 source <p> (proven p-by-p against the source XHTML, zero mismatches;
        # no <br/>, no images, no set-off formatting). FIVE mid-phrase splits where
        # the SOURCE broke one sentence across two <p> (faithfully reproduced by
        # the extractor): L13/14 (弹是子弹，药就|是可以致命的毒药 — 药就|是);
        # L153/154 (墙里面，|有一方小院落 — a comma split); L167/168 (这不是汪|精卫
        # 还有谁 — 汪|精卫, split mid-name); L175/176 (最愉快的一段|时刻 — 一段|时刻);
        # L208/209 (「午夜□□」那两|节故事 — 两|节). The MANY ；/：-ended lines are
        # DELIBERATE separate <p> and are NOT merged: the announced attack plan
        # (L59 lead-in, L60-65 bullets), the three decisions (L88/L90), the
        # job-division (L143/144), the reader-questions (L125 lead-in), and the
        # three quoted-book lead-ins in section (五) (L189, L210) with their
        # multi-<p> quoted blocks kept whole.
        "merges": [(13, 14), (153, 154), (167, 168), (175, 176), (208, 209)],
        # five sub-headings, all numbered-in-parens (一)-(五) (cf. ch12/ch13),
        # each its own <p> (all standalone; no glued tails).
        "glued": {},
        "standalone": [3, 51, 97, 131, 185],
    },
    "ch16": {
        "file": "17_index-split-000-0015.txt",
        "title": "第六章 奸伪卑劣 寿张为幻",
        "drop": 2,             # running header + <h2> chapter title
        # 121 source <p> (proven p-by-p against the source XHTML, zero mismatches;
        # no <br/>, no images, no set-off formatting). TWO mid-phrase splits where
        # the SOURCE broke one sentence across two <p> (faithfully reproduced by
        # the extractor), both inside the two long quoted Wang documents:
        #   L65/66 (行状: ...茫茫后死之感，何时|已乎！ — split mid-clause);
        #   L96/97 (举一个例: ...何况现时|除第三国际外... — split mid-clause).
        # The meeting-record ATTENDEE ROSTER inside 「举一个例」 (L85 出席/时间/地址,
        # L86 列席, L87 主席/秘书长/秘书主任) breaks across three <p>: these are
        # DELIBERATE document formatting, NOT extractor splits, and are NOT merged
        # (cf. ch12/ch13/ch15 quoted documents). The many ：-ended lead-ins (L18,
        # L80, L104) and the two quoted-document title lines (L64 曾仲鸣先生行状,
        # L81 举一个例) are DELIBERATE separate <p> and are NOT merged. The chapter
        # body carries an in-text "(第六章完)" coda at L117 (cf. ch12/ch13), after
        # which four further <p> (L118-121) close Part Two and bridge to Part Three.
        "merges": [(65, 66), (96, 97)],
        # four sub-headings, all numbered-in-parens (一)-(四) (cf. ch12/ch15):
        # (一),(三),(四) are each their own <p> (standalone); (二) is GLUED onto the
        # tail of a preceding <p> (cf. ch08) and is split off as its own heading.
        "glued": {48: "(二)曾仲鸣事汪以忠虽枉死应无怨尤"},
        "standalone": [3, 76, 111],  # (一),(三),(四)
    },
    "ch17": {
        "file": "18_index-split-000-0016.txt",
        "title": "第七章 临深履薄锲而不舍",
        "drop": 2,             # running header + <h2> chapter title
        # 151 source <p> (proven p-by-p against the source XHTML: 1 <h2> + 151
        # <p>, zero mismatches; no <br/>, no images, no set-off formatting). ONE
        # mid-phrase split where the SOURCE broke one sentence across two <p>
        # (faithfully reproduced by the extractor), inside the quoted Kagesa
        # memoir passage: L74/75 (...我(汪氏)决不过问，| 断然引咎下野，以明心迹。」 —
        # a comma split). The tail L151/L152 read as run-on but each is a
        # COMPLETE <p> ending on a terminal char, so they are NOT merged.
        # The many ：-ended lead-ins are DELIBERATE separate <p> and are NOT
        # merged: the six-point 「南华日报」 list (L10 lead-in, L11-14 bullets —
        # points 二/三/四 glued in one source <p> at L12), the quoted Wang→Long
        # Yun letter (L50 lead-in; L51 salutation ends ：; L52-53 body), the
        # three-point agreement (L60 lead-in, L61-63 三点协议), the quoted
        # Kagesa memoir (L66, L73 lead-ins) and 蒋总统秘录 excerpts (L78, L80,
        # L85, L89 lead-ins), the 板垣 four-point talks (L80 lead-in, L81-84),
        # and the "使我难以忘怀的是─" dash lead-in at L112 (introduces L113-117).
        # NO in-text "(第七章完)" coda; the final <p> (L153) forward-references
        # the book's 后记 accounting for the 十九个 Hanoi participants.
        "merges": [(74, 75)],
        # three sub-headings, all numbered-in-parens (一)-(三) (cf. ch12/ch15),
        # each its own <p> (all standalone; no glued tails).
        "glued": {},
        "standalone": [3, 45, 108],
    },
    "ch18": {
        "file": "19_index-split-000-0017.txt",
        "title": "第八章 再接再励前仆后继",
        "drop": 2,             # running header + <h2> chapter title
        # 143 source <p> (proven p-by-p against the source XHTML: 1 <h2> + 143
        # <p>, zero mismatches; no <br/>, no images, no set-off formatting).
        # FOUR mid-phrase splits (last char a comma or mid-word, next <p> ends
        # terminal, no chains): L20/21 (...如果汪家也相信妈妈经的话，| 这就不是一个
        # 好兆头。), L39/40 (...合盘告 | 知吴赓恕先生。 — mid-word 告|知), L57/58
        # (...就是一去无音信，其中 | 当然免不了...), L134/135 (...他不是走 | 出来的，
        # 是手脚着地爬出来的！ — mid-word 走|出来). The ：-ended enumerated lead-ins
        # (L6 还有：, L12 再说汪的行踪…：, L113 再说下落不明的：, L132 …只剩下三个人
        # 了：) and the martyr-roster label lines (L35 其一：… glued to its own
        # body with a dash; L51 其二：陈三才先烈 and L62 其三：黄逸光先烈 each its own
        # <p>) are DELIBERATE separate <p> and are NOT merged (cf. ch16/ch17).
        # NO in-text "(第八章完)" coda (cf. ch14/ch15/ch17); the final <p> (L145)
        # closes Part Two, forward-referencing Part Three (百战声威) and Part Four.
        "merges": [(20, 21), (39, 40), (57, 58), (134, 135)],
        # three sub-headings, all numbered-in-parens (一)-(三): (一) is its own
        # <p> (standalone, L3); (二) and (三) are GLUED onto the tail of a
        # preceding <p> (cf. ch08/ch16) and split off as their own headings.
        "glued": {31: "(二)痛定思痛字字为汪案牺牲者悼念",
                  86: "(三)生死荣辱之中也有幸与不幸"},
        "standalone": [3],     # (一)总是跟在后头就已失去机先
    },
    "ch19": {
        "file": "20_index-split-000-0018.txt",
        "title": "「英雄无名」作者小启",
        "drop": 2,             # running header + <h1> notice title
        # 4 source <p> (proven p-by-p against the source XHTML: 1 <h1> + 4 <p>,
        # zero mismatches; no <br/>, no images). NO sub-headings. The four <p>
        # are the 拙着…第三部 announcement (L3), the 三种态度 body (L4), the 来信
        # 请寄 line (L5), and the 陈恭澍谨启七十二年五月 signature (L6). The
        # signature ends non-terminal (…月) but is a DELIBERATE separate <p>
        # kept as its own paragraph, NOT merged.
        "merges": [], "glued": {}, "standalone": [],
    },
    "ch20": {
        "file": "21_index-split-000-0019.txt",
        "title": "「上海抗日敌后行动」自序",
        # drop=3 (cf. ch10, the Part Two preface): running header +
        # <h1>「百战声威」 (the Part Three banner, rendered from book.json's
        # `part` field) + <h3>「上海抗日敌后行动」自序 (the preface's own title,
        # re-emitted from `title`/book.json title_en). Confirmed p-by-p against
        # the source XHTML: 1 <h1> + 1 <h3> + 26 <p>, zero mismatches; no <h2>,
        # no <br/>, no images, no set-off formatting. The 26 body <p> (L4-L29)
        # map 1:1 to the 26 source <p> — NO extractor mid-phrase splits. The
        # lone non-terminal line, L12 ("...大致有如下者–"), ends on a dash lead-in
        # that is its OWN source <p> introducing the region-structure list that
        # follows; it is DELIBERATE separate <p>, NOT a split, and is NOT merged
        # (cf. the ；/：-ended lead-ins in ch16/ch17/ch18). NO sub-headings; no
        # in-text "(...完)" coda. Grep for [\d+] note markers: none present.
        "drop": 3,
        "merges": [], "glued": {}, "standalone": [],
    },
    "ch21": {
        "file": "22_index-split-000-0020.txt",
        "title": "第一章 十里洋场重振雄威",
        "drop": 2,             # running header + <h2> chapter title
        # 162 source <p> (proven p-by-p against the source XHTML: 1 <h2> + 162
        # <p>, zero mismatches; no <h1>, no <br/>, no images, no [\d+] note
        # markers). THREE mid-phrase splits where the source <p> boundary severs
        # one sentence (first ends non-terminal, no chains): L56/57 (…是办理制裁 |
        # 汪精卫的项目。 — one enumerated 一、 item split at 制裁|汪精卫), L93/94
        # (…工作甚为吃重，这或者 | 就是戴先生不同意他留在上海的理由了吧。), L107/108
        # (…也要提供不少 | 条件再加上一番经营才成。). The ：/-ended lead-ins (L19 …作了
        # 一番分析：, L45 …补充说明者：, L51 「七一四事件之有惊无险」- and L66 「惠尔登舞厅
        # 内之惊险一幕」- the quoted-title dash lead-ins, L52 …其原因如下：, L55 …再加以
        # 解释如下：, L71 …得知如下情况：, L75 …再加以解释如下：), the 一、-八、 / 1-4
        # enumerated items, and the 『』-closed dialogue lines are DELIBERATE
        # separate <p> and are NOT merged (cf. ch16/ch17/ch18). L86 (…如何应用了)
        # ends on 了 with the source's 。 dropped — a DELIBERATE paragraph break
        # (new topic follows), NOT a split; rendered as its own paragraph.
        # WATCH: the serialization coda "(第一章完下期续载)" is glued to the tail of
        # L157, with SEVEN further <p> (L158-L164) after it — a magazine-installment
        # seam faithfully reproduced (cf. the "(第N章完)" coda in ch12/ch13/ch16);
        # resolved p-by-p and preserved as body text.
        "merges": [(56, 57), (93, 94), (107, 108)],
        # four couplet-style sub-headings (NO number prefix; cf. ch11/ch14), each
        # its own plain <p> in the source (standalone): L3 死无对证永成悬疑的一桩大反间,
        # L37 危机四伏中稳扎稳打渡过难关, L82 我们的敌后工作指挥中心别具一格,
        # L112 无形火线上无所不在的战斗行动者剪影. No glued tails.
        "glued": {},
        "standalone": [3, 37, 82, 112],
    },
}


def build(cid, spec):
    path = os.path.join(ROOT, "data", "src", spec["file"])
    raw = [l.rstrip("\n") for l in open(path, encoding="utf-8")]
    n = len(raw)
    kept = list(range(spec["drop"] + 1, n + 1))  # 1-based body line numbers

    merge_from = {a: b for a, b in spec["merges"]}
    merge_into = {b for _, b in spec["merges"]}
    glued = spec["glued"]
    standalone = set(spec["standalone"])

    out = ["### " + spec["title"]]
    verify_src = []   # kept source <p> raw text, in order
    verify_out = []   # emitted raw text (paragraph bodies + heading texts)

    i = 0
    while i < len(kept):
        ln = kept[i]
        text = raw[ln - 1].strip()
        if ln in merge_into:
            i += 1
            continue  # consumed by its partner already
        if ln in standalone:
            out.append("### " + text)
            verify_src.append(text)
            verify_out.append(text)
            i += 1
            continue
        # apply a merge starting at this line; follow the chain so a paragraph
        # the extractor split into 3+ fragments (e.g. (89,90),(90,91)) is
        # rejoined whole. A plain pair is just a chain of length one.
        if ln in merge_from:
            verify_src.append(text)
            cur = ln
            while cur in merge_from:
                partner = merge_from[cur]
                ptext = raw[partner - 1].strip()
                verify_src.append(ptext)
                text = text + ptext
                cur = partner
        else:
            verify_src.append(text)
        # split a glued trailing heading
        if ln in glued:
            head = glued[ln]
            assert text.endswith(head), \
                "%s L%d does not end with glued heading %r" % (cid, ln, head)
            body = text[: -len(head)]
            out.append(body)
            out.append("### " + head)
            verify_out.append(body)
            verify_out.append(head)
        else:
            out.append(text)
            verify_out.append(text)
        i += 1

    # verification: raw characters must be conserved exactly
    if "".join(verify_src) != "".join(verify_out):
        sys.exit("VERIFY FAIL %s: emitted text != source text" % cid)

    dest = os.path.join(ROOT, "data", "zh", cid + ".txt")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    body_paras = sum(1 for l in out if not l.startswith("#"))
    heads = sum(1 for l in out if l.startswith("### ")) - 1  # minus title
    print("%s: %d body paragraphs, %d sub-headings, source conserved OK"
          % (cid, body_paras, heads))


def main():
    for cid, spec in UNITS.items():
        build(cid, spec)


if __name__ == "__main__":
    main()
