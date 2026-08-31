#!/usr/bin/env python3
"""Add the ch12/13/14 glossary rows STRAIGHT INTO the people section (the
glossary.json is SECTIONED; apparatus_merge flattens it -- HANDOFF trap). en =
the Wade-Giles / conventional-English form Isaacs prints; pinyin = the modern
form, agreeing with authority.json where the shelf has settled one (谭延闿 Tan
Yankai, 阎锡山 Yan Xishan, 叶挺 Ye Ting are "agreed" shelf-wide; 向忠发 Xiang
Zhongfa, 许克祥 Xu Kexiang, 何键 He Jian, 苏兆征 Su Zhaozheng, 朱培德 Zhu Peide are
new to the shelf). Only Chinese figures go in the glossary; the batch's foreign
figures (Tanaka, Austen Chamberlain, Danton, Coue, Albert Treint, Togliatti/
Ercoli, Purcell/Hicks/Citrine) stay in the notes, as Browder / Doriot / Mann /
Pilsudski / Malraux did.

No principal promotion this batch: Chiu Chiu-pei (Qu Qiubai) is heavily quoted
here as a Central Committee member and retrospective analyst but does not yet
lead the party; he succeeds Chen Tu-hsiu in August 1927 (ch16), which is when
his promotion is due. Principals stay Sun 1, Chiang 2, Chen Tu-hsiu 3, Borodin
4, Wang Ching-wei 5, Chow En-lai 6. Idempotent; re-reads glossary.json to verify.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GPATH = os.path.join(ROOT, "glossary.json")

PEOPLE = {
    "谭延闿": {"en": "Tan Yen-kai", "pinyin": "Tan Yankai", "status": "attested",
        "note": "1880&#8211;1930. Hunanese elder of the Kuomintang and chairman "
        "of the Nationalist government, at Wuhan and then Nanking, where he "
        "headed the Executive Yuan until his death."},
    "阎锡山": {"en": "Yen Hsi-shan", "pinyin": "Yan Xishan", "status": "attested",
        "note": "1883&#8211;1960. The &#8220;model governor&#8221; warlord of "
        "Shansi from 1911, who joined the Northern Expedition in 1927 and held "
        "the province almost without a break until 1949."},
    "向忠发": {"en": "Hsiang Chung-fah", "pinyin": "Xiang Zhongfa",
        "status": "attested",
        "note": "1880&#8211;1931. Hupeh boatmen&#8217;s and labor organizer who "
        "became the nominal general secretary of the Chinese Communist Party in "
        "1928; arrested and shot in Shanghai in 1931."},
    "叶挺": {"en": "Yeh Ting", "pinyin": "Ye Ting", "status": "attested",
        "note": "1896&#8211;1946. Communist commander of the Northern "
        "Expedition&#8217;s &#8220;Ironsides,&#8221; who led the Nanchang "
        "uprising and the Canton Commune of 1927 and later the New Fourth Army; "
        "died in a 1946 plane crash."},
    "许克祥": {"en": "Hsu Keh-chang", "pinyin": "Xu Kexiang", "status": "attested",
        "note": "1890&#8211;1964. Kuomintang regimental commander at Changsha "
        "who launched the Horse Day coup of May 21, 1927 against the Hunan mass "
        "organizations, opening the rural terror."},
    "何键": {"en": "Ho Chien", "pinyin": "He Jian", "status": "attested",
        "note": "1887&#8211;1956. Hunanese general who became the "
        "province&#8217;s military governor after the 1927 terror and a byword "
        "for anti-Communism; his regime executed Mao Tse-tung&#8217;s wife, Yang "
        "Kai-hui, in 1930."},
    "苏兆征": {"en": "Hsu Chao-jen", "pinyin": "Su Zhaozheng", "status": "attested",
        "note": "1885&#8211;1929. Seamen&#8217;s-union leader of the Hong Kong "
        "and Canton&#8211;Hong Kong strikes and chairman of the All-China "
        "Federation of Trade Unions; minister of labor in the Wuhan government."},
    "朱培德": {"en": "Chu Pei-teh", "pinyin": "Zhu Peide", "status": "attested",
        "note": "1888&#8211;1937. Yunnanese general commanding the Third Army and "
        "governing Kiangsi, whose 1927 purge of the Communists was comparatively "
        "bloodless &#8212; he had them escorted out rather than shot."},
}


def main():
    g = json.load(open(GPATH, encoding="utf-8"))
    added = 0
    sec = g.setdefault("people", {})
    for zh, row in PEOPLE.items():
        if zh in sec:
            continue
        sec[zh] = row
        added += 1

    with open(GPATH, "w", encoding="utf-8") as fh:
        json.dump(g, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    back = json.load(open(GPATH, encoding="utf-8"))
    for zh in PEOPLE:
        if zh not in back["people"]:
            raise SystemExit("re-read verification failed: %s" % zh)
    print("glossary: %d rows added; people=%d" % (added, len(back["people"])))


if __name__ == "__main__":
    main()
