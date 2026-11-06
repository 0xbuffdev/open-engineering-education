# APP15 — Advanced TypeScript/Rust Application Development

**Program:** APP — Application Engineering
**Classification:** `elective`
**Type:** `course`
**Prerequisites:** [APP2](APP2.md), [APP3](APP3.md), [APP6](APP6.md)
**Duration:** 7 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Build applications using TypeScript and Rust where explicit type contracts, runtime boundaries, ownership and concurrency matter. Compare their strengths without presenting one language as universally superior, and integrate a Rust component into a TypeScript-facing application through a documented interface.

This specialization is optional and not required for APP9 or APP graduation.

## Learning outcomes

By the end of this course, the learner will be able to:

- Model domain invariants with TypeScript discriminated unions, strict narrowing and runtime validation.
- Explain Rust ownership, borrowing, lifetimes and error handling through executable examples.
- Design a stable typed boundary between TypeScript and Rust using explicit serialization and versioning.
- Test async and concurrent behavior, cancellation and error propagation across boundaries.
- Measure integration costs and defend a deliberate language/tool choice.

## Modules

### Module 1 — TypeScript Contracts & Runtime Boundaries

#### Outcomes

- Distinguish compile-time types from runtime validation.
- Design discriminated data models and safe parsing boundaries.

#### Lessons

1. **Course introduction: Advanced TypeScript/Rust Application Development** — `lesson`

   Build applications using TypeScript and Rust where explicit type contracts, runtime boundaries, ownership and concurrency matter. Compare their strengths without presenting one language as universally superior, and integrate a Rust component into a TypeScript-facing application through a documented interface.
2. **Discriminated unions, generics and strict narrowing** — `lesson`
3. **Runtime validation and versioned schema contracts** — `lesson`
4. **Type safety versus runtime safety** — `test`
5. **Harden a TypeScript API boundary** — `lab`

### Module 2 — Rust Ownership & Error Semantics

#### Outcomes

- Explain moves, borrows, lifetimes and trait-based abstraction.
- Handle fallible operations with Result and explicit error context.

#### Lessons

1. **Ownership, borrowing and lifetimes** — `lesson`
2. **Enums, traits and structured errors** — `lesson`
3. **Reasoning about ownership** — `test`
4. **Repair ownership and error defects** — `lab`

### Module 3 — Interoperability & Contract Evolution

#### Outcomes

- Design a language-independent wire or FFI boundary.
- Avoid unchecked memory sharing and version coupling.

#### Lessons

1. **Serialization and public interface boundaries** — `lesson`
2. **FFI versus process interfaces and compatibility** — `lesson`
3. **Choosing an integration mechanism** — `test`
4. **Integrate a typed Rust component** — `lab`

### Module 4 — Async, Concurrency & Diagnostics

#### Outcomes

- Explain cancellation, backpressure and shared-state hazards.
- Measure and diagnose performance without relying on language stereotypes.

#### Lessons

1. **Async execution and bounded work** — `lesson`
2. **Thread safety, tracing and benchmarking** — `lesson`
3. **Diagnosing concurrency failures** — `test`
4. **Reproduce a concurrency defect** — `lab`

### Module 5 — TypeScript–Rust Integrated Application

#### Outcomes

- Integrate the elective's techniques in a working and verifiable application change or system.
- Evaluate correctness, operational limitations and trade-offs through reproducible evidence.

#### Lessons

1. **TypeScript–Rust Integrated Application** — `lab`

## Completion requirements

- Complete the required module checkpoints and practical exercises, then complete the final integration lab.
- State tools, versions, system assumptions and test data for reproducibility.
- Retain artifacts, test results, design decisions, an investigated failure and a technical retrospective in accordance with [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required module checkpoints and practical work:**

- **Module 1 — TypeScript Contracts & Runtime Boundaries:** Pass `Type safety versus runtime safety` by explaining and applying the module outcomes; perform the `Harden a TypeScript API boundary` lab: Replace unchecked casts with validated inputs and tests for invalid, missing and newer-version fields. Retain Type-level checks, malformed-input tests and schema documentation.
- **Module 2 — Rust Ownership & Error Semantics:** Pass `Reasoning about ownership` by explaining and applying the module outcomes; perform the `Repair ownership and error defects` lab: Build a small Rust parser/library, repair seeded ownership and error-handling mistakes and demonstrate deterministic failures. Retain Compiler diagnostics, tests and a short ownership explanation.
- **Module 3 — Interoperability & Contract Evolution:** Pass `Choosing an integration mechanism` by explaining and applying the module outcomes; perform the `Integrate a typed Rust component` lab: Expose a Rust data transform to a TypeScript client via a process/API or well-defined binding; test corrupt and mixed-version inputs. Retain Interface specification, build recipe and contract tests.
- **Module 4 — Async, Concurrency & Diagnostics:** Pass `Diagnosing concurrency failures` by explaining and applying the module outcomes; perform the `Reproduce a concurrency defect` lab: Introduce controlled cancellation or concurrent load; detect races/partial work and implement a bounded, tested fix. Retain Concurrency test, traces and measurement conditions.

**Final integration lab — TypeScript–Rust Integrated Application:**

Create a TypeScript application or API that uses a Rust library or service for a bounded domain capability. Define and version the interface, validate untrusted input, test concurrency and failure behavior and measure whether the split improves the intended constraint.

**Success criteria:**

- Run both components from a clean checkout with documented toolchain versions.
- Reject malformed data and demonstrate compatibility or explicit failure across interface versions.
- Show safe, bounded concurrent operation and evidence for recovery from one injected failure.
- Explain ownership and runtime safety boundaries, benchmark limitations and the cost of the language split.

**Evidence to retain:**

- Version-controlled implementation and configuration, including clean-rebuild instructions.
- Inputs and repeatable tests, output or measurements, and failure/recovery records.
- Trade-off analysis, limitations and technical retrospective.

**Failure analysis:**

Analyze mismatched schemas, panics escaping service boundaries, stale generated bindings, cancellation races, and overgeneralization from microbenchmarks.

**Exit demonstration:**

Demonstrate the resulting implementation, explain its key mechanisms, reproduce at least one failure and recovery and defend the chosen trade-offs with inspectable evidence.
