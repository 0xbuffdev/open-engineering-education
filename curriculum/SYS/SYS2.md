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

1. **Rust compiler contracts and the SEF boundary** — Compile a small, defined-behavior C calculation in Rust under a declared stable toolchain, target and edition. Identify what SEF already establishes about C and Unix interfaces, what Rust now adds, and which behavior depends on the language, compiler, library or platform. Record actual build identity without presenting one Rust version as universal.
2. **Bindings, expressions and checked numeric decisions** — Translate a bounded C computation using let/mut, expressions, if/match, typed returns and checked conversions. Distinguish rebinding from mutation and test overflow, zero and invalid widths rather than assuming safe arithmetic removes input-validation duties.
3. **Structs, enums and explicit variants** — Represent a request, successful result and distinct failure categories with structs, enums and exhaustive pattern matching. Predict state-specific output for valid and invalid inputs, and identify where a supposedly impossible state was merely left unhandled.
4. **Crate boundaries, Cargo and repeatable builds** — Create a library/binary crate with purposeful public/private module interfaces, a manifest and reproducible build commands; distinguish a module, dependency, binary target and edition/feature choice. Explain the role and limits of Cargo.lock and --locked, including dependency availability.
5. **Generics and traits as bounded contracts** — Implement one genuinely useful generic or trait-bounded operation and test it against two small implementations; justify which constraints belong in the interface and when a generic abstraction would obscure instead of simplify resource ownership.
6. **Iterators, closures and allocation behavior** — Trace a slice through a borrowed iterator and a capturing closure; compare laziness, early exit, collecting into a new buffer and a simple loop. Verify equivalent outputs and explicitly identify what can allocate, move or keep a borrow alive.
7. **Test design and reproducibility** — Separate unit/integration tests from compile checks, format checks and runtime behavior verification. Derive expected outcomes independently for normal, boundary and invalid cases, reproduce from a clean checkout and explain why a successful compile or local passing test is not a correctness proof.

*Optional formative feedback:* Construct a C-to-Rust equivalence map for a checked integer parser, then test a Rust module's boundary cases and explain one compiler diagnostic rather than simply suppressing it.

### Module 2 — Ownership, Borrowing, Lifetimes and Resource Invariants

#### Outcomes

- SYS2-O2
- SYS2-O4
- SYS2-O9

#### Lessons

1. **Moves, Copy, Clone and unique resource ownership** — Trace assignment, argument passing and return for resource-owning and Copy values. Explain why Clone may perform a separate allocation or handle duplication and show a negative case where assuming a moved resource remains available would be invalid.
2. **Shared, exclusive and scoped borrows** — Trace immutable/mutable borrows, reborrowing and nonoverlapping scopes through branches and early returns. Diagnose genuine alias conflicts from compiler output and repair a rejected snippet by changing borrow scope or state, not by gratuitous cloning.
3. **Slices and bounded collections** — Operate on Vec, String and byte slices with correct length/capacity and indexing behavior. Test empty, oversized and invalid-UTF-8 data; distinguish an owned buffer from a borrowed view and disclose allocation/resource limits not guaranteed by type checking.
4. **Lifetime relationships and capture** — Derive a function returning a view into one input, then trace borrowing versus moving a value into a callback or iterator. Explain that lifetime annotations relate references but never extend an object's lifetime; use a compile-fail and corrected variant to reveal a misconception.
5. **RAII, Drop and fallible cleanup** — Draw a state/ownership trace across success, error and early return for buffers, files and process handles. Distinguish deterministic ordinary Drop from explicit fallible completion, child reaping and process-abort limitations; do not claim file close implies durability.
6. **OwnedFd, BorrowedFd and raw handle obligations** — Analyze ownership transfer and borrowing through the stable std::os::fd traits. Show why a forged or multiply-owned raw descriptor can violate safety, why duplicating an fd need not create an independent open-file description, and how to avoid executing unsafe ownership defects.
7. **Interior mutability and language-enforced limits** — Use Cell or RefCell only for a bounded single-thread design that needs it; predict a RefCell runtime borrow failure and contrast it with compile-time exclusion of invalid reference aliases. Distinguish these rules from cross-thread Send/Sync and atomic correctness, which SYS3 assesses.

*Optional formative feedback:* Given a graph of a buffer, file handle and returned slice, identify unique owners, allowed loans and the exact resource-drop order; contrast compiler rejection with a separate runtime logic defect.

### Module 3 — Explicit States, Errors and Bounded Input

#### Outcomes

- SYS2-O1
- SYS2-O3
- SYS2-O11
- SYS2-O14

#### Lessons

1. **Typed fallible APIs and error propagation** — Design Option/Result and a documented error type that distinguishes absence, malformed bytes, interrupted I/O and internal invariant failure. Propagate errors with ? while preserving recovery decisions and safe source context; test a counterexample where a generic error loses necessary state.
2. **Impossible-state prevention and transition tables** — Model requested, running, exited, canceled and failed operations with enums and a transition table. Reject double completion, missing ownership and invalid retry transitions before integrating a real child process.
3. **Checked quantities and resource budgets** — Convert untrusted counts and lengths through checked integer operations and explicit maxima before allocation, spawn or buffering. Test zero, negative-represented, huge and overflowing values; distinguish a declared policy limit from a Rust allocation guarantee.
4. **Byte framing and incremental parsing** — Define a bounded byte protocol with length or delimiter, EOF and invalid-prefix rules, then parse partial records without treating bytes as UTF-8 by default. Check malformed lengths, truncation, empty messages and incremental completion against independent expected outputs.
5. **Unix argument and path identity; safe diagnostics** — Use OsStr/OsString for non-UTF-8 Unix paths and arguments, keeping display escaping separate from identity and authorization. Specify concise error/exit classifications while redacting secrets and untrusted terminal control sequences.
6. **Independent parser and failure tests** — Exercise a parser and fallible adapter through independently prepared normal, boundary, interrupted, partial and invalid cases; use a controlled fault seam rather than assuming the real OS will fail on command. Explain why the tests support specific behaviors but not every resource-safety claim.

*Optional formative feedback:* Implement a byte parser with a fixed maximum; hand-derive at least five acceptance/rejection examples and explain why a passing happy-path test does not establish resource bounds.

### Module 4 — C/Rust Safety and FFI Contracts

#### Outcomes

- SYS2-O2
- SYS2-O5
- SYS2-O9
- SYS2-O10
- SYS2-O14

#### Lessons

1. **C and Rust correctness promises** — Contrast a documented defined-behavior C11 operation with safe Rust, separating compile-time alias/lifetime guarantees from logic, protocol, security and availability obligations. Identify implementation-defined ABI/OS assumptions and reject a comparison based on undefined C output.
2. **FFI representations and calling contracts** — Derive a named-target #[repr(C)] layout against a C struct and identify field types that cannot simply cross the boundary. Distinguish C ABI/calling conventions from size coincidence and verify an independently documented layout/oracle.
3. **Raw pointers, aliasing and unsafe invariants** — Inspect a small unsafe/FFI wrapper without executing undefined behavior; write its validity, alignment, provenance, alias and lifetime preconditions and identify how an invalid safe-wrapper promise would expose a caller to unsoundness.
4. **Foreign strings, buffers and allocation ownership** — Compare CString/CStr NUL-terminated contracts with byte-slice length contracts. Specify which side allocates, borrows, retains and deallocates a buffer; reject embedded-NUL confusion, allocator mismatches and use-after-free through state diagrams or supplied diagnostics.
5. **Callbacks and retained foreign state** — Analyze a callback and user-data pointer retained after a call, including ownership, reentrancy and when destruction is permitted. Identify a trace where an initially valid Rust borrow becomes invalid through foreign retention and provide a bounded refusal or corrected contract.
6. **Unwinding and boundary failure diagnosis** — Differentiate panic strategies, foreign exceptions and an explicitly permitted C-unwind ABI from a non-unwinding C boundary. For a supplied FFI fault, locate the breached invariant and justify a safe interface or recovery boundary without claiming all cross-language unwinding is categorically forbidden.

*Optional formative feedback:* Review an FFI boundary with a struct, returned buffer and callback, identify ownership/panic invariants, and propose a safe API or bounded refusal when the contract cannot be justified.

### Module 5 — Files, Descriptors and Portable Unix Resource Policies

#### Outcomes

- SYS2-O4
- SYS2-O6
- SYS2-O8
- SYS2-O11
- SYS2-O14

#### Lessons

1. **Descriptor identity and Rust ownership** — Apply SEF7's descriptor/open-file-description model to Rust File, OwnedFd, BorrowedFd and try_clone/dup-like operations. Show who owns each handle, what can be inherited and why an fd number alone is not a lifetime guarantee.
2. **Partial I/O and buffering contracts** — Implement bounded std::io reads and writes with partial, EOF and interrupted/error outcomes. Compare BufReader/BufWriter with kernel I/O, verifying what has actually been flushed and explaining why a single read/write need not transfer the full request.
3. **Fallible completion versus crash durability** — Distinguish dropping a File, user-space flush, explicit file synchronization and directory metadata persistence where applicable. Demonstrate an injected sync/close failure policy and state clearly that SYS5—not SYS2—owns engine-level ordering and crash recovery.
4. **Descriptor inheritance and child stdio policy** — Trace which owned handles become child stdin/stdout/stderr and which remain in the parent, including inheritance/close-on-exec assumptions. Identify how an unintentionally retained pipe writer can prevent EOF without claiming std abstracts away every Linux descriptor rule.
5. **Path authority, races and Linux-specific defenses** — Threat-model symlinks, path components, current directory and canonicalize-then-open races within owned fixtures. Explain the conceptual role of directory-relative APIs and optional Linux openat2, while refusing to promise general hostile-path confinement from lexical checks.
6. **Safe file publication and failure evidence** — Compare create-new and overwrite under missing, denied, partial-write or injected disk-full cases. Specify how prior output and temporary owned files are protected, and record the OS/target assumptions necessary to interpret the observed failure.

*Optional formative feedback:* Trace owned descriptors through spawn, a failed write and cleanup; identify both safe RAII guarantees and errors that need explicit reporting.

### Module 6 — Process Execution, Ownership and Lifecycle States

#### Outcomes

- SYS2-O3
- SYS2-O6
- SYS2-O7
- SYS2-O8
- SYS2-O14

#### Lessons

1. **Executable, arguments and environment policy** — Configure Command with an explicitly authorized executable and separate OsString arguments, a controlled working directory and minimal environment. Show that Command is not a shell, but PATH resolution, inherited variables and executable selection still require policy.
2. **Spawn, exit and direct-child ownership** — Differentiate spawn failure from nonzero/signal exit, and use Child/ExitStatus to trace every directly owned child from creation to wait/reap. Reject a lifecycle that drops Child without reaping or assumes PID identity is permanently unique.
3. **Process-tree and descriptor scope** — Distinguish a direct Child from descendants and inherited stream endpoints; identify which cleanup the Rust standard process API can establish and what descendant/group containment would require platform-specific mechanisms not mandated here.
4. **Monotonic time and cancellation conditions** — Specify Instant-based deadlines, polling/notification and bounded scheduling assumptions for a child state machine. Analyze race cases where natural exit and cancellation coincide; do not promise guaranteed wall-clock completion during arbitrary host overload.
5. **Termination, signals and cleanup** — Derive a controlled request-to-terminate, force-kill and wait/reap sequence for a direct child, with status and error handling for repeated attempts. Distinguish forceful Child::kill from graceful SIGTERM and optional process-group signaling; compare safe signal-policy claims with SEF7 without re-teaching handlers.
6. **Lifecycle oracle and negative states** — Write an independently expected transition ledger for successful spawn, missing executable, nonzero exit, timeout, cancel and already-reaped/error cases. Link public result/error values to actual observed transitions and flag an impossible double-wait or unowned child.

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

1. **Pipes, EOF and cyclic waiting** — Trace a finite-pipe schedule where a parent writes stdin or waits while a child blocks on full stdout/stderr. Show the necessary closure/EOF transitions and predict a deadlock before choosing the supervisor's I/O strategy.
2. **Concurrent stream handling with bounded helpers** — Teach sufficient safe std-thread and channel ownership to write bounded child stdin and drain both outputs without cyclic blocking. Specify a finite helper/thread budget and join/error policy, leaving atomic-order, lock-free and generalized concurrency proofs to SYS3.
3. **Streaming resource ceilings** — Enforce maximum stdin/frame bytes, per-stream output capture and aggregate memory across all live children during acquisition, not after collection. Prove with a flood fixture why wait_with_output or post-hoc truncation fails a hard memory bound.
4. **Frame extraction under partial I/O** — Apply M3's parser incrementally to child-generated bytes and an explicitly specified maximum frame, rather than teaching framing afresh. Distinguish malformed payload, partial data, early EOF, interrupted write and broken pipe through typed outcomes and an independent test.
5. **Cancellation, open endpoints and reaping** — Coordinate deadline expiry, stream closure, direct-child termination, helper completion and wait/reap across success and partial failure. Explain the unavoidable limits of local process control, including descendants that retain pipe endpoints or a helper that cannot be joined promptly.
6. **Multiple children and aggregate outcomes** — Run two or more directly owned synthetic children under an explicit concurrency and output budget. Derive deterministic per-child and aggregate status rules despite completion order, without an unbounded backlog or hidden worker spawning.
7. **Fault fixtures and observable cleanup** — Test immediate exit, output flood, backpressure, malformed frame, failure to spawn, short read/write and timeout with owned local fixtures. Record independent expected status, limited diagnostic fields and repeatable evidence of directly owned child cleanup; do not claim finite tests prove all races absent.

*Optional formative feedback:* Independently draw the two-pipe deadlock schedule, then inspect a bounded-capture design that must stop an output-flooding fixture without unbounded allocation or a remaining directly owned child.

### Module 8 — Independent C/Rust Verification and Resource Trust

#### Outcomes

- SYS2-O5
- SYS2-O9
- SYS2-O10
- SYS2-O14

#### Lessons

1. **Independent C/Rust equivalence** — Before attributing a result to language safety, prepare one shared bounded-byte or resource-operation oracle for C and Rust; execute normal, boundary and invalid fixtures against both and document any actual specified semantic differences.
2. **Controlled defects and what Rust does not prove** — Investigate a reproducible defined C resource mistake, an safely isolated or supplied sanitizer case where appropriate, and a corresponding borrow-checker rejection if applicable. Separately reproduce a safe Rust logic, bounds or process-policy failure; distinguish evidence of memory-safety restrictions from overall utility correctness.
3. **Unsafe/FFI safety review with independent oracles** — Audit a small foreign-facing API for representation, ownership, alias, allocation, callback lifetime and unwind policy, with a supplied negative counterexample. Independently check claims against the public contract rather than accepting a sanitizer's silence or compilation as a proof.
4. **Executable/path trust and assessment provenance** — Audit the real utility's selected executable, args, inherited environment, path handling, output disclosure and resource limits through safe malicious-fixture cases. Record toolchain, OS, test oracles and claim limits; classify each guarantee as Rust, C, library, ABI, POSIX, Linux or environment-specific.

*Optional formative feedback:* Review a report claiming 'Rust makes the utility safe'; require one compiler-enforced guarantee, two surviving non-memory risks, actual failure fixtures and bounded technical conclusions.

### Module 9 — Cumulative Rust Utility and Engineering Defense

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

1. **One cumulative Rust supervisor contract** — State the utility's CLI and error semantics, permitted owned synthetic children, byte/frame maxima, concurrent child count, aggregate capture/deadline limits and explicit out-of-scope process-tree policies. Derive these from required outcomes rather than a new feature checklist.
2. **Integrate earlier modules, not duplicate projects** — Re-use AS1's bounded/error components and AS3's supervised-child engine in a clearly separated CLI, parser, process adapter, limits and reporting implementation. Verify ownership and failure-propagation boundaries instead of submitting an unrelated second supervisor.
3. **Independently verified faults and recovery** — Run the same executable against the previously defined happy-path, invalid bytes, output floods, early exits, broken pipes, permission denial, timeout and aggregate-budget tests. Record state transition and resource cleanup evidence, and repair a failing path without overstating descendant containment.
4. **Clean reproduction and operator handoff** — Demonstrate a fresh checkout with pinned/declared toolchain and freely accessible dependencies; publish concise runbook commands, bounded fixtures, exit-code behavior, diagnostic redaction and realistic portability/authority limitations.
5. **New failure diagnosis and independent defense** — Predict the cause of an unfamiliar Rust ownership, C/Rust boundary or Unix child-resource discrepancy before running a fixture. Present competing explanations, an independently checkable change or justified bounded refusal, a regression against previously correct behavior, and a reviewable technical defense without redoing AS1–AS4.

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
  - **Criteria:** Actual maximum child count, input/frame size, per-stream stdout/stderr capture limits **and aggregate captured bytes across live children** are enforced **during streaming**, not only checked after unbounded collection. The parent never waits on a producer while leaving that producer blocked by a full undrained pipe; both output streams are handled without cyclic waiting or uncontrolled helper threads. Spawn failures, normal/nonzero exits, early EOF, partial I/O, malformed messages, timeouts and cancellation map to distinguishable documented results. Every directly owned child is accounted for and waited/reaped on all tested completion and cleanup paths, including resource-limit termination. One actual child-stream ownership/inheritance trace must distinguish Rust std::process handle contracts from relevant Unix descriptor and Linux-specific behavior, rather than relying solely on a passing process test to claim SYS2-O8. A simple std::process supervisor does not claim to manage grandchildren or guarantee graceful TERM on every platform.
  - **Evidence:** Executable supervisor source and state diagram, explicit numerical resource/deadline contracts, independently expected child outcomes, fault helper source, repeatable bounded-time failure traces, clean build/run commands, descriptor/child cleanup checks and platform limits.

- **SYS2-AS4** — Reproducible Integrated Rust Unix Utility
  - **Outcomes:** SYS2-O1, SYS2-O3, SYS2-O4, SYS2-O6, SYS2-O7, SYS2-O8, SYS2-O11, SYS2-O12.
  - **Work:** Integrate the **same AS3 supervisor** into one multi-module, nonprivileged Rust utility with an executable CLI, input validation, bounded byte framing, clear result/error contracts, safe local fixture access, process authorization policy, diagnostic redaction and documented run/cleanup behavior. Include a small public runbook and independent regression/failure harness; do not build a second process supervisor merely to fill this assessment.
  - **Criteria:** Fresh checkout reproduces required behavior with a stable declared toolchain and available free dependencies; both successful and malformed, huge-input/output, missing-binary, permission-denied, timeout, interrupted and partial-failure cases are covered with explicit expected outcomes. Project limits are enforced without root, public network, private grader, untrusted shell construction or undocumented credentials. State and file/descriptor ownership are demonstrably coherent, exit codes and logs do not silently disclose secrets, and unsupported descendant-process containment or filesystem-race protections are not falsely promised.
  - **Evidence:** Integrated source tree, manifest/lockfile, fixture programs and data, CLI/limits documentation, build/runbook and exit-code table, independent golden outputs, automated normal/fault tests, reproduction logs and relevant safety/portability limitations.

- **SYS2-AS5** — Unfamiliar Rust/C Resource-Failure Diagnosis and Defense
  - **Outcomes:** SYS2-O13.
  - **Work:** Investigate one **previously unseen**, bounded Rust ownership, C/Rust interface or Unix resource scenario supplied by an independent reviewer (or a public variant-generation rule), differing materially from the learner's AS2 comparison and AS3 fault fixtures. Predict failure and ownership transitions before testing; compare rival explanations, reproduce the discrepancy safely, identify a violated invariant and make an evidenced minimal correction or justified bounded refusal. Defend this **new transfer and diagnosis competence**, rather than treating an OR-choice of scenario as a fresh evaluation of every earlier C/Rust, FFI and integrated utility outcome; those remain required under AS1–AS4.
  - **Criteria:** The learner correctly traces the relevant ownership/resource transition under stated Rust/C/library/ABI/OS contracts, selects a test or observation that distinguishes plausible causes and explains the actual failure precondition without assuming predictable results from undefined C. Independent before/after fixtures support a correction where feasible; otherwise a bounded refusal explains why safe resolution is not established. The result protects previously correct behavior, qualifies unobserved risks and distinguishes memory-safety reasoning from availability and security promises. Review demonstrates individual authorship and genuine unfamiliar-case diagnosis rather than a memorized fix. Earlier O2/O5/O9/O10/O12/O14 decisions depend on their own AS1–AS4 evidence and are not auto-awarded by this scenario.
  - **Evidence:** New challenge description/seed, ordered predictions and actual observations, minimal patch or analysis, independent regression outcomes, cause/ownership diagrams, documented reproduction steps, trade-offs and reviewable defense decision.

### Course boundaries, implementation safety and independent access

All fourteen SEF7 outcomes and seven SEF7 assessments remain assessed **in SEF7**; no SEF7 outcome is transferred or automatically awarded by SYS2. SEF6 already assesses C11 pointer/object lifetime and SEF7 covers baseline file descriptors, fork/exec/wait, signals, pipes, and one single-peer loopback service. SYS2 specializes in **Rust from foundations, comparative safety contracts, more complex owned resource graphs and failure-aware multi-child supervision**. SYS10 develops kernel mechanisms; SYS3 develops threads/atomics and concurrent correctness; SYS4 takes responsibility for multi-client services; SYS5 covers data-engine durability rather than assuming File::sync_all proves an entire transaction's crash safety. APP15 remains an optional application interoperability course, not a prerequisite for SYS graduation.

Use only learner-owned, explicitly bounded local processes, fixture paths and test data. Never demand deliberate uncontrolled UB execution, unreviewed `unsafe` implementations, root permissions, public network access or shell commands assembled from untrusted strings. Safe std-thread use for concurrent pipe draining is **taught within this course** and does not presume SYS3. Alternative reviewable text diagrams, state tables or written/recorded defenses must demonstrate identical required reasoning. Simulator/diagnostic reports disclose provenance, tested conditions and limitations.

### Assessment records and readiness

Each decision records the learner's source revision, Rust/C/OS environment, assessed outcomes, independent fixture results, reviewer and resource or ABI limitations. Implemented resource and process behavior must be reproducible. The course remains `draft` until learner testing and qualified review support a status change.

## Optional disciplinary references

All sources are public, support lesson research and are **not** mandatory paid readings or hidden grading requirements:

- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — editions, ownership, structs/enums, traits, generic types, modules and tests.
- [The Rust Reference](https://doc.rust-lang.org/stable/reference/) and [Rustonomicon — FFI](https://doc.rust-lang.org/stable/nomicon/ffi.html) — unsafe/FFI requirements, ABI/unwinding and limits of Rust guarantees.
- [Rust std::process::Child](https://doc.rust-lang.org/stable/std/process/struct.Child.html), [Command](https://doc.rust-lang.org/stable/std/process/struct.Command.html) and [Stdio](https://doc.rust-lang.org/stable/std/process/struct.Stdio.html) — process spawning, wait/reaping and pipe-deadlock concerns.
- [Rust std::os::fd](https://doc.rust-lang.org/stable/std/os/fd/) and [std::os::unix::ffi](https://doc.rust-lang.org/stable/std/os/unix/ffi/) — borrowed/owned descriptors and Unix non-UTF-8 data.
- [Linux man-pages](https://man7.org/linux/man-pages/) — actual Linux/POSIX resource and process behavior.
