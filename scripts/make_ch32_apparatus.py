# Build data/ch32_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi (+ em dashes), then every
# non-ASCII char is converted to a numeric character reference before writing.
# EVERY non-ASCII hanzi glyph used in a note body is asserted to occur in ch32's
# own authoritative data/zh/ch32.txt (a Write-tool corruption would produce a
# glyph absent from the source and trip the assert). Anchors are ASCII substrings
# of ch32_reading.md, with no em dash and no quote/apostrophe. Pinyin in bodies
# is untoned (ASCII) by policy.
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "ch32"
zh = open(os.path.join(ROOT, "data", "zh", CID + ".txt"), encoding="utf-8").read()
reading = open(os.path.join(ROOT, "out", CID + "_reading.md"), encoding="utf-8").read()

NOTES = [
    {
        "anchor": "the war to suppress the rebellion",
        "note": (
            "Chen writes throughout Part Four in the political idiom of the "
            "Nationalist (Kuomintang) side in the Chinese civil war of 1946 to "
            "1949. The Communists are 'bandits' (共匪, gongfei); the campaign "
            "against them is a 'pacification' (绥靖, suijing) and a 'suppression "
            "of rebellion' (戡乱, kanluan), casting the Communist forces as rebels "
            "against the lawful government rather than as one side in a civil war. "
            "Communist and much later historiography calls the same events the War "
            "of Liberation. The framing is the author's own and is preserved here, "
            "not softened; where a particular claim is contested by scholarship, "
            "the notes say so."
        ),
    },
    {
        "anchor": "the Fifth Part",
        "note": (
            "Chen numbers the Beiping-Tianjin volume the fifth part of his Nameless "
            "Heroes series, although his preface to the Shanghai volume (Part Three "
            "above) numbered that book the third. A fourth part is thus implied "
            "that this collected edition, which presents four books, does not carry "
            "separately. The count is the author's own and is left as written, the "
            "discrepancy noted rather than smoothed over."
        ),
    },
    {
        "anchor": "Marshall",
        "note": (
            "General George C. Marshall (1880-1959), the United States Army chief "
            "of staff during the Second World War, sent to China by President "
            "Truman late in 1945 to mediate between the Nationalists and the "
            "Communists. The truce machinery of early 1946 comprised the 'Committee "
            "of Three'—Marshall, with Zhang Qun for the government and Zhou "
            "Enlai for the Communists—and, to police the cease-fire, a "
            "Military Mediation Executive Headquarters at Beiping jointly staffed "
            "by the two Chinese sides and the Americans. The mission failed; "
            "Marshall left China in January 1947 and became Secretary of State."
        ),
    },
    {
        "anchor": "Lizhi Plan",
        "note": (
            "The Lizhi Plan (励志计划): 励志 (lizhi) means to steel the will or to "
            "better oneself. Under this plan the Ministry of National Defense "
            "raised and trained the special 'pacification' units of Part Four, "
            "passing their cadres through the Lizhi Training Class at the Central "
            "Training Corps in Nanjing. Chen commanded the First Brigade of the "
            "resulting Pacification Corps."
        ),
    },
    {
        "anchor": "the Jiangxi bandit-suppression",
        "note": (
            "The 'bandit-suppression' (剿匪, jiaofei) campaigns Chiang Kai-shek "
            "waged against the Communist base areas in Jiangxi in the early 1930s "
            "—the Encirclement Campaigns that forced the Communists onto the "
            "Long March in 1934. The special-detachment units (别働总队) raised for "
            "that fighting, on a Japanese model, were the precedent Chiang recalled "
            "in forming the postwar Pacification Corps."
        ),
    },
    {
        "anchor": "Youth Army",
        "note": (
            "The Youth Army (青年军), a Nationalist force of educated young "
            "volunteers raised late in the war of resistance under the slogan 'a "
            "hundred thousand youths, a hundred thousand soldiers' (十万青年十万军). "
            "Its demobilized cadres were a chief source of recruits for the "
            "pacification units."
        ),
    },
    {
        "anchor": "Beiping-Liaoning line",
        "note": (
            "The five railways named are the trunk lines running out of Beiping "
            "and Tianjin, under their Republican-era names: the Beiping-Liaoning "
            "line (北宁线, the old Peking-Mukden Railway, Beiping to the Northeast); "
            "the Tianjin-Pukou line (津浦线, Tianjin to Pukou opposite Nanjing); the "
            "Beiping-Hankou line (平汉线, Beiping to Hankou); the Beiping-Gubeikou "
            "line (平古线, north to the Great Wall pass at Gubeikou); and the "
            "Beiping-Suiyuan line (平绥线, west toward Suiyuan). Chen's five command "
            "rooms were posted along them."
        ),
    },
    {
        "anchor": "Fu Zuoyi",
        "note": (
            "Fu Zuoyi (1895-1974), the Nationalist commander-in-chief of the North "
            "China Bandit Suppression Headquarters and the defender of Beiping. In "
            "January 1949, with Lin Biao's army at the walls—the siege in the "
            "background of this preface—he handed the city over to the "
            "Communists by negotiated agreement, sparing it a battle."
        ),
    },
    {
        "anchor": "Fenghua",
        "note": (
            "Fenghua, in Zhejiang, was Chiang Kai-shek's native place. He was there "
            "because he had just stepped down as President of the Republic in "
            "January 1949, retiring to his hometown while Li Zongren served as "
            "acting president; from there he still directed affairs, as the order "
            "to the brigade to stand guard shows."
        ),
    },
    {
        "anchor": "Temple of Agriculture",
        "note": (
            "The Temple of Agriculture (先农坛) in the southern city of Beiping was "
            "the imperial altar where the emperor performed the ritual spring "
            "plowing. During the 1948-49 siege, with the airfields outside the "
            "walls lost, a swath of its ancient cypresses was felled to make a "
            "makeshift airstrip within the city."
        ),
    },
]


def to_ncr(s):
    return "".join(ch if ord(ch) < 128 else "&#%d;" % ord(ch) for ch in s)


def main():
    for e in NOTES:
        assert e["anchor"] in reading, "anchor not in reading: %r" % e["anchor"]
        for ch in e["anchor"]:
            assert ord(ch) < 128, "anchor has non-ASCII: %r" % e["anchor"]
            assert ch not in "—\"'‘’“”", \
                "anchor has a forbidden char: %r" % e["anchor"]
        for ch in e["note"]:
            if ord(ch) >= 128 and ch != "—":
                assert ch in zh, \
                    "note glyph not in data/zh/%s.txt: %r" % (CID, ch)
        e["note"] = to_ncr(e["note"])
    dest = os.path.join(ROOT, "data", CID + "_apparatus.json")
    json.dump({"notes": {CID: NOTES}}, open(dest, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print("wrote %s (%d notes)" % (dest, len(NOTES)))


if __name__ == "__main__":
    main()
