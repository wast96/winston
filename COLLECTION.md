# COLLECTION.md — the shelf, not the book

The finished translations form a collection, and most of them share a world:
Republican-era China, Shanghai, and its secret wars. This file holds the
conventions that make the books read and shelve as a set, and the cross-book
knowledge no single project can see. It lives on the template branch; consult
it at Step 0a of every new book.

## Series metadata (so reading apps shelve the set together)

Every `book.json` sets:

- `series`: `"Winston Translations"` for the shelf as a whole (rename once,
  here, if a different shelf name is preferred; then cascade on the next
  rebuild of each book).
- `series_index`: the next free number; keep the assignment list here.

The builder emits both the calibre series metas and the EPUB3
belongs-to-collection form. Keep one cover system across the set (the
generated typographic covers already share a design).

## The shelf as of 2026-08

| # | Book | Kind | Period |
|---|------|------|--------|
| 1 | Wang Yaqiao (narrative history) | history, partly assessed | 1920s-30s Shanghai |
| 2 | The Theory and Practice of Secret Service Work (Gu Shunzhang) | tradecraft manual | 1933 |
| 3 | Inside the Juntong (Shen Zui) | memoir | 1930s-40s |
| 4 | The Huang Mulan memoir | memoir | 1920s-40s |
| 5 | The Whistling Wind (Xu Xu) | novel | wartime Shanghai |
| 6 | Midnight (Mao Dun) | novel | 1930 Shanghai |
| 7 | A Thousand Li of Rivers and Mountains (Sun Ganlu) | novel | 1933 Shanghai |
| 8 | On a Hair Trigger | novel | Republican era |
| 9 | The Longest Day in Chang'an (Ma Boyong) | novel | Tang dynasty |

## Suggested reading order (the Republican-era spine)

The nonfiction frames the fiction. A reader who wants the world before the
stories: 2 (the tradecraft manual, the rules of the game) → 3 (the Juntong
from inside) → 4 (the underground from the other side) → 1 (the freelance
third force). Then the novels against that ground: 6 → 7 → 5 → 8. Book 9
stands alone (Tang, not Republican) and can be read any time.

## Cross-book connections worth a reader's note

When a new book meets one of these, the footnote may say the subject is
treated at length in another book of the collection:

- **Gu Shunzhang** is the AUTHOR of book 2 and a recurring figure in 1, 3, 4
  and 7's world. The books do not agree about him; that disagreement is
  content, not error.
- **Shen Zui** (author of 3) discusses figures who appear across 1 and 2;
  his conspicuous silences were themselves evidence in book 1's fact-check.
- **Dai Li and the Juntong** appear in 1, 2, 3, 4 and 8's world; the agreed
  shelf rendering is in `authority.json` (reconcile the current three-way
  drift on 军统 before the next book uses it).
- The **Shanghai concessions' streets and institutions** (Bubbling Well
  Road, the Municipal Police, the Lyceum, Wing On) recur everywhere; the
  authority file carries the observed renderings, including the deliberate
  period-flavor deviations (Chungking/Kweilin in the 1940s memoir voice).
- The books sometimes CONTRADICT each other about the same events. That is a
  feature of the shelf: note it, do not harmonize it.

## Authority discipline

`authority.json` (same branch) is the machine-readable side of this file:
every zh term used by two or more books, every rendering observed, and a
`reconcile` status on live disagreements. Rules:

1. New book: consult before deciding any rendering a previous book may have
   decided already.
2. Deliberate deviation (register, period flavor): allowed, but record it in
   the book's own glossary note AND leave the authority entry as it stands.
3. Completion: feed the book's decided renderings back in.
4. A corrections pass that changes a shelf-wide rendering updates the
   authority file in the same commit.
