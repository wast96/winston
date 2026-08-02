#!/usr/bin/env python3
"""B07 apparatus merge: add glossary rows, footnotes, and figure specs for
ch17-ch19. Idempotent-ish: glossary rows are added only if the zh key is absent;
notes/figures for a unit are REPLACED (so re-running is safe)."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(name):
    return json.load(open(os.path.join(ROOT, name), encoding="utf-8"))


def save(name, obj):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1)
        fh.write("\n")


# ---- glossary ----
g = load("glossary.json")
PEOPLE = {
 "陈训畲": ("Chen Xunshe", "Chén Xùnshē", "attested", "Younger brother of Chen Bulei; head of the Shanghai branch of the Kuomintang&#8217;s Central Daily News."),
 "陈布雷": ("Chen Bulei", "Chén Bùléi", "attested", "Chiang Kai-shek&#8217;s chief secretary and speechwriter; elder brother of Chen Xunshe."),
 "陈宝骅": ("Chen Baohua", "Chén Bǎohuá", "attested", "A cousin of Chen Lifu; a Kuomintang official in Shanghai during the resistance."),
 "潘鲁岩": ("Pan Luyan", "Pān Lǔyán", "attested", "Manager of the Tongyi Company."),
 "李直夫": ("Li Zhifu", "Lǐ Zhífū", "provisional", "A Kuomintang-side collaborator in opening the Hong Kong&#8211;Haiphong transport line."),
 "吴铁城": ("Wu Tiecheng", "Wú Tiěchéng", "attested", "Kuomintang statesman; former Guangdong governor and later overseas department minister."),
 "胡志明": ("Ho Chi Minh", "Hú Zhìmíng", "decided", "Vietnamese revolutionary leader (1890&#8211;1969); the conventional English form is used. See the footnote in Chapter 17 on the anachronism of the memoir&#8217;s account."),
 "许世英": ("Xu Shiying", "Xǔ Shìyīng", "attested", "Chairman of the Nationalist government&#8217;s Central Relief Commission."),
 "屈映光": ("Qu Yingguang", "Qū Yìngguāng", "attested", "Style name Wenliu (1883&#8211;1973), from Linhai, Zhejiang; briefly Zhejiang&#8217;s military governor in 1916; vice-chairman of the Relief Commission from 1938."),
 "区梦觉": ("Ou Mengjue", "Ōu Mèngjué", "attested", "Guangdong Communist woman cadre active in the resistance."),
 "陈涤": ("Chen Di", "Chén Dí", "provisional", "Husband of Deng Xianyu; said in the memoir to have captained the warship Zhongshan; tortured to death by the Japanese in Hong Kong for refusing a puppet post."),
 "陈策": ("Chen Ce", "Chén Cè", "decided", "The Kuomintang &#8216;one-legged admiral,&#8217; known in English as Chan Chak; nephew&#8217;s-uncle to Chen Di. Pinyin used in the text; Chan Chak noted here."),
 "邓先玉": ("Deng Xianyu", "Dèng Xiānyù", "attested", "Christian physician who sheltered the author in Hong Kong; wife of Chen Di."),
 "陈小江": ("Chen Xiaojiang", "Chén Xiǎojiāng", "attested", "Son of Chen Di and Deng Xianyu; later a Xinhua News Agency reporter."),
 "袁溥之": ("Yuan Puzhi", "Yuán Pǔzhī", "attested", "An old friend and &#8216;elder sister&#8217; in whose home the author later lodged."),
 "黄成": ("Huang Cheng", "Huáng Chéng", "provisional", "Wife of Chen Xiaojiang."),
 "顾嘉棠": ("Gu Jiatang", "Gù Jiātáng", "attested", "A Green Gang chief who had fled from Shanghai to Hong Kong; helped arrange the refugee ship out of occupied Kowloon."),
 "王新衡": ("Wang Xinheng", "Wáng Xīnhéng", "attested", "A friend of Chiang Ching-kuo and figure in the Military Statistics Bureau."),
 "蒋经国": ("Chiang Ching-kuo", "Jiǎng Jīngguó", "decided", "Chiang Kai-shek&#8217;s son; the conventional Wade&#8211;Giles English form is used."),
 "杨云史": ("Yang Yunshi", "Yáng Yúnshǐ", "attested", "Poet, once secretary-general to Wu Peifu; lodged with the author in Hong Kong and died there."),
 "吴佩孚": ("Wu Peifu", "Wú Pèifú", "attested", "Northern warlord of the 1920s."),
 "潘小萼": ("Pan Xiao'e", "Pān Xiǎo&#8217;è", "provisional", "Secretary-general of the Chinese Red Cross headquarters; a schoolmate of Song Meiling&#8217;s wife."),
 "张仲仁": ("Zhang Zhongren", "Zhāng Zhòngrén", "attested", "Former education minister of the Northern Warlord government; a poet in Hong Kong exile."),
 "秦联奎": ("Qin Liankui", "Qín Liánkuí", "provisional", "A well-known lawyer in Hong Kong exile."),
 "王绍鏊": ("Wang Shao'ao", "Wáng Shào&#8217;áo", "attested", "Later one of New China&#8217;s first vice-ministers of finance."),
 "叶恭绰": ("Ye Gongchuo", "Yè Gōngchuò", "attested", "Former transport minister of the Northern government; scholar and collector."),
 "胡泳骐": ("Hu Yongqi", "Hú Yǒngqí", "provisional", "Insurance-company owner and a founder of the Tuesday Dining Club."),
 "彭泽民": ("Peng Zemin", "Péng Zémín", "attested", "Kuomintang Central Committee member and noted physician of Chinese medicine."),
 "徐采臣": ("Xu Caichen", "Xú Cǎichén", "provisional", "A chief disciple of Du Yuesheng."),
 "王艮仲": ("Wang Genzhong", "Wáng Gěnzhòng", "attested", "A progressive figure of the Shanghai Local Association."),
 "李南香": ("Li Nanxiang", "Lǐ Nánxiāng", "attested", "A professor in Chen Zhigao&#8217;s progressive study circle; in contact with the Party."),
 "张太雷": ("Zhang Tailei", "Zhāng Tàiléi", "attested", "Early Communist leader; interpreter to the Soviet advisers during the Northern Expedition."),
 "张笃和": ("Zhang Duhe", "Zhāng Dǔhé", "provisional", "Helped smuggle Dong Biwu out of Wuhan in 1927."),
 "赵畹华": ("Zhao Wanhua", "Zhào Wǎnhuá", "attested", "A woman comrade of the Northern Expedition years; helped get Dong Biwu out of Wuhan."),
 "叶蓬": ("Ye Peng", "Yè Péng", "attested", "The Wang Jingwei puppet regime&#8217;s &#8216;defense minister.&#8217;"),
 "杨度": ("Yang Du", "Yáng Dù", "attested", "One of the &#8216;six gentlemen of the Chouan Society&#8217; who urged Yuan Shikai to become emperor; in old age a secret Communist Party member."),
 "马寅初": ("Ma Yinchu", "Mǎ Yínchū", "attested", "Economist, later famous for advocating population control."),
 "史慰慈": ("Shi Weici", "Shǐ Wèicí", "provisional", "Daughter of Zhu Libo."),
 "朱文央": ("Zhu Wenyang", "Zhū Wényāng", "provisional", "Cai Shuhou&#8217;s second wife; a resistance activist and writer."),
 "李桐村": ("Li Tongcun", "Lǐ Tóngcūn", "provisional", "A Shanghai banking-circle commissioner sent to recover goods from occupied Hong Kong."),
 "赵乐天": ("Zhao Letian", "Zhào Lètiān", "provisional", "A Shanghai banking-circle commissioner sent to occupied Hong Kong."),
 "骆剑冰": ("Luo Jianbing", "Luò Jiànbīng", "provisional", "A comrade who wrote the mistaken memorial for the author in the Xinhua Daily."),
 "杨惠敏": ("Yang Huimin", "Yáng Huìmǐn", "attested", "The Girl Guide who swam Suzhou Creek in 1937 to bring a flag to the Eight Hundred Heroes at the Sihang Warehouse."),
 "谢晋元": ("Xie Jinyuan", "Xiè Jìnyuán", "attested", "Colonel who led the &#8216;Eight Hundred Heroes&#8217; defending the Sihang Warehouse in 1937."),
 "余汉谋": ("Yu Hanmou", "Yú Hànmóu", "attested", "Senior Kuomintang general of Guangdong; a Whampoa-era student of Liao Zhongkai."),
 "廖仲恺": ("Liao Zhongkai", "Liào Zhòngkǎi", "attested", "Kuomintang left leader assassinated in 1925; husband of He Xiangning."),
 "李宗仁": ("Li Zongren", "Lǐ Zōngrén", "attested", "Guangxi Clique leader; later acting president of the Republic of China."),
 "郭德洁": ("Guo Dejie", "Guō Déjié", "attested", "Wife of Li Zongren."),
 "梁漱溟": ("Liang Shuming", "Liáng Shùmíng", "attested", "Philosopher and rural-reconstruction advocate; among those rescued from Hong Kong."),
 "金山": ("Jin Shan", "Jīn Shān", "attested", "Stage and film actor; among those rescued from Hong Kong."),
 "高伯时": ("Gao Boshi", "Gāo Bóshí", "provisional", "Relief Commission staff member; head of general affairs at Qujiang."),
 "张浩然": ("Zhang Haoran", "Zhāng Hàorán", "provisional", "The author&#8217;s sister-in-law; head of accounting at the Qujiang Relief Commission office."),
 "赵天民": ("Zhao Tianmin", "Zhào Tiānmín", "provisional", "A trusted household servant turned Relief Commission odd-jobs man."),
 "黄彰传": ("Huang Zhangchuan", "Huáng Zhāngchuán", "attested", "The author&#8217;s eldest younger brother, styled Bopei; head of the Qujiang Relief Commission office."),
 "陈尔新": ("Chen Erxin", "Chén Ěrxīn", "provisional", "The author&#8217;s granddaughter."),
 "允中": ("Yunzhong", "Yǔnzhōng", "decided", "The author&#8217;s elder daughter with Chen Zhigao."),
 "大中": ("Dazhong", "Dàzhōng", "decided", "The author&#8217;s younger daughter with Chen Zhigao."),
 "陈绍贤": ("Chen Shaoxian", "Chén Shàoxián", "provisional", "A clerk at the Wind and Rain Bookroom who later joined the New Fourth Army."),
 "刘为民": ("Liu Weimin", "Liú Wéimín", "decided", "An alias used by Liu Shaowen."),
}
PLACES = {
 "曲江": ("Qujiang", "Qūjiāng", "attested", "County town in northern Guangdong (present-day Shaoguan); wartime relief hub."),
 "韶关": ("Shaoguan", "Sháoguān", "attested", "Present-day name of the Qujiang area."),
 "桂林": ("Guilin", "Guìlín", "attested", "City in Guangxi."),
 "贵阳": ("Guiyang", "Guìyáng", "attested", "Capital of Guizhou."),
 "重庆": ("Chongqing", "Chóngqìng", "attested", "The Nationalist wartime capital (the &#8216;great rear&#8217;)."),
 "广东": ("Guangdong", "Guǎngdōng", "attested", "South China province."),
 "广西": ("Guangxi", "Guǎngxī", "attested", "South China province/region."),
 "福建": ("Fujian", "Fújiàn", "attested", "Southeastern coastal province."),
 "江西": ("Jiangxi", "Jiāngxī", "attested", "Southeastern province."),
 "浙江": ("Zhejiang", "Zhèjiāng", "attested", "Eastern coastal province."),
 "江苏": ("Jiangsu", "Jiāngsū", "attested", "Eastern coastal province."),
 "九龙": ("Kowloon", "Jiǔlóng", "attested", "Mainland part of Hong Kong."),
 "海防": ("Haiphong", "Hǎifáng", "attested", "Port city in northern Vietnam."),
 "昆明": ("Kunming", "Kūnmíng", "attested", "Capital of Yunnan."),
 "越南": ("Vietnam", "Yuènán", "attested", "Then under French colonial rule."),
 "安南": ("Annam", "Ānnán", "attested", "Older name for Vietnam."),
 "暹罗": ("Siam", "Xiānluó", "attested", "Older name for Thailand."),
 "罗马尼亚": ("Romania", "Luómǎníyà", "attested", "European country."),
 "海南岛": ("Hainan Island", "Hǎinán Dǎo", "attested", "Island off south China."),
 "淡水": ("Danshui", "Dànshuǐ", "attested", "A town in coastal Guangdong on the refugee route."),
 "惠阳": ("Huiyang", "Huìyáng", "attested", "Town in Guangdong; the author&#8217;s first safe stop out of Hong Kong."),
 "潮州": ("Chaozhou", "Cháozhōu", "attested", "Region of eastern Guangdong."),
 "复兴中路": ("Fuxing Middle Road", "Fùxīng Zhōnglù", "attested", "Shanghai street where the author lived (formerly Rue Lafayette)."),
 "启德机场": ("Kai Tak Airport", "Qǐdé Jīchǎng", "attested", "Hong Kong&#8217;s airport."),
 "青山寺": ("Qingshan Temple", "Qīngshān Sì", "attested", "Buddhist temple in the Kowloon outskirts."),
 "月仙楼": ("Yuexian Lou", "Yuèxiān Lóu", "provisional", "A building on Kimberley Road where the author rented rooms."),
 "临海": ("Linhai", "Línhǎi", "attested", "City in Zhejiang; birthplace of Qu Yingguang."),
 "衡阳": ("Hengyang", "Héngyáng", "attested", "City in Hunan."),
 "西江": ("West River", "Xījiāng", "attested", "Major river of Guangdong/Guangxi."),
 "苏州河": ("Suzhou Creek", "Sūzhōu Hé", "attested", "River through central Shanghai."),
 "四行仓库": ("Sihang Warehouse", "Sìháng Cāngkù", "attested", "The &#8216;Four Banks&#8217; warehouse defended by the Eight Hundred Heroes in 1937."),
 "万国公墓": ("International Cemetery", "Wànguó Gōngmù", "attested", "Shanghai cemetery."),
 "西伯利亚": ("Siberia", "Xībólìyà", "attested", "Region of the Soviet Union."),
 "江汉关": ("Jianghan Customs", "Jiānghàn Guān", "attested", "The maritime customs house at Hankou."),
}
ORGS = {
 "保卫中国大同盟": ("China Defence League", "attested", "Founded by Song Qingling in Hong Kong on 14 June 1938."),
 "中央赈济委员会": ("Central Relief Commission", "attested", "Nationalist government relief body (&#20013;&#36049;&#20250;); Chen Zhigao served as its Ninth War Zone special commissioner."),
 "中华戏剧社": ("China Drama Society", "provisional", "A Shanghai theater group led by Yu Ling."),
 "中法联谊会": ("Sino-French Friendship Association", "provisional", "A French-Concession friendship body used as a cover for resistance activities."),
 "西南运输公司": ("Southwest Transport Company", "attested", "A transport firm in the Hong Kong&#8211;Haiphong&#8211;Kunming supply line."),
 "太昶公司": ("Taichang Company", "provisional", "A transport company in the southwestern supply line."),
 "滇越铁路": ("Yunnan–Vietnam Railway", "attested", "The Kunming&#8211;Haiphong railway."),
 "中央日报": ("Central Daily News", "attested", "The Kuomintang&#8217;s official party newspaper."),
 "文汇报": ("Wenhui Bao", "attested", "A Shanghai newspaper."),
 "中美日报": ("Sino-American Daily", "attested", "A Shanghai newspaper of the solitary-island period."),
 "中华妇女节制会": ("Chinese Women's Temperance Association", "attested", "The Chinese affiliate of the Woman&#8217;s Christian Temperance Union, led by Liu Wang Liming."),
 "东江游击队": ("East River guerrillas", "attested", "Communist-led anti-Japanese force in the Dongjiang region; forerunner of the East River Column."),
 "国际第一收容所": ("First International Shelter", "provisional", "A Shanghai refugee shelter where several Relief Commission staff had worked."),
 "童子军抗日后援会": ("Boy Scouts' Resistance Support Association", "provisional", "The Shanghai scouting body under whose banner Yang Huimin acted in 1937."),
 "新华日报": ("Xinhua Daily", "attested", "The Communist Party&#8217;s newspaper in the Nationalist areas."),
 "新华社": ("Xinhua News Agency", "attested", "The Communist Party&#8217;s news agency."),
 "励志社": ("Lizhi Society", "attested", "A Nationalist officers&#8217; welfare society; here its Qujiang premises."),
 "中国红十字会": ("Chinese Red Cross", "attested", "Its headquarters office was at Du Yuesheng&#8217;s Hong Kong residence."),
 "军统": ("Military Statistics Bureau", "attested", "The Nationalist military intelligence service (&#20891;&#32479;)."),
 "潮州同乡会": ("Chaozhou Native-Place Association", "provisional", "A native-place association used to charter the refugee ship."),
 "华东军政委员会": ("East China Military and Political Commission", "attested", "An early-PRC regional government body."),
 "青帮": ("Green Gang", "attested", "The Shanghai secret society to which Du Yuesheng belonged."),
 "筹安会": ("Chouan Society", "attested", "The 1915 society that promoted Yuan Shikai&#8217;s bid to become emperor."),
 "洪帮": ("Hong Society", "attested", "A secret society (the Hongmen); Li Fang was one of its chiefs."),
}
TERMS = {
 "统筹统汇": ("unified planning and unified remittance", "The Kuomintang policy of channeling all overseas donations through the Nationalist government for redistribution."),
 "戎马书生": ("Scholar in the Saddle", "&#25101;&#39532;&#20070;&#29983;: a man of letters who has taken to soldiering."),
 "维持会": ("peace-maintenance committee", "A collaborationist body of local notables set up under Japanese occupation."),
 "大后方": ("the great rear", "The unoccupied Nationalist-held interior, centered on Chongqing."),
}

added = {"people": 0, "places": 0, "organizations": 0, "terms": 0}
for zh, (en, py, st, note) in PEOPLE.items():
    if zh not in g["people"]:
        g["people"][zh] = {"en": en, "pinyin": py, "status": st, "note": note}
        added["people"] += 1
for zh, (en, py, st, note) in PLACES.items():
    if zh not in g["places"]:
        g["places"][zh] = {"en": en, "pinyin": py, "status": st, "note": note}
        added["places"] += 1
for zh, (en, st, note) in ORGS.items():
    if zh not in g["organizations"]:
        g["organizations"][zh] = {"en": en, "status": st, "note": note}
        added["organizations"] += 1
for zh, (en, note) in TERMS.items():
    if zh not in g["terms"]:
        g["terms"][zh] = {"en": en, "note": note}
        added["terms"] += 1
save("glossary.json", g)
print("glossary added:", added)

# ---- notes ----
n = load("notes.json")
n["ch17"] = [
 {"anchor": "China Defence League",
  "note": "The China Defence League (&#20445;&#21355;&#20013;&#22269;&#22823;&#21516;&#30431;) was founded by Song Qingling in Hong Kong on 14&#160;June 1938 to publicize China&#8217;s resistance abroad and channel international donations to the Communist-led Eighth Route and New Fourth Armies. The date and place are corroborated by the historical record."},
 {"anchor": "Chairman Ho Chi Minh",
  "note": "Ho Chi Minh (&#32993;&#24535;&#26126;, 1890&#8211;1969), later president of the Democratic Republic of Vietnam. Two details of the memoir&#8217;s account do not square with the record: he is not documented to have taken the name &#8216;Ho Chi Minh&#8217; or held any &#8216;Chairman&#8217; title until about 1940&#8211;45, and in 1939 he was based inland in South China (Guangxi and Yunnan) rather than at the Vietnamese port of Haiphong. The meeting and the hand-carved seal are the memoir&#8217;s own recollection and are otherwise uncorroborated. &#8216;Scholar in the Saddle&#8217; renders &#25101;&#39532;&#20070;&#29983; (<i>rongma shusheng</i>), a man of letters turned soldier."},
 {"anchor": "East River anti-Japanese guerrillas",
  "note": "The East River guerrillas &#8212; the Communist-led anti-Japanese force in the East River (Dongjiang) region of Guangdong, forerunner of the East River Column (&#19996;&#27743;&#32437;&#38431;) &#8212; carried out the 1942 evacuation of prominent figures from Japanese-occupied Hong Kong recounted in Chapter&#160;19."},
]
n["ch18"] = [
 {"anchor": "General Chen Ce",
  "note": "Chen Ce (&#38472;&#31574;, 1893&#8211;1949), the Kuomintang &#8216;one-legged admiral,&#8217; better known in English as Chan Chak. On 25&#160;December 1941, the day Hong Kong surrendered, he led some sixty men out of the colony by motor torpedo boat to Mirs Bay and then overland to the mainland &#8212; a celebrated escape. The lost leg and the escape are both corroborated."},
 {"anchor": "the warship Zhongshan",
  "note": "The <i>Zhongshan</i> (&#20013;&#23665;&#33328;, formerly the <i>Yongfeng</i>) was a gunboat famous in Republican history, notably for the 1926 &#8216;Zhongshan Warship Incident.&#8217; That a man named Chen Di (&#38472;&#28173;) once captained her is not found in the available scholarship and is given here on the memoir&#8217;s authority alone."},
 {"anchor": "peace-maintenance committee",
  "note": "A &#8216;peace-maintenance committee&#8217; (&#32173;&#25345;&#20250;) was a collaborationist body of local notables that the Japanese set up to run an occupied town until a regular puppet administration could be installed. To refuse to head or serve on one, as Chen Di did, was an act of open defiance."},
]
n["ch19"] = [
 {"anchor": "Yang Huimin",
  "note": "Yang Huimin (&#26472;&#24800;&#25935;, c.&#160;1915&#8211;1992), a young Girl Guide who on the night of 28&#160;October 1937 crossed Suzhou Creek to deliver a national flag to Colonel Xie Jinyuan and the defenders of the Sihang Warehouse &#8212; the &#8216;Eight Hundred Heroes,&#8217; a garrison of some four hundred publicized as eight hundred &#8212; during the Battle of Shanghai. The episode is corroborated and made her a national celebrity."},
 {"anchor": "a rescue on a grand scale",
  "note": "This is the operation later known as the &#8216;Great Rescue&#8217; (&#32988;&#21033;&#22823;&#33829;&#25937;). Between January and November 1942 the Communist Party, through the Guangdong guerrillas (forerunner of the East River Column), evacuated more than eight hundred cultural figures and democratic personages, along with their relatives and international friends, from Japanese-occupied Hong Kong. Mao Dun, himself among the rescued, called it the greatest work of rescue since the War of Resistance began. The scale and the roster of those saved are corroborated."},
 {"anchor": "the martyr Lin Gengbai",
  "note": "Lin Gengbai (&#26519;&#24248;&#30333;, 1896&#8211;1941), a poet of the Southern Society. On 19&#160;December 1941 he was shot dead by Japanese soldiers near the observatory in Kowloon and his wife Lin Beili was wounded, as the memoir recounts; he was forty-five. The date, the circumstances, and his age are corroborated. He appears in passing in earlier chapters; the note is placed here, where his death is the subject."},
 {"anchor": "Qu Yingguang",
  "note": "Qu Yingguang (&#23624;&#26144;&#20809;, style name Wenliu, 1883&#8211;1973), a native of Linhai in Zhejiang who briefly served as the province&#8217;s military governor in 1916 and was appointed a vice-chairman of the Nationalist government&#8217;s Relief Commission in 1938. The particulars are corroborated."},
]
save("notes.json", n)
print("notes set: ch17=%d ch18=%d ch19=%d" % (len(n["ch17"]), len(n["ch18"]), len(n["ch19"])))

# ---- figures ----
f = load("figures.json")
f["ch17"] = [
 {"file": "00045.jpg", "before": "mother was an enlightened, warm-hearted",
  "alt": "Chen Zhigao and Huang Dinghui with the Chen Xunshe couple",
  "caption": "Chen Zhigao and Huang Dinghui (Mulan), husband and wife, with Mr. Chen Xunshe — head of the Shanghai branch of the Kuomintang’s Central Daily News and younger brother of Chen Bulei — and his wife."},
 {"file": "00046.jpg", "before": "Old Madame Pan",
  "alt": "Portrait of Du Yuesheng",
  "caption": "Du Yuesheng (1888–1951), a famous figure of the Shanghai Green Gang in modern times."},
 {"file": "00047.jpg", "before": "Wang Xinheng and Chiang Ching-kuo",
  "alt": "Huang Dinghui visiting Wu Jufang in 1991",
  "caption": "August 1991: Huang Dinghui (Mulan), with her youngest son Chen Wenzhong and granddaughter Chen Erxin, visiting Wu Jufang (second from right)."},
 {"file": "00048.jpg", "before": "In Hong Kong, besides my title of adviser",
  "alt": "A garden party in Hong Kong",
  "caption": "A garden outing organized by Niuwei. From left: Wang Xinheng and his wife, and Cai Shuhou’s elder sister."},
 {"file": "00049.jpg", "before": "Unlike Song Meiling",
  "alt": "Huang Dinghui and Wang Huazhen, 1940",
  "caption": "1940: Huang Dinghui (Mulan) and Wang Huazhen, photographed together in Hong Kong."},
]
f["ch19"] = [
 {"file": "00050.jpg", "before": "In mid-January 1942",
  "alt": "Chen Zhigao with First International Shelter colleagues at Qujiang",
  "caption": "1941: Chen Zhigao with colleagues from the First International Shelter, photographed at Qujiang. Front row: Chen Zhigao (center), Huang Zhangchuan (left); back row, right: Gao Boshi."},
]
save("figures.json", f)
print("figures set: ch17=%d ch19=%d" % (len(f["ch17"]), len(f["ch19"])))
