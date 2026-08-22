# ch12 corrections-pass edits (source-dependent faithfulness items)
#
# Resolves the two ch12 flags logged in PROGRESS.md's R04 entry, both
# crop-verified against source.pdf. Applied with
# scripts/apply_edits.py --suffix corrections ch12. The R04 register edits in
# edits/ch12_edits.md are already applied (committed a0c5d30) and NOT re-run.
# Both items are NOTE-ADD only; the prose is faithful and unchanged.
#
# Verified crops (printed folios cited):
#  - folio 381 (pdf 417): 带领边保干部瞄准陕西省会——六朝古都西安。 The source
#    prints 六朝古都 ("capital of six dynasties") for Xi'an. That is the
#    conventional epithet of Nanjing; Xi'an is conventionally the capital of
#    thirteen. Rendered as printed; NOTE-ADD states the record.
#  - folio 390 (pdf 426): …中国的情报、保卫、公安系统…中国的情报、保卫、安全、
#    公安工作… The four-item list adds 安全 to 情报/保卫/公安: 保卫 and 安全 ARE
#    distinct terms here, so the English "security" and "safety" are not a
#    redundant doubling. Faithful; NOTE-ADD distinguishes the four domains.

NOTE-ADD
ANCHOR: the ancient capital of six dynasties
NOTE: The source calls Xi'an the capital of &#8220;six dynasties&#8221; (&#20845;&#26397;&#21476;&#37117;), but that is by convention the epithet of Nanjing, whose Six Dynasties ruled from there in the third to sixth centuries. Xi'an (ancient Chang'an) is usually called the capital of thirteen dynasties, from the Western Zhou through the Tang. The author's &#8220;six&#8221; is given as printed.
WHY: a reader who knows the conventional epithets will be thrown; the note owns the source's usage.

NOTE-ADD
ANCHOR: intelligence, security, safety, and public-security work
NOTE: The near-synonyms translate four distinct Chinese terms that the source lists separately: &#24773;&#25253; (intelligence), &#20445;&#21355; (protective or internal security &#8212; the &#8220;security&#8221; of this book's own title), &#23433;&#20840; (state security, later the Ministry of State Security's domain), and &#20844;&#23433; (public security, the police). English runs the middle two together; the original keeps them apart.
WHY: "security, safety" reads as redundant doubling in English, but the source names four separate institutional domains.
