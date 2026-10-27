# S17 — Compilers & Language Runtimes

**Track:** Systems · **Prerequisite:** S2, S6 · **Elective** · **Time:** 6 weeks, 90 hours · **Project:** elective
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Demystify what happens between source text and execution. You will build a small language front end, an intermediate representation, an optimizer, and a bytecode interpreter or native backend, then study how real runtimes manage memory and concurrency.

## Outcomes

You can:

- explain lexical analysis, parsing, ASTs, and name resolution;
- build a recursive-descent parser with useful errors;
- define and implement a type checker for a small language;
- lower an AST to a typed IR and generate bytecode or assembly;
- explain SSA, constant folding, dead-code elimination, and register allocation;
- explain calling conventions, stack frames, and ABI boundaries;
- build a tree-walking interpreter and a bytecode VM;
- explain mark-and-sweep, copying, and generational garbage collection;
- explain JIT compilation, inline caches, and deoptimization at a high level;
- use a real compiler's IR and optimization pipeline as evidence.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| *Crafting Interpreters* (Nystrom) | Part I (Ch. 1–13), Part II (Ch. 14–23), selected Ch. 24–30 | Scanner, parser, resolver, interpreter, bytecode VM, GC |
| *Engineering a Compiler* (Cooper & Torczon) | Ch. **1–4, 8–10** | Front end, IR, optimization, code generation |
| *Compilers: Principles, Techniques, and Tools* (Aho et al.) | Ch. **1–3, 6, 8** | Reference for parsing and optimization |
| B2 *The C Programming Language* | Ch. **5, 7–8** (revisit) | Pointers, structures, linkage, memory |
| B3 *Digital Design and Computer Architecture* | Ch. **6–7** (revisit) | ISA and microarchitecture context |
| [LLVM Kaleidoscope tutorial](https://llvm.org/docs/tutorial/) | Chapters 1–7 | Real IR and code generation |
| [Cranelift / V8 / CPython design docs](https://github.com/bytecodealliance/wasmtime) | Selected design notes | Production runtime trade-offs |

## Modules

### 1. Front end

- source locations and diagnostics;
- lexing, tokens, maximal munch, string/number literals;
- context-free grammars, ambiguity, precedence;
- recursive descent and Pratt parsing;
- AST design and visitor patterns;
- error recovery;
- symbol tables, scopes, and name resolution;
- module/import boundaries.

### 2. Types and semantics

- type systems: static vs dynamic, structural vs nominal;
- type checking and inference (intro);
- closures, environments, and variable capture;
- evaluation order and side effects;
- mutability, aliasing, and ownership (connect to Rust);
- undefined behaviour versus runtime errors;
- specification of a small language.

### 3. Intermediate representation

- three-address code, control-flow graphs;
- SSA form and phi nodes;
- basic blocks and dominance;
- constant propagation/folding;
- dead-code elimination;
- common-subexpression elimination;
- inlining and loop optimizations;
- alias analysis and memory effects;
- debug information.

### 4. Back ends and runtimes

- instruction selection;
- register allocation (linear scan, graph colouring);
- calling conventions and stack frames;
- ABI, alignment, varargs;
- object layout and virtual dispatch;
- bytecode design and dispatch;
- stack vs register machines;
- linking, loading, and relocation (revisit S1);
- JIT, profiling, inline caches, deoptimization;
- ahead-of-time vs interpreter vs JIT trade-offs.

### 5. Memory management

- stack versus heap;
- manual memory management failure modes;
- reference counting and cycles;
- mark-and-sweep;
- copying/compacting collectors;
- generational and incremental collectors;
- write barriers and read barriers;
- finalizers and weak references;
- memory safety versus performance.

## Labs

### Lab 1 — Scanner and parser

Build a scanner and recursive-descent parser for a small expression/statement language. Include source spans, precedence, and at least three useful syntax-error messages with location.

### Lab 2 — Tree-walking interpreter

Add variables, functions, closures, conditionals, loops, and runtime errors. Write a conformance suite and a small benchmark. Explain environment capture and one bug you fixed.

### Lab 3 — Type checker or verifier

Add static types or a runtime contract verifier. Reject at least five invalid programs with precise errors. Explain one soundness limitation.

### Lab 4 — Bytecode VM

Lower the AST to bytecode. Implement a stack machine, call frames, and a garbage collector (mark-and-sweep is enough). Run the conformance suite and compare performance with the tree-walker.

### Lab 5 — Optimization and native back end

Implement three optimizations on an IR/CFG (constant folding, dead-code elimination, and one more). Measure their effect. Then either generate LLVM IR or a small native backend for a subset, and inspect the output with `objdump`.

## Exercises

1. Write a grammar and eliminate left recursion.
2. Hand-tokenize a snippet with strings and comments.
3. Draw the AST for a nested expression.
4. Explain lexical versus dynamic scoping with an example.
5. Convert a basic block to SSA.
6. Apply constant propagation to a small CFG.
7. Explain liveness and register interference.
8. Trace a function call through the calling convention.
9. Simulate mark-and-sweep on an object graph.
10. Explain one reason a JIT can beat an AOT compiler and one reason it cannot.

## Project increment (optional)

Build a small interpreter or bytecode VM, or add one optimization pass to a toy compiler. Benchmark it against a baseline, test the semantic edge cases, and document what the optimizer or runtime cannot prove. This can become a portfolio artifact or tooling for P4/P6, but it is not a new ladder project.

## Exit check

- [ ] build and run a small language from source to output;
- [ ] show syntax and type/runtime errors with locations;
- [ ] explain the AST-to-IR lowering;
- [ ] demonstrate a bytecode VM and a garbage collector;
- [ ] show one optimization with a measured effect;
- [ ] inspect generated code or LLVM IR and explain it;
- [ ] state the language's semantics and known limitations.

## Common failure modes

- Building a parser without a written grammar.
- Confusing syntax errors with semantic errors.
- Ignoring source locations until debugging becomes impossible.
- Implementing optimizations without a semantics test suite.
- Writing a GC that collects reachable objects.
- Assuming a benchmark difference proves an optimization without a profile.
- Treating undefined behaviour as "it works on my machine".

## Evidence to commit

- `labs/systems/S17/` with scanner, parser, interpreter, VM, GC, optimizer, native/LLVM output
- `notes/systems/S17/summary.md`
- A language specification and conformance suite

## Optional depth

- *Crafting Interpreters* Part III in full.
- *Modern Compiler Implementation in C/ML/Java* (Appel).
- *SICP* Chapter 4 (metalinguistic abstraction).
- LLVM `opt` pass pipeline and `llc`.
- *The Garbage Collection Handbook* (Jones, Hosking, Moss).
- CPython `ceval.c`, V8 Torque, or Wasmtime design notes.
