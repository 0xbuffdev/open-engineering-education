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

The C11 teaching sequence is organized by independently necessary exit competencies: defined C operations and representations; separate translation units with reproducible diagnosis; bounded pointer and language-semantic reasoning; failure-safe allocation and API ownership; portable text records; explicit-length binary framing; owned dynamic arrays; owned linked lists; collision-safe hash maps; and one integrated library. The **same seven required summative assessments** combine these capabilities; module and lesson counts are not quotas, and the modules are not extra assessed assignments. Buffer, parsing and data-structure implementations, fault-injection fixtures and review evidence may be reused, rather than rebuilt for every assessment. There is no universal checkpoint/lab quota, separate mandatory final lab, paid tool, external network, production data, privileged operation or hidden grader.

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

### Module 1 — C11 Execution, Representations and Checked Values

#### Outcomes

- SEF6-O1
- SEF6-O2
- SEF6-O10
- SEF6-O15

#### Lessons

1. **Why C makes representation observable** — Connect prior Python program behavior and SEF4 algorithm invariants to C11 objects, storage and explicit constraints; explain why C source is not a direct map of physical memory, and distinguish ISO C from the later POSIX work in SEF7.
2. **A defined and reproducible first program** — Compile and run a small `main` with a C11-capable compiler; document declarations, return status, compiler mode and program output rather than treating an executable name as a language guarantee.
3. **Variables, initialization and expression values** — Trace declarations, initialized automatic objects, assignments and arithmetic; explain why an uninitialized indeterminate object is not a safe value to print or inspect as an arbitrary type.
4. **Fundamental types and a C byte** — Inspect `sizeof`, `_Bool`, integer, floating and character types alongside `CHAR_BIT`; distinguish the minimum C11 constraints and implementation properties from an assumed eight-bit octet.
5. **Literals and controlled branching** — Interpret decimal/octal/hex literals, integer suffixes, character escapes, `if`/`switch` and bounded loops, showing why a missing branch or failed loop variant changes the program contract.
6. **Limits, signedness and usual conversions** — Use `limits.h`, `sizeof` and independently derived examples to predict integer promotions, signed/unsigned comparisons, integer division and out-of-range conversion behavior without assuming the sign representation.
7. **Unsigned wrap and checked signed arithmetic** — Derive unsigned modular reduction from the actual type range while rejecting signed overflow before performing the invalid operation; give a valid size or operand boundary counterexample.
8. **Division, shifts and evaluation-order hazards** — Check zero divisors, the exceptional signed minimum divided by -1, shift counts/operands and unsequenced side effects, classifying each unsafe expression without executing it.
9. **Defined, unspecified, implementation-defined and undefined** — Classify an actual example of each C11 category, distinguishing a machine observation, a compiler warning and a standard-mandated result.
10. **Object bytes versus portable values** — Read an initialized object representation through an `unsigned char` view, explain padding and nonportable raw-object serialization, and distinguish a C byte from an external eight-bit protocol octet.
11. **Formats, character classification and parsed integers** — Match `printf` conversion types including `%zu`, `%td` and `%p` with correct pointer conversion; use `strtol`, end-pointer, `errno` and unsigned-char/EOF rules for `ctype.h` under explicit whitespace and range policy.
12. **A checked arithmetic and parsing regression** — Compare hand-derived limits, signed/unsigned values and valid/invalid decimal strings against the actual implementation; repair a defined failure and document why no result from running UB is required.

*Optional practice:* Predict the output of a safe `UINT_MAX + 1u` program and identify which similar signed expression cannot be evaluated to obtain a portable observation.

### Module 2 — Translation Units, Build Reproduction and Fault Diagnosis

#### Outcomes

- SEF6-O3
- SEF6-O8
- SEF6-O9
- SEF6-O12
- SEF6-O15

#### Lessons

1. **Function calls and explicit contracts** — Distinguish declarations from definitions, parameter passing by value from pointer-mediated mutation and a successful return from an initialized out-parameter contract.
2. **Scope, linkage and storage duration** — Trace block, file and external names, `static` linkage and automatic/static lifetimes, without conflating source visibility with ownership or memory segment placement.
3. **Header and interface stability** — Publish compatible prototypes, include guards and shared type declarations, reserving implementation state for source files instead of multiplying external definitions.
4. **Separate compilation and the build graph** — Compile a header/client/two-source example into object files and link it, explaining macro processing, compilation, link resolution and implementation-specific loading as distinct steps.
5. **Safe Make targets** — Define real source/header dependencies and bounded `build`/`test`/`clean` targets that operate only on a declared project output tree; show how a header change affects correct rebuilding.
6. **Compiler diagnostics versus language proof** — Enable actual supported standard/warning/debug options, distinguish implementation extensions from C11, and explain why warning-free compilation does not certify defined behavior.
7. **Failures at the correct phase** — Reproduce an invalid declaration and missing external symbol in disposable fixtures, separately record the compile/link failure and correct the first source-level cause.
8. **Defined-behavior debugging** — Diagnose a wrong result or failed assertion using recorded hypotheses, a reproducible input and optional breakpoint/stack inspection; avoid intentionally executing an invalid pointer access just to obtain a crash.
9. **Sanitizers and supplied unsafe traces** — Interpret available AddressSanitizer/UndefinedBehaviorSanitizer/leak diagnostics or genuinely supplied reports; name actual flags, paths and limits, never claiming that an unexecuted tool ran.
10. **A durable diagnostic regression** — Isolate one error in a minimal source revision, implement a bounded fix, rerun source/compiled tests and state what the evidence cannot establish about all possible inputs.

*Optional practice:* Compare an unresolved linker symbol with a function that compiles but returns the wrong value; record the two distinct repairs and the test evidence.

### Module 3 — Pointers, Arrays, Strings and C Semantic Boundaries

#### Outcomes

- SEF6-O4
- SEF6-O9
- SEF6-O10
- SEF6-O12
- SEF6-O15

#### Lessons

1. **Object identity, pointer types and null** — Draw initialized scalar objects, addresses and correctly typed pointers; distinguish a pointer value from the lifetime and suitability of the object to which it may refer.
2. **Pointer parameters and visible mutations** — Trace an integer passed by value versus a pointer to a writable integer and state who may mutate the referent and which result the caller actually observes.
3. **Array object, pointer parameter and `sizeof`** — Demonstrate array-to-pointer conversion in expression contexts, preserve the distinction from the complete array type, and predict `sizeof` results inside and outside a function parameter.
4. **In-bounds indexing and one-past formation** — Establish the array object and valid range before pointer arithmetic, form a legal one-past value but never dereference it, and reject an out-of-bounds access *without executing it*.
5. **Related-pointer differences and invalid comparisons** — Use `ptrdiff_t` only for related array elements where the distance is representable; do not infer stable absolute addresses or define order comparisons of unrelated objects.
6. **Lifetime and stale pointer values** — Explain why the lifetime ending makes referring pointers unusable even if a printed address is numerically familiar; analyze an unsafe trace or source snippet instead of dereferencing after free.
7. **`const`, borrowing and aliasing** — Distinguish pointer-to-const from const-pointer declarations and a borrowed reference from an owning allocation, without treating `const` as universal memory safety.
8. **Effective type, alignment and permitted byte access** — Analyze why incompatible type-punning and misaligned accesses may be invalid while `unsigned char` may inspect object representations; avoid unsupported union tricks.
9. **Unsequenced side effects and semantic categories** — Diagnose an expression with unspecified evaluation order or unsequenced modification, separating C11 standard constraints from an optimizer's observed code path.
10. **Strings require storage and terminators** — Model a NUL-terminated character array, `strlen` and permitted standard string operations, distinguishing a text string from a general byte buffer with embedded NULs.
11. **Copying, overlap and bounded formatting** — Check `memcpy` versus `memmove` preconditions and `snprintf` size/return/truncation behavior; do not assume `strncpy` always produces a terminator.
12. **A trace with unfamiliar boundary values** — Predict scalar, array and caller-visible values, four-element pointer relations and empty/invalid string policy, then compare real defined observations and a safe failure/repair regression.

*Optional practice:* Diagram four array elements and a one-past pointer; predict which accesses or comparisons are permitted before compiling a safe trace.

### Module 4 — Object Lifetimes, Allocation and Public Ownership Contracts

#### Outcomes

- SEF6-O4
- SEF6-O5
- SEF6-O9
- SEF6-O12
- SEF6-O15

#### Lessons

1. **Lifetime is not a machine memory region** — Distinguish automatic, static and allocated object lifetimes, without claiming the C standard promises a concrete “stack” or “heap” virtual address layout.
2. **API state, ownership and borrowing** — Specify uninitialized, valid-empty, populated and disposed states, who allocates/frees and who may borrow or mutate each resource.
3. **A heap-backed buffer's invariants** — Define pointer, size and capacity coherently, with explicit empty/zero-capacity and repeated-destruction policies and no unexplained uninitialized outputs.
4. **Allocation sizes before arithmetic** — Check `size_t` addition/multiplication/doubling against declared limits before evaluating byte counts; reject a requested capacity that cannot be represented.
5. **Zero-size allocation policy** — Handle requests for zero elements without relying on implementation-dependent `malloc(0)` or `realloc(p,0)` behavior or accidentally treating a zero-byte allocation as a usable array.
6. **Growth with `realloc` and preserved state** — Hold `realloc` output in a temporary pointer, keep the original valid allocation and elements on positive-size failure, and update the owner atomically only on actual success.
7. **Old aliases and post-`realloc` invalidation** — Explain why references to the original allocation cannot be used after a successful `realloc` call, even when the allocator returns the same numerical address.
8. **Explicit failure contracts and output state** — Specify error kinds, initialized output parameters, preserved sizes/links/data and who owns each temporary allocation after any operation fails.
9. **Deterministic allocator fault injection** — Inject failure on a chosen positive-size `malloc`/`realloc` request using a documented local interface, not an attempt to exhaust memory or hide the production allocation path.
10. **Cleanup under partial initialization** — Track acquired memory/streams and release exactly once along a defined failure path; verify destroy/reinitialize preconditions without double-free.
11. **Borrowed element and mutation invalidation** — Compare internal address borrowing with copying an element, and state exactly when append, remove or reallocation invalidates a client's view.
12. **Independent buffer state-model regression** — Derive empty, singleton, growth and failed-growth output/invariant expectations independently; compare with real C results and repair a seeded owner or cleanup defect.
13. **C versus Python object lifetime** — Compare the manually controlled C release/alias contracts with Python-managed references and possible logical alias bugs; do not claim either language automatically proves full application correctness.

*Optional practice:* Predict the size, pointer ownership and data values after a simulated failed growth, including which aliases would be invalid if a later growth succeeds.

### Module 5 — C Structs, Standard I/O and Bounded Text Records

#### Outcomes

- SEF6-O6
- SEF6-O7
- SEF6-O12
- SEF6-O15

#### Lessons

1. **Structures, nodes and member representation** — Model `struct` members, alignment and padding, nested ownership and a self-referential node pointer without treating raw memory layout as a public text or binary schema.
2. **Unions and bit-fields have constraints** — Explain what selected union/bit-field declarations actually promise under C11 and why their implementation-sensitive representation is not a portable encoding.
3. **Checked `FILE *` lifetime** — Use `fopen`, `fclose`, `fgets`, `fputs` and `fread`/`fwrite` with declared ownership and real return-value checks; separate clean EOF from I/O error with `feof`/`ferror`.
4. **A declared line-record schema** — State integer ID, bounded name, delimiter, maximum line length, encoding assumptions and whether a final record may omit a newline.
5. **Truncated `fgets` fragments** — Recognize when a line exceeds the input buffer; reject or explicitly drain an overlong record instead of accepting the first fragment as a complete message.
6. **Numeric and character field validation** — Use `strtol`, `errno`, end-pointer, width/range and full-consumption checks, with correct `ctype.h` preconditions and a deterministic whitespace/duplicate-ID policy.
7. **Invalid, empty and duplicate records** — Distinguish EOF, an empty valid file, malformed fields, duplicate keys, disallowed embedded NUL and failed reads, returning observable statuses without merging bad data.
8. **Portable text writing and cleanup** — Serialize by documented fields rather than `fwrite(struct)` bytes; detect failed writes, close resources, and avoid publishing partial or unowned state after a rejected record.
9. **Independent text fixtures and round-trip limits** — Hand-derive normal, truncated, delimiter, final-line, duplicate and I/O-fault examples; verify that encoder/decoder mutual agreement alone cannot establish a correct external schema.

*Optional practice:* Feed an overlong line and a final line without newline into the same bounded text parser; predict two different outcomes according to the published policy.

### Module 6 — Explicit-Length Binary Framing and Parser Safety

#### Outcomes

- SEF6-O6
- SEF6-O7
- SEF6-O11
- SEF6-O12
- SEF6-O15

#### Lessons

1. **An external byte-count framing contract** — Specify header, lengths, maximum payload and trailing-data policy in `unsigned char` units; distinguish native C bytes from a separately required eight-bit-octet interchange format.
2. **Pointer-plus-length preconditions** — Treat the input as `(const unsigned char *, size_t)`, check accepted null/empty combinations and establish remaining count before any buffer access.
3. **Safe incremental framing checks** — Verify header presence, advertised length and truncation with subtraction only under established bounds; avoid forming an overflowing `offset + length` expression.
4. **Binary data is not a C string** — Preserve embedded NULs and binary length exactly, never apply `strlen`/text splitting to untrusted nonterminated input, and reject platform-dependent raw-struct framing.
5. **Cleanly owned result and fault rollback** — Declare who allocates decoded records, keep output fully initialized on rejection, and inject a positive-size allocation failure without leaking partial objects.
6. **Independent valid and adversarial frame tests** — Hand-construct empty, exact-boundary, truncated, oversized, trailing-byte and malformed header examples and compare expected statuses/bytes independently of any matching encoder.
7. **Portability and representation defense** — Explain native endianness, `CHAR_BIT`, padding and framing-unit assumptions; demonstrate what a round trip actually proves and one new reviewer-supplied fault's bounded repair.

*Optional practice:* Given a short purported frame and its advertised payload length, calculate the bytes remaining and predict rejection before calling the C parser.

### Module 7 — Owned Dynamic Arrays and Failure-Atomic Operations

#### Outcomes

- SEF6-O5
- SEF6-O12
- SEF6-O13
- SEF6-O15

#### Lessons

1. **Reuse the assessed buffer as a vector** — Extend the same AS3 buffer to the AS6 integer dynamic-array API rather than independently implementing another growing array to satisfy a lesson count.
2. **Invariants and explicit empty state** — Enforce `0 <= size <= capacity`, initialized output/status policies and an understood pointer state after construction and disposal.
3. **Append, read, remove and index limits** — Implement only defined in-range operations, reject invalid indices before access, and explain the array-shift consequences of removal.
4. **Checked geometric growth** — Justify a capacity policy, validate size/doubling/element byte counts before allocation, and preserve the original state on injected `realloc` failure.
5. **Stable logical values versus unstable borrows** — Explain how growth invalidates a retained element pointer, even if the same numeric address is observed, and choose a safe external API.
6. **Independent state-model and fault testing** — Compare seeded insert/read/remove/growth transitions to a separately derived reference, with empty/one/failure cases and invariant assertions after every operation.
7. **Amortized versus single-step cost** — Transfer SEF4's geometric-growth argument to explicit C memory copying, distinguishing aggregate cost, one expensive append, allocation implementation limits and measured timings.

*Optional practice:* Predict vector contents and owner state after two appends and a deliberately failed third growth, then compare against the real source contract.

### Module 8 — Owned Singly Linked Lists and Link Integrity

#### Outcomes

- SEF6-O4
- SEF6-O5
- SEF6-O12
- SEF6-O13
- SEF6-O15

#### Lessons

1. **Nodes, link identity and list invariants** — Define the singly linked node layout, head/tail/count rules, empty and one-node states and a single owner for each allocated node.
2. **Insertion that preserves reachability** — Trace head, middle and tail insertion, the ordering of `next` rewrites and the invariant that every live node remains reachable once from the head.
3. **Removal without leaks or stale uses** — Rewire predecessors, update head/tail/count and release exactly the removed node, documenting borrowed-pointer invalidation and empty-list errors.
4. **Allocation failure before structural commitment** — Inject a failed new-node allocation and prove that previously reachable links, count and payloads remain unchanged.
5. **Destruction and partial cleanup** — Traverse and free each owned node exactly once, recording when repeated disposal or reinitialization is allowed by the API.
6. **Independent sequence and reachability oracle** — Model insert/remove operations with an unrelated simple sequence, compare state after duplicate, empty and singleton transitions and detect one faulty link update.
7. **Vector versus list workload trade-offs** — Contrast indexed access, ordered traversal and insertion costs based on actual representation and lifetime/borrow contracts rather than assuming lists are always faster.

*Optional practice:* Draw a three-node chain, remove its head and tail in two independent trials, and predict how the last node remains reachable.

### Module 9 — Hash Maps, Key Ownership and Collision-Safe Updates

#### Outcomes

- SEF6-O5
- SEF6-O12
- SEF6-O14
- SEF6-O15

#### Lessons

1. **Public key and value contract** — Define key encoding, equality, ownership or copying policy, missing lookup, duplicate update/reject and deletion results before choosing buckets.
2. **Hash function versus equality** — Show with known colliding keys why equal hashes do not mean equal keys, and avoid treating a chosen table capacity as a universal collision guarantee.
3. **Chain or probe representation** — Choose separate chaining or open addressing, declaring how tombstones, buckets and allocated entries are owned and traversed.
4. **Collision and duplicate behavior** — Verify insertion, lookup, update and removal across same-bucket distinct keys and repeated identical keys with independently expected results.
5. **Load factor, capacity and cost model** — Distinguish expected lookup complexity under stated hash/input assumptions from worst-case collision paths; document resizing threshold or a justified fixed capacity.
6. **Overflow-safe growth and rehash** — Check allocation size before evaluation, publish resized bucket state only after verified success and preserve all preexisting entries on injected failure.
7. **Lifecycle and failure postconditions** — Guarantee each key/value allocation has one release path, retain the old map on failed insert/resize, and make empty/duplicate/deletion results distinguishable.
8. **Independent map oracle and adversarial fixtures** — Use a separately modeled key/value set to compare collisions, reinsertion, deletion, duplicate order, forced allocator faults and one corrected bug.
9. **Cross-container contract consistency** — Compare the map's status/borrow rules with vector and list without claiming their representations or failure semantics must be identical.

*Optional practice:* Derive the expected keys after a colliding update, deletion and injected failed resize, then show which public map invariant each operation preserves.

### Module 10 — Integrated C11 Library, Reproduction and Technical Defense

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

1. **One coherent library, not repeated projects** — Assemble the same assessed AS3 buffer, AS4 parser and AS6 vector/list/map code into clear public headers and implementation units; reuse previous evidence where the published criterion is genuinely met.
2. **Build from a clean disposable checkout** — Document compiler standard, flags, dependencies, Make targets and safe cleaning, verify a real compiled client and report toolchain assumptions rather than requiring hosted infrastructure.
3. **A cross-structure contract-driven client** — Compose at least two structures around a synthetic record workload, preserving documented error/status, owner and data-lifetime rules.
4. **Independent normal and failure evidence** — Test zero/one/growth, duplicate/collision, bounded parser rejection and forced positive-size allocation failures with independently expected state and output results.
5. **Diagnose one unfamiliar fault** — Start with a genuinely observed failure or labeled supplied diagnostic, isolate a source line and causal mechanism, repair it safely and retain a regression for the exact contract violation.
6. **C/Python lifetime and design comparison** — Explain C object lifetime, borrow invalidation and manual cleanup versus Python reference-managed objects, without falsely equating memory management with all application correctness.
7. **Independent reviewer reproduction** — Provide a complete README, fixtures and accessible source/ownership map for a real reviewer to build and exercise normal and error cases and challenge one additional valid scenario.
8. **Evidence matrix and limits of the defense** — Map the original seven assessments and all sixteen outcomes to actual artifacts, discuss a design alternative and a remaining tool/platform limitation, and distinguish warning/sanitizer observations from proofs.

*Optional practice:* Have a peer follow the clean-start instructions with no optional sanitizer and present one unfamiliar allocator-failure trace for an independently predicted result.

## Completion requirements

### Teaching sequence and existing assessment alignment

The table identifies where **existing published assessments** obtain their first substantive instructional preparation, not a new grading contract or one mandatory lab per module. The original Work, Criteria and Evidence requirements below are unchanged.

| Existing assessment | Primary teaching stages | Existing inspectable mastery |
| --- | --- | --- |
| `SEF6-AS1` | Module 1 | C11 representations, integer conversions, checked arithmetic, implementation-specific observations and safe `strtol` validation |
| `SEF6-AS2` | Modules 2–3 | Translation units, Make, compiler/link diagnostics, pointer/array diagrams and defined in-object arithmetic |
| `SEF6-AS3` | Modules 3–4 | Lifetimes, owned dynamic buffer, `realloc` failure, checked capacity and deterministic injected allocation faults |
| `SEF6-AS4` | Modules 5–6 | Struct/text serialization, bounded `fgets`, valid `strtol` fields and separately framed binary parsing with defined output and cleanup |
| `SEF6-AS5` | Modules 1–3 and 4 | Source-level C11 behavioral classification and genuinely observed compile/link/runtime diagnosis or supplied unsafe traces |
| `SEF6-AS6` | Modules 4 and 7–9 | Owned vector, list and map contracts with independently checked state changes, collisions, duplicates, growth and injected faults |
| `SEF6-AS7` | Module 10, reusing prior work | One multi-file C11 library and client, actual build/negative evidence, independent review and C/Python ownership defense |

The earlier assessed AS3 buffer is reused as the AS6 vector where its tested public contract meets that criterion. SEF4 owns algorithm choices and invariants; this course introduces their C11 storage and allocation-failure consequences. SEF7 owns POSIX descriptors, processes, signals and sockets rather than adding them to the C11 assessments.

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

All **seven required assessments** must pass their published criteria and collectively demonstrate SEF6-O1 through SEF6-O16. Earlier assessed code, diagnostics and test fixtures can be reused and improved in the integrated library; a learner need not repeat an identical lab in every module or implement three independent libraries. The instructional modules and optional practices are preparation, not hidden summative gates.

Reviewers record the decisions and enough inspectable evidence to justify each demonstrated capability. Uncorrected bounds, ownership, arithmetic, parsing, compilation or reproducibility failures block the relevant assessment. A student who cannot access a particular debugger or sanitizer must provide truthful, reviewable substitute diagnostics and run the applicable independent tests; unavailable tooling is not proof of a clean report. The course remains `draft` until the separate learner and reviewer evidence requirements in [Status Labels](../../spec/status-labels.md) are satisfied.

### Historical revision and learner evidence compatibility

This course-level amendment implements the SEF6 workload and library-depth follow-up in [accepted RFC 0003](../../rfcs/0003-sef-academic-progression.md). The original course revision is [SEF6 at OEE commit `922dbe11fd7968097d1b8711ef6f59b763fc0b17`](https://github.com/0xbuffdev/open-engineering-education/blob/922dbe11fd7968097d1b8711ef6f59b763fc0b17/curriculum/SEF/SEF6.md).

| Historical required contract | Present required contract | Evidence interpretation |
| --- | --- | --- |
| `SEF6-O1`–`SEF6-O16` | **Same 16 IDs and exactly unchanged descriptions** | Previously demonstrated competencies retain their exact meanings |
| `SEF6-AS1`–`SEF6-AS7` | **Same 7 published Work, Criteria, Evidence and review conditions** | Previously assessed evidence remains attributable to its source revision; no silent reinterpretation |
| Nine initial instruction modules, 8-week planning estimate | Later expanded to 13 modules (now consolidated into competency-owned stages); provisional 14–18 weeks | Instructional presentation changes do not add or remove a completion requirement |
| Dynamic buffer and one combined final data-structure module | Incremental vector, list, hash-map and library integration stages | Reuse the same implementation and review evidence; no second assessed library or hidden per-module quota |

**Subsequent competency-first review:** The earlier 13-module/138-lesson expansion repeated language arithmetic/UB claims, separate diagnostic setups, resource/ownership contracts and text parsing across different modules, including nine identical eleven-lesson module lengths. This revision consolidates those mechanisms and grants distinct ownership to explicit-length binary frames, dynamic arrays, linked lists and hash maps based on their actual invariants—not a target count. All existing sixteen outcome definitions and seven summative Work/Criteria/Evidence contracts remain unchanged; historical student evidence stays pinned to its assessed revision. No new mandatory system interface, independent application or readiness status is inferred from restructuring.

The old completion remains associated with the old revision and is neither revoked nor automatically regraded by a teaching-sequence change. No independent new outcome or additional assessment has been introduced. Learner readiness remains `draft`, with the estimated duration calibrated only after measured student/reviewer work. No change is made to SEF3/SEF4/SEF5 prerequisite codes, SEF7's POSIX scope, repository-wide OEE specification requirements, or a paid/hosted tooling obligation.
