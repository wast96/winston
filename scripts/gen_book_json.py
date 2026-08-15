#!/usr/bin/env python3
"""One-shot generator for this book's book.json structure.

Offset is CONSTANT at 36 across the whole body (printed = pdf - 36), verified
at four chapter openers spanning the book (ch2 46->82, ch5 148->184,
ch10 307->343, ch12 375->411). Section opener pdf pages are computed
printed+36; spot-verify each at batch time (an inline full-page plate can nudge
a single section opener by +-1).
"""
import json

OFFSET = 36

# (chapter_zh, chapter_en, subtitle_zh, subtitle_en, [(sec_zh, sec_en, printed), ...])
CH = [
 ('第一章 “枪杆子”与“刀把子”', "Chapter 1. “The Gun” and “The Knife”",
  '恐怖镇压催生特别组织', 'Terror and Repression Breed a Special Organization', [
   ('现代中国的第一个“特务”组织', "Modern China’s First “Secret Service” Organization", 1),
   ('中央特科', 'The Central Special Branch', 5),
   ('巅峰对决', 'Showdown at the Summit', 10),
   ('国家政治保卫局', 'The State Political Security Bureau', 14),
   ('苏区肃反', 'Purging Counter-revolutionaries in the Soviet Areas', 18),
   ('红军长征的“杀手锏”', "The Red Army’s “Trump Card” on the Long March", 21),
   ('落脚陕北的第一步', 'The First Step to a Foothold in Northern Shaanxi', 25),
   ('密晤少帅的神秘人', 'The Mysterious Man Who Secretly Met the Young Marshal', 34),
   ('“特区”与“特务”', "“Special Zones” and “Special Agents”", 38),
  ]),
 ('第二章 暗战', 'Chapter 2. Secret War',
  '党派合作中的隐蔽斗争', 'The Hidden Struggle Within a United Front', [
   ('周恩来遇险', 'Zhou Enlai in Danger', 46),
   ('“中统”和“军统”赫然成局', "“Zhongtong” and “Juntong” Take Formal Shape", 51),
   ('出逃事件！', 'The Defection Incident!', 58),
   ('中共中央社会部', 'The CCP Central Social Affairs Department', 62),
   ('陕甘宁边区保安处', 'The Shaanxi-Gansu-Ningxia Border Region Security Office', 68),
   ('知青进入特训班', 'Educated Youth Enter the Special Training Class', 73),
   ('延安防线', "The Yan’an Defense Line", 84),
   ('大布局', 'The Grand Deployment', 88),
  ]),
 ('第三章 从“地下”到“地上”', "Chapter 3. From “Underground” to “Aboveground”",
  '公开与秘密结合的活动方式', 'Combining Open and Secret Methods of Operation', [
   ('遍地开花的“八办”', "The “Eighth Route Army Offices” Blossom Everywhere", 98),
   ('绝密的“重庆联络图”', "The Top-Secret “Chongqing Contact Chart”", 105),
   ('“闲棋冷子”与“战略间谍”', "“Idle Chessmen” and “Strategic Spies”", 108),
   ('为党赚钱的“公司”', "The “Companies” That Made Money for the Party", 114),
   ('遥远的“海外工作”', "Distant “Overseas Work”", 118),
   ('西安大斗法的谜底', "The Answer to the Great Contest in Xi’an", 122),
   ('周恩来的情报搜集方式——广交朋友', "Zhou Enlai’s Way of Gathering Intelligence: Making Friends Widely", 128),
  ]),
 ('第四章 拔钉子', 'Chapter 4. Pulling Out the Nails',
  '维护政权安全的隐蔽斗争', 'The Covert Struggle to Secure Political Power', [
   ('“双重政权”', "“Dual Regimes”", 135),
   ('争抢“宝葫芦”', "Fighting Over the “Treasure Gourd”", 139),
   ('“红色福尔摩斯”出招', "The “Red Sherlock Holmes” Makes His Move", 142),
   ('反腐风暴', 'The Anti-Corruption Storm', 143),
   ('“护送出境”', "“Escorted Out of the Territory”", 144),
  ]),
 ('第五章 深入虎穴', "Chapter 5. Into the Tiger’s Den",
  '中共情报员全线出击', 'CCP Intelligence Officers Go on the Offensive', [
   ('“东方大黑暗”！', "“The Great Darkness in the East”!", 148),
   ('是谁向斯大林通报德国侵苏情报？', "Who Warned Stalin of Germany’s Invasion of the USSR?", 151),
   ('毛泽东的情报分析方式——调查研究', "Mao Zedong’s Method of Intelligence Analysis: Investigation and Study", 157),
   ('延安出击', "Yan’an Strikes Out", 161),
   ('西安织网', "Weaving the Net in Xi’an", 164),
   ('战地军情急', 'Urgent Military Intelligence at the Front', 167),
   ('突破“国防线”！', "Breaking Through the “National Defense Line”!", 171),
   ('挑战情报强国', 'Challenging the Intelligence Powers', 175),
  ]),
 ('第六章 东方大谍', 'Chapter 6. The Great Spies of the East',
  '国际战略情报的跨国竞争', 'The Transnational Contest for Strategic Intelligence', [
   ('上海滩有个日本“国策学校”', "A Japanese “State-Policy School” on the Shanghai Bund", 187),
   ('“机关”中的机关', "The Agency Within the “Agency”", 191),
   ('延安也有个日本学校', "Yan’an Had a Japanese School Too", 195),
   ('巧施离间计', 'A Deft Stratagem to Sow Discord', 198),
   ('从“巴巴罗萨”到“关特演”', "From “Barbarossa” to the “Kwantung Army Special Maneuvers”", 200),
   ('绝密情报深藏虎穴', "Top-Secret Intelligence Hidden Deep in the Tiger’s Den", 204),
   ('最高统帅的最高责任', "The Supreme Commander’s Supreme Responsibility", 207),
   ('异国兄弟，生死相助', 'Brothers from Foreign Lands, Aiding Unto Death', 214),
  ]),
 ('第七章 锄奸', 'Chapter 7. Rooting Out Traitors',
  '复杂深奥的反间谍之战', 'The Deep and Intricate War of Counter-espionage', [
   ('行刺总司令的“双料特务”', "The “Double Agent” Who Tried to Kill the Commander-in-Chief", 220),
   ('大安庄来了个“好鬼子”', "A “Good Devil” Comes to Da’anzhuang", 224),
   ('军统总台有个“党支部”', "A “Party Branch” Inside Juntong’s Main Station", 226),
   ('关中有个“双重间谍”', "A “Double Agent” in Guanzhong", 232),
   ('“雷公咋不打毛泽东？”', "“Why Doesn’t the Thunder God Strike Mao Zedong?”", 238),
   ('反间计', 'The Counter-espionage Stratagem', 241),
  ]),
 ('第八章 延安反特第一案', "Chapter 8. Yan’an’s First Great Counter-espionage Case",
  '“化敌为我服务”的制胜方针', "The Winning Policy of “Turning the Enemy to Serve Us”", [
   ('军统有个“死间”特训班', "Juntong’s Special Training Class for “Expendable Agents”", 246),
   ('放线与织网', 'Casting the Line and Weaving the Net', 248),
   ('大案惊天！', 'A Case to Shake the Heavens!', 252),
   ('侦控特务联络员', "Tracking the Agents’ Couriers", 255),
   ('深挖独立小组', "Digging Out the Independent Cell", 258),
   ('反用特务', 'Turning Enemy Agents to Our Use', 259),
  ]),
 ('第九章 “抢救运动”', "Chapter 9. The “Rescue Campaign”",
  '政治运动中反特斗争扩大化', 'How a Political Campaign Broadened the Hunt for Agents', [
   ('“侦破”与“运动”同步', "“Case-Cracking” in Step with the “Campaign”", 269),
   ('从“老号疑犯”到“山东肃托”', "From the “Old-Case Suspects” to the “Shandong Anti-Trotskyist Purge”", 273),
   ('“四大特务”和“红旗党”', "The “Four Great Agents” and the “Red-Flag Party”", 276),
   ('“外来知识分子”中“特务如麻”？', "Were the “Outside Intellectuals” “Riddled with Agents”?", 281),
   ('“群众运动”加“逼、供、信”', "“Mass Campaigns” Plus “Coerce, Confess, Believe”", 283),
   ('毛泽东道歉', 'Mao Zedong Apologizes', 288),
   ('《刘巧儿告状》', "“Liu Qiao’er Brings Suit”", 295),
   ('到前线去自己做结论！', 'Go to the Front and Draw Your Own Conclusions!', 299),
  ]),
 ('第十章 阳谋', 'Chapter 10. The Open Scheme',
  '和战之间的秘密较量', 'The Secret Contest Between Peace and War', [
   ('秘密战线提前较劲', 'The Secret Front Locks Horns Early', 307),
   ('假戏真做的重庆谈判', 'The Chongqing Negotiations: A Play Performed in Earnest', 311),
   ('是谁错过了历史机遇？', 'Who Missed the Historic Opportunity?', 315),
   ('激活“冷藏间谍”', "Activating the “Cold-Storage Spies”", 320),
   ('中国还有“民主联军”', "China Also Had a “Democratic Allied Army”", 323),
   ('中共情报界的“后三杰”', "The “Latter Three Heroes” of CCP Intelligence", 325),
   ('延安大撤退', "The Great Withdrawal from Yan’an", 328),
   ('延安游击队', "The Yan’an Guerrillas", 336),
  ]),
 ('第十一章 大策反', 'Chapter 11. The Great Turning',
  '秘密斗争的至高境界', 'The Highest Art of Secret Struggle', [
   ('黄土高原上演电子对抗', 'Electronic Warfare on the Loess Plateau', 348),
   ('谁先收到胡宗南的作战电报？', "Who Received Hu Zongnan’s Battle Orders First?", 352),
   ('情报工作最成功的时期', 'The Most Successful Period of Intelligence Work', 356),
   ('“华北五烈士”', "The “Five Martyrs of North China”", 357),
   ('不战而屈人之兵', "Subduing the Enemy Without a Fight", 360),
   ('中将之死', 'Death of a Lieutenant General', 367),
   ('建国大业', 'The Great Enterprise of Founding the Nation', 370),
  ]),
 ('第十二章 明暗易位', 'Chapter 12. Light and Dark Change Places',
  '走上执政舞台的强力机构', 'A Powerful Apparatus Takes the Governing Stage', [
   ('中国公安“一百单八将”', "China’s Public Security “Hundred-and-Eight Heroes”", 375),
   ('西进！南下！', 'West! South!', 379),
   ('哪个国家最早反恐？', 'Which Country Fought Terror First?', 384),
   ('公安局长也挨整', 'Even the Police Chiefs Were Purged', 387),
   ('“砸烂公检法！”', "“Smash the Police, Procuratorate, and Courts!”", 388),
   ('发掘文化基因', 'Excavating the Cultural Gene', 390),
  ]),
]

structure = []

# Front matter: Preface (own printed sequence 1-3, PDF 33-35)
structure.append({
    "level": 1, "id": "ch00", "chapter": 0,
    "matter": "front",
    "title": "前言 探秘",
    "title_en": "Preface: Probing the Secret",
    "pdf_page": 33, "printed_page": 1,
    "sections": [],
})

for ci, (czh, cen, subzh, suben, secs) in enumerate(CH, start=1):
    cid = "ch%02d" % ci
    first_printed = secs[0][2]
    chap = {
        "level": 1, "id": cid, "chapter": ci,
        "title": czh,
        "subtitle": subzh,
        "title_en": "%s: %s" % (cen, suben),
        "pdf_page": first_printed + OFFSET,
        "printed_page": first_printed,
        "sections": [],
    }
    for si, (szh, sen, printed) in enumerate(secs, start=1):
        chap["sections"].append({
            "id": "%ss%02d" % (cid, si),
            "section": si,
            "title": "%d. %s" % (si, szh),
            "title_en": "%d. %s" % (si, sen),
            "pdf_page": printed + OFFSET,
            "printed_page": printed,
        })
    structure.append(chap)

# Back matter: Afterword (后记, PDF 431-434, printed 395-398)
structure.append({
    "level": 1, "id": "ch13", "chapter": 13,
    "matter": "back",
    "title": "后记",
    "title_en": "Afterword",
    "pdf_page": 431, "printed_page": 395,
    "sections": [],
})

book = json.load(open("book.json", encoding="utf-8"))

# --- Step 0a: EPUB metadata ---
meta = {
    "deliverable": "out/chinas_secret_war.epub",
    "title_en": "China's Secret War",
    "subtitle_en": "A Documentary Record of the CCP's Intelligence and Security Work",
    "title_zh": "中国秘密战：中共情报、保卫工作纪实",
    "title_file_as": "China's Secret War",
    "author_en": "Hao Zaijin",
    "author_zh": "郝在今",
    "author_file_as": "Hao, Zaijin",
    "year": 2015,
    "publication_date": "2015-01-01",
    "publisher": "Gold Wall Press (金城出版社)",
    "language": "en",
    "source_language": "zh",
    "source_script": "zh-Hans",
    "series": "Winston Translations",
    "series_index": 10,
    "rights": "Original work © the author and Gold Wall Press. This English translation is an independent, non-commercial, annotated edition prepared for private study.",
    "source_ref": "中国秘密战：中共情报、保卫工作纪实 (最新升级图文版 / 2nd ed.), 北京: 金城出版社, 2015. ISBN 978-7-5155-1071-2. Scanned copy: Internet Archive (archive.org/details/zhongguomimizhan0000unse), from Contra Costa County Library.",
    "description": (
        "A veteran Chinese literary-historical journalist's documentary account of "
        "the hidden front of the Chinese Communist Party: the intelligence and "
        "internal-security services that grew up alongside its army, from the "
        "\"special work\" cells born of the 1927 terror through the Central Special "
        "Branch, the wartime spy duels with the Nationalists and the Japanese, the "
        "excesses of the Yan'an \"Rescue Campaign,\" and the transformation of a "
        "clandestine party apparatus into the public-security organs of a new state. "
        "Built on the author's interviews with hundreds of surviving intelligence "
        "and security veterans."
    ),
    "subjects": [
        "History / Asia / China",
        "History / Military / Intelligence & Espionage",
        "Political Science / Political Freedom & Security / Intelligence",
        "History / Modern / 20th Century",
    ],
    "source_note": (
        "Image-only PDF scan, 436 pages, no text layer (Internet Archive, from "
        "Contra Costa County Library). Simplified Chinese, horizontal, left-to-right. "
        "Structure: cover and title/CIP pages (PDF 1-4); a photo-plate section "
        "interleaved with the printed table of contents (PDF 5-32, its own folio "
        "sequences); Preface 前言 探秘 (PDF 33-35, own sequence, printed 1-3); body "
        "12 chapters / 86 numbered sections (PDF 37-430, printed 1-394, offset "
        "constant: printed = pdf - 36); a source-note / interviewee section and the "
        "Afterword 后记 (PDF 427-434, printed ~391-398); library endpapers (PDF "
        "435-436). The book carries its OWN apparatus of source notes citing the "
        "author's interviews; detect and handle with detect_notes.py at batch time. "
        "Verso pages print a vertical running title in the outer (left) margin; crop "
        "before OCR. This is the '最新升级图文版' (newest upgraded illustrated edition)."
    ),
    "translator_note": [
        "This is an English translation of <i>中国秘密战：中共情报、保卫工作纪实</i> "
        "(<i>China's Secret War: A Documentary Record of the CCP's Intelligence and "
        "Security Work</i>) by Hao Zaijin, prepared from an image-only scan with no "
        "digital text layer.",
        "The book is reportage (<i>报告文学</i>), not academic history: it is built on "
        "the author's own interviews with surviving intelligence and security "
        "veterans and is told in a brisk, colloquial, frequently editorializing "
        "voice. That voice has been kept. Where the book's factual claims can be "
        "checked against the documentary record, the footnotes say whether the "
        "account is corroborated, uncorroborated, or contradicted; where it reflects "
        "the author's political vantage as a sympathetic insider, the notes say so.",
        "Chinese personal and place names use pinyin except for forms with a settled "
        "English convention. Intelligence-service terms (中统, 军统, 中央特科, 社会部) "
        "are glossed at first appearance and listed in the glossary. Footnotes cite "
        "the book's own printed page numbers. Damaged or uncertain readings from the "
        "scan are flagged honestly rather than smoothed over.",
    ],
    "pdf_end": 434,
    "printed_end": 398,
}
book.update(meta)
# drop stub keys that no longer apply
for k in ["uid", "subject", "_source_note"]:
    book.pop(k, None)

book["structure"] = structure
json.dump(book, open("book.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
n_sec = sum(len(c["sections"]) for c in structure)
print("wrote structure: %d top-level units, %d sections" % (len(structure), n_sec))
