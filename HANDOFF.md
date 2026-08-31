# HANDOFF — The Tragedy of the Chinese Revolution (annotated edition)

## THE BOOK IS COMPLETE

All 22 units (front matter + ch01–20) are prepared. There is no next batch and
no kickoff to paste. The full completion report is **COMPLETION.md** — read that
first; it records what the finished edition contains, every whole-book check and
its result, the sampled error rate, the residual uncertainties, and the exact
rebuild commands.

Status in one line: **1,308 footnotes** (1,009 author + 299 editorial), a
**144-row glossary** and 7-name Principal Characters page, a **linked
back-matter Index** (501 entries, every folio reference a live hyperlink),
`qa_epub` PASS, **epubcheck 0 errors / 0 warnings**, `check_fidelity` and
`check_apparatus` green. Deliverable:
`out/The Tragedy of the Chinese Revolution.epub`, committed to the branch with
`git add -f`.

## Further work is a CORRECTIONS PASS, not a new batch

If the commissioner reads the EPUB and files corrections, follow the corrections
workflow in CLAUDE.md: transcribe items into `CORRECTIONS.md`, apply GLOBAL
changes via a glossary/style change plus a grep-driven edit across ALL built
units (notes and glossary bodies included), rebuild, run the full QA battery,
and add a dated `CHANGELOG.md` entry. A corrections pass with zero items is
still a clean-checkout regression run (re-clone, regenerate, rebuild, re-verify,
prune stray branches).

## Rebuild from a clean checkout

setup.sh installs Chinese OCR packs the extractor never uses, NOT the English
wordlists `extract_isaacs.py` needs, so after it run
`sudo apt-get install -y wamerican wbritish`. Then:

    python3 scripts/build_reading_epub.py
    python3 scripts/qa_epub.py
    java -jar /tmp/epubcheck-5.1.0/epubcheck.jar "out/The Tragedy of the Chinese Revolution.epub"

## Do-not-revert tooling (accumulated across B01–B09)

- **scripts/extract_isaacs.py** — faithful-reset extractor (de-hyphenation,
  drop-cap fold, furniture strip, superscript-mark removal, asterisk-footnote
  capture, block-quote capture, pagemap). Blind spots still hand-fixed and
  re-verified with check_fidelity: a real compound hyphen broken at a line end
  (the "war-weary" class), a born-digital dropped hyphen in a WG name, a stray
  glyph / control char, a stray '*' that is not a footnote mark.
- **scripts/check_fidelity.py** — whole-unit letters+digits fidelity gate.
- **scripts/dump_anchors.py + anchor_offsets.py** — resolve in-text marks to
  unique verbatim anchors.
- **The per-batch note/glossary generators** (build_ch01_notes.py through
  build_ch1820_notes.py; the matching *_editorial.py and add_*_glossary.py). The
  ch1820 author builder's AST_GROUP handles a multi-paragraph asterisk footnote.
- **scripts/build_reading_epub.py** — annotated-edition chrome; `{q}` block
  quotes; TWO-STREAM per-chapter note numbering (author arabic / editorial
  roman); pagebreak anchors + page-list nav; the **linked-index renderer**
  (`render_index`, driven by `data/index.json`) and its CSS. REFUSES a build on
  an unmatched note anchor or unplaced figure spec.
- **scripts/parse_index.py** — parses the two-column printed index into
  data/index.json (column-aware, soft-hyphen join, ref-token disambiguation via
  the ≤339 page bound + roman-folio whitelist, cross-ref capture).
- **scripts/feed_authority.py, render_term_ledger.py, deep_audit.py** — the
  completion tools (authority feed-back, human-auditable ledger, fixed-seed
  letter-coverage audit).
- **GLOSSARY IS SECTIONED (trap):** glossary.json has people/organizations/
  places/terms sections; apparatus_merge FLATTENS it — add rows straight into
  their section with a small add_*_glossary.py. Notes/figures merge fine.

## Standing facts a corrections session needs

- Body offset is 23 (printed = PDF page − 23); front matter was 1. Cite ARABIC
  folios in body-chapter notes, roman in the front matter.
- Two deliberate registers: Isaacs's British 1938 spelling in the body,
  American English in the editorial apparatus. `check_reconcile.py` will always
  flag "MIXED LOCALE" — that is the design, not a defect (COMPLETION.md §checks).
- No OCR, no zh source: translation-only checks (numbers/parity/qc_entities/
  register/epithet-drift) do not apply.
- tests/run_tests.py "hook stands down on template stub" FAILS by design.
- Container is reprovisioned fresh each session; expect a stray per-task branch —
  reconcile onto `claude/tragedy-of-the-chinese-revolution`, the one working
  branch.
