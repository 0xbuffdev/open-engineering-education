# Book Maps

These pages are navigation aids for the six core reference books used by the curriculum. They map **course sections to chapters/sections**, not to page numbers. Pages differ between print, PDF, and reflowed editions; chapter and section titles are the stable identifiers.

## Local-copy policy

- Keep legally obtained PDFs/EPUBs in `books/` locally. That directory is ignored by Git for PDFs.
- Do **not** commit copyrighted books, purchased files, or scans.
- Do not rely on a search engine's page number. Use the section title and the book's own table of contents.
- If your edition differs, write the mapping in `notes/<track>/<course>/resources.md` and use the closest matching title.
- When a book has numbered sections that differ by edition, the course file names the topic as well as the number.

## The library

| Code | Book | Edition used here | Best for | Access |
| --- | --- | --- | --- | --- |
| [B1](B1-but-how-do-it-know.md) | *But How Do It Know?* — J. Clark Scott | 1st ed., 2009 | Gates → CPU → OS, absolute beginner | Purchase or local copy |
| [B2](B2-the-c-programming-language.md) | *The C Programming Language* — Kernighan & Ritchie | 2nd ed. | C, pointers, UNIX I/O | Purchase or local copy |
| [B3](B3-digital-design-and-computer-architecture.md) | *Digital Design and Computer Architecture* — Harris & Harris | 2nd ed. (MIPS) | Digital logic, architecture, caches, VM | Purchase or local copy |
| [B4](B4-operating-systems-three-easy-pieces.md) | *Operating Systems: Three Easy Pieces* — Arpaci-Dusseau | v1.10, 2023 | Processes, VM, concurrency, persistence | [Free online](https://pages.cs.wisc.edu/~remzi/OSTEP/) |
| [B5](B5-the-linux-programming-interface.md) | *The Linux Programming Interface* — Michael Kerrisk | 1st ed., 2010 | Linux syscalls, processes, sockets | Purchase or local copy |
| [B6](B6-what-every-programmer-should-know-about-memory.md) | *What Every Programmer Should Know About Memory* — Ulrich Drepper | 2007 paper | Caches, NUMA, memory performance | [Free PDF](https://people.freebsd.org/~lstewart/articles/cpumemory.pdf) |

B4 and B6 are legally free. B1–B3 and B5 require a purchased or borrowed copy. The maps work without a local file; they tell you what to read when you obtain one.

## Read in this order

```text
B1  Foundations/F1 and F3; Systems/S2
B2  Foundations/F3; Systems/S1 and S10
B3  Systems/S2–S5, S7, S13
B4  Systems/S1, S5, S6, S10–S12, S14–S15
B5  Systems/S1, S5–S6, S9–S12, S16; Security/D1–D4
B6  Systems/S3–S9, S13; AI/AI16
```

You do not need to read any book cover to cover. Each course file gives a bounded assignment. The per-book pages show the complete dependency map so you can revisit a section when a later course needs it.

## Page-number verification

If you want page-level checkpoints:

1. Open the exact edition listed above.
2. Compare its table of contents with the section titles on the book page.
3. Record the printed page range in `notes/<track>/<course>/resources.md`.
4. Never copy a page range from an online search result into the curriculum; editions and PDF offsets differ.

No PDFs are currently tracked in this repository. If you place legal local copies in `books/`, they remain untracked by design.

## What the books do not cover

The local library is strong on C, Linux, operating systems, architecture, and memory. It does **not** cover modern distributed systems, ML, cryptography, web security, cloud-native security, or AI safety in depth. Those gaps are filled by [../resources.md](../resources.md) and the course files; do not pretend a local book covers a topic it does not.
