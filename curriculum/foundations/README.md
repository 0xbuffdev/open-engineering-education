# Track 1 — Foundations

Complete this track before any specialisation. It is deliberately broader than the old four-course version: programming, data structures, engineering practice, mathematics, Rust, and data/web foundations are all prerequisites for professional work.

**Time:** 720 hours · 48 course-weeks · roughly 9–12 months at 15 h/week with overlap and buffer.

## Courses

| Code | Course | Prerequisite | Weeks | Hours | Project |
| --- | --- | --- | ---: | ---: | --- |
| [F0](F0-setup-tools-and-study-system.md) | Setup, Tools & Study System | none | 1 | 15 | environment + study log |
| [F1](F1-programming-i-python.md) | Programming I: Python | F0 | 8 | 120 | P1 ledgerlab v1 |
| [F2](F2-data-structures-and-algorithms.md) | Data Structures & Algorithms | F1 | 10 | 150 | P1 query/index work |
| [F3](F3-engineering-practice.md) | Engineering Practice: Git, Testing, Debugging, C & Linux | F1, F2 | 8 | 120 | P1 hardened + C drills |
| [F4](F4-mathematics-i.md) | Mathematics I: Discrete Math, Linear Algebra, Calculus & Probability | F1 | 10 | 150 | math notebook |
| [F5](F5-rust-foundations.md) | Rust Foundations | F3 | 6 | 90 | P2 sysprobe in Rust |
| [F6](F6-data-sql-and-web-foundations.md) | Data, SQL & Web Foundations | F2, F3 | 5 | 75 | P1 API/SQL increment |

F5 is required for the Systems and Security tracks and strongly recommended for AI. F6 is required for every track.

## Recommended order

```text
F0 -> F1 -> F2 -> F3 -> F5 -> F6
              \-> F4 (can run beside F2/F3)
```

F4 may run beside F2 or F3 if your math is weak and you need more calendar time. Do not start F5 before F3: ownership and borrowing make much more sense after C pointers and manual memory.

## What "Foundations complete" means

- You can write a tested Python CLI from an empty directory.
- You can implement the core data structures and defend their complexity.
- You can compile, test, and debug C with warnings and sanitizers.
- You can use Git branches, merges, bisect, and reflog to recover work.
- You can derive a gradient, multiply matrices, and calculate a conditional probability.
- You can write safe Rust with ownership, traits, and tests.
- You can write correct SQL and debug an HTTP request.
- You have completed P1 and can explain its biggest failure.

## Reading

The local books used here are B1 (*But How Do It Know?*), B2 (*The C Programming Language*), and selected B5 chapters. Everything else is external and listed in [../resources.md](../resources.md). Exact sections are in each course file and in [../books/](../books/README.md).

## Practice and project workspaces

Create a workspace with:

```bash
./scripts/new-course-workspace foundations F1
```

This creates `labs/foundations/F1/`, `exercises/foundations/F1/`, and `notes/foundations/F1/`. The course file is the assignment; the workspace is where you do it.

## Exit standard

You are ready for a specialisation when you can pass every F0–F6 exit check and show the P1 evidence. If one check is weak, fix it now; every later track assumes it.
