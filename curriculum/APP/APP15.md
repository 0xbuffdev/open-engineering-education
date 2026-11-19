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

**Design, implement, version, verify, distribute and defend a TypeScript-facing application feature powered by a bounded Rust component.** APP15 is an **optional** specialization and is never needed for APP9 or APP core graduation. Its direct prerequisites are **APP19 + APP21 + APP6**. APP19 provides TypeScript language competence, APP21 provides the Node process/async foundation, and APP6 provides testing, CI and incident discipline. Backend framework and browser UI knowledge are not mandatory.

**Rust entry readiness, not a second foundation course:** Learners must already demonstrate elementary Rust competence, whether obtained from [SYS2](../SYS/SYS2.md), which now formally teaches the SYS Rust foundation, or equivalent prior study. **SYS2 is an available preparation path, not an APP15 formal prerequisite**; APP19 + APP21 + APP6 remain its direct prerequisites. Use this **formative**, free self-check before assessed interop: build a Cargo-tested bounded JSON CLI with owned/borrowed data, a useful collection, explicit `Result` validation and deterministic output, then explain resource ownership. This supplies preparation feedback, **not an additional required course, a secret admission gate or an eighth assessment**. In APP15-AS1 the learner demonstrates independently assessable application-facing Rust competence through the actual Rust engine. Learners without the needed foundation may study SYS2 or equivalent Rust sources; APP15 does **not** re-teach ownership, lifetimes, C/Rust comparison or SYS process supervision.

**Reference implementation:** Choose a small useful application engine (document transformation, deterministic validation, parser, constrained search, or rule evaluation), a strict TypeScript/Node consumer and one local Rust executable. Use a clearly framed, versioned **process IPC** interface first: it is cross-language, auditable, free and does not require unsafe FFI or a specific WebAssembly toolchain. Observe actual stdout/stderr framing, spawn paths, runtime input validation, startup cost, failure, cancellation, resource limits and upgrade behavior. Use the same benchmark fixtures and semantics for a TypeScript-only comparator; the Rust option must earn its maintenance cost.

**Alternatives and limitations:** Native addons through Node-API and WebAssembly are evaluated as advanced boundary choices but are **not** mandated as extra implementations. Node-API ABI stability does not magically guarantee every wrapper or dependent native library is compatible; FFI requires explicit memory ownership and panic/error safety. WebAssembly has host/runtime/memory limits and is not inherently faster. Rust's memory safety is not input validation or application authorization. No paid hosting, unsafe FFI exercise, arbitrary external binary installer, production identity system or native mobile toolchain is required.

**Instructional sufficiency:** Seventeen outcomes require thirteen conceptually distinct mechanisms and seven independently decidable summative assessments. Every new language-boundary mechanism needs a correct model, actual frame/OS or typed example, a specific counterexample, independently observable failure and repair feedback **before** final defense. A Rust-only CLI or TypeScript declaration without a consuming process is insufficient. The reference deterministic worker is **pure and safe to recompute after response loss**, but cancel/kill is not undo and a genuinely effectful worker requires a separate **durable** idempotency/authority strategy. This difference is explicitly assessed, without imposing an APP3 database prerequisite. Lesson compression is not evidence of shorter learning or proof of mastery; source remains `draft`.

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

1. **What cross-language components can actually improve** — Trace historical process APIs, native libraries and WebAssembly against a real TS application demand; distinguish a useful existing Rust library or isolated CPU task from fashion-driven 'Rust is faster' claims.

2. **Evolution of process, native ABI and Wasm boundaries** — Compare subprocess framing, native Node-API and Wasm host boundaries by isolation, ABI and deployability, using one falsifiable input/output example.

3. **Public Rust readiness diagnostic, not extra course gate** — Compile and test a bounded Cargo JSON CLI using ownership, borrowing and Result, explain failures and identify SYS2/equivalent learning if necessary; diagnostic is formative, while AS1 judges application-facing Rust competence.

4. **One meaningful deterministic application feature** — Choose a bounded parser/validator/transform/rule engine with explicit input limits, expected failure and useful application consumer; no backend framework is required.

5. **Same-rule TS baseline and rejected complexity hypothesis** — Build an actual functionally equivalent TypeScript reference, document likely CPU/copy/startup trade-off and specify evidence that would favor keeping TS alone.

*Optional practice — architecture decision:* Reject unnecessary Rust where measured constraints or existing dependencies do not warrant it.

### Module 2 — TypeScript Package and Runtime Contracts

#### Outcomes

- APP15-O2
- APP15-O3
- APP15-O6
- APP15-O11
- APP15-O16

#### Lessons

1. **Typed package interface with explicit lifecycle contract** — Design an installable TS API with stable success/error union, AbortSignal semantics, deadlines and an honest distinction between canceled waiting and actual worker effects.

2. **Real runtime parsing over static casts** — Use APP19 knowledge to reject malformed worker JSON, unknown enum, out-of-range number or forged success even when the declared TypeScript type compiles.

3. **Public ESM exports and clean consumer** — Publish TS declarations/entrypoints and test a separate clean npm consumer, including a rejected internal/private path and a missing packaged executable.

4. **Cross-boundary units, text and precision policy** — Define exact Unicode normalization choice, byte length, decimal/counter representation, accepted integers and invalid input behavior before implementing Rust and TypeScript.

5. **Domain, transport, panic and uncertain-effect error categories** — Separate invalid request, worker domain error, malformed response, protocol mismatch, process termination and unknown completion; a Rust panic is **not** an ordinary Result and may abort or terminate the process.

6. **Owned buffers, mutation and serialization timing** — Specify TS and Rust ownership of inputs/results, distinguish clone/copy from transfer and verify no caller mutation or retained alias violates actual contract.

7. **Package API semver versus worker wire schema** — Compare compatible TS signature and semver, backward/forward wire fields and unsupported worker capabilities without assuming release versions evolve in lockstep.

8. **Actual previous consumer contract check** — Run previously pinned TS consumer against new package build and a documented invalid response, inspecting compile, runtime and error behavior separately.

*Optional practice — type illusion:* Show that a casted wire response compiles yet fails contract validation and repair the adapter.

### Module 3 — Rust Processing Component and Isolation

#### Outcomes

- APP15-O1
- APP15-O4
- APP15-O6
- APP15-O9
- APP15-O10

#### Lessons

1. **Rust Result boundary and owned output** — Use established SYS2-equivalent Rust knowledge to expose bounded deterministic operation and owned data, distinguishing recoverable validation from an intentional process termination.

2. **Cargo lock/toolchain and target identity** — Pin compiler release/edition/target, Cargo.lock and dependency features and demonstrate `cargo build --locked` rather than equating a lockfile with bit-for-bit identical build artifacts.

3. **Independent invariants before Rust speed claims** — Implement same semantics as TS with independently reasoned valid/invalid examples, then test meaningful equality rather than optimize an easier Rust problem.

4. **Malformed input, panic strategy and no false recovery** — Trigger malformed payload and explicit Rust Result; separately demonstrate controlled panic behavior in a disposable worker, explaining unwind/abort profiles and no guaranteed structured reply.

5. **Per-request state, global caches and restart** — Choose stateless operation or controlled long-lived state, reproduce wrong-request stale result after worker reuse and show clean restart/retention behavior.

6. **Bytes, allocation and CPU work ceilings** — Bound input/frame bytes, decode depth and CPU budget under a generated large fixture, acknowledging timeouts and kills are not guaranteed to undo effects.

7. **Worker filesystem/network capabilities and no sandbox illusion** — Use file-free deterministic operation by default or explicitly scoped native file access; show why a spawned executable inherits OS permissions and requires deliberate confinement.

8. **Sanitized diagnostics separate from wire protocol** — Use stderr for bounded redacted traces and stdout only for frames; include an intentionally noisy stderr case and a test where log pollution breaks parsing.

*Optional practice — bad boundary:* Repair a Rust worker that panics on a missing key and loses all pending requests.

### Module 4 — Language-Neutral Data and Versioned Envelopes

#### Outcomes

- APP15-O2
- APP15-O3
- APP15-O6
- APP15-O8
- APP15-O11

#### Lessons

1. **One exact framed protocol over byte streams** — Choose NDJSON or length-prefix with parser state, maximum byte length and partial UTF-8/frame behavior; prove one write/read chunk is not guaranteed to equal one message.

2. **Stable operation ID, version and evidence scope** — Define correlation ID, negotiated protocol/feature version, bounded payload and legitimate operation owner without accepting an untrusted claimed user as authorization.

3. **JS safe integer and Rust i64/u64 boundaries** — Round-trip 2^53-1, 2^53+1, negatives and u64 overflow; encode larger exact integers as validated decimal strings or use a deliberately specified alternative, not a lossy JS Number.

4. **UTF-8, embedded newline and Unicode normalization** — Exercise multiline text framed safely, invalid UTF-8, combining marks and byte/codepoint length using explicitly pinned transformations, not implicit TS/Rust string equivalence.

5. **Timestamp, decimal and nonfinite encoding rules** — Define UTC and precision, wall versus monotonic clocks, decimals and NaN/Infinity rejection; confirm JSON cannot express every host-language number/date unchanged.

6. **Absent versus null and unknown enums** — Test versioned omitted/null/default fields with old/new decoders, preserving meaning of unknown enum tags rather than silently converting them to success.

7. **Safe additive wire schema with old worker** — Add one field and test old Rust reader/new TS client for explicit ignored/unsupported/default rules; avoid calling arbitrary shape-compatible payload semantically compatible.

8. **Handshake and feature capability negotiation** — Test a true supported pair and an unsupported worker version/feature before sending work, with fail-closed typed error rather than guessing a fallback decoder.

9. **Partial/truncated/overlong frame and parser recovery** — Feed split JSON, duplicate IDs, length mismatch and oversized payload with bounded memory and explicit close/resync; ensure parser cannot consume stderr as protocol bytes.

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

1. **Safe fixed binary and shell-free spawning** — Use Node child_process.spawn/execFile with a fixed packaged binary, controlled argv/cwd/env and `shell: false`, explaining OS platform/path resolution and why avoiding shell alone doesn't ensure trusted code.

2. **stdout protocol and drained bounded stderr** — Continuously consume stdout frames and sanitized stderr with explicit caps; demonstrate the deadlock/memory risk of an unread child pipe.

3. **Spawn success, handshake, ready and exit distinctions** — Independently test missing binary, spawned-not-ready child, protocol mismatch and genuinely ready worker; never report the user task complete merely because PID exists.

4. **Response mapping under interleaved requests** — Run unequal-cost concurrent jobs and correlate reply IDs; exercise duplicate/unknown/late response and ensure a single bad frame cannot satisfy a different request.

5. **Crash, panic-abort, EOF and half-frame ambiguity** — Kill or cause controlled Rust panic, inspect close/exit/code/partial frame and pending request state; distinguish guaranteed no response from unknown operation completion.

6. **Node writable backpressure and stream bounds** — Respect `stdin.write() === false` and the subsequent drain, bound pending frames and both stdout/stderr reading, and demonstrate a slow child without accumulating unbounded memory.

7. **Finite restart, ready probe and circuit policy** — Apply safe bounded restart/backoff and saturation refusal after crashes while checking package compatibility and not automatically repeating effectful requests.

8. **Graceful child shutdown and escalation limits** — Drain or explicitly reject pending operations, request cooperative shutdown then time-bounded terminate/reap; acknowledge kill/AbortSignal is not a universal guarantee of immediate child exit.

*Optional practice — crash injection:* Kill the Rust worker during a request and validate the caller's unsettled-versus-failed state.

### Module 6 — Failure Semantics, Cancellation and Replay

#### Outcomes

- APP15-O3
- APP15-O6
- APP15-O7
- APP15-O8
- APP15-O15

#### Lessons

1. **Recoverable input, crash and uncertain outcome taxonomy** — Trace a normal Rust Result error, invalid protocol frame, panic/EOF, timeout and lost reply as different TS states with user/action meaning.

2. **End-to-end deadline through queue and process** — Allocate queuing, startup, work and response deadlines; test timeout while worker remains executing and show truthful cancellation acknowledgment separately.

3. **AbortSignal stops waiting, not committed work** — Cancel a controlled operation after worker start, inspect late frame and any effect; never infer Rust stopped or external effects rolled back because TS promise rejected.

4. **Lost reply after actual completed pure computation** — Drop response after the Rust deterministic engine produced result; classify outcome as unknown to caller, then show safe recomputation only because the chosen task has no external effect.

5. **Effectful alternative requires durable idempotency owner** — Use a tiny optional durable local side-effect fixture or selected genuine effect to contrast pure recomputation with an already committed write; ensure stable ID plus durable dedup **with** effect at its authority before claiming retry safety. No APP3 database course is required.

6. **Retry only operations with proven replay safety** — Compare a pure deterministic retry, a rejected ambiguous effect and correctly reconciled idempotent effect, avoiding infinite restarts and replays.

7. **Batch partial success, accounting and no double claim** — Specify atomic/prefix/item result semantics in a reproducible fixture and demonstrate a failed third item cannot be silently reported as full success.

8. **Recovery after worker exit versus authoritative effects** — Restart a process with pending requests, checking clear pure replay, externally committed state if supported, and no invented durable work from in-memory worker state.

9. **Stable TS error/unknown-state presentation** — Map panic, malformed result, timeout, compatibility and known domain error to public tagged union and safe logging without claiming APP3 HTTP framework is mandatory.

*Optional practice — lost-response incident:* Repair duplicate side effects created by naive timeout-driven resubmission.

### Module 7 — Boundary Security and Untrusted Inputs

#### Outcomes

- APP15-O2
- APP15-O5
- APP15-O6
- APP15-O9
- APP15-O15

#### Lessons

1. **Threat and authority across executable and IPC** — Map caller, package installer, binary path, argv, env, filesystem, data frames, process permissions and any external effects; a Rust worker isn't trusted solely for being memory safe.

2. **Executable path, hash and loader uncertainty** — Resolve package-contained binary rather than cwd/PATH arbitrary user input; validate known artifact digest and target before spawn while stating artifact integrity is not proof of publisher identity.

3. **Shell, environment and secret inheritance** — Test dangerous user input passed as shell interpolation versus fixed argv, trim environment and prevent credentials from entering child logs or untrusted PATH.

4. **Untrusted paths and TOCTOU/symlink issues** — Reject absolute/traversal/symlink tricks for a bounded optional file capability; prefer passing validated content bytes to a file-free worker where applicable.

5. **Allocation and CPU exhaustion across framed data** — Bound parser depth/size, nested records, decompression and execution time, and show a CPU-killed worker does not imply canceled external side effects.

6. **Caller identity cannot grant worker or origin permissions** — If the application uses protected data, establish actual parent-side action/object/property/tenant policy and restrict worker OS capabilities; do not trust a message userId string.

7. **No credentials or sensitive data in diagnostics** — Inspect stderr, stdout protocol, crash stack, traces and saved fixtures for token/private payload leaks, keeping sanitized bounded correlation.

8. **Process isolation versus actual OS sandbox** — Demonstrate that child process by default shares user-level file/network permissions, compare optional UID/container/OS isolation and reject absolute sandbox guarantees.

*Optional practice — confused deputy:* Reproduce a malicious document/path request and reject it without weakening the input schema.

### Module 8 — Concurrency, Queues and Resource Backpressure

#### Outcomes

- APP15-O5
- APP15-O6
- APP15-O7
- APP15-O8
- APP15-O13

#### Lessons

1. **Node event-loop work versus supervised native workers** — Measure actual same-task responsiveness using JS synchronous computation, worker pool and Rust child, controlling task/serialization cost before adding concurrency.

2. **Bounded queue and per-client fairness** — Set finite request, byte and worker in-flight caps, test overflow refusal and two clients with different costs without leaving stuck promises.

3. **Canceling queued versus in-flight work** — Cancel one request before send and another after execution starts, discard its late response ID and prove no accidental new user or effect state.

4. **Out-of-order completion and request correlation** — Interleave slow/fast operations, duplicate/unknown IDs and restart to demonstrate correct owner matching without FIFO completion assumptions.

5. **Rust shared-state data race and isolation scope** — Assess whether long-running process actually retains mutable state, apply safe synchronization or no shared state and test invariant under multiple requests.

6. **Streaming and chunk/flush semantics only when useful** — Compare complete response with bounded framed chunks and explicit partial-result status; don't add streaming API unless a demonstrated user task benefits.

7. **Shutdown/restart queue and visibility** — Exercise controlled upgrade while work is queued and running; decide drain/reject/reconcile with actual packet/child results and no silently lost accepted effects.

8. **Large task versus short-task scheduling fairness** — Vary workload and enqueue order, report short-request tail/queue age and implement a justified bounded concurrency or scheduling change, not a global fairness guarantee.

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

1. **Independent domain invariants before cross-language output** — Define correct parser/validation properties and negative classes without letting shared TS/Rust implementation bugs become the only oracle.

2. **Same semantic corpus, independent implementations** — Run pinned valid, invalid and edge fixtures against TS reference and real Cargo executable, comparing normalized output/error category rather than incidental stack strings.

3. **Properties for precision, Unicode, schema and framing** — Generate 2^53± and u64 bounds, malformed UTF-8/JSON, duplicate IDs, nullable fields and version incompatibility with controlled seeds.

4. **Shrink and preserve a real counterexample** — Introduce or discover a genuine TS/Rust disagreement, minimize failing data and keep a reproducible regression, explaining why a green property run alone isn't proof of no defects.

5. **Error equivalence without matching implementation traces** — Compare stable public error/unknown semantics on malformed payload, Rust Result and process exit rather than requiring identical exception wording.

6. **Actual partial pipe, EOF, crash and late-reply cases** — Test split/truncated framing, unknown operation ID, child termination mid-response, abort and restart through the actual TS process adapter.

7. **True old/new package and worker matrix** — Run independently pinned v1/v2 TS package and worker pairs with supported and incompatible schema/feature cases, recording why one pair is rejected.

8. **Negative executable, file and authority cases** — Use inert shell metacharacters, disallowed binary paths, forged owner and oversized requests; inspect no unauthorized file or effect occurs.

9. **Clean release reproducibility and limits** — Build from pinned locks and toolchains on a supported target, compare hashes under controlled environment and explain nondeterministic build paths rather than assert every rebuild byte-identical.

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

1. **Declared supported single target plus portability matrix** — Pin actual Node/OS/CPU/libc/ABI/Rust target for at least one accessible local platform, and declare other **supported only if tested** versus hypothetical builds.

2. **Complete JS+types+binary+schema release identity** — Inventory exact JS package, declaration, Rust worker, wire schema, locks, checksums and compatible feature range as one independently usable installation.

3. **Package-relative executable resolution** — Launch the packaged worker from a clean consumer working directory distinct from source repo, verifying the selected executable matches the declared target and digest.

4. **Locked build, digest, provenance and trust distinction** — Run `cargo build --locked` and pinned JS build, record inputs/target/hashes; explain lock reproducibility versus byte reproducibility, artifact digest versus authenticated publisher.

5. **Test signer, hashes and what each proves** — Compare optional signing/trust roots, checksums and provenance with a deliberately swapped worker, refusing to describe a hash alone as a trusted identity.

6. **No privileged postinstall or opaque binary fetch** — Package the locally built binary or provide a transparent controlled installer alternative with no automatic arbitrary elevated download, and verify disconnected consumer instructions.

7. **Rolling old/new JS consumer and Rust worker matrix** — Install/stage v1/v2 cross-combinations, validate handshake/capabilities, prevent partial upgrade from silently applying incompatible protocol.

8. **Rollback after changed persisted worker contract** — Inject a missing/wrong binary or new protocol upgrade, repair safely and distinguish reinstalling pure stateless worker from a non-reversible external effect or persisted data change.

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

1. **User-task performance hypothesis with TS comparator** — Specify actual accepted task and cost expectation, including reasonable no-Rust outcome; use identical domain/validation work for Rust and TS paths.

2. **Correct work and error populations first** — Run property/differential/negative tests before timing and reject results where Rust skips input validation, errors, or outputs less data.

3. **Cold spawn, handshake and worker reuse** — Measure launch/readiness/handshake separately from warm process and batching, showing where startup cost dominates a short single call.

4. **Byte/frame copies and decode/encode overhead** — Measure IPC transfer, framing and parsing for realistic sizes, comparing total app task versus compute-only time rather than presume zero-copy native speed.

5. **p50/p95, error denominator and sample variation** — Run warmup, repeated matched valid/invalid work and concurrency, report sample count, tail, timeouts and distribution of complete user-visible results.

6. **Combined Node and Rust memory/CPU, generator limits** — Record parent event-loop delay and child RSS/CPU alongside request bytes and generator saturation, not only Rust core throughput.

7. **Energy, target distribution and developer cost caveats** — Use measured CPU/bytes as limited proxies; discuss team skills, binary packaging/maintenance and no fabricated battery/host provider savings.

8. **Reproducible regression threshold with right oracle** — Make a bounded budget that fails a meaningful seeded performance regression only after correctness/security tests, including tolerated lab noise.

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

1. **Node-API ABI stability is conditional** — Compare stable Node-API version support to wrapper/third-party native ABI, Rust target/libc/toolchain constraints; don't assume every N-API wrapper is cross-platform.

2. **FFI memory, threads, panic and JS runtime affinity** — Analyze owned allocation/free, pointer lifetime, asynchronous callback/thread restrictions and a Rust panic potentially unwinding/aborting; no unsafe FFI implementation required.

3. **Wasm linear memory, runtime imports and host access** — Map Rust→Wasm values/copies and host import permissions with Node/browser environment constraints, without claiming universal sandbox security or speed.

4. **Wasm startup, memory growth and copying** — Compare one bounded in-memory transfer and module instantiation cost conceptually using documented interfaces or an optional free fixture.

5. **Process IPC isolation, latency and operational load** — Assess crash containment, upfront serialization and additional process supervision versus native addon’s same-process fault boundary.

6. **Rust/FFI/Wasm safety limits and current server rights** — Show why Rust's memory safety, Node-API stability and Wasm linear memory do not validate untrusted input or current application authorization.

7. **Evidence-based IPC, addon or Wasm choice** — Defend selected boundary with actual IPC measurements, supported target and well-labeled alternatives, allowing no added native runtime when TypeScript is adequate.

*Optional practice — adapter comparison:* Sketch an equivalent contract on an alternative boundary and identify new risks without implementing it.

### Module 13 — One Cross-Language Application and Independent Transfer Defense

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

1. **One working app and previously accepted assessed evidence** — Reuse one running TypeScript consumer and Rust engine, cite **separately accepted APP15-AS1–AS6 judgments** by source/fixture/release and avoid rebuilding six different application projects.

2. **Prove actual package, IPC correctness and honest failure** — Clean install on one declared supported OS/CPU and inspect framed version handshake, TypeScript validation, Rust Result/panic/exit, bounded pipes, actual TS-only comparator and one real late-reply failure.

3. **Recheck security, version skew, fairness and replay** — Exercise selected accepted malicious paths, concurrent result IDs, 2^53 integer representation, unsupported old/new worker pair, saturation and pure versus effectful lost-response semantics.

4. **Assessor supplies an unforeseen bounded interoperability fault** — Investigate a genuinely new malformed length/UTF-8, panic/EOF, wrong binary, prior user context, late response, version mismatch or backpressure issue with an independently observed failing-before client/process oracle.

5. **Causal patch and targeted repeatable regression** — Fix or safely contain the new issue, show clean before/after TS/Rust behavior and rerun the necessary previously accepted property, security, compatibility, resource and measurement tests.

6. **Defend personally owned mechanism and useful alternative** — Explain actual source and reused code/AI assistance, why Rust or plain TS was appropriate, Node-API/Wasm nonrequired trade-offs, versions/platform costs, no fabricated benchmarks and accessible technical review.

## Completion requirements

All **APP15-O1–APP15-O17** require **seven independently decidable required assessments** on one real TypeScript consumer and Rust child-process engine: AS1 actual application-facing Rust/TS competence; AS2 exact versioned framing; AS3 supervised bounded process and **pure-vs-effectful replay decision**; AS4 independent differential/property/security; AS5 independently installed multi-artifact release; AS6 matched TS-versus-Rust performance; AS7 **unfamiliar bounded defect** with personal technical defense. The publicly described Rust-readiness self-check is formative; **AS1 assesses Rust through the actual feature**, not an additional hidden course or standalone private pass. Previously accepted AS1–AS6 can be linked rather than submitted as six new projects; AS7 cannot waive any failed earlier decision. SYS2 and FFI/Wasm/builds for unowned OS targets are **not** compulsory; elective APP15 never affects APP9 graduation.

- **APP15-AS1** — Prior Readiness, Bounded Use Case and Public TypeScript Package
  - **Outcomes:** APP15-O1, APP15-O2, APP15-O4, APP15-O16.
  - **Work:** On the actual APP19/APP21/APP6-prepared application, define a bounded user-visible parser/validation/transformation feature and a correct TypeScript-only reference, then independently compile and test a **real Rust Cargo engine** with owned/borrowed data, explicit Result/domain errors, reproducible input limits, and a typed publicly exported TS package with actual runtime validation. The suggested separate rust-readiness diagnostic may guide or contribute supporting evidence but is **not an independent assessed admission checkpoint**. Show why a Rust process is useful or when TS alone would have sufficed.
  - **Criteria:** A clean local reviewer runs a real TypeScript consumer and meaningful bounded Rust operation with compiled/tested Rust and correctly checked untrusted input; type casts, a Rust-only CLI or an unexplained pasted project cannot pass. Rust ownership/error competence is demonstrated **in the actual application feature**, not by an extra private exam, mandatory SYS2 enrollment or a duplicate required preparatory utility. Validity, scope, source/AI reuse and justified alternative are independently explainable.
  - **Evidence:** Readiness diagnostic source and test results, package exports and contracts, domain requirements, TS reference, rationale and declared environment.

- **APP15-AS2** — Versioned Rust Component and Lossless Wire Contract
  - **Outcomes:** APP15-O2, APP15-O3, APP15-O4, APP15-O6, APP15-O11.
  - **Work:** Run actual versioned framed TypeScript ↔ Rust stdin/stdout on a known executable, including handshake/capability check, partial and concatenated frames, overflow/invalid UTF-8, an explicit JS `Number.MAX_SAFE_INTEGER` boundary and out-of-range Rust integer, UTC/precision, null/omitted/unknown enum, differing text normalization and an additive older/newer envelope. Preserve correlation ID and separately captured sanitized stderr.
  - **Criteria:** Real process bytes and typed decoded results conform to published max-frame and semantic/wire contracts under adversarial splitting, truncation and inconsistent old/new capabilities. A valid `u64` or timestamp never silently converts to a rounded JS Number or unsupported JSON NaN; use a documented exact textual encoding as appropriate. Unsupported combinations fail closed without fabricated partial success, unbounded allocation, log-injected stdout or conflated version/ABI promises.
  - **Evidence:** Pinned Rust/TS source and schemas, version matrix, golden and adversarial frames, observed subprocess trace, rejected cases and protocol decisions.

- **APP15-AS3** — Supervised Process, Uncertain Effects and Bounded Concurrency
  - **Outcomes:** APP15-O5, APP15-O6, APP15-O7, APP15-O8, APP15-O15.
  - **Work:** Integrate an actual fixed packaged Rust child from Node/TS with safe argv/cwd/env, separate bounded stdout/stderr draining, partial-frame parsing, handshake, at least two interleaved request IDs, finite writable/in-flight byte capacity and controlled restart/termination. Inject **actual worker panic/EOF**, slow pipe, AbortSignal and time budget expiry, and **drop a completed reply**. For the default **pure deterministic operation**, show legitimate recomputation/late reply suppression; additionally analyze or exercise a small labeled local side-effect fixture/real chosen effect to demonstrate **why naive replay would duplicate** and how a durable effect/idempotency owner or explicit reconciliation would be necessary.
  - **Criteria:** A fresh reviewer observes real child process/pipe behavior and no leaked shell execution, deadlocked stderr or unbounded queues; `stdin.write()` backpressure, partial data, unknown/late IDs and cancellation/kill limitations have independent tests. A Rust `Result` error and process-terminating panic lead to distinct honest typed outcomes. Lost **pure** responses can be recomputed because no effect happened; effectful retry is **not** falsely called safe without atomic durable dedup/authority proof. No extra APP3/database product, permanent mutation feature or platform-specific process scheduler is mandated.
  - **Evidence:** Startup/shutdown traces, timed injected faults, queue metrics, idempotency/authority logs, code, tests, explicit error and restart-state matrix.

- **APP15-AS4** — Security, Differential and Property Verification
  - **Outcomes:** APP15-O2, APP15-O3, APP15-O4, APP15-O9, APP15-O10, APP15-O15.
  - **Work:** Derive independent domain invariants for the actual TS/Rust feature, run valid/malformed/oversized/security-sensitive corpus on both implementations, use seeded property generators and one actual minimal counterexample with corrected regression, and exercise hostile binary path/argv/env, optional untrusted file, forged actor, bad stdout/stderr, split frame, runtime error and untrusted native output. Explain which authority belongs to a real TS application caller rather than infer permission from Rust memory safety.
  - **Criteria:** Meaningful differential/property and independent oracle evidence establishes equal semantics and correct structured failures, including precise cross-language integer/Unicode limits, not matching stack strings or cheating through a shared incorrect implementation. An observed seeded issue fails before correction and passes afterward; no arbitrary command execution, private-data leakage, unbounded parser/resource use or unauthorized side effect is present. Process spawning alone is not described as an OS sandbox, and current authorization is independently verified when a protected feature is used.
  - **Evidence:** Property generators/corpus, fixture hashes, negative authorization tests, signed-off threat matrix, sanitized logs, failure diff and reproducibility instructions.

- **APP15-AS5** — Multi-Artifact Versioned Distribution and Upgrade Defense
  - **Outcomes:** APP15-O2, APP15-O5, APP15-O11, APP15-O12, APP15-O15, APP15-O16.
  - **Work:** Publish one complete locally runnable JS package/declarations, versioned protocol manifest and compatible Rust executable from pinned TS/Cargo inputs; install from a clean outside-source TS project, inspect actual supported OS/CPU/Node/Rust target, executable path and artifact hash, and run real old/new package-worker combinations with one intentionally incompatible protocol/handshake or missing/wrong binary. Repair through explicit compatible update or safe rollback/forward fix; exclude opaque privileged postinstall and undocumented remote downloads.
  - **Criteria:** A fresh consumer invokes an actual locally built compatible binary and invalid version pairs fail visibly, without reliance on cwd/source-path, hidden installer or a preexisting Rust developer environment for ordinary use. Lockfile/toolchain reproducibility is distinguished from exact binary byte reproducibility, artifact integrity from publisher identity, and tested single-platform behavior from assumed universal native portability. Actual old/new side effects, if any, cannot be undone by merely replacing a worker binary.
  - **Evidence:** Lockfiles/toolchain, binary and package manifests, clean checkout/consumer transcript, old/new matrix, failed install/repair traces and operator notes.

- **APP15-AS6** — Fair Performance and Alternate-Mechanism Decision
  - **Outcomes:** APP15-O1, APP15-O7, APP15-O12, APP15-O13, APP15-O14, APP15-O16.
  - **Work:** Run exactly matched accepted TS-only and Rust IPC workloads through the same user-facing validation/input/output, then measure cold spawn/handshake, warm reuse, frame size/serialization/parse time, Node event-loop responsiveness, child and parent CPU/RSS, selected p50/tail, queue/concurrency and actual timeouts/denied samples. Compare process isolation/operational costs with **conceptually assessed** Node-API and Wasm alternatives under accurate ABI, memory copy, panic and runtime constraints; justify retaining a TypeScript-only implementation when supported by evidence.
  - **Criteria:** Correctness/differential/security equivalence precedes timing. A real measured Rust CPU win with worse total user latency must not be described as an application improvement. Independent sample counts, errors, workload identity, startup/steady-state, resource/tail and uncertainty are reported, including host/target limits and bounded generator work. Node-API's ABI version scope does not guarantee third-party native portability and Wasm is not automatically a sandbox against all host imports or inherently faster. No unsafe FFI or mandatory Wasm/Node-API implementation or invented energy/cloud savings.
  - **Evidence:** Input corpus, workload settings, measurement CSV/traces, system constraints, alternatives matrix, build/deploy cost model and decision with limitations.

- **APP15-AS7** — Integrated Typed Application and Independent Unfamiliar Interoperability Defense
  - **Outcomes:** APP15-O1, APP15-O2, APP15-O3, APP15-O4, APP15-O5, APP15-O6, APP15-O7, APP15-O8, APP15-O9, APP15-O10, APP15-O11, APP15-O12, APP15-O13, APP15-O14, APP15-O15, APP15-O16, APP15-O17.
  - **Work:** Defend **one evolving, actual TS consumer + packaged Rust engine**, referencing individually accepted APP15-AS1–AS6 evidence by version and outcome instead of creating seven projects. Clean-run representative correct IPC, exact numeric/text schema, child crash/late result, finite queue, security and old/new install/benchmark decisions. A reviewer introduces a **previously unseen bounded** frame corruption, safe-integer loss, panic/EOF, forged executable, version mix, cancellation/backpressure, unauthorized input or misleading speedup; obtain independent **failing-before** TS/Rust/process evidence, repair or correctly contain and rerun relevant prior regressions through the same clean consumer.
  - **Criteria:** All APP15-AS1–AS6 decisions remain **separately passed**; final AS7 cannot waive missing assessment nor impose an APP9 core requirement. An unfamiliar test requires personally explainable causal before/after proof rather than memorized screenshots, shows honest pure-versus-effectful replay, current security and supported OS/runtime claims, and reports a valid no-Rust/no-FFI alternative when necessary. Equivalent accessible written, recorded or live defense may be used without paid providers, SYS2 sign-off, arbitrary native installer or fictional cross-platform measurement.
  - **Evidence:** One pinned TS app/consumer package, Rust Cargo source and executable plus wire protocol/schema manifest, **references-first accepted APP15-AS1–AS6 outcome/evidence index**, actual framed IPC and distinct Result/panic/exit/timeout traces, property/corpus/invalid version and replay tests, target+artifact hashes, matched TS-versus-Rust timings, unfamiliar reviewer case with independent failing-before/passing-after source and accessible technical defense.

### Shared academic and interoperability boundaries

- **Preparation ownership:** Apply APP19, APP21 and APP6 as verified direct prerequisites. Rust foundations can come from [SYS2](../SYS/SYS2.md) or equivalent outside learning; the **public self-check is formative**, and actual bounded Rust code in APP15-AS1 is assessed. No required SYS2 completion, APP2/APP3/APP20, extra language course, standalone readiness grade or new core graduation gate.
- **Real boundaries:** A TypeScript wrapper that merely prints a string or a Rust-only CLI without a consuming application is insufficient. Required work has versioned executable exchange, runtime-validated cross-language contracts, actionable failures, reproducible software tests and defended reason to keep both implementations.
- **Process IPC reference:** Spawn a fixed packaged executable without shell interpolation, control cwd/env/PATH, drain and cap **both** stdout and stderr, respect Node writable backpressure, explicitly handle split/large frames and out-of-order IDs, distinguish spawn/ready/exit, time-box shutdown and never promise a kill/AbortSignal undoes work. Pure deterministic computation may be recomputed; replay of a **committed external effect** is only safe under independently demonstrated durable identity/dedup or authoritative reconciliation. A second database/network server is not a required product.
- **Versions and distribution:** Pin Cargo/Node toolchains, lockfiles, actual supported Node/OS/CPU/libc/target and JS/types/Rust binary/wire compatibility, verify a clean independent consumer and real old/new mismatch plus repair. At least **one supported locally runnable target** is required; unsupported cross-platform targets are documented, not fake-test requirements. `cargo build --locked` enforces dependency-lock consistency, not bit-for-bit reproducible native binaries; artifact digests alone do not authenticate a publisher.
- **Security and privacy:** Apply real runtime checks and client/service authorization outside the Rust worker as appropriate, reject untrusted commands and paths, protect sensitive payloads and use synthetic local data. Memory safety does not imply policy or protocol correctness.
- **Measurement integrity:** Compare identical accepted work, controlled warmup, sample counts and resource budgets; include cold start and serialization overhead. Account for uncertainty; do not infer global app speed or battery advantage from local microbenchmarks.
- **Independent defense:** An unfamiliar bounded failure must be reproduced and explained, with a corrected implementation or defensible containment, regression evidence, operator guidance, limitations and a technical retrospective.
