# CORRECTIONS

The commissioner files corrections here after reading the EPUB. A pasted chat
message ("ch12: 'X' reads oddly; global: stop rendering Y as Z") is a
first-class corrections input too: the session transcribes it into this file
before acting. This file is the ledger, not a form the commissioner must fill.

Two kinds:

- **GLOBAL** — a rendering, a register rule, or a note policy that must apply
  everywhere ("render X as Y throughout", "stop noting every idiom", "this
  person is actually Z"). Applied via a glossary/style change plus a
  grep-driven edit across ALL built units, INCLUDING note bodies and glossary
  bodies, then rebuild + full QA. A global correction applied to only some
  units is worse than not applying it.
- **LOCAL** — a fix at one spot. Apply, rebuild, QA.

After a batch of corrections: rebuild, run qa_epub, list every file touched in
the reply, and append a dated entry to CHANGELOG.md. A corrections pass with
ZERO items is still a clean-checkout regression run: re-clone, regenerate the
regenerables, rebuild, re-run the whole-book checks, prune stray branches.

## Entry form (append below; greppable, one block per item)

### [GLOBAL|LOCAL] <short title>
Unit: <chapter id, or "book-wide">
Where: <anchor phrase or short quote from the EPUB>
Problem: <what is wrong>
Fix: <what it should be>

## Pending

(none)

## Done

### [GLOBAL] Deliverable filename should carry the book's full name (2026-08-22)
Unit: book-wide
Where: book.json "deliverable" (was out/chinas_secret_war.epub)
Problem: commissioner asked in chat that the final .epub carry the full name of the book, not the short slug.
Fix: set deliverable to "out/China's Secret War - A Documentary Record of the CCP's Intelligence and Security Work.epub" (title + subtitle). Old file retired; rebuilt; QA green.

### [LOCAL] ch10 folio 339: Zhang Bingnan monument romanization collision (2026-08-22)
Where: "'Zhang Bingnan' written by mistake for 'Zhang Bingnan'"
Problem: both names romanize identically, so the English said a name was mistaken for itself.
Fix: crop-verified 章炳南 miscarved as 张炳南; text now "carves the martyr Zhang Bingnan's surname with the wrong character"; NOTE-ADD carries 章/张.

### [LOCAL] ch10 folios 307/311/323: War-of-Resistance span 14/8/15 (2026-08-22)
Where: "fifteen years" (folio 323)
Problem: chapter opens "fourteen bitter years," later "fifteen years"; blind reader flagged the clash.
Fix: crop-verified all three figures as printed (source's own inconsistency); footnoted at "fifteen years." Rendered as printed.

### [LOCAL] ch10 folio 313: three-vs-two liaison officers (2026-08-22)
Where: "became the Nationalists' open intelligence officers in Yan'an"
Problem: "three ... stayed on" then "the two liaison staff officers" reads as a contradiction.
Fix: crop-verified as the source's own slip (three posted, two named and followed); footnoted; rendered as printed.

### [LOCAL] ch10 folio 332: Wang Shiwei note vs text (2026-08-22)
Where: note on "that very night Wang Shiwei was put to death"
Problem: body text says only "put to death"; note asserted "body thrown down a well" as if from the text.
Fix: crop-verified the text (处死 only); note now attributes the well detail to the later record ("by most later accounts ... a dry well").

### [LOCAL] ch11 folio 358: unreferenced "dead fish" (2026-08-22)
Where: "quietly poisoned his food; ... would not let Mao eat the dead fish"
Problem: "the dead fish" had no antecedent in English.
Fix: crop-verified 下毒/死鱼; changed "his food" to "a fish dish" so the later "dead fish" refers back. No fact added.

### [LOCAL] ch11 folio 368: Wu Shi / Baoding vs Chiang (2026-08-22)
Where: "it produced the Nationalist commander-in-chief Chiang Kai-shek"
Problem: same paragraph credits Baoding with producing Chiang and says he only attended the Japanese officers' school.
Fix: crop-verified as printed; footnoted (Chiang passed through a 1906 Baoding preparatory class, only loosely an alumnus; Wu Shi and Bai Chongxi were full graduates). Rendered as printed.

### [LOCAL] ch11 folio 370: third-person "her" in Xiao Minghua's testament (2026-08-22)
Where: "Just let her stay in Taiwan"
Problem: her own testament refers to herself in the third person.
Fix: crop-verified (就让她在台湾吧); the third person is the source's; footnoted. Baidu Baike: executed Taipei 1950, remains returned 1982.

### [LOCAL] ch12 folio 381: Xi'an "six dynasties" (2026-08-22)
Where: "the ancient capital of six dynasties"
Problem: Xi'an is conventionally the capital of thirteen dynasties; six is Nanjing's epithet.
Fix: crop-verified 六朝古都西安 as printed; footnoted; rendered as printed.

### [LOCAL] ch12 folio 390: intelligence/security/safety/public-security quadruplet (2026-08-22)
Where: "intelligence, security, safety, and public-security work"
Problem: "security, safety" read as redundant doubling in English.
Fix: crop-verified the source lists four distinct terms (情报/保卫/安全/公安); faithful; footnoted to distinguish the four domains.
