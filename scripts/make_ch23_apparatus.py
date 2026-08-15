# Build data/ch23_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + code-point-constructed hanzi here, then
# every non-ASCII char is converted to a numeric character reference before
# writing, so the XHTML build stays clean. The hanzi are built from explicit
# code points (not typed) to defeat the CJK-mangling hazard (see HANDOFF).
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Hanzi built from code points, verified below:
#   U+4E3A 为  U+864E 虎  U+4F5C 作  U+4F25 伥(chang)
IDIOM = "".join(chr(c) for c in (0x4E3A, 0x864E, 0x4F5C, 0x4F25))  # 为虎作伥
CHANG = chr(0x4F25)                                               # 伥

notes = {
    "ch23": [
        {
            "anchor": "playing jackal to the tiger",
            "note": (
                "A rendering of the idiom " + IDIOM + " (wei hu zuo chang), "
                "literally &#8220;to act as the " + CHANG + " for the tiger.&#8221; "
                "In folk belief the " + CHANG + " is the ghost of a person killed "
                "by a tiger, held in servitude to lure fresh victims into the "
                "beast&#8217;s path; the phrase thus means to abet a powerful "
                "evildoer in preying on others. Chen turns it on &#8220;No. "
                "76,&#8221; the puppet secret service staffed by Chinese "
                "collaborators who did the Japanese occupier&#8217;s killing "
                "for it."
            ),
        }
    ]
}


def to_ncr(s):
    return "".join(ch if ord(ch) < 128 else "&#%d;" % ord(ch) for ch in s)


# eyeball the hanzi before converting
print("IDIOM =", IDIOM, "| CHANG =", CHANG)

for cid, items in notes.items():
    for e in items:
        e["note"] = to_ncr(e["note"])
        e["anchor"] = to_ncr(e["anchor"])
        assert e["anchor"].isascii(), e["anchor"]

path = os.path.join(ROOT, "data", "ch23_apparatus.json")
json.dump({"notes": notes}, open(path, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("wrote", path)
