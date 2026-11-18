# APP21 — Node.js & Backend Foundations

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `core`
**Prerequisites:** [APP18](APP18.md) — JavaScript Programming
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (planning estimate; calibrate with learner evidence)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Understand and practice the runtime mechanisms needed to build,
diagnose and operate a small backend program in Node.js **before
introducing an application framework**. Beginning with JavaScript
programming and basic Node/npm developer tooling from
[APP18](APP18.md), study Node's process and execution model, event
loop, operating-system I/O, filesystem boundaries, byte encodings,
streams and backpressure, HTTP/1.1 message handling, resource
limits, cancellation, error isolation, diagnostics and startup/
shutdown behavior. End by implementing and defending a local,
bounded HTTP service using the Node standard library.

Node.js is an execution **host** for ECMAScript, not a synonym
for JavaScript or a package manager. Distinguish V8's execution
of JS, Node's APIs, libuv's I/O infrastructure and the OS.
Promised/asynchronous work does not imply that all work executes
on a background thread. Worker threads or multiple processes
can be useful alternatives for actual CPU-parallel work;
understanding their role is required, but constructing a
production worker pool is not the exit criterion.

**APP18 is the only required APP prerequisite.** APP19
TypeScript can be used as an optional extension, but knowledge
of its static type system is not necessary to understand Node
event-loop or HTTP server mechanisms. This course introduces
minimal HTTP request/response concepts at the point of
implementation, without assuming prior completion of APP1.
APP21 does **not** teach introductory JavaScript syntax,
React, browser DOM programming, databases, persistence-layer
authorization, a framework's plugin/routing system, full
authentication, or production distributed service deployment.
Those capabilities belong to APP18, APP2/APP20, APP4,
APP3 and APP7/APP8 as appropriate.

**Reference environment:** a maintained, explicitly recorded
Node.js release, local text editor, ordinary user account,
ES modules, `node:test`, built-in `node:http`, filesystem
and stream modules, and synthetic local fixtures. Bind
experimental services only to `127.0.0.1` on a dynamically
assigned or other unprivileged port. No external service,
paid cloud account, public exposure, npm package download,
third-party framework, production secrets or real personal
data is required to run the summative assessments. Toolchain
installation can use a public download or pre-provisioned
free binaries before offline assessment execution.

**Version and operating-system behavior must be qualified.**
Node's timer/event-loop details can vary across versions;
in particular, libuv timer scheduling changed with Node 20.
Promises, `process.nextTick`, timers and I/O callbacks have
different ownership and scheduling guarantees. HTTP server
timeout defaults, signal availability and close behavior
are also version/platform-sensitive. Preserve exact
conditions with each measured or assessed claim instead
of teaching incidental output ordering as universal law.

The duration and workload are provisional; the subject
includes real failure and recovery investigations rather
than only executing a tutorial. Modules build from worked
mechanisms through controlled negative tests to an
independent service defense. Ordinary module practice is
formative, not a separate graduation gate unless explicitly
incorporated into an assessment.

## Learning outcomes

- **APP21-O1:** Explain Node.js as a JavaScript host and runtime, separating ECMAScript execution, V8, Node built-ins, event-loop and libuv mechanisms, operating-system facilities, and the development tooling already introduced in APP18.
- **APP21-O2:** Configure and reproduce a small Node.js service process using built-in ESM modules, declared runtime settings, safe environment and command-line input, explicit module boundaries, and observable startup failures.
- **APP21-O3:** Design nonblocking local filesystem operations and bounded concurrency, distinguishing asynchronous APIs from blocking work and explaining error propagation, cancellation limitations and safe filesystem path handling.
- **APP21-O4:** Predict, inspect and diagnose representative Node.js scheduling behavior involving callbacks, promises, microtasks, timers, immediates, I/O, event-loop delay and starvation without asserting unsupported cross-host timing guarantees.
- **APP21-O5:** Process binary and text data using Buffers, encodings, streams and pipeline/backpressure mechanisms, preserving byte correctness and applying bounded resource handling for slow producers or consumers.
- **APP21-O6:** Implement a framework-free HTTP/1.1 service with explicit request methods, paths, headers, status codes, body handling, response lifecycle and client-visible behavior, and distinguish runtime transport from application policy.
- **APP21-O7:** Enforce and verify service trust and resource boundaries for untrusted request targets, bodies, paths and configuration, including input size limits, explicit method/content-type policies, bounded work, safe errors and local-only exposure.
- **APP21-O8:** Classify synchronous, promise, I/O, stream and HTTP failures; implement justified timeouts, cancellation/abort ownership, idempotent cleanup and deliberate error-to-response or process-exit policies.
- **APP21-O9:** Manage service startup, readiness, lifecycle, signals, in-flight work and graceful shutdown within a declared local runtime/OS environment, distinguishing safe shutdown behavior from availability guarantees.
- **APP21-O10:** Produce minimally invasive diagnostic logs and measurements, correlate a request with its outcome, distinguish error rates/latency/resource signals, and investigate a reproducible incident without collecting sensitive payloads.
- **APP21-O11:** Verify normal and adverse service behavior through unit, integration and controlled concurrency tests using locally available tooling, and defend bounded runtime resource/throughput trade-offs with reproducible evidence.
- **APP21-O12:** Deliver, reproduce, modify and independently defend a small framework-free Node.js HTTP service that integrates the required runtime, I/O, security, failure, operations and testing capabilities.

## Modules

### Module 1 — Node.js Host Mechanisms and a Safe Local Service Boundary

#### Outcomes

- APP21-O1
- APP21-O2

#### Lessons

1. **Purpose, History and Host Responsibilities** — Situate Node's event-driven server-side origins through the actual task of running a local service. Identify what APP18 already proved about ECMAScript/modules and what this course must newly demonstrate about Node I/O, processes and HTTP.

2. **Language, V8, Node, libuv and Operating Systems** — Trace one module/callback from synchronous JavaScript through Node host facilities to supported OS I/O; classify work by owner instead of claiming every asynchronous call uses a background thread.

3. **Concurrency versus CPU Parallelism** — Distinguish overlapped I/O from JS callback execution and from real worker-thread/process parallelism on a bounded supplied task; choose an appropriate model without requiring a production worker pool.

4. **Safe Local Reference Runtime and Built-ins** — Record a maintained Node/OS baseline, locate necessary node: built-ins, run a minimal disposable service on 127.0.0.1 with an ephemeral port, and explain why a loopback test is not public service security.

*Optional practice — Host Boundary Audit:* Classify a mixed JavaScript/Node example by language, runtime or OS ownership; test one host-only assumption and explain its implications.

### Module 2 — Process Configuration, Modules and Resource Ownership

#### Outcomes

- APP21-O1
- APP21-O2
- APP21-O8
- APP21-O9

#### Lessons

1. **ESM and Runtime-Specific Exports** — Use APP18's existing ESM knowledge to organize node: imports, public functions and an isolated service entry; identify host-provided interfaces rather than recapping generic JavaScript syntax.

2. **Configuration, Paths and Reproducible Startup** — Validate bounded CLI/environment inputs, the declared Node runtime and cwd versus import.meta.url path assumptions before listening; use synthetic rather than real credentials.

3. **Startup Failure and Honest Exit Status** — Reproduce invalid port/fixture/configuration startup and inspect safe failure output, process exit semantics and how a later clean restart differs from swallowing the error.

4. **EventEmitter, Active Handles and Disposal** — Trace an event listener/error event and an open timer/socket/file handle that keeps the process alive; remove only owned listeners and close resources without assuming every callback is a Promise.

5. **Clean Local Module/Process Handoff** — From a fresh local copy execute the documented start/stop and basic test command, record version/OS and investigate one accidental open handle or environment-coupled startup.

*Optional practice — Startup Incident:* Reproduce a misconfigured startup and a lingering-handle case, then repair configuration or cleanup without hiding the symptom.

### Module 3 — Event Loop Scheduling and Bounded Nonblocking Work

#### Outcomes

- APP21-O1
- APP21-O3
- APP21-O4
- APP21-O11

#### Lessons

1. **Blocking JavaScript versus Overlapped I/O** — Contrast a bounded CPU loop and nonblocking file I/O while another local callback awaits service; predict which activity can make progress rather than equating Promise syntax with parallel execution.

2. **libuv Phases and Versioned Callback Order** — Explain poll/check/timer and other relevant phases conceptually, including the Node 20/libuv timer scheduling change, and mark observations dependent on OS, entry phase and runtime release.

3. **Promise Jobs, nextTick and Starvation** — Compare Node's process.nextTick, queueMicrotask, promises, immediates and timers in controlled CommonJS/ESM or supplied contexts; reproduce an unfair or starving loop with an explicit bound.

4. **Time Thresholds and I/O Ordering Evidence** — Show why timers are scheduling thresholds rather than deadlines; compare a bounded filesystem callback/immediate scenario and separate guaranteed order from incidental observed sequencing.

5. **Event-Loop Delay and Causal Repair** — Measure delay under reproducible blocked and corrected local conditions with a declared methodology; explain variance rather than interpreting an isolated timing as production throughput.

6. **Choose Async I/O, Workers or Processes** — Defend when cooperative I/O, a worker thread or independent process would be appropriate for an unfamiliar workload; demonstrate an explicit limitation instead of forcing a parallel implementation.

*Optional practice — Scheduling Diagnosis:* Investigate a supplied log trace containing a misleading ordering assumption and propose a corrected, reproducible explanation.

### Module 4 — Filesystem I/O, Safe Paths and Failure Isolation

#### Outcomes

- APP21-O2
- APP21-O3
- APP21-O7
- APP21-O8

#### Lessons

1. **Owned Async File Handles and Blocking Contrast** — Open/read/write/close synthetic local files with fs/promises, trace error and resource ownership, and show why a sync request-handler file operation can block unrelated callbacks.

2. **Missing Files, Permissions and Error Evidence** — Distinguish expected missing paths, permission/path faults, programming errors and late I/O failures; preserve diagnostic causes privately without disclosing real absolute paths or keys to HTTP clients.

3. **Path Resolution, Symlinks and Trust Limits** — Use an allowlisted logical file ID or tightly constrained trusted fixture tree; show why prefix/path normalization alone fails with traversal, encoded paths, symlinks or TOCTOU, without claiming a robust hostile-filesystem sandbox.

4. **Write Completion, Rename and Crash Durability** — Investigate temporary output files and rename/write behavior; distinguish successful promise resolution from a durable crash-safe transaction, filesystem-specific atomicity and unsupported guarantees.

5. **Abort Semantics and Partial-File Cleanup** — Test a supported AbortSignal boundary; explain that fs.readFile cancellation can stop its buffering without undoing individual underlying OS operations, and define actual partial-file/handle cleanup.

6. **Bounded Work and Stream Selection** — Limit identifier count, file size, read concurrency and buffered bytes, and select a stream rather than unbounded readFile when the actual data volume requires it.

*Optional practice — I/O Failure Injection:* Reproduce an invalid-path or missing-file error with a local fixture, verify cleanup and test that no other files are touched.

### Module 5 — Buffers, Encodings and Byte-Safe Data Contracts

#### Outcomes

- APP21-O3
- APP21-O5
- APP21-O7

#### Lessons

1. **Bytes, Code Units and Serialized Meaning** — Compare Buffer byte sequences, UTF-8 bytes, JS UTF-16 code units and displayed text, using a real Unicode input to expose faulty length/offset assumptions.

2. **Allocation, Views and Explicit Copying** — Allocate bounded buffers, measure byteLength and demonstrate when subarray/slice shares backing memory versus an independent copy; avoid leaking uninitialized or stale shared bytes.

3. **Chunked Unicode Decode and Representation** — Split a multibyte UTF-8 sequence across chunks, reproduce corrupt per-chunk decoding, then repair it with a streaming TextDecoder/StringDecoder according to documented encoding assumptions.

4. **Body-Byte Budget and Parsed Data Contracts** — Count actually received bytes rather than trusting Content-Length or character length, then distinguish bounded JSON syntax failures, correctly parsed but invalid domain shapes and expected response serialization.

*Optional practice — Encoding Defect:* Repair a chunk-splitting or truncation bug with a fixture containing multibyte characters and a reproducible byte-count check.

### Module 6 — Streams, Backpressure and Error Propagation

#### Outcomes

- APP21-O3
- APP21-O5
- APP21-O8
- APP21-O11

#### Lessons

1. **Stream Directions, Completion and Ownership** — Use Readable/Writable/Transform interfaces to trace data, end/finish/close/error and explicit ownership; distinguish successful completion from premature destruction.

2. **Backpressure and High-Water Boundaries** — Predict write() false/drain behavior and highWaterMark buffering; show that backpressure limits *flow*, not the total permitted HTTP body or file payload.

3. **Pipeline, Abort and Failed Stream Cleanup** — Use node:stream/promises pipeline for bounded local input/transformation/output, trigger early termination, and inspect promise rejection and owned resource cleanup without promising rollback.

4. **Async Iteration and Bounded Record Processing** — Use for-await and a simple incremental transform without accumulating unbounded data; preserve byte/record boundaries and explain early-exit effects.

5. **Slow Consumer and Memory Pressure Diagnosis** — Feed a synthetic slow writable, compare bounded in-flight/buffer behavior with an implementation ignoring backpressure, and explain where producer/consumer work must pause.

6. **Prove a Corrected Stream Boundary** — Demonstrate output integrity for split Unicode and an injected failure before/after a causal repair; record the stream lifecycle, error policy, partial output disposition and resource state.

*Optional practice — Backpressure Repair:* Diagnose a stream-copy implementation that ignores backpressure or drops an error; repair and retest using controlled local inputs.

### Module 7 — HTTP/1.1 Protocol and the Framework-Free Service

#### Outcomes

- APP21-O1
- APP21-O6
- APP21-O7
- APP21-O8

#### Lessons

1. **HTTP Host Entry, Message and Local Listener** — Map method, request-target, headers, status and response lifecycle to node:http; implement createServer on 127.0.0.1 ephemeral port and test a real local client. Review protocol concepts only when needed, not APP1's entire Web course.

2. **Exact Routing, Methods and Valid Targets** — Parse requests with a known local URL base, allowlist bounded methods/paths, classify 404 versus 405 and validate route identifiers rather than treat URL parsing as authorization.

3. **Status, HEAD, No-Body and Response Finality** — Set deliberate status/content-type and finish once; compare GET with HEAD and 204/304-style no-body cases and inspect headersSent/writableEnded behavior before reporting a late failure.

4. **Incremental Request Bytes and Domain Validation** — Read request chunks against actual byte limits and explicit media-type/JSON-shape rules; distinguish a malformed body, an unacceptable domain value and incomplete/truncated client input.

5. **Connections, Disconnections and Late Results** — Investigate HTTP keep-alive, an aborted client or a handler failing after headers were sent; define when a public response can still be sent and when only cleanup/logging is possible.

6. **Public Contract versus Future Framework Policy** — Publish a minimal read-only and bounded processing route with normal/negative fixtures; explain precisely which richer routing, validation, auth and framework lifecycle competencies are deferred to APP3.

*Optional practice — HTTP Trace:* Use a local Node client or equivalent tool to inspect a response sequence and repair an incorrect status, header or lifecycle handling issue.

### Module 8 — HTTP Trust Boundaries and Resource Protection

#### Outcomes

- APP21-O6
- APP21-O7
- APP21-O8
- APP21-O11

#### Lessons

1. **Threat Model, Safe Exposure and Bounded Work** — Name untrusted request targets, method/header/body data, concurrent clients and local configuration; make loopback-only binding observable while acknowledging loopback does not prove immunity to hostile local clients or DNS rebinding.

2. **Body Limits, Slow Arrival and HTTP Timeouts** — Reject actual excessive bytes and cap in-flight requests; compare headersTimeout, requestTimeout, socket/keep-alive settings with an application body limit. Examine a slow/chunked input and record version-dependent server behavior.

3. **Method, Content-Type and Parser Contracts** — Use explicit accepted methods, media types and runtime JSON/domain validation; ensure failures are consistent and do not continue buffering indefinitely after rejection.

4. **Path Safety, Host/Proxy Headers and Authorization Limits** — Demonstrate a safe logical identifier/allowlist, reject traversal or untrusted URL paths, and avoid treating Host, X-Forwarded-* or caller-supplied identity as authoritative; APP3 owns authentication/authorization.

5. **Response Errors, MIME Types and Secret-Free Output** — Map observed client versus internal faults to stable statuses and data, avoid executable or ambiguous output MIME types, and protect stacks, configuration, keys and body contents from public responses/logs.

6. **Negative Client and Resource Matrix** — From a local client, test oversized/chunked body, wrong method/type, malformed JSON, disconnected socket, slow client and denied path, recording actual byte count, final resource disposition and tested/untested safeguards.

*Optional practice — Negative-Path Attack Fixture:* Inject malformed JSON, oversize input, wrong media type and an unauthorized-looking request; verify controlled behavior and clearly state protections not implemented.

### Module 9 — Service Failure, Cancellation and Graceful Lifecycle

#### Outcomes

- APP21-O2
- APP21-O8
- APP21-O9
- APP21-O10

#### Lessons

1. **Boundary-Specific Errors and Stable HTTP Mapping** — Classify programmer errors, runtime I/O/stream failures, invalid client requests, shutdown races and internal faults; send safe HTTP statuses only while a response remains writable.

2. **Timeouts, Abort Ownership and Real Cancellation Limits** — Define application deadlines and supported AbortSignal consumers; demonstrate that setting a timer or aborting a Promise does not guarantee reversal of filesystem/server work already completed.

3. **Idempotent Cleanup Across Partial Initialization** — Use finally and explicit ownership to dispose file handles, pending timers, connections, pipelines and listeners, including partially initialized and already-closed states; avoid double-send and double-close defects.

4. **Fatal/Unrecoverable Failure Policy** — Distinguish a handled request failure from unhandled EventEmitter error, rejection and process-corrupting exception; justify controlled fail/exit policy rather than uncaught-error recovery magic.

5. **Startup, Readiness and Secret-Safe Configuration** — Define starting, ready, draining, stopped and failed; implement a bounded health/readiness status that checks declared service capability without exposing secrets or claiming general availability.

6. **Signals and Portable Programmatic Shutdown** — Observe SIGINT/SIGTERM behavior only where supported by the recorded Node/OS; provide a direct controlled shutdown function so tests are not platform- or shell-specific.

7. **Graceful Drain, Keep-Alive and Active Requests** — Stop accepting new work, bound existing work/keep-alive handling, verify graceful completion or defined interruption and document exactly what server.close/closeIdleConnections behavior means in the declared Node version.

8. **Injected Shutdown, Restart and Resource Leak** — Trigger shutdown during a controlled in-flight request and a late I/O failure, record actual success/rejection/status behavior, bounded forced-stop policy and clean restart with no unexplained open handles.

9. **Lifecycle Invariant and Regression Review** — Trace one request through start/ready/respond/drain/stop, prove no stale response or sensitive log after closure, and recheck failure/cleanup invariants after a bounded lifecycle change.

*Optional practice — Cancellation Incident:* Inject a timeout and a late failure in a local operation, trace state transitions and prove the system does not leak its owned resources.

### Module 10 — Testing, Observability and Resource Diagnosis

#### Outcomes

- APP21-O4
- APP21-O6
- APP21-O7
- APP21-O8
- APP21-O10
- APP21-O11

#### Lessons

1. **Independent Unit and Local HTTP Test Harness** — Use node:test with strict assertions, ephemeral-port server setup/teardown and an independent local client; separate pure domain behavior from actual node:http/stream integration.

2. **Adversarial HTTP, Stream and Shutdown Cases** — Create deterministic normal/negative tests for 204/HEAD, errors, wrong media, chunked/oversize payloads, canceled streams, late I/O, partial responses and in-flight shutdown, not just screenshots or successful localhost GETs.

3. **Minimal Structured Logging and Correlation** — Correlate a synthetic request ID with route class, status, duration and error code while omitting secrets, unredacted payloads, complete untrusted URLs and sensitive absolute paths.

4. **CPU/Memory/Event-Loop Observability** — Use monotonic timing, a supported loop-delay observation and bounded process memory/CPU readings; distinguish an actual measurement from a universal capacity/security claim.

5. **Controlled Local Overload/Blocking Experiment** — Compare a constrained baseline to a deliberately blocking or slow-consumer fixture under limits on client concurrency, duration and machine resources; preserve fairness and finish without hanging connections.

6. **Unfamiliar Incident and Causal Correction** — Given ambiguous traces for slow disk, a blocked JS callback, stalled client or forgotten handle, state a testable hypothesis, demonstrate a targeted repair and rerun focused functional and resource regressions.

*Optional practice — Incident Analysis:* Given fixture logs and measured traces, distinguish a slow client, slow disk, blocking callback and unhandled error, then defend one verified change.

### Module 11 — One Reproducible Node HTTP Service and Defense

#### Outcomes

- APP21-O1
- APP21-O2
- APP21-O3
- APP21-O4
- APP21-O5
- APP21-O6
- APP21-O7
- APP21-O8
- APP21-O9
- APP21-O10
- APP21-O11
- APP21-O12

#### Lessons

1. **One Domain, Service Contract and Evidence Plan** — Select a bounded synthetic local task, publish permitted routes, input/output/byte/time policies and failure states, and plan to reuse **the same** evolving source and accepted APP21-AS1–AS4 evidence.

2. **Integrate Runtime, Streams and Trusted Boundaries** — Build a cohesive framework-free service with separable domain, filesystem/stream, HTTP and lifecycle modules; preserve safe paths and error/cleanup semantics without importing a framework or database.

3. **Acceptance, Performance and Lifecycle Recheck** — Execute normal and negative client/service tests, verified bounded stream pressure, request correlation and graceful in-flight shutdown; link earlier accepted tests/traces instead of replaying all assessments as separate projects.

4. **Unfamiliar Bounded Change and Regression Evidence** — Accept a changed route, byte limit, failure policy or cancellation condition from an assessor, reproduce the resulting defect and verify a focused correction and earlier invariants.

5. **Clean Reproduction and Technical Defense** — Provide a fresh-checkout offline-capable start/test/stop path, a compact outcomes-to-evidence index, actually measured limits and a reviewable defense of Node-host versus framework/production responsibilities.

## Completion requirements

All **twelve outcomes** must be demonstrated through **five
independently decidable required summative assessments**.
The assessments can develop and inspect **one evolving Node.js
codebase**, including focused non-HTTP experiments during
APP21-AS1/AS2 and the eventual local HTTP service.
APP21-AS5 integrates earlier accepted evidence, introduces
an unfamiliar bounded requirement and independently verifies
the final service; it does **not** require five unrelated
servers or duplicate test reports. Previously accepted
evidence may be referenced, and optional module practice
does not create extra completion gates.

| Required assessment | Required outcome coverage | Principal evidence |
| --- | --- | --- |
| `APP21-AS1` — Node Runtime and Scheduling Investigation | APP21-O1, APP21-O2, APP21-O3, APP21-O4, APP21-O11 | Versioned local fixture and startup commands, prediction-versus-observation table, timestamped/annotated ordering trace, event-loop delay evidence with limitations, before/after regression tests and mechanism-based rationale |
| `APP21-AS2` — Asynchronous File, Byte and Stream Boundary | APP21-O2, APP21-O3, APP21-O5, APP21-O7, APP21-O8, APP21-O11 | Synthetic files and expected checksums/outputs, modular source, run/test commands, byte/stream/backpressure observations, invalid path/size/abort tests, recorded failure propagation and resource-cleanup evidence |
| `APP21-AS3` — Framework-Free HTTP Contract and Security Review | APP21-O6, APP21-O7, APP21-O8, APP21-O11 | Runnable framework-free server and local client, route/response contract, negative-path matrix with status/body/header observations, validated request-size counters, failed-and-repaired tests, exposure/threat boundary notes |
| `APP21-AS4` — Service Lifecycle, Cancellation and Observability Drill | APP21-O2, APP21-O4, APP21-O7, APP21-O8, APP21-O9, APP21-O10, APP21-O11 | Configuration/health contract, state diagram and signal or programmatic shutdown log, synthetic failure injection and clean restart results, local structured request correlation records, bounded latency/resource samples and test/limitation notes |
| `APP21-AS5` — Local HTTP Service Engineering Defense | APP21-O1, APP21-O2, APP21-O3, APP21-O4, APP21-O5, APP21-O6, APP21-O7, APP21-O8, APP21-O9, APP21-O10, APP21-O11, APP21-O12 | Version-controlled source and local synthetic fixtures, reproducible `node --test`/start/stop commands, route and acceptance matrix, normal/adverse integration logs, bounded workload results, before/after defect/change evidence, error/shutdown traces, README and a written/recorded/accessible technical defense |

### Shared local execution, evidence and security boundaries

- Use a maintained documented Node.js version with local
  built-in modules and `node:test`. Record OS/runtime,
  environment assumptions, test commands and actual
  resource/timeout settings where relevant. Do not impose
  a specific editor, package registry, paid host, Web
  framework, TypeScript compiler, database or cloud account.
- Test services on `127.0.0.1`, using ephemeral or
  unprivileged ports and synthetic data. Run negative client
  tests only against learner-controlled disposable
  processes. No Internet port scan, public deployment,
  privileged bind, real credentials or private data
  collection is required.
- Do not treat `Promise` scheduling as proof of a parallel
  JavaScript thread. Qualify timer, immediate and
  `process.nextTick` order by execution context, ESM
  behavior and declared Node version; distinguish observed
  traces from guaranteed ordering. The event loop cannot
  service other callbacks while the JS thread is blocked.
- HTTP clients are untrusted even on loopback. Read body
  bytes with explicit limits, validate declared media types
  and data values, use exact route/method policies, avoid
  interpolating untrusted paths or commands, and use safe
  response/error messages. Body size is not safely bounded
  by checking `Content-Length` alone.
- Stream backpressure controls **flow**, not a hard total
  payload size. Handle slow clients, errors and early stream
  termination under an explicit byte/concurrency/handle
  budget. A timeout/AbortSignal cannot guarantee that an
  underlying operating-system request or completed file
  effect was rolled back; Node's fs.readFile abort can
  terminate buffering without canceling individual OS
  read requests. Verify actual cleanup rather than assume it.
- HTTP server lifecycle claims must cover startup
  failure, readiness, active requests, drain and shutdown
  under a **declared Node/OS release**. Distinguish
  `headersTimeout`, `requestTimeout`, idle/socket/
  keep-alive timeouts and an application byte/work limit;
  no configured timeout replaces all others. Test
  `server.close()` with real active/keep-alive requests,
  qualify release-specific idle connection behavior,
  and never send a second response after headers/end.
  Use programmatic shutdown when signals are unavailable.
- Distinguish testable local **runtime correctness** from
  production security and availability. APP21 does not
  certify authentication, authorization, public TLS,
  proxy trust, production fault tolerance or framework
  API design; those require later APP courses.
- Use generated request identifiers and safe sanitized
  logging fields. Never write tokens, raw personal data,
  complete request bodies or filesystem secrets into
  test evidence. State limitations and disclose missing
  observations rather than inventing success.
- An independent reviewer may choose a bounded unfamiliar
  failure or change tied to a published outcome. Written,
  recorded, synchronous or equivalent accessible
  explanation may demonstrate the technical defense;
  a reviewer must not impose hidden proprietary tooling
  or unpublished architecture requirements.

### Required summative assessments

- **APP21-AS1** (required node runtime and scheduling investigation)
  - Outcomes: APP21-O1, APP21-O2, APP21-O3, APP21-O4, APP21-O11
  - Work: On a supplied **local** fixture or the initial stage of the same service, investigate synchronous JS, a Node built-in, Promise jobs, `process.nextTick`, timers, `setImmediate` and filesystem completion. Record Node/OS and execution context (including ESM), distinguish ECMAScript from Node/libuv/OS, and **predict only guaranteed order** before observing a real trace. Reproduce a bounded blocking/starvation defect, measure its effect on another callback, repair it without losing required behavior, then demonstrate one invalid startup configuration and an owned-handle cleanup path.
  - Criteria: JS, V8, Node, libuv and OS responsibilities are described accurately, with **async I/O overlap distinguished from JavaScript CPU parallelism**. Node 20/libuv and ESM/CJS/phase-dependent timer/nextTick ordering is appropriately version-qualified, not memorized as a fixed universal sequence. An actual local callback-delay observation supports the seeded defect and correction. Configuration failure and clean resource exit are demonstrated without reliance on arbitrary sleep-time assertions.
  - Evidence: Versioned local fixture and startup commands, prediction-versus-observation table, timestamped/annotated ordering trace, event-loop delay evidence with limitations, before/after regression tests and mechanism-based rationale.

- **APP21-AS2** (required asynchronous file, byte and stream boundary)
  - Outcomes: APP21-O2, APP21-O3, APP21-O5, APP21-O7, APP21-O8, APP21-O11
  - Work: Extend the evolving Node source with a **local bounded** file-processing adapter: stream synthetic records to a slow target with a proper pressure-aware pipeline, safely decode a UTF-8 code point split across arbitrary chunks, and verify expected output bytes independently. Enforce an allowlisted file identifier/contained trusted fixture and a real byte/concurrency budget, inject missing file and rejected stream/early abort cases and record handle and partial-output cleanup. Demonstrate why a naive prefix check, declared length or highWaterMark alone does not establish containment or total-size safety; no HTTP server is necessary for this stage.
  - Criteria: Independent byte-level expectations match output, including multibyte split cases, and input identifiers do not reach unrelated files in the tested threat model. The pipeline actually responds to slow-consumer backpressure, enforces a **separate total-byte bound**, propagates failure and closes its owned handles. Abort and failed writes follow the documented partial-file disposition without claiming OS I/O or already written data was reversed. A naive path-prefix test or unbounded read-all does not pass.
  - Evidence: Synthetic files and expected checksums/outputs, modular source, run/test commands, byte/stream/backpressure observations, invalid path/size/abort tests, recorded failure propagation and resource-cleanup evidence.

- **APP21-AS3** (required framework-free HTTP contract and security review)
  - Outcomes: APP21-O6, APP21-O7, APP21-O8, APP21-O11
  - Work: On the **same evolving source**, implement node:http with one read-only and one bounded JSON-processing route, exact URL path/method rules, suitable media types and a real byte-counted request limit. Using a local client, test GET/HEAD or another declared bodyless response, supported and unsupported methods, invalid content type, malformed/incorrect-shaped JSON, oversized content with and without a Content-Length claim, slow/chunked arrival, disconnected clients, and late failure **before and after headers are committed**. Demonstrate that binding only to loopback is a scope constraint, not authentication/authorization or proof of DNS-rebinding resistance.
  - Criteria: Actual status, headers and body/no-body semantics match the declared contract and HTTP/1.1 lifecycle; count **received** bytes and terminate oversized/incomplete work without unbounded buffering. Wrong type, unknown shape and failure paths receive controlled nonsecret responses while the socket remains writable; after response commitment, no double-send attempt occurs and the connection/failure is safely closed or logged. Node version and header/request/socket timeout assumptions are disclosed rather than presented as total resource protection. No framework, live backend, database or real identity service is required.
  - Evidence: Runnable framework-free server and local client, route/response contract, negative-path matrix with status/body/header observations, validated request-size counters, failed-and-repaired tests, exposure/threat boundary notes.

- **APP21-AS4** (required service lifecycle, cancellation and observability drill)
  - Outcomes: APP21-O2, APP21-O4, APP21-O7, APP21-O8, APP21-O9, APP21-O10, APP21-O11
  - Work: Add an explicit starting/ready/draining/stopped/failed lifecycle to the same local service, with validated startup settings, no-secret health/status response, safe request IDs, bounded concurrency and documented header/request/socket/keep-alive timeouts versus own application limits. Inject an invalid start, slow/aborted client, late stream/I/O failure and shutdown **with a live in-flight request**; observe active versus idle keep-alive behavior under a pinned Node version, bounded drain/force-stop, restart and controlled process/handle cleanup. Use platform-supported signals if relevant but supply **a programmatic shutdown test path**. Compare local event-loop delay, latency and resource samples under disclosed conditions, without production-availability claims.
  - Criteria: State transitions and effective readiness checks are inspectable, invalid configuration prevents listening, and in-flight/keep-alive shutdown traces match **the documented Node/OS release**, without mistaking server.close() for an unlimited wait or a forced guaranteed safe shutdown. Deadlines and AbortSignals have explicit owners, cleanup is idempotent, and deliberately rejected operations preserve privacy-aware diagnostics without leaking source paths, bodies or credentials. Local measurement method, variance and resource budget are disclosed; no broad production availability/capacity claim is inferred.
  - Evidence: Configuration/health contract, state diagram and signal or programmatic shutdown log, synthetic failure injection and clean restart results, local structured request correlation records, bounded latency/resource samples and test/limitation notes.

- **APP21-AS5** (required local HTTP service engineering defense)
  - Outcomes: APP21-O1, APP21-O2, APP21-O3, APP21-O4, APP21-O5, APP21-O6, APP21-O7, APP21-O8, APP21-O9, APP21-O10, APP21-O11, APP21-O12
  - Work: Finish **the one cumulative locally served Node HTTP component** begun in APP21-AS1–AS4. Integrate separately owned runtime/domain, filesystem/stream, HTTP, security and lifecycle behavior, plus repeatable tests and meaningful resource evidence. Reference **previously evaluated** source, traces and client matrices instead of building five servers or copying every log again. Independently reproduce from a clean local checkout and fix a new unfamiliar but bounded route, byte/time/cancellation or error-lifecycle requirement, proving regression behavior and defending why a raw Node mechanism—not a framework/auth/database/deployment feature—is the appropriate course boundary.
  - Criteria: Clean local startup, test and stop work with maintained free Node built-ins and synthetic data; every required limit, byte/stream/HTTP/timeout, secure output, shutdown and diagnostics claim is supported by actual tests and version-qualified observations. An unknown change is diagnosed and repaired with no regression to prior accepted capabilities; a passing AS5 cannot excuse a missing AS1–AS4 competency. Unhandled errors, unsafe public data exposure, unbounded work and unclosed handles block completion even when disclosed. The learner explains what APP3/APP7 must add for production auth/framework/deployment without pretending this local service is production-ready.
  - Evidence: **One** versioned source/fixture package with a clean start/test/stop guide, concise references to independently accepted APP21-AS1–AS4 evidence, a fresh unfamiliar change and targeted before/after tests, material combined HTTP/stream/shutdown observations, explicit unsupported claims and a reviewable written, recorded or equivalently accessible technical defense.

### Completion decision and revision safety

To complete APP21, a reviewer must establish that
`APP21-AS1` through `APP21-AS5` satisfy their public
criteria and jointly cover `APP21-O1` through
`APP21-O12`. Automated tests, code coverage,
a one-time successful HTTP request, or copied
console traces are not alone proof of runtime
understanding, bounded resource behavior or
independent engineering competence.

Material violations of published safety, input,
error-handling, stream, shutdown or reproduction
criteria must be repaired before passing. Review
records should preserve the source/spec revision,
assessment and outcome IDs, environment, meaningful
observations, failure analysis and limitations under
[OEE Evidence Rules](../../spec/evidence-rules.md).

APP21 remains an outcome-driven OEE `v0.2.0` **draft**,
not learner-tested, independently verified or accredited
by structural validation. The APP catalog **already
contains** the required APP3 and APP9 course definitions:
APP3 explicitly builds on APP19, APP21 and APP4 for
typed framework/API engineering. This course does not
change the prerequisite graph, change APP3's published
assessments or retroactively reinterpret prior APP18,
APP21 or other learner records, which remain tied to
their actually evaluated course/specification revisions.

### Public non-mandatory study references

These references support mechanism investigation and
version-specific review. The public course definition
above contains the actual assessable requirements;
no paid book, video or commercial course is required.

- [Node.js Learn — The Node.js Event Loop](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick)
  for phases, microtasks, callbacks, timers and version changes.
- [Node.js process API](https://nodejs.org/api/process.html)
  for lifecycle, signals, environment and exit behavior.
- [Node.js filesystem API](https://nodejs.org/api/fs.html)
  for sync/async methods, cancellation limits and handles.
- [Node.js Buffer API](https://nodejs.org/api/buffer.html)
  and [stream API](https://nodejs.org/api/stream.html)
  for bytes, encoding, pipelines and backpressure.
- [Node.js HTTP API](https://nodejs.org/api/http.html)
  for server/client message lifecycle and timeout controls.
- [Node.js test runner](https://nodejs.org/api/test.html)
  for built-in tests and reproducible local assertions.
- [Node.js performance hooks](https://nodejs.org/api/perf_hooks.html)
  for event-loop and timing diagnostics.
- [Node.js security guidance](https://nodejs.org/en/learn/getting-started/security-best-practices)
  for bounded, version-aware runtime risk reviews.
