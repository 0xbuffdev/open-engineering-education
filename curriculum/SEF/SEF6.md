# SEF6 — C Programming & Machine Memory

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF3](SEF3.md), [SEF4](SEF4.md), [SEF5](SEF5.md)
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Use C to examine the machine-level boundaries that a higher-level programming language often hides. Write and build multi-file programs, interpret C11 types and object representations, trace pointers and array bounds, manage dynamic memory, parse inputs defensively, and investigate failures with compiler warnings and diagnostics. Apply that reasoning to a small reusable library of dynamic arrays, linked lists, and hash maps. Prior [SEF4](SEF4.md) study establishes representation and operation invariants, recursion and termination reasoning, algorithmic cost assumptions, and independent expected-value models; this course transfers those methods to C object lifetime, allocation-failure and undefined-behavior boundaries without requiring a second SEF4 algorithm portfolio.

A **nonprivileged, local C11-capable toolchain**, Make, and a terminal are the reference environment. GCC or Clang on Linux is a useful starting point, but equivalent free local tooling is acceptable when all required steps can be reproduced and tool-specific differences are disclosed. Document the compiler, operating system, architecture, `CHAR_BIT`, compilation flags, and versions. Begin with warnings and debug information (for example `-std=c11 -Wall -Wextra -Wpedantic -g -O0`); use supported AddressSanitizer, UndefinedBehaviorSanitizer, debugger, or other memory-analysis tools when available, clearly recording what each tool did and did not check.

C11 does not require that plain `char` be signed, that a byte contain exactly eight bits, that all pointer addresses be stable, or that undefined behavior produce a useful diagnostic. Treat each of those distinctions as part of the engineering model. **Do not intentionally dereference an invalid pointer, overflow a signed integer, or execute other undefined operations to prove what the C standard says.** A contained teaching fixture with an available diagnostic report is sufficient to investigate such a defect; when running fault demonstrations locally, isolate the disposable process and record the limits of its tools. All substantive programming assessments require corrected, defined-behavior implementations.

The same core C11 subject areas are now arranged into **thirteen instructional modules**, moving toolchain diagnostics and language-level semantics before extensive memory ownership and separating dynamic arrays, linked lists, hash maps and integrated-library work. The **same seven required summative assessments** combine the existing capabilities; each module is not an extra assessed assignment. Buffer, parsing and data-structure implementations, fault-injection fixtures and review evidence may be reused, rather than rebuilt for every assessment. There is no universal checkpoint/lab quota, separate mandatory final lab, paid tool, external network, production data, privileged operation or hidden grader.

**Planning estimate:** 14–18 weeks at approximately 10–15 focused hours per week, approximately 140–270 focused hours before individual remediation or reassessment. This is a provisional instructional allocation, **not** an empirically validated duration or a mastery claim: reading C source, tracing pointer/lifetime invariants, handling allocation failures, practicing diagnostic interpretation and building a reusable three-structure library justify a substantially larger range than the old eight weeks. Learners may need additional time; assessment criteria, not elapsed weeks, decide mastery. The course remains `draft` pending real learner and reviewer evidence.

**C11 versus POSIX boundaries:** ISO C11 library headers and facilities are the required baseline. `getline`, `strdup`, POSIX `read`/`write`, platform-specific memory maps and `strace` are not ISO C11 requirements. Such tools may be discussed or used optionally with transparent provenance, but are **not required** to pass. Later [SEF7](SEF7.md) owns the deeper POSIX file-descriptor and process interfaces. Compiler warnings, debugger reports and sanitizer observations are evidence about the inspected configuration, not automatic proof that a program has defined behavior.

For optional public technical reference, use the [WG14 C11 working-draft information](https://open-std.org/jtc1/sc22/wg14/www/standards), [SEI CERT C coding rules](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/) and [GCC instrumentation documentation](https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html). These are supplementary cross-checks rather than paid, proprietary or hidden completion requirements.

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

### Module 1 — C Programs, Types and Control Flow

#### Outcomes

- SEF6-O1
- SEF6-O2
- SEF6-O8
- SEF6-O10

#### Lessons

1. **Course purpose and C11 scope** — Connect prior SEF2 Python programs and SEF4 invariants to explicit C representations and manually managed resources; distinguish learning C11 from using POSIX extensions.
2. **The smallest compiled program** — Read headers, a main function, return status, declarations, statements and a reproducible compile/run command using a C11-capable compiler.
3. **Variables, expressions and initialization** — Distinguish declaration, definition, initialization, assignment, automatic storage and an indeterminate uninitialized value.
4. **Fundamental scalar types** — Inspect integer, floating, character and _Bool types, the sizeof operator, alignment needs and when actual properties depend on the implementation.
5. **Control and boolean conditions** — Predict if/else, switch, for, while, do/while, break and continue under stated loop invariants and termination assumptions.
6. **Integer and character literals** — Interpret decimal, octal, hexadecimal, integer suffixes, escapes, character encodings and correct printf format types.
7. **Arrays versus scalars** — Declare fixed arrays and bound loops before introducing pointer arithmetic; prevent invalid indexing even in demonstration code.
8. **Standard input/output basics** — Use printf, puts, getchar or fgets in small supported cases, checking return status and distinguishing a failed read from valid input.
9. **Compile warnings and diagnostic claims** — Enable language-standard and warning flags; categorize a diagnostic versus a C language guarantee.
10. **Portability baseline** — Record compiler, standard mode, platform, CHAR_BIT, limits and the effects of assuming an eight-bit C byte.
11. **First defined-behavior repair** — Identify a harmless assertion failure caused by a missing bounds precondition and correct the program without intentionally executing UB.

*Optional practice:* Build a disposable small program that prints its environment and type sizes, rejects an invalid index and records exact compile/run commands.

### Module 2 — Object Representation, Integer Conversions and Checked Arithmetic

#### Outcomes

- SEF6-O1
- SEF6-O2
- SEF6-O10
- SEF6-O15

#### Lessons

1. **Bits, bytes and storage units** — Explain that sizeof(char) is one C byte, CHAR_BIT gives its bit width, and an octet is an explicitly eight-bit protocol unit, not automatically a C byte.
2. **Signed and unsigned ranges** — Read limits.h and test the actual plain-char signedness without assuming two's complement or that char has a fixed signedness.
3. **Integer promotions and usual conversions** — Predict types and values after promotions, comparisons between signed and unsigned operands, integer division and explicit casts.
4. **Unsigned modular arithmetic** — Derive the modulus from actual type width; distinguish mathematically defined unsigned wrap from a safe policy for size calculations.
5. **Signed overflow and boundary arithmetic** — Reject overflow before evaluating an addition or multiplication; do not run invalid signed arithmetic to observe a supposedly reliable result.
6. **Shift, divide and conversion constraints** — Check nonzero denominators, shift counts and signed shift preconditions; state which out-of-range integer conversions are implementation-defined.
7. **Byte-wise object inspection** — Explain why unsigned char may inspect object representation and why padding bytes or raw struct bytes are not a portable serialization format.
8. **Format and variadic function contracts** — Use matching printf conversions including %zu and %td, and convert object pointers to void * for %p; distinguish format mismatch UB from unusual output.
9. **Numeric text conversion** — Use strtol, end pointers, errno and range checks to reject empty, trailing, too-large or disallowed signed input; declare whitespace policy explicitly.
10. **Character classification** — Pass EOF or values representable as unsigned char to ctype character functions; avoid feeding negative plain-char values directly.
11. **Independent arithmetic oracle** — Compare a few explicit hand-derived input classes and a separately reasoned range-check model with corrected C output, not a copied expression.

*Optional practice:* Predict a boundary addition, a mixed signed/unsigned comparison and a strtol failure before running safe C11 checks.

### Module 3 — Functions, Interfaces and Translation Units

#### Outcomes

- SEF6-O3
- SEF6-O8
- SEF6-O12

#### Lessons

1. **Function declarations and definitions** — Specify return and parameter types, prototypes, argument evaluation and call-by-value behavior.
2. **Scope, linkage and storage duration** — Separate automatic, static, block, file and external symbols, including object lifetime and visibility.
3. **The header contract** — Write include guards, consistent prototypes and public data-type declarations while leaving private implementation decisions in source files.
4. **Separate C translation units** — Use one interface header, two implementation units and a client; avoid multiple external definitions and mismatched declarations.
5. **Preprocessing versus compilation** — Explain macro expansion, header inclusion, preprocessing diagnostics and proper single-evaluation choices.
6. **Object files, linking and loading** — Interpret an unresolved symbol separately from a syntax/type error, and describe implementation-dependent executable/loading steps.
7. **Make dependency graphs** — Write bounded build, test and clean targets with correct source/header dependencies and no command that deletes outside the project.
8. **Function result and output contracts** — Distinguish return status from output pointers, specify initialized outputs on success and failure and how callers retain ownership.
9. **Static storage versus allocation ownership** — Explain why storage duration differs from what an API may borrow, return or mutate.
10. **Build regression on an unfamiliar change** — Predict a header change's dependency impact, seed a non-UB compile/link error and verify a repaired clean build.

*Optional practice:* Prepare a multi-file local fixture with one deliberate missing-symbol error, preserve the failing diagnostic and repair it.

### Module 4 — Compiler Diagnostics, Debugging and Defined Test Fixtures

#### Outcomes

- SEF6-O8
- SEF6-O9
- SEF6-O10
- SEF6-O15

#### Lessons

1. **Toolchain contract and reproducible builds** — Record C11 mode, warnings, debug symbols, optimization flags, supported architectures and compiler versions.
2. **Build-stage troubleshooting** — Distinguish preprocessing, compile-time, linking and run-time failures from the evidence each tool can supply.
3. **Asserted preconditions and safe failure** — Introduce a deliberately incorrect but defined result or rejected input to obtain a reproducible failure without executing undefined operations.
4. **Debugger basics** — Inspect supported breakpoints, step-over/into, locals and stack traces using a controlled failing assertion or trace.
5. **Warnings are not semantic proof** — Explain why warning-free code can still be incorrect and an unrecognized extension or compiler warning does not establish a standard guarantee.
6. **Sanitizer coverage and caveats** — Explain AddressSanitizer, UndefinedBehaviorSanitizer and leak diagnostics where available, their runtime dependencies and unexercised-path limitations.
7. **Analyzing supplied unsafe traces** — Use an instructor-provided crash or sanitizer transcript to locate potential invalid lifetime, bounds or arithmetic without reproducing uncontrolled UB.
8. **Diagnosis and repair log** — Document hypotheses, exact tool configuration, observed evidence, suspected line, bounded repair and a reliable regression check.
9. **Portability of investigation** — Use a free source-level review and deterministic tests when no optional debugger or sanitizer works on the learner's toolchain.

*Optional practice:* Reproduce a harmless failing assertion and a missing-link-symbol error, then explain why neither demonstrates absence of memory defects.

### Module 5 — Pointers, Arrays, Strings and Object Bounds

#### Outcomes

- SEF6-O4
- SEF6-O10
- SEF6-O12

#### Lessons

1. **Addresses and pointer values** — Relate object identity and lifetime to & and *, null pointers and correctly typed pointer declarations.
2. **Pointer arguments and mutation** — Trace what a pointer parameter can modify versus a passed scalar value, and specify whether a referent is borrowed or owned.
3. **Array indexing and decay** — Distinguish an array object from a pointer parameter, and show when sizeof an array is not sizeof a pointer.
4. **Valid pointer arithmetic** — Work within one actual array object, explain one-past formation without dereference, and compare/difference only permitted related pointers.
5. **Pointer provenance and lifetime** — Explain why a pointer becomes unusable after referent lifetime ends even if a numerical address still looks familiar.
6. **Const-qualified contracts** — Distinguish a pointer to const data from a const pointer and explain promises/limitations without mistaking const for universal memory safety.
7. **C strings and terminators** — Use character arrays, bounds, strlen and standard string routines only after establishing valid NUL termination and sufficient storage.
8. **Safe copies and formatting** — Compare explicit-length copying with bounded snprintf and interpret truncation/error status rather than assuming strncpy always gives a string.
9. **Memory overlap and byte views** — Distinguish memcpy and memmove preconditions and explain unsigned-char object representation access.
10. **Null, empty and one-element cases** — Define each pointer/length combination and avoid treating null plus zero length as automatically valid for every library call.
11. **Pointer diagrams and proof of access** — Document expected element indices, ownership and termination on a new four-element array without relying on stable printed addresses.

*Optional practice:* Predict the pointer and object values before and after a supported in-array update; create a one-past pointer without dereferencing it.

### Module 6 — Defined, Unspecified, Implementation-Defined and Undefined C Behavior

#### Outcomes

- SEF6-O2
- SEF6-O4
- SEF6-O9
- SEF6-O10

#### Lessons

1. **Four categories of C semantics** — Distinguish defined, implementation-defined, unspecified and undefined behavior using documented concrete examples.
2. **Evaluation order and side effects** — Explain unsequenced updates and why source reading order is not an evaluation-order guarantee.
3. **Integer traps and conversions** — Review signed overflow, shifts, divisions, usual arithmetic conversions and implementation-defined narrowing.
4. **Object initialization and representation** — Distinguish uninitialized reads, padding, signed representations and safe unsigned-char inspection.
5. **Pointer bounds and lifetime** — Diagnose out-of-bounds access, misaligned conversions, freed objects and comparisons outside allowed array relationships.
6. **Aliasing and effective type** — Explain incompatible lvalue accesses and why a permitted character-byte inspection does not authorize arbitrary type punning.
7. **Strings, variadic calls and formats** — Spot unterminated-string traversal, mismatched printf conversions and dangerous assumptions about pointer formatting.
8. **Memory diagnostics versus language reasoning** — Explain why an absence of crashes or sanitizer warnings on a finite run cannot prove defined C behavior.
9. **Portable versus platform-specific features** — Identify GNU/POSIX additions or compiler extensions as such, with C11 alternatives where the assessed work permits them.
10. **Source review of an unsafe fixture** — Use a supplied trace and precise source rule to diagnose a potential violation without intentionally invoking invalid operations.
11. **Corrected contract case** — Replace a flawed expression or bounds check with a defined implementation and verify normal, boundary and failure behavior.

*Optional practice:* Classify examples of signed wrap, unsigned wrap, one-past formation, out-of-range dereference and unsequenced side effects before reviewing safe corrections.

### Module 7 — Storage Duration, Allocation, Reallocation and Cleanup

#### Outcomes

- SEF6-O4
- SEF6-O5
- SEF6-O9
- SEF6-O12
- SEF6-O15

#### Lessons

1. **Automatic and static object lifetimes** — Compare stack-like automatic storage, static duration and dynamically allocated objects without equating physical memory segments with language guarantees.
2. **Heap allocation and ownership** — Use malloc and free, checked allocation size and single-owner responsibility; distinguish a pointer value from the allocation's lifetime.
3. **Zero-size allocation policy** — Declare a deterministic application policy for zero requested elements rather than depending on differing malloc(0) or realloc(p,0) results.
4. **Size arithmetic before evaluation** — Check size_t multiplication, addition and capacity doubling before computing a byte count or calling allocation routines.
5. **Growth and realloc failure** — Use a temporary return pointer and preserve the original allocation and data when a positive-size realloc fails; discard all old aliases after successful reallocation.
6. **Borrowed pointers and alias invalidation** — Explain which clients may retain an element pointer and how append/growth or delete can invalidate it even when numerical addresses appear unchanged.
7. **Allocation-failure injection** — Wrap or inject an allocator with deterministic failure on a chosen positive-size request rather than exhausting real memory.
8. **Error-state postconditions** — Specify initialized outputs, valid size/capacity, no leaked ownership and deterministic return statuses after each failing operation.
9. **Single-exit or structured cleanup** — Choose clear resource-release paths, avoid double-free, and make repeated destruction behavior explicit under its documented preconditions.
10. **Comparing C and Python lifetimes** — Trace referent ownership, identity and garbage collection versus explicit free without equating Python names with raw C pointers.
11. **Buffer failure regression** — Verify empty/one/growth cases, failed realloc state, invalid operation policy and independently derived integer sequences.

*Optional practice:* Adapt the SEF4 dynamic-array model into a C buffer, then inject one failed expansion and show preserved prior contents and owner state.

### Module 8 — Structures, Layout and C Standard-Library I/O

#### Outcomes

- SEF6-O6
- SEF6-O7
- SEF6-O10
- SEF6-O12

#### Lessons

1. **Structures and member lifetime** — Declare struct fields, member access, nested ownership, padding and alignment without assuming in-memory bytes form a portable record.
2. **Pointers to structures** — Use -> correctly, explain self-referential node records and show why list nodes need a clear allocation and free policy.
3. **Unions, bit-fields and layout** — Discuss valid representation assumptions and implementation dependence without suggesting arbitrary union reinterpreting is portable.
4. **Standard streams and status** — Use FILE *, fopen, fclose, fgets, fputs and fread/fwrite only with checked results; distinguish EOF from an I/O error via feof/ferror.
5. **Line boundaries with fgets** — Detect overflow or truncation, handle final lines without newline and choose a clear maximum permitted record length.
6. **Numeric fields** — Use strtol with errno, end pointer, sign/range checks, and an explicit delimiter/whitespace rule.
7. **Text encodings and characters** — Declare encoding and NUL/line-ending policies, avoid silent locale assumptions and keep text parsing separate from raw bytes.
8. **Serialization as an external contract** — Specify fields, delimiters, maximum lengths and error behavior; reject raw fwrite(struct) as a portable interchange format.
9. **Resource cleanup on I/O failure** — Check full reads/writes, close streams and avoid partially publishing a record after malformed input.
10. **Independent schema fixtures** — Hand-derive expected valid, truncated, duplicate and malformed cases rather than copying a parser's own output.

*Optional practice:* Read synthetic short lines and distinguish a complete final record from a truncated fgets fragment without writing outside the fixture tree.

### Module 9 — Resource Ownership and Public C API Contracts

#### Outcomes

- SEF6-O5
- SEF6-O11
- SEF6-O12
- SEF6-O15

#### Lessons

1. **Contract vocabulary** — Define ownership, borrowing, aliasing, mutation authority, lifetime and initialized output expectations.
2. **Initial and final states** — Distinguish uninitialized, valid-empty, valid-populated and destroyed objects; say which operations accept which states.
3. **Header-level function contracts** — Document input/output pointers, lengths, return/error statuses and all failure postconditions in a client-visible header.
4. **Single and borrowed owners** — Specify ownership transfer, copy versus borrow, who frees a returned value and when a borrowed view becomes invalid.
5. **Capacity and buffer contracts** — Model size <= capacity, positive growth, checked multiplication and either preserve-on-failure or an explicitly documented alternative.
6. **Opaque versus exposed representation** — Compare a public struct layout with an opaque handle, acknowledging different static-allocation and ABI trade-offs.
7. **Cleanup on partial initialization** — Track acquired allocations and files in reverse order, and ensure an error leaves the object in a documented usable or destroyable state.
8. **Error propagation** — Return distinguishable invalid-input, out-of-memory and not-found statuses rather than swallowing errors or guessing errno from unrelated calls.
9. **Dependency-injected allocators** — Separate real malloc/realloc/free from a narrowly scoped failure simulator without hiding production allocator behavior.
10. **Ownership review with client code** — Review an unfamiliar caller that inserts, retrieves and deletes an element, and identify stale borrows or double-free paths.
11. **Contract test design** — Combine independently modeled state transitions, fault injection and negative cases with a real compiled client.

*Optional practice:* Draft a compact ownership/borrow/error table for a generic container API and trace the client-visible result of a failed append.

### Module 10 — Bounded Text and Binary Parsers

#### Outcomes

- SEF6-O6
- SEF6-O7
- SEF6-O11
- SEF6-O12
- SEF6-O15

#### Lessons

1. **Input is untrusted and bounded** — Publish an explicit schema, encoding or byte model, maximum supported record and incomplete/trailing-data policies.
2. **Text records and fgets** — Detect newline and overlong fragments, distinguish clean EOF from input error, and allow/reject a final unterminated line by policy.
3. **Numeric fields and duplicates** — Use validated strtol conversions, check duplicate IDs and distinguish malformed records from legitimately empty data.
4. **Output state on parse failure** — Keep produced records either fully valid and owned or entirely rolled back, without partially published state or leaked resources.
5. **Binary framing independent of host structs** — Define explicit field lengths and byte order rather than memcpy-ing C struct padding or relying on native endianness.
6. **C bytes versus octets** — Explain that an octet-specific external format requires eight-bit units; for a portable C11 teaching fixture, define framing in C unsigned-char units and document the compatibility limit.
7. **Pointer and remaining-length discipline** — Check remaining length before access, subtract only under established bounds, and preclude size_t overflow in advertised payload arithmetic.
8. **Embedded NUL and string functions** — Use explicit buffer lengths on arbitrary binary data and never call strlen on untrusted nonterminated bytes.
9. **Oversized and trailing data** — Reject or document missing headers, invalid lengths, exact-boundary payloads, oversized frames and trailing bytes.
10. **Allocation failures and cleanup** — Inject allocation failure in parsed-record construction and verify status, ownership and preserved previous output.
11. **Independent parser oracles** — Hand-encode byte arrays and error cases; verify round trips separately without letting encoder and decoder mutually validate the same wrong format.

*Optional practice:* Design an explicit-length framed message on disposable unsigned-char arrays and hand-check both a correct and truncated input before reading it in C.

### Module 11 — Owned Integer Dynamic Arrays and Linked Lists

#### Outcomes

- SEF6-O5
- SEF6-O12
- SEF6-O13
- SEF6-O15

#### Lessons

1. **Reuse the earlier buffer** — Adapt the already-assessed SEF6-AS3 heap-backed buffer into the integer vector in SEF6-AS6; do not build another unrelated array solely to satisfy module structure.
2. **Vector representation invariant** — Enforce zero <= size <= capacity and a valid allocation/empty-state policy before and after append, read and delete.
3. **Vector growth and fault handling** — Guard addition, multiplication and doubling, inject malloc/realloc failures and preserve the documented state.
4. **Indexing and pointer invalidation** — Document index boundaries and how reallocation affects clients holding addresses into storage.
5. **Singly linked-list node model** — Define next pointers, head/tail, count, empty and one-element policies and consistent node ownership.
6. **List insert and remove** — Trace head/middle/tail insertions, deletion and pointer rewiring without orphaning or double-freeing nodes.
7. **List failure atomicity** — Inject a failed node allocation and show previous links, counts and ownership remain valid.
8. **Lifecycle and cleanup** — Define initialization/destroy/repeated-use preconditions; release every owned node once with a bounded loop.
9. **API equivalence and limits** — Compare vector indexing, list traversal and insertion complexity under actual representation assumptions from SEF4.
10. **Independent state-model oracles** — Compare seeded operation traces with a separate small reference model and deliberately corrupt a link/count check in a contained test.
11. **Reusable C test harness** — Keep allocation stub, fixture reset, check macros and error outputs inspectable without a proprietary unit-test framework.

*Optional practice:* Implement a linked-list deletion after a failed node allocation and compare the preserved node chain against an independently drawn expected list.

### Module 12 — Hash Maps, Collisions and Adversarial Allocation Tests

#### Outcomes

- SEF6-O5
- SEF6-O12
- SEF6-O14
- SEF6-O15

#### Lessons

1. **Hash-map contract** — Choose key/value representation and copy-or-borrow semantics, define duplicate-key, not-found and deletion behavior.
2. **Hashing and comparison** — Specify the hash domain, equality function and dependence on encoding or length; avoid conflating identical hash with identical keys.
3. **Bucket representation** — Choose separate chaining or open addressing and explain allocation ownership, tombstones or chain traversal as appropriate.
4. **Collision-heavy fixtures** — Use deliberately colliding keys, distinguish collision from duplicate and independently verify all still-reachable entries.
5. **Load factor and resize policy** — Specify threshold and resizing or a justified bounded fixed capacity; guard byte counts and rehash failure behavior.
6. **Insert, update and remove** — Maintain key/value ownership and state invariants through duplicate, replacement, deletion and empty/one-element transitions.
7. **No partial commit on failed growth** — Inject a failure during entry creation or rehash, then prove previous data remain valid and retrievable under the declared policy.
8. **Reference models and metamorphic checks** — Compare a small separate map model, insertion-order-independent lookup and repeated retrieval after collision/deletion.
9. **Cross-container failure semantics** — Check that vector, list and map return compatible documented status values without making their internal policies falsely identical.
10. **Algorithmic cost** — Explain average expected behavior only with actual hash/distribution assumptions and worst-case collision paths without relying on timing alone.
11. **Unfamiliar reviewer challenge** — Predict an adversarial duplicate/collision/failure sequence and record a source-located repair.

*Optional practice:* Hand-design a key set with collisions, then reason about a failed resize before exercising the tested implementation.

### Module 13 — Integrated C11 Data-Structure Library and Engineering Defense

#### Outcomes

- SEF6-O3
- SEF6-O6
- SEF6-O8
- SEF6-O9
- SEF6-O12
- SEF6-O13
- SEF6-O14
- SEF6-O15
- SEF6-O16

#### Lessons

1. **Library boundaries and public headers** — Organize previously assessed vector, linked-list and hash-map sources and verify matching declarations and ownership contracts.
2. **No duplicate implementations** — Reuse and refine the SEF6-AS3, AS4 and AS6 components, fixtures and evidence in one library, rather than rebuilding separate grading projects.
3. **Build and test from a clean tree** — Document compiler mode, warning policy, Make targets, include paths, generated outputs and a clean rule bounded to owned directories.
4. **Cross-structure client** — Create a small synthetic-data client using at least two structures with explicit normal, boundary and error contracts.
5. **Independent acceptance oracles** — Include hand-derived expectations, seeded model tests and compiler/test logs for actual public APIs, not merely a passing mock.
6. **Failure matrix** — Exercise empty/one/growth, duplicate keys, collisions, malformed records, invalid pointers under documented preconditions and injected allocation failures.
7. **Diagnostics and portability** — Record supported warnings/sanitizer/debugger results or honestly labeled supplied traces, including what was not exercised.
8. **C/Python ownership comparison** — Explain manual lifetimes, realloc invalidation, aliasing and cleanup versus Python-managed object references, without implying Python cannot have logical aliasing defects.
9. **Reviewer clean-room reproduction** — Ask an independent reviewer to build and run normal/failure scenarios, inspect one ownership contract and request an unfamiliar input variant.
10. **Design defense and release limits** — Present a capability-to-evidence map, one corrected defect, changed design trade-off, compiler/architecture assumptions and remaining risks.

*Optional practice:* Prepare a reviewer checklist and reuse the same library across all seven assessments, recording why warning-free and sanitizer-clean runs alone are insufficient.

## Completion requirements

### Teaching sequence and existing assessment alignment

The table below clarifies **where the original seven assessments draw their taught capabilities**. It is not a new grading contract or an instruction to submit thirteen separate labs. The assessment Work, Criteria and Evidence sections below remain authoritative and unchanged.

| Existing assessment | Primary teaching stages | Existing inspectable mastery |
| --- | --- | --- |
| `SEF6-AS1` | Modules 1–2 and 6 | C11 representations, integer conversions, checked arithmetic, implementation-dependent assumptions, and safe numeric parsing |
| `SEF6-AS2` | Modules 3–5 | Translation units, Make, linked source, pointer/array diagrams and within-object arithmetic |
| `SEF6-AS3` | Modules 5, 7 and 9 | Dynamic buffer ownership, `realloc` failure postconditions, checked growth and deterministic allocation faults |
| `SEF6-AS4` | Modules 8–10 | C struct/text representation, bounded `fgets` and `strtol` policy, explicit-length framed parsing and error cleanup |
| `SEF6-AS5` | Modules 2, 4 and 6 | Compile/link/runtime diagnostic distinction, C11 behavior classification and source-located repair without requiring uncontrolled UB |
| `SEF6-AS6` | Modules 9, 11 and 12 | Owned vector/list/map contracts, collisions, duplicate policies and independent fault-injection models |
| `SEF6-AS7` | Module 13 using prior assessed evidence | One multi-file library, client, reproducible build, normal/failing paths, independent reviewer and C/Python ownership defense |

When a lesson prepares an AS3 buffer that later serves as the AS6 vector, the same inspected source revision can support both outcomes where the **published** criteria are actually met. C11 standard-library foundations here feed SEF7's POSIX interfaces; neither POSIX sockets nor Rust are silently added as SEF6 obligations.

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

All **seven required assessments** must pass their published criteria and collectively demonstrate SEF6-O1 through SEF6-O16. Earlier assessed code, diagnostics and test fixtures can be reused and improved in the integrated library; a learner need not repeat an identical lab in every module or implement three independent libraries. The thirteen learning modules and optional practices are preparation, not hidden summative gates.

Reviewers record the decisions and enough inspectable evidence to justify each demonstrated capability. Uncorrected bounds, ownership, arithmetic, parsing, compilation or reproducibility failures block the relevant assessment. A student who cannot access a particular debugger or sanitizer must provide truthful, reviewable substitute diagnostics and run the applicable independent tests; unavailable tooling is not proof of a clean report. The course remains `draft` until the separate learner and reviewer evidence requirements in [Status Labels](../../spec/status-labels.md) are satisfied.

### Historical revision and learner evidence compatibility

This course-level amendment implements the SEF6 workload and library-depth follow-up in [accepted RFC 0003](../../rfcs/0003-sef-academic-progression.md). The original course revision is [SEF6 at OEE commit `922dbe11fd7968097d1b8711ef6f59b763fc0b17`](https://github.com/0xbuffdev/open-engineering-education/blob/922dbe11fd7968097d1b8711ef6f59b763fc0b17/curriculum/SEF/SEF6.md).

| Historical required contract | Present required contract | Evidence interpretation |
| --- | --- | --- |
| `SEF6-O1`–`SEF6-O16` | **Same 16 IDs and exactly unchanged descriptions** | Previously demonstrated competencies retain their exact meanings |
| `SEF6-AS1`–`SEF6-AS7` | **Same 7 published Work, Criteria, Evidence and review conditions** | Previously assessed evidence remains attributable to its source revision; no silent reinterpretation |
| Nine condensed instruction modules, 8-week planning estimate | Thirteen sequenced modules, provisional 14–18 weeks | Instructional presentation changes without adding or removing any completion requirement |
| Dynamic buffer and one combined final data-structure module | Incremental vector, list, hash-map and library integration stages | Reuse the same implementation and review evidence; no second assessed library or hidden per-module quota |

The old completion remains associated with the old revision and is neither revoked nor automatically regraded by a teaching-sequence change. No independent new outcome or additional assessment has been introduced. Learner readiness remains `draft`, with the estimated duration calibrated only after measured student/reviewer work. No change is made to SEF3/SEF4/SEF5 prerequisite codes, SEF7's POSIX scope, repository-wide OEE specification requirements, or a paid/hosted tooling obligation.
