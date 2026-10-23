# F5 — Rust Foundations

**Track:** Foundations · **Prerequisite:** F3 · **Core for Systems and Security, strongly recommended for AI** · **Time:** 6 weeks, 90 hours · **Project:** P2 sysprobe in Rust

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Rust is the default language for the systems projects because it makes ownership, lifetimes, and concurrency explicit. You cannot write safe concurrent systems by hoping; Rust forces you to state who owns what and for how long. This course gives you enough Rust to read and write the systems labs without fighting the compiler every day.

## Outcomes

You can:

- explain ownership, borrowing, lifetimes, and move semantics;
- model data with structs, enums, pattern matching, and traits;
- use `Option`, `Result`, `?`, and custom error types;
- write generic code and trait bounds without over-abstracting;
- use `Box`, `Rc`, `RefCell`, `Arc`, and `Mutex` appropriately;
- write unit, integration, and documentation tests;
- use Cargo workspaces, features, and dependencies responsibly;
- write a small concurrent program with threads and channels;
- call C from Rust and explain the `unsafe` boundary;
- use `clippy`, `rustfmt`, and `miri` as part of the workflow.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [The Rust Programming Language](https://doc.rust-lang.org/book/) | Ch. **1–10** | Core language |
| The Rust Book | Ch. **11–13**, 15–16 | Testing, closures/iterators, smart pointers, threads |
| The Rust Book | Ch. **19–20** | Unsafe, FFI, advanced traits (selected) |
| [Rustlings](https://github.com/rust-lang/rustlings) | All exercises | Active recall |
| [Rust Atomics and Locks](https://marabos.nl/atomics/) | Ch. **1–2** | Threads and atomics preview; full read in S6 |
| [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/) | Naming, docs, errors | Professional habits |

## Modules

### 1. Ownership and borrowing

- stack vs heap, moves, copies, clones;
- immutable and mutable references;
- borrowing rules and aliasing XOR mutability;
- lifetimes: elision, struct lifetimes, `'static`;
- slices and string types (`String` vs `&str`);
- ownership in function signatures and APIs.

### 2. Data modelling

- structs, tuple structs, methods, associated functions;
- enums and exhaustive pattern matching;
- `Option`, `Result`, `?`, error propagation;
- modules, crates, visibility;
- traits, default methods, trait objects vs generics;
- `derive`, `Debug`, `Clone`, `PartialEq`, `Eq`, `Hash`;
- newtypes and type-state patterns.

### 3. Collections, iterators, closures

- `Vec`, `HashMap`, `BTreeMap`, `HashSet`, `VecDeque`;
- iterators, laziness, `map`/`filter`/`fold`/`collect`;
- closures, captures, `Fn`/`FnMut`/`FnOnce`;
- `Iterator` implementation;
- performance: allocation, `&str` vs `String`, `Cow`.

### 4. Errors, testing, tooling

- `Result` vs panics; when to panic;
- custom error enums, `thiserror`, `anyhow` (choose one policy);
- unit/integration/doc tests;
- property testing with `proptest` or `quickcheck`;
- `cargo fmt`, `clippy`, `miri`, `cargo audit`;
- Cargo features, workspaces, dependency hygiene.

### 5. Smart pointers and concurrency

- `Box`, `Rc`, `RefCell`, `Weak`;
- `Arc`, `Mutex`, `RwLock`, channels;
- `Send`/`Sync` (concept);
- scoped threads;
- async/await overview (do not deep-dive before S6);
- common deadlocks and lock poisoning.

### 6. FFI and unsafe

- `extern "C"`, `#[no_mangle]`, `bindgen` (intro);
- raw pointers, `unsafe` blocks, safety comments;
- `repr(C)`, layout, alignment;
- calling Rust from C and C from Rust;
- what `unsafe` does and does not guarantee.

## Labs

### Lab 1 — Rustlings and core exercises

Complete Rustlings. Then implement ten small programs: temperature converter, word count, CSV parser, JSON round trip, matrix multiply, linked list, stack/queue, binary search, trait-based shape area, and error-handling CLI.

### Lab 2 — Library with tests

Build a small library crate with a public API, documentation, unit tests, integration tests, and one property test. Run `clippy` and `miri`.

### Lab 3 — Concurrent counter and bounded queue

Implement an atomic counter and a bounded queue with `Mutex`/`Condvar` or channels. Write a test that would fail with a race. Benchmark single-thread vs multi-thread.

### Lab 4 — C FFI

Write a C function and call it from Rust. Then expose a Rust function to C. Document the safety contract, ownership, and error handling across the boundary.

### Lab 5 — P2 sysprobe in Rust

Rewrite the F3 C sysprobe in safe Rust. Compare the guarantees and the places where `unsafe` or OS-specific APIs are still required.

## Exercises

1. Fix ten borrow-checker errors and explain each fix.
2. Implement a generic stack and queue with trait bounds.
3. Write a custom error type and propagate it with `?`.
4. Implement `Iterator` for a custom type.
5. Use `Rc<RefCell<T>>` to build a shared tree, then explain why `Arc<Mutex<T>>` is different.
6. Write a thread-safe cache with `RwLock`.
7. Write a test that catches a use-after-free equivalent at compile time.
8. Explain `Send` and `Sync` in one paragraph each.
9. Write a safety comment for an `unsafe` block.
10. Compare a `Vec<String>` and a `Vec<&str>` API.

## Project increment — P2 sysprobe (Rust)

Implement a CLI that prints process ID, memory maps, open file descriptors, and one syscall result. Add tests and a comparison with the C version.

**Brief:** [P2 — sysprobe](../projects/project-ladder.md#p2--sysprobe)

## Exit check

- [ ] explain ownership and borrowing with a diagram;
- [ ] write a generic function with trait bounds;
- [ ] handle errors without `unwrap` in library code;
- [ ] write a concurrent program and explain why it is correct;
- [ ] call C from Rust and state the safety contract;
- [ ] use `clippy`, `rustfmt`, and tests in a clean checkout;
- [ ] explain one thing Rust prevents and one thing it does not.

## Common failure modes

- Fighting the borrow checker with `.clone()` everywhere.
- Using `Rc<RefCell<T>>` as a default instead of a deliberate choice.
- `unwrap()` in library code.
- Over-abstracting with traits before there are two implementations.
- Assuming `unsafe` means "fast" or "no rules."
- Ignoring `Send`/`Sync` when moving data across threads.

## Evidence to commit

- `labs/foundations/F5/` with Rustlings notes, library, concurrency lab, FFI lab
- P2 sysprobe Rust version
- `notes/foundations/F5/summary.md`

## Optional depth

- *Programming Rust* (Blandy, Orendorff, Tindall) for deeper systems patterns.
- *Rust for Rustaceans* (Gjengset) for API design and advanced traits.
- *Async Rust* (Wasmuth) before S6/S10.
- Read the standard library docs for `std::sync`, `std::thread`, and `std::error`.
