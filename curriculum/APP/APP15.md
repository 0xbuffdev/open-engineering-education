# APP15 — Advanced TypeScript/Rust Application Development

**Program:** APP — Application Engineering
**Classification:** `elective`
**Type:** `course`
**Prerequisites:** [APP2](APP2.md), [APP3](APP3.md), [APP6](APP6.md)
**Duration:** 10 weeks
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
- Create and evolve a reusable TypeScript package with compatible runtime and type contracts.
- Build safe Rust application components with explicit ownership, error contracts and tested concurrency.
- Integrate TypeScript and Rust through a versioned, validated interface with documented memory and failure boundaries.
- Profile a reproducible cross-language workload and defend the build/deployment and architecture trade-offs.

## Modules

### Module 1 — TypeScript Contracts & Runtime Boundaries

#### Outcomes

- Distinguish compile-time types from runtime validation.
- Design discriminated data models and safe parsing boundaries.

- Model interfaces with TypeScript types while verifying real runtime input.

#### Lessons

1. **Course introduction: Advanced TypeScript/Rust Application Development** — `lesson`

   Build applications using TypeScript and Rust where explicit type contracts, runtime boundaries, ownership and concurrency matter. Compare their strengths without presenting one language as universally superior, and integrate a Rust component into a TypeScript-facing application through a documented interface.
2. **Discriminated unions, generics and strict narrowing** — `lesson`
3. **Runtime validation and versioned schema contracts** — `lesson`
4. **Advanced conditional and mapped types** — `lesson`
5. **Strict compiler options and type narrowing** — `lesson`
6. **Safe runtime parsing and schema migration** — `lesson`
7. **Type safety versus runtime safety** — `test`
8. **Harden a TypeScript API boundary** — `lab`

### Module 2 — Rust Ownership & Error Semantics

#### Outcomes

- Explain moves, borrows, lifetimes and trait-based abstraction.
- Handle fallible operations with Result and explicit error context.

- Build a Rust library with explicit ownership, testable error contracts and safe resource handling.

#### Lessons

1. **Ownership, borrowing and lifetimes** — `lesson`
2. **Enums, traits and structured errors** — `lesson`
3. **Cargo projects, packages and Rust test tooling** — `lesson`
4. **Ownership, borrowing and move semantics** — `lesson`
5. **Lifetimes, trait objects and error ergonomics** — `lesson`
6. **Modules, visibility and safe resource cleanup** — `lesson`
7. **Reasoning about ownership** — `test`
8. **Repair ownership and error defects** — `lab`

### Module 3 — Interoperability & Contract Evolution

#### Outcomes

- Design a language-independent wire or FFI boundary.
- Avoid unchecked memory sharing and version coupling.

- Choose interoperation mechanisms according to reliability, security and deployment constraints.

#### Lessons

1. **Serialization and public interface boundaries** — `lesson`
2. **FFI versus process interfaces and compatibility** — `lesson`
3. **Process, JSON and FFI boundary trade-offs** — `lesson`
4. **Schema evolution and compatibility testing** — `lesson`
5. **Encoding, ABI and memory ownership across language boundaries** — `lesson`
6. **Choosing an integration mechanism** — `test`
7. **Integrate a typed Rust component** — `lab`

### Module 4 — Async, Concurrency & Diagnostics

#### Outcomes

- Explain cancellation, backpressure and shared-state hazards.
- Measure and diagnose performance without relying on language stereotypes.

- Implement observable asynchronous workflows without unbounded resource consumption.

#### Lessons

1. **Async execution and bounded work** — `lesson`
2. **Thread safety, tracing and benchmarking** — `lesson`
3. **Tokio-style async concepts and executors** — `lesson`
4. **Cancellation, bounded work and backpressure** — `lesson`
5. **Synchronization, shared state and tracing** — `lesson`
6. **Diagnosing concurrency failures** — `test`
7. **Reproduce a concurrency defect** — `lab`

### Module 5 — Advanced TypeScript Architecture

#### Outcomes

- Publish a predictable TypeScript package with coherent runtime and type contracts.
- Control module boundaries and version changes without depending on unsafe type assertions.

#### Lessons

1. **Type-level modeling and inference boundaries** — `lesson`
2. **Module resolution, ESM and package exports** — `lesson`
3. **Build and bundling strategies** — `lesson`
4. **Type-safe APIs with runtime validation** — `lesson`
5. **Type soundness and package compatibility** — `test`
6. **Publish and test a reusable TypeScript module** — `lab`

### Module 6 — Rust Systems Foundations for Applications

#### Outcomes

- Implement a safe bounded service component using Rust ownership and concurrency rules.
- Test parsers and state transitions against invalid and adversarial inputs.

#### Lessons

1. **Memory layout and data representation** — `lesson`
2. **Iterators, ownership-aware collections and traits** — `lesson`
3. **Error composition, tracing and panics** — `lesson`
4. **Concurrency primitives and Send/Sync** — `lesson`
5. **Testing, fuzzing and property-based verification** — `lesson`
6. **Rust memory, concurrency and error mechanisms** — `test`
7. **Build a tested Rust processing engine** — `lab`

### Module 7 — Cross-Language API Evolution & Security

#### Outcomes

- Evolve a TypeScript–Rust integration without hidden coupling.
- Choose isolation based on memory and failure consequences.

#### Lessons

1. **Contract-first schema design** — `lesson`
2. **Version negotiation and compatibility matrices** — `lesson`
3. **Boundary authentication, encoding and validation** — `lesson`
4. **FFI safety audits and process isolation** — `lesson`
5. **Data ownership, lifetimes and failure translation** — `lesson`
6. **Cross-language schema and memory safety** — `test`
7. **Break and repair a versioned TS–Rust contract** — `lab`

### Module 8 — Build, Debug, Measure & Ship

#### Outcomes

- Operate a hybrid application from reproducible build to deployment and debugging.
- Measure the language boundary cost using defensible benchmarks and trace propagation.

#### Lessons

1. **Reproducible Cargo and TypeScript build pipelines** — `lesson`
2. **Tracing and profiling across process boundaries** — `lesson`
3. **Throughput versus latency benchmarks** — `lesson`
4. **Binary distribution and artifact supply chain** — `lesson`
5. **Hybrid deployment and benchmarking claims** — `test`
6. **Release a measured cross-language feature** — `lab`

### Module 9 — TypeScript–Rust Integrated Application

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

**Expanded module assessment and lab requirements:**

- **Module 1 checkpoint and micro-lab:** Catch invalid versioned API payloads through runtime tests and preserve compile-time exhaustiveness.
- **Module 2 checkpoint and micro-lab:** Demonstrate why the compiler rejects an invalid borrow and how explicit result types prevent silent failures.
- **Module 3 checkpoint and micro-lab:** Reject malformed payloads, handle version mismatches and avoid unsound foreign memory ownership.
- **Module 4 checkpoint and micro-lab:** Reproduce and repair cancellation or concurrent-state bugs under a controlled workload.

- **Module 5 — Advanced TypeScript Architecture (Publish and test a reusable TypeScript module):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Construct a small versioned package consumed by two application configurations, including intentionally malformed runtime input.
  - Verification: Both consumers compile, malformed data fails deterministically and package export rules work in supported runtimes.
  - Evidence: Source, package metadata, build outputs, consumers and contract tests.
  - Failure analysis: Explain ESM/CJS interoperability faults, dangerous any casts and stale declaration files.
- **Module 6 — Rust Systems Foundations for Applications (Build a tested Rust processing engine):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Implement a streaming parser or queued worker with bounded memory, explicit errors and property-based tests against invalid payloads.
  - Verification: Demonstrate deterministic failure behavior and no unbounded queue growth under a reproducible workload.
  - Evidence: Cargo project, tests, profiling traces and documented invariants.
  - Failure analysis: Distinguish recoverable errors, panic boundaries, deadlocks and memory growth.
- **Module 7 — Cross-Language API Evolution & Security (Break and repair a versioned TS–Rust contract):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Evolve a field in both implementations, test old and new clients, inject invalid encoding and handle boundary failures gracefully.
  - Verification: Document compatibility and demonstrate rejection of malformed fields and correct resource cleanup.
  - Evidence: Schema, consumer matrix, integration tests and failure traces.
  - Failure analysis: Address ABI instability, encoding corruption, stale generated bindings and panics crossing an unsafe FFI boundary.
- **Module 8 — Build, Debug, Measure & Ship (Release a measured cross-language feature):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Deploy a TS frontend/service backed by a Rust component, profile one workload and compare an alternative implementation boundary.
  - Verification: Clean build succeeds, errors propagate with correlation IDs, and measurements cite workload and runtime conditions.
  - Evidence: Build scripts, provenance notes, trace data and trade-off report.
  - Failure analysis: Identify unrealistic benchmarks, build artifact mismatch and hidden platform dependencies.

**Exit assessment expectation:**

Demonstrate the subject outcomes on an unfamiliar example, show at least one negative path and retain evidence allowing another reviewer to reproduce the result. Checkpoint answers must explain mechanisms, while the final integration lab must integrate and verify the expanded topics.

**Exit demonstration:**

Demonstrate the resulting implementation, explain its key mechanisms, reproduce at least one failure and recovery and defend the chosen trade-offs with inspectable evidence.
