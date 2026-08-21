#!/usr/bin/env python3
# Add B13 (ch23/ch24) glossary rows, nested into people so qc_entities can reach
# them.  Every row carries en + pinyin + status.  Idempotent: only adds if absent.
import json
import os

ROOT = "/home/user/winston"
G = os.path.join(ROOT, "glossary.json")

PEOPLE = {
    # ch23
    "方志敏": "Fang Zhimin", "李杜": "Li Du", "史沫特莱": "Smedley",
    "杨森": "Yang Sen",
    "吴成方": "Wu Chengfang", "张克云": "Zhang Keyun", "赵瑛": "Zhao Ying",
    "梁柏台": "Liang Baitai", "曾传六": "Zeng Chuanliu", "康泽": "Kang Ze",
    "孙儒珍": "Sun Ruzhen", "焦鼎铠": "Jiao Dingkai", "杨广山": "Yang Guangshan",
    "王少春": "Wang Shaochun", "张振华": "Zhang Zhenhua", "刘杞夫": "Liu Qifu",
    "陈原道": "Chen Yuandao", "周仲英": "Zhou Zhongying", "刘亚雄": "Liu Yaxiong",
    "殷鉴": "Yin Jian", "郭亚先": "Guo Yaxian", "廖划平": "Liao Huaping",
    "赖德": "Lai De", "徐兰芝": "Xu Lanzhi", "李富春": "Li Fuchun",
    "蔡畅": "Cai Chang", "聂荣臻": "Nie Rongzhen", "卢伟良": "Lu Weiliang",
    "黄华": "Huang Hua", "赵毅": "Zhao Yi", "曾宗达": "Zeng Zongda",
    "李介生": "Li Jiesheng", "陈寿昌": "Chen Shouchang",
    "刘少白": "Liu Shaobai", "钱椒椒": "Qian Jiaojiao",
    # ch24
    "张长庚": "Zhang Changgeng", "王一心": "Wang Yixin", "陈蔚如": "Chen Weiru",
    "刘英": "Liu Ying", "张国栋": "Zhang Guodong", "洪兰友": "Hong Lanyou",
    "季源溥": "Ji Yuanpu", "叶其称": "Ye Qicheng", "王世德": "Wang Shide",
    "陈庆斋": "Chen Qingzhai", "胡洪涛": "Hu Hongtao", "王国栋": "Wang Guodong",
    "童国忠": "Tong Guozhong", "张长庚": "Zhang Changgeng", "吴星伯": "Wu Xingbo",
    "季源溥": "Ji Yuanpu", "宋志先": "Song Zhixian", "吕瑞京": "Lü Ruijing",
    "王思诚": "Wang Sicheng", "张永琴": "Zhang Yongqin", "谷正伦": "Gu Zhenglun",
    "张萍": "Zhang Ping", "李志远": "Li Zhiyuan", "吴大钧": "Wu Dajun",
    "顾凤鸣": "Gu Fengming", "过得诚": "Guo Decheng", "曹清澄": "Cao Qingcheng",
    "陆元虎": "Lu Yuanhu", "王斌": "Wang Bin", "濮孟九": "Pu Mengjiu",
    "钱丹泉": "Qian Danquan", "臧公惠": "Zang Gonghui", "周廉": "Zhou Lian",
}

PLACES = {
    "塘沽": "Tanggu", "劝业场": "Quanyechang", "细柳巷": "Xiliuxiang",
    "安品街": "Anpin Street", "汀州": "Tingzhou", "长汀": "Changting",
    "汕头": "Shantou", "大埔": "Dapu", "瞻园": "Zhanyuan",
}

WORKS = {
    "红色中华": "Red China", "红旗": "Red Flag",
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
