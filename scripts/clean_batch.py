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
    "ch22": {
        "file": "23_index-split-000-0021.txt",
        "title": "第二章 春云乍展风雷初动",   # the stray 杀 fused onto the source
        # <h2> (第二章 春云乍展风雷初动杀) is a digitization glitch, dropped here;
        # book.json title_en is already clean. The couplet is 春云乍展／风雷初动.
        "drop": 2,             # running header + <h2> chapter title
        # 292 source <p> (proven p-by-p against the source XHTML: 1 <h2> + 292
        # <p>, zero mismatches; no <h1>, no <br/>, no images, no [\d+] note
        # markers). THREE mid-phrase splits where the source <p> boundary severs
        # one sentence (first ends non-terminal, no chains): L31/32 (…知道这件事
        # 的有关人士 | 有以指教。), L221/222 (…笔者敢于如此肯 | 定，是体验… — 肯定
        # split), L279/280 (…王先生…立即避 | 入了女用洗手间，得脱此难。— 避入 split).
        # The ：-ended lead-ins (L17 …其经过概略是这样的：, L41 …原文如下：, L45 …
        # 补充说明如下：, L100 …其原文如下：, L128 …几项约定：, L146 …作分析判断：,
        # L179 …的阵容：, L192 …情报来源：, L220 …大致如下：, L224 …作为说明：, L289
        # …几项要点：), the ─-ended dash lead-ins (L7 …我猜─, L46 …略述其大概──, L183
        # …有如下者─), the 一、-三、 / 1- enumerated items, the roster lines (L184/
        # L185), and the 「」/『』-closed dialogue lines are DELIBERATE separate <p>
        # and are NOT merged (cf. ch21). L215 (…谈谈我们的纪律) ends on 律 with the
        # source's 。 dropped — a short prose transition INSIDE the L202 section,
        # NOT a heading and NOT a split; rendered as its own paragraph. L250 (…
        # 要多杀几个发动侵略战争的日本人) also ends with a dropped 。 — its own
        # paragraph (new topic follows at L251), NOT a split.
        # WATCH: the serialization coda "(第三章完，下期续载)" is glued to the tail of
        # L294 — a magazine-installment seam (cf. ch21's "(第一章完下期续载)"). Its
        # "第三章" is off-by-one from ch21's correct 第一章完 for the book's Ch1, so
        # the 三 is a 三→二 glitch (this is book Ch2); rendered to plain sense as
        # "Chapter Two" in the reading text and listed in PROGRESS.
        "merges": [(31, 32), (221, 222), (279, 280)],
        # three couplet-style standalone sub-headings (NO number prefix; cf.
        # ch11/ch14/ch21), each its own plain <p> in the source: L3 一警百清除障碍
        # 以展示威力, L40 一波未平一波又起内部又出祸害, L64 人事经费时常困扰着陷区单位.
        # TWO glued sub-headings fused onto a paragraph tail: L108 …反而不去动脑筋了。
        # + 异地重逢又展开一场曲境探幽, L202 …分出来另做记述。+ 从铁的纪律生杀权限说到
        # 道德观念 (which L203-L204 then enumerate as 作风风气/铁的纪律/生杀权限/道德观念).
        "glued": {
            108: "异地重逢又展开一场曲境探幽",
            202: "从铁的纪律生杀权限说到道德观念",
        },
        "standalone": [3, 40, 64],
    },
    "ch23": {
        "file": "24_index-split-000-0022.txt",
        "title": "第三章 爱国情操 道德规范",
        # A SHORT framing chapter. Source XHTML parses to 1 <h2> + 8 <p>, zero
        # mismatches (no <h1>, no <br/>, no images, no [\d+] note markers). The
        # txt has 10 lines: L1 running header, L2 <h2> title, L3 couplet
        # sub-heading, L4-L10 = 7 body paragraphs, all ending on terminal
        # punctuation, so 1:1 with no merges. L3 初生之犊组成了一枝生力军 is the
        # opening COUPLET-style sub-heading (NO number prefix; cf.
        # ch11/ch14/ch21/ch22) -> standalone.
        # GLITCHES (render to plain sense; not footnoted): L6 百性 for 百姓
        # (homophone), L10 交赋 for 交付.
        "drop": 2,             # running header + <h2> chapter title
        "merges": [], "glued": {},
        "standalone": [3],     # 初生之犊组成了一枝生力军
    },
    "ch24": {
        "file": "25_index-split-000-0023.txt",
        "title": "第四章 三面受敌 一往无前",
        # A FULL chapter. Source XHTML parses to 1 <h2> + 166 <p>, proven p-by-p
        # against the txt body (166 body lines, zero mismatches; no <h1>, no
        # <br/>, no images, no [\d+] note markers; the txt's 167 wc -l vs 168
        # awk-NR is a no-trailing-newline artifact). ch24 shares its chapter
        # title AND opening couplet with ch14 (三面受敌 一往无前); keep them
        # consistent. drop=2 (running header + <h2> title).
        "drop": 2,
        # THREE merges where a source <p> boundary severs one sentence:
        #   L26/L27  …有关抗日 | 活动)          (克莱登's parenthetical, 抗日活动 split)
        #   L106/L107 …随时会出去逮 | 捕「抗日份子」。 (逮捕 split)
        #   L11/L12  (一) | (四)请派员…          a STRAY orphan enumerator "(一)"
        #            (a digitization glitch: a dangling sub-enumerator between the
        #            (三)-continuation L10 and (四) L12 of the 「新案」 list) merged
        #            forward into (四) so no orphan "(1)" paragraph appears; the
        #            stray 一 is conserved in data/zh and noised in the reading.
        # NOT merged (DELIBERATE separate <p>, roster / list / lead-in, cf.
        # ch21/ch22): the 「新案」 list items L7-L12 (一)-(四); the ：/﹔-ended
        # lead-ins (L34 名称如下：, L153 …参差之处，如﹔); the dash-lead-in roster
        # of gendarmerie district-commands (L57, ends 无线电通报); the sanction-
        # case roster L125 (三cases run together, ends on the name 何行健) and its
        # continuation L126; the 申报 news-article <p> (L141-L148, each opening 「);
        # the 沪上往事 / 申报 juxtaposition lines L154-L159. L33 ends on a complete
        # parenthetical (等于分局) and L34 名称如下： is a soft list lead-in — kept
        # separate, NOT merged.
        "merges": [(11, 12), (26, 27), (106, 107)],
        # THREE tail-glued section headings (fused onto a paragraph tail; cf.
        # ch16/ch22). The chapter anatomizes the "three-sided enemy" in five
        # sections, each a heading: (一)公共租界巡捕房 (head-glued L33), (二)法租界
        # 巡捕房 (standalone L38), then these:
        #   L46  …当另以专页记之。+ 「日本宪兵队」惨无人道   (the gendarmerie section)
        #   L95  …日本宪兵的控制之下。+ 罪恶昭彰的「七十六号」 (the No.76 section; note
        #        its tail ends in a full-width 」 — easy to miss in a non-terminal
        #        scan — but reads as the section heading, parallel to L46)
        #   L122 …道德传统。+ 以雷霆万钧之势打击魔鬼         (the sanctions section)
        "glued": {
            46: "「日本宪兵队」惨无人道",
            95: "罪恶昭彰的「七十六号」",
            122: "以雷霆万钧之势打击魔鬼",
        },
        # ONE head-glued numbered section heading (fused onto the paragraph HEAD;
        # its sibling (二)法租界巡捕房 L38 is standalone):
        #   L33  (一)公共租界巡捕房 + 公共租界中央巡捕房，设于…
        "glued_head": {33: "(一)公共租界巡捕房"},
        # standalone sub-headings: L3 opening couplet (REUSE ch14's rendering),
        # L38 the (二)法租界巡捕房 section heading.
        "standalone": [3, 38],
    },
    "ch25": {
        "file": "26_index-split-000-0024.txt",
        "title": "第五章 全面检讨奇人奇事",
        "drop": 2,             # running header + <h2> chapter title
        # A FULL chapter. Source XHTML parses to 1 <h2> + 191 <p> + 2 <br/>,
        # zero mismatches (no <h1>, no <img>, no [\d+] note markers), proven
        # p-by-p: after drop=2 the txt's 193 body lines map to the 191 <p> once
        # the two intra-<p> <br/> pairs are rejoined. NINE merges in all:
        #   TWO are the intra-<p> <br/> line breaks (a NEW trigger vs ch24 -- a
        #   <br/> INSIDE one <p>, not a <p> boundary):
        #     L46/L47  …爆破器材等。<br/>以及和主管人事的部门治商人事问题。
        #     L105/L106 …庆斌兄的确比我有见地。<br/>而况且这原是公家之物…
        #   SEVEN are source <p> boundaries that sever one sentence (first ends
        #   non-terminal), exactly the class merged since ch06 (cf. ch21/ch22/
        #   ch24). Two of them CHAIN into a <br/> pair above:
        #     L5/L6    …所处的地位不同，| 在感应上自然会各有差异。 (comma split)
        #     L45/L46/L47  …用「副本」，而秦 | 同志就得凭… (秦|同志 split, then <br/>)
        #     L52/L53  …爆破训练班之人事，应即予 | 加强，… (应即予|加强 split)
        #     L61/L62  …亦无充份之标 | 准也。」 (标|准 split, inside a quoted line)
        #     L84/L85  …离开本 | 局之立场，… (离开本|局 split)
        #     L104/L105/L106 …果真成为事实，到时 | 候虽然… (到时|候 split, then <br/>)
        #     L118/L119 …征求聂大夫的同意。结果 | 如何，… (结果|如何 split)
        # NOT merged (DELIBERATE separate <p>, cf. ch21/ch22/ch24): the quoted-
        # directive lead-ins ending ：(L10,L18,L25,L29,L41,L47… as ：/如下/如次),
        # the 1.-6. / 1.-15. enumerated directive/summary items ending ；, the
        # sub-list headers 对战区：/ 对后方：, the reader-question lead-ins, the
        # 范行-analysis list items (L175/L176 ；), and the two dash-lead-in
        # section labels 破坏部份─ (L29) and 行动部份─ (L60) -- each its OWN <p>
        # ending on ─, a run-in label introducing the quoted directive that
        # follows, rendered as its own short prose line (cf. ch20 L12 dash
        # lead-in; NOT a split, NOT a heading). The 情报部份─ label (L8) and the
        # 检讨总结─本局工作当前之缺点：label (L70) are HEAD-glued onto their content
        # in the source and kept inline as prose (run-in labels), matching how
        # the source presents them.
        "merges": [(5, 6), (45, 46), (46, 47), (52, 53), (61, 62),
                   (84, 85), (104, 105), (105, 106), (118, 119)],
        # THREE sub-headings. L3 is the opening review-section title (standalone
        # couplet, cf. ch11/ch14/ch21/ch22/ch23/ch24). L88 and L126 are the two
        # "奇人奇事" story titles fused onto a paragraph TAIL (cf. ch24; L88's ends
        # non-terminal after a space+─, L126's ends on the terminal 事 but reads
        # as the section heading for the 张啸林/范行 narrative that follows).
        "glued": {
            88: "未经许可接受了 ─一批赠与的武器经手",
            126: "有政治背景无反间作用的奇人奇事",
        },
        "standalone": [3],     # 八年抗战初期「军统局」工作检讨
    },
    "ch26": {
        "file": "27_index-split-000-0025.txt",
        "title": "第六章 泰山鸿毛 同此一掷",
        "drop": 2,             # running header + <h2> chapter title
        # A FULL chapter. Source XHTML parses to 1 <h2> + 280 <p> + 54 <br/>,
        # zero mismatches, proven byte-exact p-by-p against the txt body (after
        # drop=2 the 334 body lines map to the 280 <p> once the 54 intra-<p>
        # <br/> are accounted for); no <h1>, no <img>, no [\d+] note markers.
        # ALL 54 <br/> fall in just FOUR <p>, and they are NOT sentence-splits
        # but TABLE/roster line breaks (kept as separate rows, per CLAUDE.md's
        # "roster lines are DELIBERATE separate lines, do NOT merge") EXCEPT one
        # prose block:
        #   p#177 (34 <br/> = 35 rows): the enemy-compiled 「蓝衣社在沪所犯案件
        #     统计表」 tally of our sanctions of Japanese personnel (name/date/
        #     place/casualty/action-group) -> rows KEPT (L180-L214 body lines).
        #   p#214 (9 <br/> = 10 rows) + p#217 (9 <br/> = 10 rows): the Japanese
        #     gendarmerie's own 「大陆宪兵实录」 record of anti-Japanese incidents
        #     (July-Oct, in Japanese) -> rows KEPT.
        #   p#211 (2 <br/> = 3 segments, L248-L250): three complete reflective
        #     PROSE sentences the author set in one <p> with line breaks -> MERGED
        #     into one paragraph (cf. ch25's intra-<p> <br/> prose merge; one <p>
        #     = one paragraph). This is the ONLY <br/>-prose merge in the chapter.
        # SEVEN source-<p> boundaries that sever one sentence (first ends
        # non-terminal), the class merged since ch06 (cf. ch21/ch22/ch24/ch25):
        #   L25/L26   …大饭店前处理 | 之。 (处理|之, inside a quoted letter)
        #   L31/L32   …那是说在 | 安全撤退… (说在|安全撤退)
        #   L90/L91   …也正是为了一个 | 「权」宇。 (一个「权」字; source glitch 宇->字)
        #   L161/L162 …一日，在 | 江湾附近… (comma split inside the quoted 统计表)
        #   L263/L264 …「イワノフ〔伊凡诺夫〕」 | 暗杀 (the 14-Sept row's verb, a
        #             gendarmerie-table row split across the <p> boundary)
        #   L304/L305 …奋不顾身的干 | 起来了。 (干|起来了)
        #   L323/L324 …一小包(块) | 放在电车轨道上… ((块) parenthetical continuation)
        # NOT merged (DELIBERATE separate <p>, cf. ch21/ch22/ch24/ch25): the
        # quoted-telegram/letter/document lead-ins ending ：(L58/L60/L62/L65/L79/
        # L81/L108/L117/L129/L133/L176/L186/L204/L206…), the ─-ended dash lead-ins
        # (L162?→no; L162 is the merge above; the true dash lead-ins L162… are the
        # "这样的──" lines), the (一)-(六) news-report enumerated list items and the
        # 一、二、三、 three-point list (L128-L130), the two roster label lines
        # (L177 「被害者」, L178 header), the run-together Japanese-table <p>
        # (L263), and the 「」/『』-closed quoted lines. Dropped-。 breaks (L37
        # 萧氏一家满门忠贞, a new scene follows) are DELIBERATE paragraph breaks,
        # NOT splits (cf. ch21 L86/ch22 L215/L250).
        "merges": [(25, 26), (31, 32), (90, 91), (161, 162),
                   (248, 249), (249, 250), (263, 264), (304, 305),
                   (323, 324)],
        # TWO tail-glued couplet-style section headings (a short thematic phrase
        # fused onto a paragraph's TAIL after a terminal 。, ending non-terminal
        # or in a full-width 」; cf. ch22/ch24/ch25's tail-glued headings):
        #   L38  …死于敌后工作的又一例证。+ 萧氏一家满门忠贞  (the Xiao-family section;
        #        the source glues it here, then reaches the Xiao family through a
        #        narrative bridge — the declined inspection tour, then Jiang Anhua
        #        and the Xiao-house liaison station — a faithful discursive order)
        #   L76  …这就要再深一层去研究了。+ 我们的同志作了敌伪的「活人祭」 (the section
        #        on the three comrades martyred at No.76; ends in 」, which a
        #        non-terminal scan misses — the three-tell's 」 case)
        "glued": {38: "萧氏一家满门忠贞",
                  76: "我们的同志作了敌伪的「活人祭」"},
        "glued_head": {},
        # FOUR standalone sub-headings, each its own plain <p> (no glued tails/
        # heads): L3 opening couplet-style sub-heading 没有名籍生死不明的先烈们
        # (cf. ch11/ch14/ch21-25); L96 the reproduced Xu Wenqi essay's title
        # 中日战争中死难无名英雄之一; L218 the enumerated section heading 二、日本
        # 宪兵留下来的一段记录 (its "一、" sibling, the enemy-compiled 统计表 above,
        # is presented without an explicit "一、" label — a faithful numbering
        # anomaly); L277 the section heading 「抗日杀奸团」为抗战奉献牺牲.
        "standalone": [3, 96, 218, 277],
    },
    "ch27": {
        "file": "28_index-split-000-0026.txt",
        "title": "第八章 大亨之死 扑朔迷离",
        "drop": 2,             # running header + <h2> chapter title
        # A FULL chapter (the Zhang Xiaolin tycoon-death case). Source XHTML
        # parses to 1 <h2> + 136 <p>, proven byte-exact p-by-p against the txt
        # body (136 body lines after drop=2, zero mismatches; no <h1>, no <br/>,
        # no <img>, no [\d+] note markers). This chapter uses ENUMERATED 一、二、
        # 三、 SECTION headings (NOT couplet-style; cf. Part One's 一/二/三):
        #   L3   一、这件案子不一定是我们干的          (standalone, its own <p>)
        #   L64  …时有著作发表。 + 二、事实该怎么样便怎么样  (tail-glued after 。)
        #   L94  …我们有办法把你弄出来。」 + 三、一篇游戏文章写的满纸荒唐 (tail-glued
        #        after a full-width 」; cf. ch24/ch26's 」-ending tail-glued heads)
        # TWO source-<p> boundaries that sever one sentence (first ends
        # non-terminal), the class merged since ch06:
        #   L13/L14  …历经一年的谈判，始于清 | 道光二十九年(一八四九)正式成立。 (始于清|
        #            道光 split mid-phrase, inside the quoted 「上海租界问题」 引言)
        #   L41/L42  …至于林怀部这个名字，也在新闻中 | 出现过，只可惜找不到更多的当年
        #            报纸了。 (新闻中|出现过 split)
        # NOT merged (DELIBERATE separate <p>, cf. ch21-26): the ：-ended
        # quoted-document / list lead-ins (L9 说明如下：, L28 是这样的：, L29 消息
        # 称：, L88 诸如：, L97 原文如下：, L106 有十八点可资反驳者：), the closed
        # parentheticals ending 。) (L26 (…「林怀步」。), L92 (…请多原谅)), and the
        # quoted 林怀部-letter paragraphs (each opening 「) with Chen's inline
        # (1)-(19) rebuttal-reference markers embedded — including L99 which ends
        # on a trailing "(3)" marker after a terminal 。, a NEW quoted paragraph
        # (L100 opens 「) following, NOT a split. The Chen rebuttal points
        # (1)-(19) at L107-L128 are enumerated LIST items rendered as ordinary
        # paragraphs per parity, NOT section headings.
        "merges": [(13, 14), (41, 42)],
        "glued": {64: "二、事实该怎么样便怎么样",
                  94: "三、一篇游戏文章写的满纸荒唐"},
        "glued_head": {},
        "standalone": [3],     # 一、这件案子不一定是我们干的
    },
    "ch28": {
        "file": "29_index-split-000-0027.txt",
        "title": "第九章 声威大震血浪腥风",
        "drop": 2,             # running header + <h2> chapter title
        # A FULL chapter (the height-of-renown-and-blood period; continues ch27's
        # tail on the 特区法院 / 中央储备银行 offensive). Source XHTML parses to
        # 1 <h2> + 224 <p>, proven byte-exact p-by-p against the txt body (224
        # body lines after drop=2, zero mismatches; no <h1>, no <br/>, no <img>,
        # no [\d+] note markers). This chapter uses THREE ENUMERATED 一、二、三
        # SECTION headings, all STANDALONE (their own <p>, whole line = heading;
        # cf. ch27 where 2 were tail-glued):
        #   L3   一、一个特务工作者的心态与感受   (standalone)
        #   L49  二、铲除巨奸寒敌胆树立声威       (standalone)
        #   L129 三、谁来清偿这笔寃孽债           (standalone)
        # FOUR source-<p> boundaries that sever one sentence (first ends
        # non-terminal), the class merged since ch06:
        #   L80/L81   …那倒不在话下，照我们的 | 经验，一般小小不然的事… (照我们的|经验)
        #   L135/L136 …这是订有协议的—— | 「上海公共租界特区法院协议」是在… (trailing
        #             em-dash introduces the named agreement in the next <p>; source
        #             prints a glitch "——-" ASCII hyphen after the em-dash)
        #   L157/L158 …周将交涉「接收」上海法租界法院 | 事，电告南京的汪精卫。 (法院|事)
        #   L214/L215 …谁也不知道将要发生什么 | 事？有的，还莫名其妙的… (什么|事？)
        # NOT merged (DELIBERATE separate <p>, cf. ch21-27): the ：-ended
        # quoted-document / list lead-ins (L20 提示如下：, L76 补充及说明：, L94 谈话
        # 如下：, L107 说明如下：, L134 主要内容如下：, L140 主要内容如下：, L148 说明事
        # 实如下：, L170 说明如下：), and the INNER enumerated 一、二、三 DOCUMENT-CLAUSE
        # lists — the two reproduced court agreements: the 公共租界 courts agreement
        # (L137-139: 一、/二、/三、 clauses under L136's lead-in) and the 法租界
        # 会审公廨/地方法院 agreement (L143-145: 一、/二、/三、、四、 clauses under L142's
        # lead-in). These are ordinary body lines per parity (like ch27's (1)-(19)
        # rebuttal list), NOT section headings, and NOT in `standalone`. Each clause
        # excerpt is a complete terminal 。sentence (the source abridges: "其主要内容
        # 如下" — one long <p> per clause; L145 packs 三、and 四、together). L222 ends
        # non-terminal 事 but is a DROPPED-STOP glitch of a complete sentence (那是他
        # 们的事[。]); L223 opens 不过、 a distinct closing paragraph — NOT a merge.
        "merges": [(80, 81), (135, 136), (157, 158), (214, 215)],
        "glued": {},
        "glued_head": {},
        "standalone": [3, 49, 129],
    },
    "ch29": {
        "file": "30_index-split-000-0028.txt",
        "title": "第十章 祸不单行 柱折梁摧(上)",
        "drop": 2,             # running header + <h2> chapter title
        # The (上) half of a two-part chapter (ch30 = the 下 half); the
        # disaster/collapse chapter, continuing ch28's tail (the crackdown +
        # Chen's own capture). Source XHTML parses to 1 <h2> + 72 <p>, proven
        # byte-exact p-by-p against the txt body (72 body lines after drop=2,
        # zero mismatches; no <h1>, no <br/>, no <img>, no [\d+] note markers).
        # TWO enumerated 一、二 SECTION headings:
        #   L3   一、是我误了他的锦绣前程                  (standalone, its own <p>)
        #   L33  …他怎么说我就怎么答应了。 + 二、人性理性交织下的特务活动
        #        (tail-glued after a terminal 。)
        # ONE source-<p> boundary that severs one sentence (first ends
        # non-terminal), the class merged since ch06:
        #   L65/L66  …所有的问题必可负责代为 | 解决。 (代为|解决 split mid-phrase)
        # NOT merged (DELIBERATE separate <p>, cf. ch21-28): the memoir/document
        # lead-ins — L17 以下这一段…细说他这一段不平凡的历程 (a complete lead-in
        # sentence whose final 。 the source drops — a glitch, not a split; the
        # next <p> opens Liu Yuanshen's first-person account), and the ：-ended
        # lead-ins L32 原文如下：(actually L32 下面这一段…原文如下：) and L40 …也不
        # 能无疑：. These introduce the quoted 沪滨三次历险实录 memoir and the 朱敏
        # report and stay as their own lines.
        "merges": [(65, 66)],
        "glued": {33: "二、人性理性交织下的特务活动"},
        "glued_head": {},
        "standalone": [3],     # 一、是我误了他的锦绣前程
    },
    "ch30": {
        "file": "31_index-split-000-0029.txt",
        "title": "第十章 祸不单行 柱折梁摧(下)",
        "drop": 2,             # running header + <h2> chapter title
        # The (下) half of Chapter Ten (ch29 = the 上 half). Source XHTML parses
        # to 1 <h2> + 110 <p>, proven byte-exact p-by-p against the txt body
        # (110 body lines after drop=2, zero mismatches; no <h1>, no <br/>, no
        # <img>, no [\d+] note markers). The chapter carries sections 三/四/五
        # (ch29 held 一/二). Per ch31's own erratum #8, sections 一/二/三 are
        # Liu Yuanshen's (刘原深) memoir manuscript and section 四 onward is
        # again Chen's own narration, though the source marks no switch — the
        # "我" of section 四/五 is the District Chief 区长 who "led the Shanghai
        # District," i.e. Chen, narrating his OWN arrest.
        # THREE enumerated SECTION headings:
        #   L3   三、仁者之心终为幺么所乘                 (standalone, its own <p>)
        #   L22  …敬乞里公笑纳。晚朱敏拜。」 + 四、霎时间发生了巨大变故
        #        (tail-glued after a terminal 」)
        #   L76  …这该是最后的一瞥了！ + 五、保持住应有的人格与尊严
        #        (tail-glued after a terminal ！)
        # ONE source-<p> boundary that severs one sentence (first ends
        # non-terminal), the class merged since ch06:
        #   L91/L92  …尽量的 | 多了解，也许更便于应付。 (尽量的|多了解 mid-phrase)
        # NOT merged (DELIBERATE separate <p>): the ：-ended dialogue lead-ins
        # (e.g. L70 …他追问：, introducing the quoted interrogation in the next
        # <p>) and the memoir/document lead-in L4 …其文如下：. The inline
        # 第一、/第二、 enumerations INSIDE a single <p> (L12 p#10, L108 p#106)
        # and the 三、四尺 number-range (p#67) are body text, NOT headings.
        "merges": [(91, 92)],
        "glued": {22: "四、霎时间发生了巨大变故",
                  76: "五、保持住应有的人格与尊严"},
        "glued_head": {},
        "standalone": [3],     # 三、仁者之心终为幺么所乘
    },
    "ch31": {
        "file": "32_index-split-000-0030.txt",
        "title": "写在「英雄无名」第三部专书出版前",
        "drop": 2,             # running header + <h1> front-matter title
        # The Part-Three closing note. Source XHTML parses to 1 <h1> + 14 <p>,
        # proven byte-exact p-by-p (14 body lines after drop=2, zero
        # mismatches; no <h2>, no <br/>, no <img>, no [\d+] note markers). The
        # enumerated 一、–八、 items are an ERRATA/addendum LIST correcting
        # earlier chapters (each cites an earlier chapter by 页/page number that
        # our EPUB does not carry); they are DOCUMENT-CLAUSE body lines per
        # parity, NOT section headings, so no standalone/glued entries. No
        # severed-<p> boundaries.
        "merges": [], "glued": {}, "glued_head": {}, "standalone": [],
    },
    "ch32": {
        "file": "33_index-split-000-0031.txt",
        "title": "自序",
        # drop=3 (cf. ch10/ch20, the part prefaces): running header +
        # <h1>平津地区绥靖戡乱 (the Part Four super-title, rendered from book.json's
        # `part` field) + <h3>自序 (the preface's own title, re-emitted from
        # book.json title_en "Author's Preface"). Confirmed p-by-p against the
        # source XHTML: 1 <h1> + 1 <h3> + 35 <p>, zero mismatches; no <h2>, no
        # <br/>, no <img>, no [\d+] note markers. The 35 body <p> (L4-L38) map
        # 1:1 to the 35 source <p> — every <p> ends terminal, so NO severed-<p>
        # boundaries / mid-phrase splits. NO section headings inside: the two
        # enumerated-LOOKING line starts (L22 五个指挥室分布在… and L37 三十八年
        # 一月杪…) are BODY sentences opening on a numeral, NOT headings, kept as
        # ordinary body lines. Digitization glitches (dropped 。 mid-<p> at L10/
        # L11/L13/L17/L19/L26/L29, mismatched guillemets ﹃﹄, a stray ？ at L17,
        # a stray 》 at L19) are rendered to plain sense, listed in PROGRESS.md,
        # not merged and not footnoted (mechanical typos).
        "drop": 3,
        "merges": [], "glued": {}, "glued_head": {}, "standalone": [],
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
    glued_head = spec.get("glued_head", {})   # heading FUSED onto a paragraph HEAD
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
        # split a glued LEADING heading (heading fused onto the paragraph head)
        if ln in glued_head:
            head = glued_head[ln]
            assert text.startswith(head), \
                "%s L%d does not start with glued_head %r" % (cid, ln, head)
            rest = text[len(head):]
            out.append("### " + head)
            out.append(rest)
            verify_out.append(head)
            verify_out.append(rest)
        # split a glued trailing heading
        elif ln in glued:
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
