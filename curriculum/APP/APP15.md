# APP15 — TypeScript–Rust Application Interoperability

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `elective`
**Prerequisites:** [APP19](APP19.md) — TypeScript Programming, [APP21](APP21.md) — Node.js & Backend Foundations, [APP6](APP6.md) — Software Quality & Engineering Operations
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (provisional; validate with learners)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

**Design, implement, version, verify, distribute and defend a TypeScript-facing application feature powered by a bounded Rust component.** APP15 is an **optional** specialization and is never needed for APP9 or APP core graduation. Its accepted direct APP preparation is **APP19 + APP21 + APP6**, replacing legacy APP2 + APP3 + APP6. APP19 provides TypeScript language competence, APP21 provides the Node process/async foundation, and APP6 provides testing, CI and incident discipline. Backend framework and browser UI knowledge are not mandatory.

**Rust entry readiness, not a second foundation course:** Learners must already demonstrate elementary Rust competence, whether obtained from a future reviewed SYS curriculum or equivalent prior study. The precise SYS course code remains **undecided until SYS is redesigned**; legacy SYS2 must not be claimed as the formal prerequisite. Before starting assessed interop, independently complete this public diagnostic: create a small Cargo-tested CLI that parses a bounded JSON request, uses ownership/borrowing and a useful data structure, returns explicit `Result` errors for invalid input, and produces a documented deterministic response; explain how memory/resource ownership and error propagation work. This checks readiness; it does **not** teach Rust grammar, ownership, lifetimes, C-versus-Rust comparison, compiler internals or the broader SYS concurrency curriculum. Learners who cannot yet pass should acquire those skills separately; the diagnostic is formative and does not replace the seven published APP15 summative assessments.

**Reference implementation:** Choose a small useful application engine (document transformation, deterministic validation, parser, constrained search, or rule evaluation), a strict TypeScript/Node consumer and one local Rust executable. Use a clearly framed, versioned **process IPC** interface first: it is cross-language, auditable, free and does not require unsafe FFI or a specific WebAssembly toolchain. Observe actual stdout/stderr framing, spawn paths, runtime input validation, startup cost, failure, cancellation, resource limits and upgrade behavior. Use the same benchmark fixtures and semantics for a TypeScript-only comparator; the Rust option must earn its maintenance cost.

**Alternatives and limitations:** Native addons through Node-API and WebAssembly are evaluated as advanced boundary choices but are **not** mandated as extra implementations. Node-API ABI stability does not magically guarantee every wrapper or dependent native library is compatible; FFI requires explicit memory ownership and panic/error safety. WebAssembly has host/runtime/memory limits and is not inherently faster. Rust's memory safety is not input validation or application authorization. No paid hosting, unsafe FFI exercise, arbitrary external binary installer, production identity system or native mobile toolchain is required.

Seventeen measurable outcomes are developed across thirteen varied modules and seven public required summative assessments. Authored source remains `draft` pending learner testing and independent academic review.

## Learning outcomes

- **APP15-O1:** Select a TypeScript–Rust boundary only for an evidenced application capability, comparing a TypeScript-only implementation and total maintenance cost.
- **APP15-O2:** Publish a TypeScript-facing package interface with runtime validated inputs/outputs, explicit errors and a stable consumer compatibility policy.
- **APP15-O3:** Model language-neutral request, response and event envelopes with wire/version compatibility, integer, text, time and binary data semantics.
- **APP15-O4:** Integrate a bounded Rust processing component while respecting documented prior ownership, borrowing, Result and Cargo proficiency rather than re-teaching SYS foundations.
- **APP15-O5:** Operate a local child-process/IPC integration with safe spawning, clean shutdown, supervision and bounded stdout, stderr and resource behavior.
- **APP15-O6:** Translate cross-boundary errors, panics, malformed results and uncertain execution into honest typed application states without silent loss or double effects.
- **APP15-O7:** Implement cancellation, explicit deadlines and bounded concurrency/backpressure for async TypeScript-to-Rust work while proving observable behavior.
- **APP15-O8:** Define reliable command identity, replay and idempotency when a boundary may fail after performing an effect but before returning a reply.
- **APP15-O9:** Defend the boundary against malformed payloads, arbitrary code execution, untrusted paths, credential leakage and confused-deputy authorization.
- **APP15-O10:** Build deterministic differential, property-based and adversarial tests that compare Rust and TypeScript behavior against independently justified invariants.
- **APP15-O11:** Evolve package and wire versions with old/new TS and Rust compatibility matrices and safe rollback or forward repair.
- **APP15-O12:** Build and distribute reproducible multi-artifact TypeScript/Rust releases with declared runtime/OS/CPU constraints, integrity and provenance.
- **APP15-O13:** Measure end-to-end workload latency, tail behavior, memory, serialization/copy and startup overhead against a fair TypeScript-only baseline.
- **APP15-O14:** Compare process IPC with native Node-API addons and WebAssembly, correctly analyzing ABI, memory ownership, sandbox and platform limitations without mandatory FFI.
- **APP15-O15:** Observe and recover from worker crashes, corrupt streams, stale version negotiation, lost replies and partial upgrades through privacy-safe traces and runbooks.
- **APP15-O16:** Document security, operating, portability and developer experience trade-offs of the chosen integration with reproducible independent evidence.
- **APP15-O17:** Deliver and defend a complete TypeScript-facing application feature using a bounded Rust component under an unfamiliar interoperability or failure change.

## Modules

### Module 1 — Boundary Need, History and Rust Readiness

#### Outcomes

- APP15-O1
- APP15-O4
- APP15-O14
- APP15-O16
- APP15-O17

#### Lessons

1. **Why mix languages** — Compare scenarios where Rust's native execution, existing library or determinism is worth shipping another runtime.

2. **Historical integration routes** — Trace executable protocols, native shared libraries, WebAssembly and modern Node-API to explain design alternatives.

3. **Prior APP competence** — Locate APP19 type/runtime boundaries, APP21 Node processes and APP6 testing responsibilities without re-teaching fundamentals.

4. **Rust Readiness and Repair Plan** — Compile a small Cargo crate using ownership-aware data, Result errors, JSON decode and unit tests to demonstrate prior readiness; identify missing Rust ownership, borrowing or error skills for study in SYS or equivalent foundations before assessed integration.

5. **Choose a bounded task** — Select a deterministic parser, formatter, document transformer or rule evaluator with meaningful validated inputs.

6. **TypeScript-only comparison** — Build a correct in-process reference implementation to avoid language-fashion justification.

7. **Hazard and cost register** — Identify binary distribution, process startup, copies, security and staff-maintenance costs.

*Optional practice — architecture decision:* Reject unnecessary Rust where measured constraints or existing dependencies do not warrant it.

### Module 2 — TypeScript Package and Runtime Contracts

#### Outcomes

- APP15-O2
- APP15-O3
- APP15-O6
- APP15-O11
- APP15-O16

#### Lessons

1. **Consumer-first API** — Specify one stable TypeScript function and honest promises, cancellation semantics and error variants.

2. **Types are not validators** — Reuse APP19 principles to validate all untrusted native/IPC responses at runtime.

3. **Strict public exports** — Design ESM package exports, declarations and supported runtime entrypoints rather than relying on private paths.

4. **Input normalization** — Publish units, limits, Unicode normalization policy and accepted numeric ranges.

5. **Domain error vocabulary** — Distinguish user-correctable input, transient worker, incompatible protocol and internal faults.

6. **Ownership of mutable results** — Decide which side may mutate buffers and when a result becomes immutable to consumers.

7. **Package semver contracts** — Separate compatible API additions, breaking signatures and wire version changes with examples.

8. **Consumer compatibility probe** — Run a fixture client pinned to previous TypeScript declarations and runtime behavior.

*Optional practice — type illusion:* Show that a casted wire response compiles yet fails contract validation and repair the adapter.

### Module 3 — Rust Processing Component and Isolation

#### Outcomes

- APP15-O1
- APP15-O4
- APP15-O6
- APP15-O9
- APP15-O10

#### Lessons

1. **Rust public operation surface** — Define functions with owned result data and explicit Result conditions at a stable component boundary.

2. **Cargo artifact identity** — Pin Rust toolchain, dependencies, features and target triple for reproducible builds.

3. **Correctness before optimization** — Implement the same deterministic domain rules as the TypeScript reference and publish invariants.

4. **Non-panic input handling** — Validate large, malformed and unknown records without relying on panic as a routine error.

5. **State lifetime design** — Choose request-scoped versus long-lived worker state and document cleanup and reentrancy.

6. **Explicit memory budgets** — Bound per-request allocation, total input size and retained shared state.

7. **Resource effects** — Decide whether the Rust worker may access files or networks and enforce minimum necessary capability.

8. **Diagnostic stack** — Instrument local trace context and structured errors without serializing secrets.

*Optional practice — bad boundary:* Repair a Rust worker that panics on a missing key and loses all pending requests.

### Module 4 — Language-Neutral Data and Versioned Envelopes

#### Outcomes

- APP15-O2
- APP15-O3
- APP15-O6
- APP15-O8
- APP15-O11

#### Lessons

1. **Framing the wire** — Compare newline-delimited JSON, length-delimited messages and message-size boundaries.

2. **Request identity** — Include operation ID, protocol version, correlation key and a bounded payload in every request.

3. **Cross-language integers** — Test signed, unsigned and JavaScript safe-integer limits without silent precision loss.

4. **Unicode and bytes** — Round-trip UTF-8, invalid encoding, byte length and composed text with declared transformations.

5. **Time and precision** — Specify timezone, timestamp precision, monotonic versus wall-clock use and special numeric values.

6. **Null, missing and defaults** — Distinguish omitted fields, explicit null and unknown enum variants in both languages.

7. **Backward-compatible fields** — Add an optional field while exercising older runtime defaults and unknown-field policy.

8. **Version negotiation** — Design explicit feature capability and incompatible version rejection rather than best-effort silent decoding.

9. **Message length abuse** — Reject oversized, truncated, duplicated and malformed frames before allocating unbounded buffers.

*Optional practice — mixed-version replay:* Use an old Rust response with a new TS client and record the versioned failure/result.

### Module 5 — Spawned Process and IPC Lifecycle

#### Outcomes

- APP15-O3
- APP15-O5
- APP15-O6
- APP15-O7
- APP15-O9
- APP15-O15

#### Lessons

1. **Why IPC first** — Choose child-process JSON over FFI for inspectable isolation and manageable cross-platform setup.

2. **Safe process spawning** — Spawn a fixed executable with separate argument vector, no untrusted shell interpolation and controlled working directory.

3. **Channel separation** — Reserve stdout for framed protocol, stderr for sanitized diagnostics and logs.

4. **Handshake and readiness** — Distinguish executable found, process spawned, handshake accepted and worker ready to receive tasks.

5. **Request multiplexing** — Correlate concurrent responses by operation ID and prevent one slow request from blocking all progress.

6. **Crash and exit semantics** — Observe exit code, signal, closed streams and partially written output without fabricating success.

7. **Bounded buffers and pipes** — Limit queued writes, parser frames and unread stderr to prevent deadlock or memory exhaustion.

8. **Supervision policy** — Apply finite restarts, backoff, circuit state and a manual stop switch.

9. **Graceful termination** — Drain or reject outstanding requests with a finite deadline then terminate an unresponsive child.

*Optional practice — crash injection:* Kill the Rust worker during a request and validate the caller's unsettled-versus-failed state.

### Module 6 — Failure Semantics, Cancellation and Replay

#### Outcomes

- APP15-O3
- APP15-O6
- APP15-O7
- APP15-O8
- APP15-O15

#### Lessons

1. **Semantic failure taxonomy** — Model invalid input, Rust domain error, unknown outcome, process failure and incompatible version separately.

2. **Deadlines as contracts** — Pass bounded execution deadlines through TS queue and worker and report observed cancellation.

3. **Abort is not undo** — Show why a client AbortSignal does not reverse already completed Rust or database side effects.

4. **Response-loss window** — Deliberately drop a reply after the worker has completed and explain remaining uncertainty.

5. **Idempotency ownership** — Use stable operation identifiers and durable effect deduplication where any external mutation is allowed.

6. **Retry eligibility** — Retry pure deterministic operations safely and distinguish them from replay-sensitive writes.

7. **Partial results** — Specify whether a batch returns all-or-nothing, per-item errors or a durable committed prefix.

8. **Worker restart recovery** — Reconcile uncertain requests against authoritative state instead of assuming failed means uncommitted.

9. **Propagation into API** — Map boundary failures to stable TypeScript/APP3 user-visible errors without leaking panic internals.

*Optional practice — lost-response incident:* Repair duplicate side effects created by naive timeout-driven resubmission.

### Module 7 — Boundary Security and Untrusted Inputs

#### Outcomes

- APP15-O2
- APP15-O5
- APP15-O6
- APP15-O9
- APP15-O15

#### Lessons

1. **Boundary threat model** — Map caller, executable, IPC transport, filesystem, runtime and application authority for every trust decision.

2. **Execution path safety** — Pin the worker binary path and integrity rather than accepting an arbitrary user-supplied command.

3. **Argument and environment hygiene** — Restrict inherited environment, working directories, PATH and unsafe shell invocation.

4. **Untrusted file references** — Validate path traversal, symlinks and capability boundaries before allowing Rust to open files.

5. **Payload size and cost** — Bound depth, count, numeric range, CPU budget and decompression bombs.

6. **Authorization provenance** — Enforce origin-side principal/object/tenant rules before giving worker a privileged task.

7. **Sensitive diagnostics** — Prevent secrets, private payloads and stacks from entering stdout protocol or persistent logs.

8. **Sandbox limits** — Compare process user/OS permissions and optional stronger isolation without claiming process spawning is a sandbox.

*Optional practice — confused deputy:* Reproduce a malicious document/path request and reject it without weakening the input schema.

### Module 8 — Concurrency, Queues and Resource Backpressure

#### Outcomes

- APP15-O5
- APP15-O6
- APP15-O7
- APP15-O8
- APP15-O13

#### Lessons

1. **Parallelism placement** — Compare Node event loop, worker pool and native worker processes at a controlled concurrency level.

2. **Bounded in-flight operations** — Set queue, worker and per-principal limits and return an intelligible busy outcome.

3. **Cancellation race** — Verify whether a canceled request can still emit a late response and how its ID is discarded.

4. **Reordering and correlation** — Send concurrent tasks with different costs and prevent response mix-ups.

5. **Safe shared state** — Decide where Rust state must be synchronized and test invariant-preserving access patterns.

6. **Streamed results** — Evaluate chunk framing, partial data and backpressure before promising incremental responses.

7. **Queue shutdown behavior** — Drain, reject or preserve pending operations explicitly during restart and upgrade.

8. **Fairness under load** — Prevent a large batch from starving a short request without claiming a global scheduler guarantee.

*Optional practice — queue exhaustion:* Fix a worker API that exhausts memory under simultaneous expensive documents.

### Module 9 — Differential, Property and Contract Testing

#### Outcomes

- APP15-O2
- APP15-O3
- APP15-O4
- APP15-O6
- APP15-O9
- APP15-O10
- APP15-O11

#### Lessons

1. **Shared invariant catalogue** — Write domain laws independent of implementation language for valid/invalid input classes.

2. **Cross-language golden corpus** — Execute identical versioned fixtures against TypeScript and Rust and compare semantic outputs.

3. **Generator design** — Produce boundary cases for lengths, Unicode, integers, ordering and parser ambiguity.

4. **Shrinkable failure** — Reduce a discovered property counterexample into a stable short regression.

5. **Error equivalence** — Compare typed error categories without requiring identical internal exception strings.

6. **Transport fault matrix** — Inject split frames, malformed JSON, process exit, timeout and out-of-order responses.

7. **Version-matrix CI** — Test old/new public package and worker combinations against published compatibility rules.

8. **Negative security tests** — Exercise injected paths, command characters, unauthorized calls and overlarge frames.

9. **Build reproducibility** — Re-run clean dependency/toolchain installs and verify exact artifact hashes or explain nondeterminism.

*Optional practice — independently seeded fault:* Correct a property failure whose original hidden fixture was not in the published test suite.

### Module 10 — Reproducible Builds and Multi-Artifact Delivery

#### Outcomes

- APP15-O2
- APP15-O5
- APP15-O11
- APP15-O12
- APP15-O15
- APP15-O16

#### Lessons

1. **Runtime target matrix** — Declare supported Node versions, OS platforms, CPU architectures, libc and Rust target triples.

2. **Artifact inventory** — Record JS, declarations, worker binary, schema and lockfiles as one compatible release set.

3. **Process bundle location** — Find the packaged Rust executable independent of fragile developer source paths.

4. **Release manifests** — Publish checksums, toolchain versions and protocol compatibility with controlled download/install steps.

5. **Permissions and signing choices** — Distinguish code signing, artifact integrity and authenticated installation without inventing trust.

6. **No arbitrary installer execution** — Avoid privileged postinstall scripts or opaque remote binary fetching as mandatory prerequisites.

7. **Upgrade order** — Model new-client/old-worker and old-client/new-worker before replacing a running binary.

8. **Rollback and migration** — Reject unsafe downgrade when persisted worker data or message contracts cannot be interpreted.

*Optional practice — missing binary incident:* Repair a package that works in source checkout but fails in a clean consuming project.

### Module 11 — Workload Measurement and Design Economics

#### Outcomes

- APP15-O1
- APP15-O7
- APP15-O12
- APP15-O13
- APP15-O14
- APP15-O16

#### Lessons

1. **Hypothesis and baseline** — State the expected gain in a bounded realistic workload and establish a TS-only correct reference.

2. **Correctness equivalence** — Refuse to compare speed until both implementations pass identical domain and security tests.

3. **Cold start and handshake** — Measure worker startup and process readiness cost separately from steady-state compute.

4. **Serialization and copy cost** — Record byte count, frame parse time and transfer overhead rather than assuming zero-copy.

5. **Latency distribution** — Compare median, high percentile and resource use under fixed sample count and concurrency.

6. **Memory and CPU observation** — Report resident process memory, Node event-loop impact and limitations of host monitoring.

7. **Energy and operating cost** — Explain platform and maintenance trade-offs without inventing battery or cloud cost results.

8. **Performance regression contract** — Create a bounded reproducible budget that fails only after correctness checks.

*Optional practice — false speedup:* Diagnose a faster Rust result caused by missing validation or a different input fixture.

### Module 12 — Native Addon, Wasm and Alternative Boundary Review

#### Outcomes

- APP15-O1
- APP15-O3
- APP15-O9
- APP15-O12
- APP15-O13
- APP15-O14
- APP15-O16

#### Lessons

1. **Node-API stability scope** — Explain Node-API ABI guarantees and the limits imposed by wrappers, native dependencies and target packages.

2. **FFI Ownership, Threads and Errors** — Model allocation, free, aliasing, lifetimes and panic translation without requiring learner-written unsafe glue; explain how native add-ons must respect JS runtime affinity and error propagation.

3. **WebAssembly execution model** — Contrast WASM linear memory, host calls, browser and Node support and ecosystem constraints.

4. **WASM copy semantics** — Compare host bridging, memory growth, binary size and async integration overhead.

5. **Process isolation advantage** — Evaluate crash containment and deploy simplicity versus native-call latency and sharing.

6. **Security claims audit** — Explicitly reject claims that Rust memory safety automatically enforces input validity or tenant authorization.

7. **Decision matrix** — Choose process IPC, Node-API or WASM per platform constraints with empirical evidence or bounded analysis.

*Optional practice — adapter comparison:* Sketch an equivalent contract on an alternative boundary and identify new risks without implementing it.

### Module 13 — Integrated Cross-Language Feature and Defense

#### Outcomes

- APP15-O1
- APP15-O2
- APP15-O3
- APP15-O4
- APP15-O5
- APP15-O6
- APP15-O7
- APP15-O8
- APP15-O9
- APP15-O10
- APP15-O11
- APP15-O12
- APP15-O13
- APP15-O14
- APP15-O15
- APP15-O16
- APP15-O17

#### Lessons

1. **Defensible feature brief** — Define one real application behavior, input hazards, user errors and TypeScript-only alternative.

2. **Rust readiness provenance** — Show diagnostic evidence or prior equivalent competence without asking for a new mandatory SYS course code.

3. **Working TS consumer** — Publish an installable typed package and actual application integration, not only a CLI demonstration.

4. **Verified Rust processor** — Execute domain logic under a versioned Cargo toolchain against real adversarial input.

5. **IPC contract** — Trace framed request, version handshake, correlated reply and bounded process lifecycle.

6. **Security and privilege defense** — Reject malicious paths, forged inputs, unknown identity and resource exhaustion attempts.

7. **Cancellation and uncertainty** — Demonstrate process crash, late response, lost reply and correct typed failure or reconciliation.

8. **Compatibility proof** — Run a two-dimensional old/new package-worker matrix and inspect both supported and rejected combinations.

9. **Independent quality evidence** — Present property/differential fuzz regressions, cross-platform build constraints and exact test commands.

10. **Fair performance report** — Compare TS-only, IPC Rust and optional analyzed FFI/WASM cost against identical accepted work.

11. **Recovery and rollback** — Restart, re-provision and roll forward a broken binary with version and resource guardrails.

12. **Unfamiliar technical defense** — Diagnose and correct a reviewer-supplied bounded encoding, protocol, worker, security or performance defect.

## Completion requirements

All **APP15-O1–APP15-O17** require independently inspectable evidence across **seven mandatory summative assessments**. One integrated TypeScript application and Rust engine may support them all. The public Rust-readiness diagnostic supplies feedback before entry; APP15-AS1 separately evaluates application-facing Rust competence. This does not impose a specific SYS course or an additional private exam. Module formative checks are not completion tests; no particular SYS course identifier, native FFI, WASM build, paid service or web framework is required.

- **APP15-AS1** — Prior Readiness, Bounded Use Case and Public TypeScript Package
  - **Outcomes:** APP15-O1, APP15-O2, APP15-O4, APP15-O16.
  - **Work:** Demonstrate independent Rust readiness, define an application problem and publish strict TypeScript API declarations, validation, supported errors and TS-only comparator.
  - **Criteria:** Cargo fixture compiles/tests with ownership-aware code and Result error paths; TypeScript consumer rejects forged and invalid runtime inputs; Rust is justified by evidence or specialized capability, not a universal performance slogan.
  - **Evidence:** Readiness diagnostic source and test results, package exports and contracts, domain requirements, TS reference, rationale and declared environment.

- **APP15-AS2** — Versioned Rust Component and Lossless Wire Contract
  - **Outcomes:** APP15-O2, APP15-O3, APP15-O4, APP15-O6, APP15-O11.
  - **Work:** Implement a Rust component and a framed versioned IPC exchange that represents valid/invalid texts, integers, times, nulls and message limits.
  - **Criteria:** Identical semantic output on TS/Rust fixtures; malformed or incompatible input is rejected with typed error; unsafe lossy conversions and unbounded frames are absent; old/new compatibility is explicit.
  - **Evidence:** Pinned Rust/TS source and schemas, version matrix, golden and adversarial frames, observed subprocess trace, rejected cases and protocol decisions.

- **APP15-AS3** — Supervised Process, Uncertain Effects and Bounded Concurrency
  - **Outcomes:** APP15-O5, APP15-O6, APP15-O7, APP15-O8, APP15-O15.
  - **Work:** Integrate a supervised Rust child process through a Node/TS API, inject crash, split reply, cancellation, concurrent requests, exhaustion and unknown committed outcome.
  - **Criteria:** Fixed executable spawn without shell injection; no unbounded queues/pipes; deadlines, exit status, late replies and retry semantics are observable; replay-sensitive effects are not doubled under uncertain replies.
  - **Evidence:** Startup/shutdown traces, timed injected faults, queue metrics, idempotency/authority logs, code, tests, explicit error and restart-state matrix.

- **APP15-AS4** — Security, Differential and Property Verification
  - **Outcomes:** APP15-O2, APP15-O3, APP15-O4, APP15-O9, APP15-O10, APP15-O15.
  - **Work:** Produce an independently justified invariant suite and malformed/adversarial corpus across the TS/Rust boundary, including attacker-controlled paths and privilege requests.
  - **Criteria:** Run matched inputs through both implementations; preserve authorized task boundaries; show reproducible shrinking/regression or seeded repair; keep secrets and user data out of diagnostic output.
  - **Evidence:** Property generators/corpus, fixture hashes, negative authorization tests, signed-off threat matrix, sanitized logs, failure diff and reproducibility instructions.

- **APP15-AS5** — Multi-Artifact Versioned Distribution and Upgrade Defense
  - **Outcomes:** APP15-O2, APP15-O5, APP15-O11, APP15-O12, APP15-O15, APP15-O16.
  - **Work:** Package a typed JS library with a compatible Rust binary, run clean consumer installs and stage old/new package-worker upgrades and rollback/failure recovery.
  - **Criteria:** Independent installation works with declared supported runtime and OS; incompatible pairs reject deliberately; no hidden privileged postinstall; artifact hashes and compatibility behavior are inspectable.
  - **Evidence:** Lockfiles/toolchain, binary and package manifests, clean checkout/consumer transcript, old/new matrix, failed install/repair traces and operator notes.

- **APP15-AS6** — Fair Performance and Alternate-Mechanism Decision
  - **Outcomes:** APP15-O1, APP15-O7, APP15-O12, APP15-O13, APP15-O14, APP15-O16.
  - **Work:** Benchmark TS-only versus actual Rust IPC under same validated workload; review Node-API and WASM as genuine alternatives without requiring native FFI implementation.
  - **Criteria:** Correctness equivalence precedes timing; report startup, serialization, p50/tail, memory and uncertainty with consistent sample controls; defend whether complexity is justified.
  - **Evidence:** Input corpus, workload settings, measurement CSV/traces, system constraints, alternatives matrix, build/deploy cost model and decision with limitations.

- **APP15-AS7** — Integrated Typed Application and Independent Unfamiliar Interoperability Defense
  - **Outcomes:** APP15-O1, APP15-O2, APP15-O3, APP15-O4, APP15-O5, APP15-O6, APP15-O7, APP15-O8, APP15-O9, APP15-O10, APP15-O11, APP15-O12, APP15-O13, APP15-O14, APP15-O15, APP15-O16, APP15-O17.
  - **Work:** Rebuild and demonstrate an application feature using a versioned supervised Rust component; independently resolve an unfamiliar bounded protocol, compatibility, security, crash or measurement defect.
  - **Criteria:** Clean installation works; failure and attack tests are observable; state/cancellation/replay claims are honest; full version and performance evidence supports chosen boundary; defend source decisions and remaining risk.
  - **Evidence:** Complete source and artifacts, schema/golden corpus, clean TS consumer, runnable Rust binary, test/upgrade/fault traces, comparative measurements, review change and technical defense.

### Shared academic and interoperability boundaries

- **Preparation ownership:** APP19 and APP21 are used, not re-taught. Prior Rust competence may come from future SYS or documented equivalent study. Do not prescribe SYS2 or require APP2/APP3/APP20 as hidden prerequisites. The public diagnostic discloses expected Rust knowledge, not an additional course-wide assessment gate.
- **Real boundaries:** A TypeScript wrapper that merely prints a string or a Rust-only CLI without a consuming application is insufficient. Required work has versioned executable exchange, runtime-validated cross-language contracts, actionable failures, reproducible software tests and defended reason to keep both implementations.
- **Process IPC reference:** Use fixed executable paths, controlled argv/environment, explicit message framing, size and concurrency bounds, correct stdout versus stderr roles, correlation IDs, trustworthy errors, clean shutdown and meaningful crash/restart behavior. A retry after uncertain side effects is not necessarily safe.
- **Versions and distribution:** Publish exact toolchain, Cargo/Node dependency locks, target support, binary/build hashes and paired package-worker compatibility. Verify independent clean-state consumption and at least one intentional incompatible or interrupted upgrade. Do not claim automatic binary portability.
- **Security and privacy:** Apply real runtime checks and client/service authorization outside the Rust worker as appropriate, reject untrusted commands and paths, protect sensitive payloads and use synthetic local data. Memory safety does not imply policy or protocol correctness.
- **Measurement integrity:** Compare identical accepted work, controlled warmup, sample counts and resource budgets; include cold start and serialization overhead. Account for uncertainty; do not infer global app speed or battery advantage from local microbenchmarks.
- **Independent defense:** An unfamiliar bounded failure must be reproduced and explained, with a corrected implementation or defensible containment, regression evidence, operator guidance, limitations and a technical retrospective.
