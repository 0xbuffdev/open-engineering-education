# SEF6 — C Programming & Machine Memory

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF3](SEF3.md), [SEF4](SEF4.md), [SEF5](SEF5.md)
**Duration:** 8 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Use C to examine the machine-level boundaries that a higher-level programming language often hides. Write and build multi-file programs, interpret C11 types and object representations, trace pointers and array bounds, manage dynamic memory, parse inputs defensively, and investigate failures with compiler warnings and diagnostics. Apply that reasoning to a small reusable library of dynamic arrays, linked lists, and hash maps. Prior [SEF4](SEF4.md) study establishes representation and operation invariants, recursion and termination reasoning, algorithmic cost assumptions, and independent expected-value models; this course transfers those methods to C object lifetime, allocation-failure and undefined-behavior boundaries without requiring a second SEF4 algorithm portfolio.

A **nonprivileged, local C11-capable toolchain**, Make, and a terminal are the reference environment. GCC or Clang on Linux is a useful starting point, but equivalent free local tooling is acceptable when all required steps can be reproduced and tool-specific differences are disclosed. Document the compiler, operating system, architecture, `CHAR_BIT`, compilation flags, and versions. Begin with warnings and debug information (for example `-std=c11 -Wall -Wextra -Wpedantic -g -O0`); use supported AddressSanitizer, UndefinedBehaviorSanitizer, debugger, or other memory-analysis tools when available, clearly recording what each tool did and did not check.

C11 does not require that plain `char` be signed, that a byte contain exactly eight bits, that all pointer addresses be stable, or that undefined behavior produce a useful diagnostic. Treat each of those distinctions as part of the engineering model. **Do not intentionally dereference an invalid pointer, overflow a signed integer, or execute other undefined operations to prove what the C standard says.** A contained teaching fixture with an available diagnostic report is sufficient to investigate such a defect; when running fault demonstrations locally, isolate the disposable process and record the limits of its tools. All substantive programming assessments require corrected, defined-behavior implementations.

The original nine-module topic sequence is retained. Seven summative assessments combine related capabilities; an integrated library may reuse previously verified implementations, fixtures and diagnostics. No universal checkpoint-and-lab pair, separate mandatory final lab, paid tool, external network, production data, privileged operation, or hidden grader is required. The eight-week workload estimate is provisional; the course remains `draft` pending independent learner and reviewer evidence.

## Learning outcomes

- **SEF6-O1:** Inspect C11 fundamental types, integer limits, character representation, and byte-level object representation while distinguishing portable language guarantees from implementation-dependent observations.
- **SEF6-O2:** Write and explain defined C expressions, conversions, branches, loops, and checked integer arithmetic without evaluating signed overflow or other undefined operations.
- **SEF6-O3:** Design separate translation units with public headers, well-defined function contracts, scope and storage duration; diagnose preprocessing, compilation, linking, and loading stages.
- **SEF6-O4:** Trace object addresses, pointer values, arrays, string terminators, argument passing, and within-array pointer arithmetic while avoiding invalid dereferences and lifetimes.
- **SEF6-O5:** Distinguish automatic, static, and allocated object lifetimes; allocate, grow, and release owned memory with checked sizes, simulated allocation failure, and failure-safe cleanup.
- **SEF6-O6:** Use structures and related C representations with explicit layout assumptions, and design a portable text-record format rather than relying on raw structure bytes.
- **SEF6-O7:** Parse bounded text and numeric input with documented length, delimiter, range, encoding, and error policies; reject malformed and truncated records without leaking resources.
- **SEF6-O8:** Build, test, and inspect a multi-file C11 program with reproducible compiler options, Make rules, warnings, and actual compiler/linker/runtime diagnostics.
- **SEF6-O9:** Investigate suspected memory and semantic defects using a debugger, compiler diagnostics, sanitizers where available, or supplied traces; document their limitations and a verified repair.
- **SEF6-O10:** Classify defined, unspecified, implementation-defined, and undefined C behavior, including signed overflow, invalid bounds, aliasing, and object-lifetime violations.
- **SEF6-O11:** Implement a length-bounded binary parser accepting an explicit pointer and byte count, validating framing and arithmetic before access or allocation.
- **SEF6-O12:** Specify and enforce API ownership, borrow, mutation, and result/error contracts, including clean output state and deterministic resource handling on failure.
- **SEF6-O13:** Implement and verify integer dynamic-array and singly linked-list interfaces with documented invariants, boundary handling, and allocation-failure behavior.
- **SEF6-O14:** Implement and verify a hash map with documented key/value ownership, collision handling, duplicate-key semantics, and resizing or a justified fixed-capacity contract.
- **SEF6-O15:** Produce independent deterministic test oracles, boundary/invalid inputs, controlled allocation faults, and source-located regression evidence for C implementations.
- **SEF6-O16:** Integrate and defend a reusable multi-file C data-structure library through reproducible build/test steps, bounded memory claims, a reviewer walkthrough, and comparison with managed-language lifetimes.

## Modules

### Module 1 — C Data & Control Flow

#### Outcomes

- SEF6-O1
- SEF6-O2
- SEF6-O10

#### Lessons

1. Course introduction: C Programming & Machine Memory
2. C types and values
3. Operators and expressions
4. C control flow
5. Binary and hexadecimal
6. Integer representation
7. Characters and text

*Optional practice:* Examine `CHAR_BIT`, the signedness of plain `char`, integer limits, and a bounded unsigned-byte dump; compare expected and observed representation without assuming a fixed byte size.

### Module 2 — Functions & Program Structure

#### Outcomes

- SEF6-O3
- SEF6-O8
- SEF6-O12

#### Lessons

1. Functions and arguments
2. Scope and storage
3. Header files and multiple source files
4. The C preprocessor

*Optional practice:* Write a three-file demonstration using a guarded header, two translation units, and a client; diagnose a seeded undefined external symbol separately from a compiler error.

### Module 3 — Addresses & Pointers

#### Outcomes

- SEF6-O4
- SEF6-O10

#### Lessons

1. Addresses
2. Pointers
3. Pointers and function arguments
4. Pointers and arrays
5. Address arithmetic
6. Strings as arrays of characters

*Optional practice:* Draw an object-reference diagram with a local integer and an array; distinguish a valid one-past pointer value from an invalid dereference.

### Module 4 — Stack, Heap & Dynamic Memory

#### Outcomes

- SEF6-O5
- SEF6-O9
- SEF6-O12
- SEF6-O15

#### Lessons

1. Address space of a process
2. Stack frames and function calls
3. Heap allocation with `malloc` and `free`
4. Lifetime errors: leaks, double free, and dangling pointers
5. Buffer overruns
6. C and Python lifetimes compared

*Optional practice:* Simulate allocation failure in a fixed-size buffer, compare unsafe direct `realloc` assignment with a failure-safe temporary pointer, and explain the recovered invariant.

### Module 5 — Structures & Input/Output

#### Outcomes

- SEF6-O6
- SEF6-O7

#### Lessons

1. Structures
2. Pointers to structures and self-referential structures
3. Unions and bit-fields
4. Formatted output and input
5. File access with the standard library

*Optional practice:* Model a small struct record and a line-based file with clear field delimiters, maximum length, and numeric parsing; reject a truncated final line.

### Module 6 — Building & Debugging C Programs

#### Outcomes

- SEF6-O3
- SEF6-O8
- SEF6-O9

#### Lessons

1. Compiling C
2. Linking
3. Executables and loading
4. Automating builds with Make
5. Debugging with GDB
6. Finding memory errors with sanitizers

*Optional practice:* Compile once with warnings and debugging symbols, inspect an intentional compile or link error, and analyze a supplied diagnostic for a contained memory defect.

### Module 7 — C Semantics & Undefined Behavior

#### Outcomes

- SEF6-O2
- SEF6-O4
- SEF6-O10

#### Lessons

1. Integer promotions, signedness and overflow
2. Arrays, pointer arithmetic and bounds
3. Object lifetime and aliasing basics
4. Undefined versus implementation-defined behavior
5. Const correctness and interfaces

*Optional practice:* Compare checked signed addition with unsafe signed-overflow reasoning; identify which aspects of a printed representation depend on the implementation.

### Module 8 — Ownership, Interfaces & Defensive Parsing

#### Outcomes

- SEF6-O7
- SEF6-O11
- SEF6-O12
- SEF6-O15

#### Lessons

1. Resource ownership and cleanup paths
2. Header contracts and separate compilation
3. Buffer lengths and binary/text representation
4. Recoverable error returns and diagnostics
5. Parser validation and testing malformed inputs

*Optional practice:* Write down the framing and ownership contract of a short byte record, then trace invalid lengths, embedded NULs, and a simulated allocation failure.

### Module 9 — C Data-Structure Library

#### Outcomes

- SEF6-O12
- SEF6-O13
- SEF6-O14
- SEF6-O15
- SEF6-O16

#### Lessons

1. Library interface and ownership policies
2. Dynamic-array growth, overflow checks, and allocation failure
3. Linked-list invariants and cleanup
4. Hash-map collisions, resizing, and duplicate-key policy
5. Deterministic test harness and diagnostic evidence
6. Clean build, README, reviewer reproduction, and C/Python lifetime comparison

*Optional practice:* Sketch header interfaces and independent test-model operations for a dynamic array, linked list, and collision-heavy hash map before building the library.

## Completion requirements

### Assessment environment and review

Use C11, a documented local compiler/Make setup, synthetic data, and a disposable project directory. Publish the relevant source revision, separate header/source files where required, exact build and test commands, input fixtures, expected and observed results, warnings and diagnostic records, and known environmental limitations. `make clean` and test commands must only touch explicitly owned build paths. A free offline source/build path is required; no sanitizer or debugger is assumed available on every implementation, and equivalent reviewable diagnostic reasoning is acceptable when a particular tool is unsupported.

For memory-owning code, specify the successful and failing postconditions for each operation: which object owns an allocation, who may mutate or free it, which output pointers are initialized, and what state remains after a failed operation. Test allocation failure by an explicit injectable allocator or deterministic test mechanism, never by trying to exhaust the user's machine. Prevent size multiplication and capacity doubling overflow before allocation. Use only valid pointer arithmetic within a documented array object; one-past pointers must not be dereferenced.

A required outcome passes only through the **published assessment criteria and inspectable evidence**, not through an unchecked code listing, a sanitizer badge, a screenshot, or a guessed machine address. Reviewers may provide unfamiliar, equivalent fixtures and request a written, recorded, live, or otherwise accessible technical defense. Substantial correctness, lifetime, safety, data-loss, and reproducibility defects block passing until corrected. Reused evidence must identify the original source revision and explain which new criteria it establishes.

### Required summative assessments

- **SEF6-AS1** (required C representations and checked arithmetic)
  - Outcomes: SEF6-O1, SEF6-O2, SEF6-O10
  - Work: Write a C11 program that prints `CHAR_BIT`, `sizeof` and limits for relevant character and integer types, reports the actual plain-`char` signedness, and inspects initialized unsigned-integer object bytes through an `unsigned char` view. Predict an unsigned maximum-plus-one result under the actual unsigned width and observe its defined wrap. Implement a checked signed-integer addition and a bounded numeric-input path using `strtol` with end-pointer and range checks. Compare these portable guarantees with implementation-defined representation details and describe an example of unspecified and undefined behavior without evaluating undefined expressions.
  - Criteria: Integer/character claims match the C11 language rules and recorded `limits.h` values, byte output reflects the actual implementation, and no assumption about eight-bit bytes or particular endianness is unqualified. `UINT_MAX + 1u` wraps as defined, whereas signed overflow is rejected **before** invalid arithmetic is evaluated. Decimal parsing distinguishes valid, empty, trailing-garbage, out-of-range and sign-boundary inputs and does not silently truncate values. The learner correctly distinguishes defined, implementation-defined, unspecified and undefined behavior.
  - Evidence: C source and build commands, compiler/OS/`CHAR_BIT` metadata, predicted-versus-observed byte and arithmetic table, input/error fixtures, controlled status outputs, and reasoning distinguishing guarantees from observations.

- **SEF6-AS2** (required multi-file program and defined pointer trace)
  - Outcomes: SEF6-O3, SEF6-O4, SEF6-O8
  - Work: Split a small integer-processing C program into a guarded public header, two implementation files and a client, build with separately compiled object files and an explicit link step, and provide a Makefile for the same build. Document call-by-value versus pointer-output behavior and any static-storage assumptions. In a separate safe tracing fixture, draw and predict the referents and values of an automatic integer, an array of at least four elements, a pointer passed to a function, and valid within-array element positions. Form a one-past pointer without dereferencing it; print object pointer values using the `void *` convention for `%p` and use `ptrdiff_t` only for pointers within the same array. Deliberately introduce and diagnose one header declaration or link-stage fault in a copied fixture, then repair it.
  - Criteria: The clean build compiles/link-runs all translation units with warning and C11 flags, and outputs match the documented original behavior. The learner identifies which errors arise during preprocessing/compilation/linking and describes what loading does without assuming a particular executable binary format. Pointer predictions, in-array differences and caller-visible changes are correct; absolute addresses are not assumed repeatable. Header declarations do not create duplicate externally linked definitions. A diagnostic failure and corrected build are reproducible.
  - Evidence: Source/header/Makefile, individual compile and link transcripts, original-versus-revised output fixtures, pointer/object diagram and observed trace, recorded failing build and repair, and toolchain/environment notes.

- **SEF6-AS3** (required object lifetime and failure-safe dynamic memory)
  - Outcomes: SEF6-O4, SEF6-O5, SEF6-O9, SEF6-O12, SEF6-O15
  - Work: Implement a heap-backed integer buffer with clear `size`, `capacity`, pointer and owner contracts, supporting initialization, append/growth, read and disposal. Include explicit pre-allocation guards for `capacity * sizeof(element)` and doubling overflow, and define a deterministic policy for requested zero capacity. Use an injectable allocator to cause failures of positive-size `malloc` and `realloc`; demonstrate safe temporary-pointer handling and preserved original data/ownership when growth fails. Diagnose a supplied leak/double-free/overrun trace or a contained tool-supported fault fixture; correct an actual seeded cleanup or growth defect without requiring execution of uncontrolled undefined behavior. Compare automatic, static and allocated lifetime to relevant SEF2/Python object lifetimes.
  - Criteria: Invariants hold for empty, one-element, growth and repeated disposal cases; all successful allocations have a single documented release responsibility. Failed allocation cannot lose the original allocation, corrupt the existing logical buffer, or leave an ambiguous output state. Arithmetic checks happen before multiplication or doubling, and no use-after-free or invalid pointer access is required to demonstrate understanding. Diagnostic claims are bounded by the tool paths actually exercised; no clean sanitizer run is presented as proof of total memory safety.
  - Evidence: Buffer source and owner/interface contract, seeded allocator-failure and state-preservation tests, before/after invariant checks and bytes where relevant, supplied or observed diagnostic with fault reasoning and repair, and a C/Python lifetime comparison.

- **SEF6-AS4** (required portable text and bounded binary parsing)
  - Outcomes: SEF6-O6, SEF6-O7, SEF6-O11, SEF6-O12, SEF6-O15
  - Work: Define a line-delimited text-record schema with an integer ID, bounded name, explicit delimiter, and maximum line length. Read and validate lines without accepting a truncated `fgets` fragment as a complete record; check numeric conversion and duplicate IDs, including an optional final line without newline. Encode records by documented field rules, not by writing raw structure bytes. Then implement a separate framed binary parser accepting `(const unsigned char *data, size_t length)`, with a fixed, documented byte-count format (not assuming eight-bit bytes for cross-platform interoperability), bounded advertised payload size, and explicit trailing-byte policy. Check header and remaining length before every access, preclude length arithmetic overflow, and document who owns any resulting allocation. Test empty, truncated, oversized, embedded-NUL, exact-boundary and injected allocation-failure cases.
  - Criteria: Valid text and framed inputs round-trip or parse as specified with a deterministic output schema. Malformed, duplicate, partial and oversized inputs return an explicit error without out-of-bounds reads, partial published records, memory leaks or undefined string traversal. Explicit-length parsing never relies on `strlen` over an untrusted buffer; ownership/output state is defined on success and failure. The learner explains why C struct padding, unions/bit-fields, endianness and raw `fwrite` structures are unsuitable as an undocumented portable interchange format.
  - Evidence: Schema examples, source and ownership contracts, hand-derived valid/error fixtures, exact-length test arrays, error statuses, independent expected-value comparisons, allocation-failure and cleanup records, and a concise serialization/portability rationale.

- **SEF6-AS5** (required diagnostic and C11 semantics investigation)
  - Outcomes: SEF6-O2, SEF6-O8, SEF6-O9, SEF6-O10, SEF6-O15
  - Work: Prepare a small warnings-enabled multi-file C project and separately inspect one compile-time error, one unresolved-link error and one runtime-memory diagnostic from an isolated teaching fixture or supplied trace. Reproduce a safe bound-check or checked-addition defect using a **defined** failing assertion or precondition, then repair it and retain a regression test. When locally supported, use a debugger backtrace and ASan/UBSan/LeakSanitizer on disposable inputs, recording exact options and what was exercised. Otherwise analyze a provided diagnostic and demonstrate the repaired program with standard tests and warnings. Classify the original potential defect under the C11 semantics categories and distinguish a compiler warning, sanitizer observation, crash, and language-level correctness argument.
  - Criteria: Each failure is assigned to the correct tool/build phase and traced to a specific source-level cause. Corrected code avoids the invalid operation rather than merely hiding its diagnostic; boundary and normal tests pass. The learner does not infer that undefined behavior must crash, that all memory errors are detected, or that the absence of sanitizer findings proves the absence of defects. Reported tools actually ran, or their unavailability and evidence substitution are stated. No production system, privileged operation or unrelated process is affected.
  - Evidence: Minimal source fixtures, build-phase and test transcripts, diagnostic/backtrace or supplied report with line/context mapping, supported tool flags and versions, repaired regression, and an explicit discussion of defined versus invalid operations.

- **SEF6-AS6** (required owned dynamic array, linked list and hash map)
  - Outcomes: SEF6-O5, SEF6-O12, SEF6-O13, SEF6-O14, SEF6-O15
  - Work: Implement a C11 library with separate interfaces for an integer dynamic array, singly linked list, and hash map. Define initialization, insertion, retrieval, removal and destruction, including invalid pointers, empty containers, duplicate keys, caller-owned versus copied values, and observable status values. State dynamic-array capacity and link invariants, pre-check growth and allocation arithmetic, and document the hash map's collision and resizing or fixed-capacity policy. Use a deterministic allocation wrapper and independent small reference models to test failure injection, growth, collisions, duplicate insertion, deletion, empty/singleton behavior and repeated lifecycle operations. Show at least one deliberately broken owner or collision scenario in a contained test model and its corrected regression.
  - Criteria: Each interface and ownership rule is internally consistent; normal and boundary sequences match independent models; collisions do not silently drop a key; duplicates follow the documented replacement/rejection policy; all valid elements remain reachable across growth and removal. A failed allocation preserves the declared previous valid state and leaves exactly one owner for each acquired resource. Cleanup and repeated initialization/destruction respect the documented preconditions. All tests are reproducible using free tooling, and any observed sanitizer results are attributed to the actual tested paths only.
  - Evidence: Public headers, implementation files, invariant and ownership tables, deterministic operation/fault fixtures, independent oracle comparisons, error/cleanup logs, a repaired defect, and recorded compile/test/diagnostic commands.

- **SEF6-AS7** (required integrated C library and technical defense)
  - Outcomes: SEF6-O3, SEF6-O6, SEF6-O8, SEF6-O9, SEF6-O12, SEF6-O13, SEF6-O14, SEF6-O15, SEF6-O16
  - Work: Combine the previously assessed dynamic-array, linked-list, and hash-map implementations into a cleanly built library with headers, separate C source files, a Makefile exposing documented build/test/clean targets, and a small client that exercises at least two structures together on synthetic records. Reuse validated source and test artifacts from SEF6-AS1–AS6; no second independent copy is required. Create a clean-checkout test harness covering routine use, zero/one/growth boundaries, real collisions, malformed inputs and deterministically injected allocation errors. Have an independent reviewer follow the README, build and run both a normal and failure path, and inspect an outcome-to-evidence matrix. Provide a reasoned comparison of C ownership, aliasing and manual lifetimes with the relevant Python abstraction and defend one changed design decision and its failure/recovery evidence.
  - Criteria: A fresh reviewer checkout builds and executes the documented operations without hidden dependencies or warnings that violate the stated acceptance policy. The client preserves independently specified results, module boundaries and ownership invariants; failed operations do not silently corrupt data, discard unrelated resources, or claim success. Required diagnostic tools are used if supported or their absence is truthfully documented with bounded alternative evidence. The outcome map accounts for the library's APIs, tests and failure behavior. The defense explains the C type/lifetime/ownership trade-offs and their consequences without claiming verified readiness or universal absence of memory defects.
  - Evidence: Source revision and portable repository, README and tool/version requirements, reproducible build/test commands, public API and error/ownership documentation, representative client fixtures and expected/actual outputs, normal and injected-failure test logs, supported memory diagnostic results or labeled alternatives, independent reviewer reproduction notes, outcome-to-evidence map, and an accessible technical defense.

### Completion decision

All **seven required assessments** must pass their published criteria and collectively demonstrate SEF6-O1 through SEF6-O16. Earlier assessed code, diagnostics and test fixtures can be reused and improved in the integrated library; a learner need not repeat an identical lab in every module or implement three independent libraries. The nine learning modules and optional practices are preparation, not hidden summative gates.

Reviewers record the decisions and enough inspectable evidence to justify each demonstrated capability. Uncorrected bounds, ownership, arithmetic, parsing, compilation or reproducibility failures block the relevant assessment. A student who cannot access a particular debugger or sanitizer must provide truthful, reviewable substitute diagnostics and run the applicable independent tests; unavailable tooling is not proof of a clean report. The course remains `draft` until the separate learner and reviewer evidence requirements in [Status Labels](../../spec/status-labels.md) are satisfied.
