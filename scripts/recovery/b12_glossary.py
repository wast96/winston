#!/usr/bin/env python3
# Add B12 (ch21/ch22) glossary rows, nested into people/organizations/places/
# works so qc_entities can reach them.  Every row carries en + pinyin + status.
# Idempotent: only adds a key if absent.  Foreign names whose ZH carries an OCR
# middot are left out (handled in footnotes) to avoid substring-match noise.
import json
import os

ROOT = "/home/user/winston"
G = os.path.join(ROOT, "glossary.json")

PEOPLE = {
    # ch21
    "谭国辅": "Tan Guofu", "谭人凤": "Tan Renfeng", "邓文仪": "Deng Wenyi",
    "陈连生": "Chen Liansheng", "史济美": "Shi Jimei", "吕克勤": "Lü Keqin",
    "马绍武": "Ma Shaowu", "谷正伦": "Gu Zhenglun", "吴凯声": "Wu Kaisheng",
    "王云程": "Wang Yuncheng", "于学忠": "Yu Xuezhong", "吴忠信": "Wu Zhongxin",
    "王均": "Wang Jun", "赵冠英": "Zhao Guanying", "岳维峻": "Yue Weijun",
    "汤恩伯": "Tang Enbo", "牛惠霖": "Niu Huilin", "牛惠生": "Niu Huisheng",
    "邵达夫": "Shao Dafu", "张良诚": "Zhang Liangcheng", "黄海明": "Huang Haiming",
    "黄励": "Huang Li", "钱瑛": "Qian Ying", "何宝珍": "He Baozhen",
    "熊天荆": "Xiong Tianjing", "夏之栩": "Xia Zhixu", "帅孟奇": "Shuai Mengqi",
    "张小妹": "Zhang Xiaomei", "陈月先": "Chen Yuexian", "钮传琦": "Niu Chuanqi",
    "张琴秋": "Zhang Qinqiu", "叶剑英": "Ye Jianying", "朱德": "Zhu De",
    "刘伯承": "Liu Bocheng", "陈绍纯": "Chen Shaochun", "陈炯明": "Chen Jiongming",
    "宋教仁": "Song Jiaoren", "黄兴": "Huang Xing", "罗文干": "Luo Wengan",
    "陈藻英": "Chen Zaoying",
    # ch22
    "杨铨": "Yang Quan", "杨杏佛": "Yang Xingfo", "潘梓年": "Pan Zinian",
    "应修人": "Ying Xiuren", "邝惠安": "Kuang Hui'an", "文鸿恩": "Wen Hong'en",
    "胡也频": "Hu Yepin", "茅盾": "Mao Dun", "邹韬奋": "Zou Taofen",
    "叶圣陶": "Ye Shengtao", "郁达夫": "Yu Dafu", "柳亚子": "Liu Yazi",
    "申彦俊": "Shen Yanjun", "王志之": "Wang Zhizhi", "曹聚仁": "Cao Juren",
    "汪盛荻": "Wang Shengdi", "彭学沛": "Peng Xuepei", "冯雪峰": "Feng Xuefeng",
    "张天翼": "Zhang Tianyi", "杨尚昆": "Yang Shangkun", "张闻天": "Zhang Wentian",
    "余泽鸿": "Yu Zehong", "何香凝": "He Xiangning", "许德珩": "Xu Deheng",
    "侯外庐": "Hou Wailu", "马哲民": "Ma Zhemin", "沈钧儒": "Shen Junru",
    "孙传芳": "Sun Chuanfang", "任弼时": "Ren Bishi", "李达": "Li Da",
    "林成荫": "Lin Chengyin", "蔡飞": "Cai Fei", "沈醉": "Shen Zui",
    "赵理君": "Zhao Lijun", "王克全": "Wang Kequan", "林金生": "Lin Jinsheng",
    "杨小佛": "Yang Xiaofo", "周海婴": "Zhou Haiying", "许广平": "Xu Guangping",
    "高德臣": "Gao Dechen", "过得诚": "Guo Decheng", "李阿大": "Li Ada",
    "施芸之": "Shi Yunzhi", "范广珍": "Fan Guangzhen",
}

ORGS = {
    "中国左翼作家联盟": "League of Left-Wing Writers",
    "中国济难会": "China Relief Society",
    "国民御侮自救会": "National Salvation Association Against Foreign Aggression",
    "全国总工会": "All-China Federation of Trade Unions",
    "同盟会": "Tongmenghui",
    "蓝衣社": "Blue Shirts",
}

PLACES = {
    "老虎桥": "Laohuqiao", "提蓝桥": "Tilanqiao", "康奈尔大学": "Cornell",
    "哈佛大学": "Harvard", "东南大学": "Southeast University",
    "亚尔培路": "Avenue du Roi Albert", "霞飞路": "Avenue Joffre",
    "晓庄": "Xiaozhuang", "南浔铁路": "Nanchang-Jiujiang railway",
}

WORKS = {
    "北斗": "Big Dipper", "民族日报": "National Daily",
    "字林西报": "North China Daily News", "大公报": "Da Gong Bao",
    "大美晚报": "Da Mei Evening News",
    "危害民国紧急治罪法": "Emergency Law for Crimes Endangering the Republic",
}


def add(cat, mapping):
    n = 0
    for zh, en in mapping.items():
        if zh in cat:
            continue
        cat[zh] = {"en": en, "pinyin": en, "status": "attested"}
        n += 1
    return n


g = json.load(open(G))
tot = 0
tot += add(g["people"], PEOPLE)
tot += add(g["organizations"], ORGS)
tot += add(g["places"], PLACES)
tot += add(g["works"], WORKS)
json.dump(g, open(G, "w"), ensure_ascii=False, indent=1)
print("added %d glossary rows" % tot)
