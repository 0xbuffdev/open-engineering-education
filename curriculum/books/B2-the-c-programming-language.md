# B2 — *The C Programming Language*

**Authors:** Brian W. Kernighan & Dennis M. Ritchie · **Edition:** 2nd, 1988 (ANSI C) · **Level:** intermediate

The canonical compact C book. It teaches the language through complete, idiomatic programs and then the UNIX system interface. It is terse: read with a compiler open, type every example, and do the exercises. The book is old, so pair it with a modern compiler's warnings and sanitizers.

## Structure

| Chapter | Title | Use |
| --- | --- | --- |
| 1 | A Tutorial Introduction | First C program, types, control flow, functions, arrays |
| 2 | Types, Operators, and Expressions | Integer widths, conversions, bitwise operators |
| 3 | Control Flow | `if`, loops, `break`/`continue`, `goto` |
| 4 | Functions and Program Structure | Scope, storage classes, preprocessor, recursion |
| 5 | Pointers and Arrays | The core of C; read every section slowly |
| 6 | Structures | Structs, self-referential types, unions, bit-fields |
| 7 | Input and Output | `stdio`, formatted I/O, files, errors |
| 8 | The UNIX System Interface | File descriptors, low-level I/O, `malloc` implementation |
| A | Reference Manual | Lookup, not linear reading |
| B | Standard Library | Lookup |

## Key sections

| Section | Title | Notes |
| --- | --- | --- |
| 5.1 | Pointers and Addresses | Address-of and dereference |
| 5.2 | Pointers and Function Arguments | Pass-by-value, simulate output parameters |
| 5.3 | Pointers and Arrays | Array decay and pointer arithmetic |
| 5.4 | Address Arithmetic | Bounds, one-past-the-end, pointer difference |
| 5.5 | Character Pointers and Functions | String literals and mutable arrays |
| 5.6 | Pointer Arrays; Pointers to Pointers | `argv`, sorting pointers |
| 5.7 | Multi-dimensional Arrays | Row-major layout |
| 5.8 | Initialization of Pointer Arrays | Tables of strings |
| 5.9 | Pointers vs. Multi-dimensional Arrays | Different memory layouts |
| 5.10 | Command-line Arguments | `argc`/`argv` |
| 5.11 | Pointers to Functions | Callbacks, dispatch tables |
| 5.12 | Complicated Declarations | `cdecl`-style reading |
| 6.2 | Structures and Functions | Pass/return by value and pointer |
| 6.3 | Arrays of Structures | Records |
| 6.4 | Pointers to Structures | `->` and linked structures |
| 6.5 | Self-referential Structures | Linked lists and trees |
| 6.7 | Typedef | Naming types |
| 6.8 | Unions | Overlapping storage; type-punning hazards |
| 6.9 | Bit-fields | Portability caveats |
| 7.5 | File Access | `fopen`, modes, `fclose` |
| 7.6 | Error Handling | `ferror`, `perror`, `exit` |
| 7.7 | Line Input and Output | `fgets`, `fputs` |
| 7.8 | Miscellaneous Functions | `malloc`, `free`, `system`, `exit` |
| 8.1 | File Descriptors | The kernel object behind `FILE *` |
| 8.2 | Low Level I/O — Read and Write | `read`/`write`, partial I/O, `errno` |
| 8.3 | Open, Creat, Close, Unlink | Flags and permissions |
| 8.4 | Random Access — Lseek | Offset semantics |
| 8.5 | Example — Fopen and Getc | Buffering implementation |
| 8.6 | Example — Listing Directories | `opendir`/`readdir` |
| 8.7 | Example — A Storage Allocator | Free-list allocator, alignment, coalescing |

## Course map

| Course | Read | Why | Check |
| --- | --- | --- | --- |
| [F3](../foundations/F3-engineering-practice.md) | Ch. **1–3**, §§**5.1–5.4**; recommended Ch. **4**, §§**5.5–5.12**, Ch. **6**, §§**7.5–7.8**, §§**8.1–8.4**, §**8.7** | C syntax, pointers, structs, file I/O, allocator | Write a small multi-file C program with tests |
| [S1](../systems/S1-computer-systems-foundations.md) | Ch. **4–6**, §§**7.5–7.8**, §§**8.1–8.7** | Functions, pointers, structs, syscalls, allocator | Trace a `read`/`write` and a leak |
| [S10](../systems/S10-linux-systems-programming-and-networking.md) | Ch. **8** | UNIX system interface | Build a socket client/server with correct I/O |
| [D2](../security/D2-memory-corruption-and-binary-exploitation.md) | Ch. **5**, §§**8.1–8.7** | Pointers, arrays, allocation | Explain one overflow and one lifetime bug |
| [S17](../systems/S17-compilers-and-language-runtimes.md) | Ch. **5**, **7–8** (revisit) | Pointers, structures, linkage, memory | Map C constructs to runtime layout |

## Reading route

1. **F3:** Ch. 1–3, then §5.1–5.4. Stop and compile every example. Do at least six exercises.
2. **S1:** Ch. 4–6, then §7.5–7.8 and Ch. 8. Focus on file descriptors, partial I/O, and the allocator.
3. **S10:** Ch. 8 again, now with `strace`, `valgrind`, and a real service.
4. **D2:** Ch. 5 and §8.7; connect pointer/lifetime bugs to memory corruption.

## Exercises that are worth the time

- 1-13, 1-19, 1-22 (line/word handling)
- 2-6, 2-7, 2-8 (bit operations)
- 3-2, 3-3, 3-5 (control flow and escapes)
- 4-1, 4-2, 4-12 (functions and recursion)
- 5-3, 5-5, 5-7, 5-8, 5-10, 5-13, 5-17 (pointers, arrays, sorting)
- 6-2, 6-4, 6-6 (structures and tables)
- 7-1, 7-2, 7-6 (I/O and diff)
- 8-3, 8-5, 8-7 (syscalls, directory walk, allocator)

## Edition and compiler notes

- The book is ANSI C (C89). Use `-std=c17 -Wall -Wextra -Wpedantic -Wconversion` and expect warnings for old idioms.
- `gets` is removed/unsafe; never use it. Replace examples with `fgets`.
- `malloc` casts are unnecessary in C and the book avoids them. Do not "fix" that.
- The book's `char` signedness, integer sizes, and allocator assumptions are platform-dependent. Test on your actual Linux target.
- Do not treat every example as a security template; D2 shows where these APIs fail.

## Acquisition

Purchase or borrow a legal copy. Do not commit a PDF. The ISBN for the 2nd edition is 978-0131103627.
