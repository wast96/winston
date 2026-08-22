#!/usr/bin/env python3
# Add B14 (ch25/ch26/ch27) glossary rows, nested into people/places/works so
# qc_entities can reach them.  Every row carries en + pinyin + status.
# Idempotent: only adds if absent.
import json
import os

ROOT = "/home/user/winston"
G = os.path.join(ROOT, "glossary.json")

PEOPLE = {
    # ch25 Wu Hao Notice affair
    "江青": "Jiang Qing", "林彪": "Lin Biao", "博古": "Bo Gu",
    "周少山": "Zhou Shaoshan", "陈志皋": "Chen Zhigao",
    "黄慕兰": "Huang Mulan", "黄定慧": "Huang Dinghui", "巴和": "Ba He",
    "史量才": "Shi Liangcai", "陶行知": "Tao Xingzhi",
    "秦杰": "Qin Jie", "连承义": "Lian Chengyi",
    "杨匏安": "Yang Pao'an", "罗绮园": "Luo Qiyuan", "陈华": "Chen Hua",
    "张春桥": "Zhang Chunqiao", "姚文元": "Yao Wenyuan", "吴法宪": "Wu Faxian",
    "许世友": "Xu Shiyou", "谢富治": "Xie Fuzhi", "汪东兴": "Wang Dongxing",
    "赵容": "Zhao Rong", "鲍君甫": "Bao Junfu",
    # ch26 Conclusion
    "阎宝航": "Yan Baohang", "阎明诗": "Yan Mingshi", "李政文": "Li Zhengwen",
    "陈忠经": "Chen Zhongjing", "申健": "Shen Jian", "沈安娜": "Shen Anna",
    "何应钦": "He Yingqin", "白崇禧": "Bai Chongxi", "陈诚": "Chen Cheng",
    "吴克坚": "Wu Kejian", "王冶秋": "Wang Yeqiu", "何基沣": "He Jifeng",
    # ch27 Afterword
    "柯麟": "Ke Lin", "杨献珍": "Yang Xianzhen",
}

PLACES = {
    "瑞金": "Ruijin", "宁都": "Ningdu", "永定": "Yongding",
    "钓鱼台": "Diaoyutai", "台儿庄": "Tai'erzhuang", "枣庄": "Zaozhuang",
    "梅园": "Meiyuan", "徐州": "Xuzhou",
}

WORKS = {
    "斗争": "Struggle",
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
tot += add(g["places"], PLACES)
tot += add(g["works"], WORKS)
json.dump(g, open(G, "w"), ensure_ascii=False, indent=1)
print("added %d glossary rows" % tot)
