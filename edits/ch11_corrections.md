# ch11 corrections-pass edits (source-dependent faithfulness items)
#
# Resolves the three ch11 flags logged in PROGRESS.md's R04 entry, each
# crop-verified against source.pdf. Applied with
# scripts/apply_edits.py --suffix corrections ch11. The R04 register edits in
# edits/ch11_edits.md are already applied (committed a0c5d30) and NOT re-run.
#
# Verified crops (printed folios cited):
#  - folio 358 (pdf 394): 潜伏...特务悄悄下毒，幸亏警卫人员不让毛泽东吃死鱼。
#    The source is terse: it poisons the meal (下毒) then names the "dead fish"
#    (死鱼) with no separate antecedent. The old English inherited the dangling
#    "the dead fish." TOUCH gives it the fish antecedent the source implies;
#    no fact added (the poisoned dish was the fish).
#  - folio 368 (pdf 404): 这保定军校是中国的第一军校，出了国军总司令蒋介石。…
#    而蒋介石不过上了日军的士官学校。 The paragraph both credits Baoding with
#    "producing" Chiang and says his real schooling was the Japanese officers'
#    school. Rendered as printed; NOTE-ADD carries the checked record (Wu Shi
#    was a full Baoding academy graduate, 3rd class 1915; Chiang passed through
#    a Baoding preparatory class in 1906 before Japan, and is only loosely
#    counted an alumnus — which is why the two clauses sit oddly together).
#  - folio 370 (pdf 406): 女党员肖明华在遗书中这样安排自己的遗骨：
#    "就让她在台湾吧。" The testament refers to her own remains in the third
#    person (她/"her"); the English is faithful and the NOTE-ADD says so.

### p358 [T6] TOUCH
OLD: quietly poisoned his food; luckily the guards would not let Mao eat the dead fish
NEW: quietly poisoned a fish dish; luckily the guards would not let Mao eat the dead fish
WHY: 悄悄下毒，幸亏警卫人员不让毛泽东吃死鱼。 The source poisons the meal and then names the "dead fish"; "his food" left the later "the dead fish" without a referent. Naming the poisoned dish a fish (which the source's 死鱼 makes plain) restores the antecedent without adding any fact.

NOTE-ADD
ANCHOR: it produced the Nationalist commander-in-chief Chiang Kai-shek
NOTE: The Baoding Military Academy (1902&#8211;1923) trained many of the Nationalists' senior generals, Wu Shi and Bai Chongxi among them, both full graduates. Chiang Kai-shek's tie to it is looser: he passed through a Baoding army preparatory class in 1906 and then left for Japan's Shinbu Gakk&#333; without completing the officer course, so sources differ on whether to count him a Baoding alumnus. That is why the same paragraph can both credit the academy with &#8220;producing&#8221; him and add, a few lines on, that his real schooling was the Japanese officers' school.
WHY: without the note the sentence reads as a plain contradiction; it is the author's loose usage, and the record is worth stating.

NOTE-ADD
ANCHOR: Just let her stay in Taiwan
NOTE: The testament refers to her own remains in the third person &#8212; &#8220;her&#8221; &#8212; as the original does (&#23601;&#35753;&#22905;&#22312;&#21488;&#28286;&#21543;). Xiao Minghua was executed in Taipei in 1950, aged 28; her wish was that her remains be left in Taiwan, though in 1982 they were brought back to the mainland.
WHY: the third-person self-reference is the source's, not a translation slip; the reader should know it was deliberate.
