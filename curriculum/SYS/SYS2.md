# SYS2 — Systems Programming with C & Rust

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** [SYS1](SYS1.md) (completed SEF includes SEF6 and SEF7)
**Duration:** 16–20 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; validate with learners)

> [Systems Engineering](README.md) · [Course format](../../spec/course-format.md) · [Curriculum design guide](../DESIGN-GUIDE.md)

## Overview

**SYS2 is the first formally taught and assessed Rust course in the SYS core pathway.** Its purpose is not to repeat SEF6's C object-memory work or SEF7's Unix API introductions, nor to promote Rust as intrinsically free of operating-system, protocol or security failures. It builds new Rust language/ownership expertise, compares C/Rust correctness contracts, develops safe user-space Unix resource handling and produces a **bounded, failure-aware, multi-child process supervisor** with independently reviewable evidence.

Rust is **taught from its foundations**: toolchain/edition and Cargo; expressions, patterns, structs, enums, traits and iterators; moves, shared/mutable borrowing, lifetimes, RAII and compiler diagnostics; then error types, bounded byte parsing and OS handles. ABI/FFI/unsafe reasoning follows those prerequisites. Process state, cancellation, simultaneous pipe draining and explicit memory/output caps precede the integrated utility; no SYS3-level atomic memory-order reasoning is assumed. [SYS10](SYS10.md) owns **kernel implementation**, [SYS3](SYS3.md) owns advanced concurrency, [SYS4](SYS4.md) owns scalable networking and [SYS5](SYS5.md) owns storage internals and crash-recovery protocols.

**Environment:** A local nonprivileged Linux system, stable Rust toolchain, C11-capable compiler, Cargo and small self-authored deterministic fixtures. The reference solution can use the Rust standard library without proprietary services, public sockets, host-kernel changes, root rights or mandatory unsafe code. Free and documented third-party crates may be used if pinned and reproduced; the required capabilities and criteria are independent of that choice. Declare Rust compiler release, edition, target, Cargo dependencies/lockfile and relevant Linux behavior; distinguish platform-specific extensions from cross-platform guarantees. A limited Linux VM or equivalent isolated local environment is an acceptable teaching alternative when its limitations are recorded.

**Safety and precision:** `Command` configures an executable and arguments rather than invoking a shell by default, but its executable search, environment and child processes still require explicit authority controls. `Child` does not automatically wait/reap merely when dropped. `wait_with_output` can buffer arbitrarily large child output unless the producer/reader design guarantees a cap; the required utility must genuinely bound output. RAII destructors release many resources on ordinary control paths but cannot promise durable writes, fallible-close reporting, child reaping or cleanup after every kind of process termination. Unsafe code may be *studied* with bounded invariants without requiring learners to execute undefined C/Rust behavior.

**Planning allocation:** The current **16–20 weeks** at roughly **10–15 focused hours/week** (160–300 focused hours) remains explicitly provisional. Real study covers Rust foundations, compile-fail analysis, C/Rust comparisons, supervised I/O, fault injection, reproducible testing, feedback and a defense. Cumulative assessment artifacts must be reused where they demonstrate distinct outcomes; learners are not assigned duplicate final utilities merely to satisfy five assessment IDs. Completion depends on the published evidence contract rather than calendar hours or optional practice.

## Learning outcomes

- **SYS2-O1:** Build and test reproducible multi-module Rust programs using Cargo, explicit toolchains and robust error contracts.
- **SYS2-O2:** Explain and apply ownership, moves, borrowing, lifetimes, slices and Drop to systems-facing APIs.
- **SYS2-O3:** Model invalid, pending and completed operations with enums, Option, Result and checked conversions.
- **SYS2-O4:** Manage bounded buffers, files and other OS resources with explicit owned/borrowed lifetimes and cleanup policies.
- **SYS2-O5:** Compare equivalent C11/POSIX and Rust implementations using independently verified behavior and precise memory-safety claims.
- **SYS2-O6:** Analyze process/resource inheritance, address-space boundaries and multichild lifecycle beyond SEF7's foundational exercises.
- **SYS2-O7:** Implement failure-aware child supervision, bounded pipes, timeouts, signal policy, cancellation and reaping.
- **SYS2-O8:** Use Rust Unix abstractions for file, descriptor and IPC operations while identifying Linux-specific behavior.
- **SYS2-O9:** Identify unsafe, FFI, ABI and panic boundaries and specify the invariants required to prevent undefined behavior.
- **SYS2-O10:** Reproduce and diagnose a C memory/resource defect and its Rust counterpart using diagnostics, independent tests and limitations.
- **SYS2-O11:** Implement bounded byte-oriented parsing, path validation and output contracts without conflating UTF-8 strings with OS paths.
- **SYS2-O12:** Deliver a reproducible multi-module Rust utility with controlled normal, invalid, partial-failure and cleanup paths.
- **SYS2-O13:** Explain a previously unseen ownership/resource failure and defend an evidenced correction.
- **SYS2-O14:** Distinguish language, library, POSIX, Linux and hardware guarantees in systems-facing decisions.

## Modules

### Module 1 — Rust Programs, Toolchains and Language Foundations

#### Outcomes

- SYS2-O1
- SYS2-O3
- SYS2-O5
- SYS2-O14

#### Lessons

1. **The SEF-to-Rust boundary** — Use already assessed SEF6 C11 object-lifetime and SEF7 POSIX APIs as prior knowledge; establish SYS2's new claim of Rust ownership and reliable multi-child resource supervision, rather than repeating introductory C syntax or Unix process exercises.
2. **Rust architecture and edition** — Explain rustc, the stable channel, Cargo, standard library, edition selection and target triples; record exact toolchain/edition and avoid assuming that one compiler release or host platform defines all Rust behavior.
3. **Bindings, mutability and expression values** — Translate a small defined C calculation into Rust expressions with let, mut, scopes, shadowing, if/match and typed returns; explain the distinction between rebinding a name and mutating a referent.
4. **Scalar values and checked arithmetic** — Use integer and boolean types with explicit width assumptions; compare checked_add, try_from and safe indexing with C's conversion/overflow pitfalls without claiming overflow checks replace logical input validation.
5. **Structs, enums and pattern matching** — Model a command request, successful result and distinct error cases with algebraic types; construct an exhaustive match and distinguish a state impossible by construction from an unhandled operating-system event.
6. **Crates, modules and visibility** — Create an executable crate with a tested library API, meaningful module boundaries and public/private interfaces; distinguish import paths, binary targets, integration tests and dependencies without making every file a new crate.
7. **Generics and trait-based behavior** — Build one small type-parameterized routine and a bounded trait interface; explain trait bounds, method resolution and where generic abstractions improve testing versus obscure a simple systems operation.
8. **Iterators, closures and data traversal** — Replace a bounded C-style loop with a Rust iterator/closure where ownership and borrowing are explicit; compare eager collection, lazy iteration and allocation or early-exit behavior with equivalent test outputs.
9. **Cargo tests, dependency policy and build identity** — Run cargo fmt/check/test and document Cargo.lock, features, toolchain constraints and clean-checkout instructions. Prefer a std-only assessed baseline or fully disclosed freely available dependencies; note that --locked does not guarantee offline availability.

*Optional formative feedback:* Construct a C-to-Rust equivalence map for a checked integer parser, then test a Rust module's boundary cases and explain one compiler diagnostic rather than simply suppressing it.

### Module 2 — Ownership, Borrowing, Lifetimes and Resource Invariants

#### Outcomes

- SYS2-O2
- SYS2-O4
- SYS2-O9

#### Lessons

1. **Move, Copy and Clone** — Trace ownership transfers through assignment, function arguments and return values; distinguish Copy semantics from explicit allocation-bearing clone and justify which operation leaves a unique resource owner.
2. **Exclusive and shared references** — Predict borrow checker acceptance of immutable versus mutable references, including overlapping lifetimes and reborrowing; link rejection to aliasing guarantees rather than memorizing syntactic workarounds.
3. **Slices, strings and dynamic storage** — Use slices and Vec/String for bounded byte and text operations; explain length versus capacity, invalid UTF-8, allocation-failure limitations and why indexing must not become an unchecked resource assumption.
4. **Lifetime relationships** — Derive a function signature that returns a view into one named input; identify why lifetime annotations document relationships and do not prolong objects or imply stack-only storage.
5. **Borrow checking across branches** — Refactor a resource-state operation using scoped borrows, pattern matches and early returns; diagnose the precise conflict rather than adding needless clones or leaking a value to force compilation.
6. **Drop and RAII boundaries** — Draw creation/move/drop paths for files, buffers and child handles; explain that destructor execution is not guaranteed after abort, kill, leak or process failure and that ordinary Drop cannot report fallible close/sync results.
7. **Owned and borrowed operating-system handles** — Distinguish owned and borrowed descriptor semantics using the std::os::fd ownership traits; analyze an example of duplicate ownership of the same raw descriptor as an unsafe contract violation without executing it.
8. **Interior mutability under a single owner** — Use Cell or RefCell when necessary, predict a runtime RefCell borrow error, and distinguish interior mutability from cross-thread shared-state correctness delegated to SYS3.
9. **Borrowing in iterators, errors and closures** — Trace capture modes and borrowed views through a bounded iterator or callback; show where ownership must be transferred to retain a value beyond its source and where a borrow is sufficient.
10. **Negative compilation as evidence** — Maintain short deliberately non-compiling borrow/lifetime cases with captured diagnostic intent and corrected versions; distinguish language-enforced rejection from a successful runtime correctness test.

*Optional formative feedback:* Given a graph of a buffer, file handle and returned slice, identify unique owners, allowed loans and the exact resource-drop order; contrast compiler rejection with a separate runtime logic defect.

### Module 3 — Explicit States, Errors and Bounded Input

#### Outcomes

- SYS2-O1
- SYS2-O3
- SYS2-O11
- SYS2-O14

#### Lessons

1. **Option, Result and error categories** — Distinguish legitimate absence, malformed input, interrupted I/O, process failure and internal invariant violation; write typed APIs whose callers must choose meaningful handling.
2. **The question-mark operator and context** — Propagate errors using ? with an explicit public error type or documented conversion; attach safe context without conflating the original OS error, partial success and the caller's recovery decision.
3. **Invalid-state prevention** — Use enums and a minimal state machine to represent requested, running, finished, canceled and failed process states; derive a transition table and reject an impossible double-finish or missing-owner case.
4. **Checked conversions and budgets** — Parse sizes and counts with try_from/checked arithmetic and explicit maximums before allocating or scheduling; challenge negative, enormous, zero and overflowing values against the published capacity policy.
5. **Byte streams versus UTF-8 text** — Define byte-level framing, validate line endings and length fields, and use String::from_utf8 or equivalent only where UTF-8 is part of the protocol; distinguish arbitrary raw bytes from characters.
6. **OsStr, OsString and Unix paths** — Show why Unix filenames and process arguments need not be UTF-8; design error messages and fixture handling that preserve path identity without converting through lossy display strings.
7. **Bounded parsing and partial records** — Write a length-aware parser over a byte slice, track cursor position safely and distinguish incomplete frame, invalid format and accepted empty payload; verify malicious length and truncated-input cases.
8. **Observability and privacy in errors** — Define stable exit statuses, user-facing diagnostics and machine-readable result classification without logging secrets, full child environments or untrusted raw control characters into terminals.
9. **Unit, regression and dependency-injected tests** — Specify independent expected output for normal, empty, malformed, overflow and partial-input paths; factor an adapter seam for controlled failing reads or child status without requiring a proprietary mocking framework.

*Optional formative feedback:* Implement a byte parser with a fixed maximum; hand-derive at least five acceptance/rejection examples and explain why a passing happy-path test does not establish resource bounds.

### Module 4 — C/Rust Memory Models, ABI and FFI Contracts

#### Outcomes

- SYS2-O2
- SYS2-O5
- SYS2-O9
- SYS2-O10
- SYS2-O14

#### Lessons

1. **What C and Rust each promise** — Compare ISO C defined/undefined/implementation-defined behavior with Rust's safe-language constraints and library guarantees; separate real memory-safety protections from logic, access-control or exhaustion failures.
2. **Representation and repr(C)** — Calculate one named target's C struct layout and inspect a corresponding #[repr(C)] Rust definition; identify which Rust types and invariants cannot be passed through C ABI merely because a field has matching size.
3. **References, raw pointers and alias assumptions** — Contrast C pointer arithmetic/object provenance with Rust borrow rules and raw-pointer obligations; document validity, alignment, provenance, exclusivity and lifetime assumptions without manufacturing arbitrary dereference addresses.
4. **Unsafe boundaries and safety arguments** — Read a tiny safe wrapper around an unsafe API or inspect a supplied code excerpt; state its safety invariant, preconditions and caller obligations, and identify how a safe API could unsoundly hide an invalid invariant.
5. **FFI strings and binary buffers** — Compare CString/CStr NUL termination and byte-slice length contracts; derive valid buffer ownership and conversion rules, and reject embedded-NUL and encoding confusions without treating all C data as UTF-8.
6. **Allocation and ownership transfer** — Specify which side allocates, borrows, frees and may retain a C/Rust buffer; reason about incompatible allocators, double-free and use-after-free using safe trace tables or captured isolated diagnostics.
7. **Calling conventions and unwind policy** — Differentiate C ABI, platform ABI, linkage, panic=abort and panics that might unwind; state why unwinding across a boundary requires the appropriate explicit ABI/contract and is never assumed safe by default.
8. **Foreign callbacks and lifetime limits** — Analyze callbacks that retain pointers or user-data beyond the call; require an explicit lifetime/owner contract and explain why a Rust borrow accepted at one scope does not authorize use after callback registration.
9. **A bounded C/Rust diagnosis** — Use one equivalent contract and independently derived oracle to compare a controlled C failure and Rust counterpart; a safe fixture or previously captured sanitizer diagnostic can establish a defect without mandating unsafe UB execution.

*Optional formative feedback:* Review an FFI boundary with a struct, returned buffer and callback, identify ownership/panic invariants, and propose a safe API or bounded refusal when the contract cannot be justified.

### Module 5 — Files, Descriptors and Portable Unix Resource Policies

#### Outcomes

- SYS2-O4
- SYS2-O6
- SYS2-O8
- SYS2-O11
- SYS2-O14

#### Lessons

1. **Resource identity beyond integers** — Revisit SEF7's descriptor/open-file-description distinction only to reason about Rust File/OwnedFd/BorrowedFd ownership transfer, inheritance and cloning; do not repeat foundational POSIX descriptor exams.
2. **RAII versus fallible completion** — Trace File drop, explicit flush, sync_all/sync_data where supported and directory metadata updates; explain why a destructor's close cannot prove durability or every close-time failure was surfaced, leaving storage recovery to SYS5.
3. **Bounded reads and writes** — Implement short-read/short-write loops through std::io traits with a fixed byte budget; distinguish EOF from interrupted and would-block outcomes based on the selected interface rather than treating each read as one whole message.
4. **Descriptor inheritance and executable isolation** — Inspect Stdio selection, inherited or duplicated handles and close-on-exec policy; identify which descriptors a child may possess, which changes are OS-specific and why raw-descriptor fabrication is unnecessary.
5. **Path identity and traversal threats** — Use a learner-owned fixture directory and describe symlink, race and path-component hazards. Explain why naive string-prefix, canonicalize-then-open or lossy UTF-8 checks do not create a general hostile-path confinement guarantee.
6. **Creation and failure modes** — Model create-new versus overwrite, read-only inputs, access denial, partial writes and disk-full/injected errors; require an explicit policy for preserving prior output and cleaning up owned temporary files.
7. **Directory-relative and Linux-specific interfaces** — Explain the role of directory-relative operations and selected Linux extensions such as openat2 conceptually or through supplied documentation; do not mandate unreviewed unsafe FFI or claim an optional Linux facility is POSIX-universal.
8. **I/O buffering and identity of observations** — Compare std::io::BufReader/BufWriter behavior with kernel I/O and explicit flushing, documenting when a user-space buffered write has not yet reached the OS; avoid claiming every successful write is crash-durable.
9. **Portable observation and limitations** — Document the actual OS, Rust target, libc/feature behavior and optional /proc or tracing limitations; use deterministic fault adapters when sandbox permissions prevent observing syscalls.

*Optional formative feedback:* Trace owned descriptors through spawn, a failed write and cleanup; identify both safe RAII guarantees and errors that need explicit reporting.

### Module 6 — Process Execution, Ownership and Lifecycle States

#### Outcomes

- SYS2-O3
- SYS2-O6
- SYS2-O7
- SYS2-O8
- SYS2-O14

#### Lessons

1. **Command is not a shell** — Use std::process::Command with an explicitly chosen executable and separate arguments; demonstrate why ordinary shell interpolation is not performed, while executable choice, PATH search and inherited environment remain authority decisions.
2. **Argument and environment contracts** — Choose safe fixture executables, use OsString where necessary and allowlist relevant environment variables/current directory; distinguish a configured process from a successfully running one and avoid inherited credentials/secrets in evidence.
3. **Spawn errors and process exits** — Distinguish OS spawn errors from a child that launched and then returned a nonzero exit, was terminated by a signal, or cannot be waited on; construct a typed outcome covering all required cases.
4. **Owned child identity and reaping** — Track each Child handle created by the supervisor, its wait/try_wait obligations and the transition to a recorded status. Rust Child's Drop does not automatically reap the process; do not assume PID reuse cannot occur.
5. **Foreground, descendants and limits** — Distinguish a directly owned child from a process tree; describe why killing a parent may leave descendants and why full process-group control is platform-specific and not silently promised by a simple standard-library supervisor.
6. **Time budgets with monotonic clocks** — Use Instant-based elapsed/deadline accounting, bounded polling or wake-up and explicit clock limitations; never use wall-clock date comparisons as the sole cancellation decision.
7. **Terminate, wait and escalate** — Specify a controlled terminate/kill/reap sequence for the owned child, classify races with natural exit and repeated cancellation, and distinguish Child::kill's forceful request from a portable graceful TERM/child-group guarantee.
8. **Safe signal handling boundary** — Compare SEF7's signal-handler restrictions with Rust's standard-library process API; keep actual handlers or platform-specific signal sending optional and explicitly sourced, without undocumented unsafe code in baseline work.
9. **Lifecycle state and oracle table** — Write a transition/state ledger for start, running, timeout, canceled, exited, failed-start and reaped cases; map each event to a public exit/error response and test impossible double-wait or orphan assumptions.

*Optional formative feedback:* Use two controlled fixture child programs to predict statuses for successful exit, missing executable and timeout; check ownership/reaping separately from reported return codes.

### Module 7 — Bounded Child I/O, IPC and Failure Recovery

#### Outcomes

- SYS2-O3
- SYS2-O4
- SYS2-O7
- SYS2-O8
- SYS2-O11
- SYS2-O12

#### Lessons

1. **Streams, EOF and backpressure** — Relate piped stdin/stdout/stderr to finite kernel pipe capacity and endpoint closure; use a supplied timeline to predict why a parent waiting before draining a producing child may deadlock.
2. **Interleaving and simultaneous drains** — Design a supervisor that writes stdin and drains stdout/stderr without cyclic blocking. A bounded dedicated safe std thread or limited channel may be introduced and taught here for I/O coordination; advanced atomic memory order/lock-free analysis belongs to SYS3.
3. **Read limits are resource policy** — Apply hard byte ceilings to each captured output stream and terminate/reap on limit violation; explain why wait_with_output alone can collect unbounded output, why merely truncating after collection is not bounded and how to avoid buffer exhaustion.
4. **Framing and streaming parsers** — Define a small binary/line frame with maximum size, EOF and malformed-prefix semantics; implement incremental parsing and distinguish partial input from an accepted complete message without trusting child output as text.
5. **Broken pipes and partial writes** — Handle early child exit, EPIPE, EINTR, partial write and closed-reader cases through the chosen Rust I/O contract; never depend on a single write completing every byte.
6. **Deadlines, cancellation and join** — Specify how a deadline aborts producing and reading work, closes owned stream ends, terminates the direct child, joins any owned helper thread and records any unresolved cleanup limitation.
7. **Multi-child supervision within a cap** — Schedule at least two directly owned child processes under an explicit maximum count and output memory budget; enforce per-child status ownership, no unbounded queueing and deterministic aggregation semantics.
8. **Fault injection without live services** — Provide short-writing, verbose, hanging, immediate-exit and invalid-frame synthetic helpers; test transitions without external daemons, network traffic or injecting faults into unrelated host processes.
9. **Race and cleanup evidence** — Repeat bounded cancellation and early-exit scenarios to look for hangs or leftover direct children; explain why observing no processes after one run cannot prove a general absence of races or descendants.
10. **Progress and timeout diagnostics** — Track successful bytes, per-child status, deadline reason and meaningful failure class without collecting unrestricted child environment or user data; present an independent reviewer with a reproducible failure trace.

*Optional formative feedback:* Independently draw the two-pipe deadlock schedule, then inspect a bounded-capture design that must stop an output-flooding fixture without unbounded allocation or a remaining directly owned child.

### Module 8 — C/Rust Comparison, Independent Tests and Trust Boundaries

#### Outcomes

- SYS2-O5
- SYS2-O9
- SYS2-O10
- SYS2-O11
- SYS2-O13
- SYS2-O14

#### Lessons

1. **One contract before two implementations** — Choose a bounded bytes-to-records operation implemented in defined C and safe Rust; publish identical input/output/error oracles and compare observable behavior before discussing toolchain or language advantages.
2. **Diagnose a controlled C defect** — Demonstrate a memory/resource fault through defined behavior, isolated diagnostic fixture or vetted sanitizer report; distinguish a reproducible leak/cleanup mistake from undefined behavior whose manifestation is not specified by ISO C.
3. **Rust rejection and residual failure** — Show a comparable compile-time rejected borrow example and a Rust implementation that still needs tests for integer bounds, protocol validation, process cancellation and correct authorization.
4. **Unsafe and FFI audit without heroics** — Inspect one small FFI or raw-pointer boundary for allocator, alignment, lifetime and unwind obligations; report whether a verified safe wrapper exists, avoiding a mandatory executable unsafe implementation.
5. **Commands, paths and authority** — Threat-model untrusted executable names, argv, environment, symlink-sensitive paths, overwrites and diagnostic disclosure using owned fixtures; distinguish memory safety, operational safety and security policy.
6. **Test harness provenance and review** — Create normal, invalid, boundary and injected-failure cases with expected results derived from a separate specification, and record build flags/toolchains/limits; explain why a green test or sanitizer silence does not prove absence of defects.
7. **Unseen resource failure analysis** — Reproduce a new ownership, child-lifecycle or C/Rust boundary discrepancy supplied by a reviewer; localize the violated invariant, propose a correction and preserve an independent before/after regression.
8. **Portability and guarantee matrix** — Tabulate what the C and Rust language rules, standard libraries, POSIX, Linux, executable ABI and host hardware respectively promise; identify which results require platform testing rather than an unconditional portability claim.

*Optional formative feedback:* Review a report claiming 'Rust makes the utility safe'; require one compiler-enforced guarantee, two surviving non-memory risks, actual failure fixtures and bounded technical conclusions.

### Module 9 — Integrated Rust Process Utility and Engineering Defense

#### Outcomes

- SYS2-O1
- SYS2-O2
- SYS2-O3
- SYS2-O4
- SYS2-O6
- SYS2-O7
- SYS2-O8
- SYS2-O11
- SYS2-O12
- SYS2-O13
- SYS2-O14

#### Lessons

1. **Public problem and scope** — Specify one locally reproducible Rust utility that supervises **at least two learner-owned synthetic child programs**, processes bounded byte inputs and reports distinct outcomes. A file-only converter cannot substitute for required multi-child supervision evidence.
2. **Package and interface boundaries** — Divide CLI validation, typed core state, process adapter, bounded stream capture, fixture implementation and report formatting into small tested modules or library/binary targets; keep the production interface understandable without overengineering.
3. **Resource and capacity contract** — Publish maxima for input bytes, concurrent children, stdout/stderr capture, deadlines, memory queueing and allowed executable paths; define exactly which resources must be released for success, cancellation and midstream failure.
4. **Cumulative supervision artifact** — Reuse AS3's supervised-child implementation and harness as the foundation for the complete utility; do **not** require an independently reimplemented process supervisor or new C safety portfolio solely for AS4.
5. **Independent failure scenario** — Replay synthetic hangs, output floods, early exits, missing binaries, malformed frames, permission failures and resource exhaustion via safe test seams; prove observed status and cleanup against independently stated expectations.
6. **Clean-room reproduction** — Build from a fresh repository checkout with recorded stable toolchain/edition, Cargo.lock where applicable, documented features and free dependencies; run all required fixtures with bounded time and no paid, root or public-network requirements.
7. **Reviewable runbook and limitations** — Publish invocation examples, input/output formats, expected exit behavior, bounded cleanup guarantees and honest limits on descendant process trees, filesystem race safety, kernel behavior and privacy of logs.
8. **Unfamiliar corrective defense** — Accept a reviewer-supplied changed input or fault, explain ownership and state transitions before patching, show a minimal fix and independent regression, and justify at least one remaining tradeoff.

*Optional formative feedback:* Conduct a dry run with an unseen multi-child fixture, predict resource/state transitions and verify that the submitted implementation and report agree without rewriting completed prior summative work.

## Completion requirements

**Five summative assessments establish the fourteen published outcomes.** Module feedback, optional investigations and teaching examples are not additional gates. AS3's child-supervisor and fault harness are **reused and extended** for AS4's complete release; AS1's Rust library can become a module of that release, and AS2's comparison may supply AS5 context. Each assessment still needs its own explicitly evaluated work, criteria and evidence. No successful compilation, sanitizer silence, elapsed time or file existence substitutes for independently demonstrated understanding.

- **SYS2-AS1** — Rust Types, Ownership and Fallible API Contract
  - **Outcomes:** SYS2-O1, SYS2-O2, SYS2-O3, SYS2-O4.
  - **Work:** Build a reproducible library/binary Rust package with a bounded byte parser or container, a fallible resource adapter and well-typed result states. Give a written ownership/move/borrow/Drop explanation and two intentionally rejected borrow/lifetime examples with corrected equivalents. Use actual Cargo tests plus boundary and injected-failure inputs; retain code as reusable material for AS4 where appropriate.
  - **Criteria:** Builds and tests under a documented stable toolchain/edition with no hidden dependencies; accepts independently specified valid inputs and rejects empty/malformed/overflow/partial inputs as contracted. Enums/Option/Result express distinct states, checked arithmetic prevents unbounded allocations, references and lifetimes have valid owners, and resource cleanup policy distinguishes RAII from explicit fallible completion. Negative compiler examples are genuine borrow/lifetime violations rather than arbitrary syntax errors; implementation uses no unjustified unsafe code and the learner explains the limit of what compilation proves.
  - **Evidence:** Source and manifest/lockfile as applicable, clean-checkout commands, independent golden inputs and negative cases, compile-fail diagnostics and corrected code, ownership/resource-state traces, plus a concise explanation of failure and cleanup policies.

- **SYS2-AS2** — Equivalent C/Rust Behavior and Unsafe-Boundary Reasoning
  - **Outcomes:** SYS2-O2, SYS2-O5, SYS2-O9, SYS2-O10, SYS2-O14.
  - **Work:** Implement one equivalent **bounded byte-processing or resource-ownership operation** in C11 and safe Rust using a common independently published input/output/error oracle. Analyze at least one controlled C memory/resource defect through a defined failure case, safe isolated diagnostic fixture or captured sanitizer result; demonstrate the corresponding Rust compiler rejection where applicable and separately test a Rust logic/resource failure that the borrow checker cannot exclude. Inspect a small FFI or unsafe API contract and identify layout, ownership, alias, allocator and panic/unwind obligations. No running undefined behavior is mandatory.
  - **Criteria:** Comparable correct implementations pass the same normal/boundary/invalid fixtures before any comparison; the defect is supported by an actual trace/diagnostic or defensible invariant analysis rather than invented sanitizer output. Rust language guarantees, unsafe-code obligations, C semantics, ABI assumptions and Linux/POSIX behavior are accurately separated; neither a passing sanitizer nor safe Rust is represented as proof of functional, security or availability correctness. A reviewer can identify the failure precondition and why a proposed correction removes it.
  - **Evidence:** C and Rust sources, common golden fixtures and test outputs, reproducible build/diagnostic commands or attributable supplied diagnostic, annotated FFI/ownership safety contract, corrected case and a claim/evidence/limitation comparison.

- **SYS2-AS3** — Bounded Failure-Aware Multi-Child Supervisor
  - **Outcomes:** SYS2-O3, SYS2-O6, SYS2-O7, SYS2-O8, SYS2-O11.
  - **Work:** Implement and test the process-supervisor engine used by AS4, launching **at least two directly owned synthetic children** under a published maximum. Give each child typed lifecycle states, an Instant-based deadline, independently owned stdin/stdout/stderr streams, bounded data capture, well-defined cancellation/forced termination and a wait/reaping policy. Supply controlled helpers for immediate exit, output flood, pipe backpressure, invalid frame, broken pipe and timeout. Basic safe std threading for draining pipes may be used after learning it in this course; advanced synchronization primitives are not assessed here.
  - **Criteria:** Actual maximum child count, input/frame size and stdout/stderr byte limits are enforced **during streaming**, not only checked after unbounded collection. The parent never waits on a producer while leaving that producer blocked by a full undrained pipe; both output streams are handled without cyclic waiting or uncontrolled helper threads. Spawn failures, normal/nonzero exits, early EOF, partial I/O, malformed messages, timeouts and cancellation map to distinguishable documented results. Every directly owned child is accounted for and waited/reaped on all tested completion and cleanup paths, including resource-limit termination. A simple std::process supervisor does not claim to manage grandchildren or guarantee graceful TERM on every platform.
  - **Evidence:** Executable supervisor source and state diagram, explicit numerical resource/deadline contracts, independently expected child outcomes, fault helper source, repeatable bounded-time failure traces, clean build/run commands, descriptor/child cleanup checks and platform limits.

- **SYS2-AS4** — Reproducible Integrated Rust Unix Utility
  - **Outcomes:** SYS2-O1, SYS2-O3, SYS2-O4, SYS2-O6, SYS2-O7, SYS2-O8, SYS2-O11, SYS2-O12.
  - **Work:** Integrate the **same AS3 supervisor** into one multi-module, nonprivileged Rust utility with an executable CLI, input validation, bounded byte framing, clear result/error contracts, safe local fixture access, process authorization policy, diagnostic redaction and documented run/cleanup behavior. Include a small public runbook and independent regression/failure harness; do not build a second process supervisor merely to fill this assessment.
  - **Criteria:** Fresh checkout reproduces required behavior with a stable declared toolchain and available free dependencies; both successful and malformed, huge-input/output, missing-binary, permission-denied, timeout, interrupted and partial-failure cases are covered with explicit expected outcomes. Project limits are enforced without root, public network, private grader, untrusted shell construction or undocumented credentials. State and file/descriptor ownership are demonstrably coherent, exit codes and logs do not silently disclose secrets, and unsupported descendant-process containment or filesystem-race protections are not falsely promised.
  - **Evidence:** Integrated source tree, manifest/lockfile, fixture programs and data, CLI/limits documentation, build/runbook and exit-code table, independent golden outputs, automated normal/fault tests, reproduction logs and relevant safety/portability limitations.

- **SYS2-AS5** — Unfamiliar Rust/C Resource-Failure Diagnosis and Defense
  - **Outcomes:** SYS2-O2, SYS2-O5, SYS2-O9, SYS2-O10, SYS2-O12, SYS2-O13, SYS2-O14.
  - **Work:** Investigate a **previously unseen** bounded Rust, C/Rust interface or Unix resource scenario supplied by an independent reviewer (or public variant-generation rule), differing materially from the learner's AS2 golden example and AS3 rehearsed faults. Predict failure/ownership transitions before executing a fixture, reproduce the discrepancy safely, identify a violated invariant, make a minimal correction or justified bounded refusal and defend the result without reconstructing unrelated prior assignments.
  - **Criteria:** Cause and predicted state are justified from documented Rust/C/library/ABI/OS contracts, with no claim that undefined C has predictable output. Independent before/after fixtures demonstrate a meaningful change and protect previously correct behavior; the learner explains any unobserved failure modes and distinguishes memory-safety reasoning from process, security and availability guarantees. The reviewer can inspect authorship, evidence and a written, recorded or live defense. Unsupported certainty, unexplained pasted tool output or a memorized fix does not establish SYS2-O13.
  - **Evidence:** New challenge description/seed, ordered predictions and actual observations, minimal patch or analysis, independent regression outcomes, cause/ownership diagrams, documented reproduction steps, trade-offs and reviewable defense decision.

### Course boundaries, implementation safety and independent access

All fourteen SEF7 outcomes and seven SEF7 assessments remain assessed **in SEF7**; no SEF7 outcome is transferred or automatically awarded by SYS2. SEF6 already assesses C11 pointer/object lifetime and SEF7 covers baseline file descriptors, fork/exec/wait, signals, pipes, and one single-peer loopback service. SYS2 specializes in **Rust from foundations, comparative safety contracts, more complex owned resource graphs and failure-aware multi-child supervision**. SYS10 develops kernel mechanisms; SYS3 develops threads/atomics and concurrent correctness; SYS4 takes responsibility for multi-client services; SYS5 covers data-engine durability rather than assuming File::sync_all proves an entire transaction's crash safety. APP15 remains an optional application interoperability course, not a prerequisite for SYS graduation.

Use only learner-owned, explicitly bounded local processes, fixture paths and test data. Never demand deliberate uncontrolled UB execution, unreviewed `unsafe` implementations, root permissions, public network access or shell commands assembled from untrusted strings. Safe std-thread use for concurrent pipe draining is **taught within this course** and does not presume SYS3. Alternative reviewable text diagrams, state tables or written/recorded defenses must demonstrate identical required reasoning. Simulator/diagnostic reports disclose provenance, tested conditions and limitations.

### Revision and evidence integrity

The fourteen established outcome IDs **SYS2-O1–O14** and five established assessment IDs **SYS2-AS1–AS5** are retained because the underlying competencies remain continuous. The tighter child-process output limits, required independent comparison oracle and explicit process-cleanup/defense criteria are **material clarifications to evaluation expectations for this course revision only**. Preserve historical learner evaluations against their applicable course/specification revision, without retroactive pass/fail. Each decision identifies the revised source, assessment, demonstrated outcomes, reviewer, evidence and limitations; executable outcomes require reproducible commands, independently derived expectations and relevant invalid/failure cases. No CI success, editorial approval or exercise tally alone promotes the educational status beyond `draft`.

## Optional disciplinary references

All sources are public, support lesson research and are **not** mandatory paid readings or hidden grading requirements:

- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — editions, ownership, structs/enums, traits, generic types, modules and tests.
- [The Rust Reference](https://doc.rust-lang.org/stable/reference/) and [Rustonomicon — FFI](https://doc.rust-lang.org/stable/nomicon/ffi.html) — unsafe/FFI requirements, ABI/unwinding and limits of Rust guarantees.
- [Rust std::process::Child](https://doc.rust-lang.org/stable/std/process/struct.Child.html), [Command](https://doc.rust-lang.org/stable/std/process/struct.Command.html) and [Stdio](https://doc.rust-lang.org/stable/std/process/struct.Stdio.html) — process spawning, wait/reaping and pipe-deadlock concerns.
- [Rust std::os::fd](https://doc.rust-lang.org/stable/std/os/fd/) and [std::os::unix::ffi](https://doc.rust-lang.org/stable/std/os/unix/ffi/) — borrowed/owned descriptors and Unix non-UTF-8 data.
- [Linux man-pages](https://man7.org/linux/man-pages/) — actual Linux/POSIX resource and process behavior.
