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

### Module 1 — Node.js as a Runtime, Not Just a Script Runner

#### Outcomes

- APP21-O1
- APP21-O2

#### Lessons

1. **Course Orientation and the Origins of Server-Side JavaScript** — Situate Node.js as a server-side JavaScript runtime; explain its event-driven motivation and where its application-runtime responsibilities differ from APP18's language and npm tooling.

2. **Language, Engine, Runtime and Operating System** — Separate ECMAScript, the V8 engine, Node-provided interfaces, libuv and OS services without claiming all asynchronous work uses the same worker pool.

3. **Node's Execution Paths** — Trace a module through parsing/execution, synchronous call stacks, event-loop callbacks and OS-backed I/O; identify the point where application code regains control.

4. **JavaScript Single Thread and Concurrency Models** — Distinguish a primary JavaScript thread, asynchronous I/O, worker threads, processes and OS threads; state which mechanisms actually run JavaScript concurrently.

5. **Runtime API Survey** — Locate `node:fs`, `node:http`, `node:stream`, `node:events`, `node:process` and `node:test`, noting that APIs and guarantees are version-specific.

6. **Web Protocol Knowledge at the Point of Use** — Review only the minimum HTTP request/status/header/message behavior needed to implement local service primitives; deeper DNS/TLS and network-to-pixels reasoning remain in APP1.

7. **Safe Loopback Environment** — Record a supported Node version and OS, use a high unprivileged port or ephemeral port on `127.0.0.1`, and explain the difference between local loopback and public exposure.

*Optional practice — Host Boundary Audit:* Classify a mixed JavaScript/Node example by language, runtime or OS ownership; test one host-only assumption and explain its implications.

### Module 2 — Process, Modules, Configuration and Startup

#### Outcomes

- APP21-O1
- APP21-O2
- APP21-O8
- APP21-O9

#### Lessons

1. **Built-in Modules and ESM Boundaries** — Import Node built-ins with the `node:` prefix, distinguish standard JavaScript modules from runtime-dependent functionality, and reuse APP18's ESM skills without reteaching syntax.

2. **Arguments and Environment Variables** — Parse bounded CLI options and optional environment settings, apply defaults explicitly, and distinguish configuration validation from untrusted request-data validation.

3. **Package Manifest and Runtime Policy** — Declare a reproducible package/run command and supported runtime range, identify which development-only npm knowledge comes from APP18 and which settings affect runtime service behavior.

4. **Working Directories and Filesystem URLs** — Reason about `process.cwd()`, `import.meta.url` and local file paths; avoid depending on an accidental launch directory.

5. **Startup Validation and Exit Status** — Fail fast on invalid port, missing required local fixture or contradictory configuration; emit safe actionable error context and an appropriate process exit status.

6. **Resource Handles and Liveness** — Explain why active sockets, timers, workers and file handles can keep a process running; identify which resources must be closed for a clean exit.

7. **EventEmitter Basics and Error Events** — Subscribe and unsubscribe safely, understand listener lifetime, recognize unhandled `error` event consequences, and avoid treating every event as a promise.

*Optional practice — Startup Incident:* Reproduce a misconfigured startup and a lingering-handle case, then repair configuration or cleanup without hiding the symptom.

### Module 3 — Event Loop, Scheduling and Nonblocking Work

#### Outcomes

- APP21-O1
- APP21-O3
- APP21-O4
- APP21-O11

#### Lessons

1. **Synchronous Execution and Blocking** — Show how a CPU-heavy callback blocks other JS callbacks even while the program uses asynchronous APIs elsewhere.

2. **libuv and Event Loop Phases** — Explain timers, pending callbacks, poll, check and close callbacks as a conceptual model; distinguish documentation guarantees from incidental measurements and version changes.

3. **Promise Jobs and Node Scheduling** — Compare promise microtasks, `queueMicrotask`, `process.nextTick`, `setImmediate` and timers, including ESM/context-dependent ordering and starvation risks.

4. **Timer Thresholds, Not Deadlines** — Demonstrate why a requested delay is a minimum scheduling threshold rather than an exact wall-clock execution promise.

5. **Callbacks and Promise-Based Node APIs** — Use `fs/promises` for local operations and recognize callback-based Node APIs without conflating asynchronous completion with parallel CPU computation.

6. **I/O Event Ordering Investigation** — Predict and record callback order in controlled filesystem/I/O scenarios; qualify which outcomes depend on OS, Node version, event-loop iteration and initialization phase.

7. **Event Loop Delay and Starvation** — Create a safe bounded blocking fixture, measure observed scheduling delay and repair a pathological busy loop without pretending every latency change is a server throughput guarantee.

8. **Choosing a Concurrency Mechanism** — Explain when cooperative async I/O, worker threads or multiple processes are appropriate; note that worker threads are not mandatory for the APP21 exit service.

*Optional practice — Scheduling Diagnosis:* Investigate a supplied log trace containing a misleading ordering assumption and propose a corrected, reproducible explanation.

### Module 4 — Filesystem I/O, Paths and Failure Policies

#### Outcomes

- APP21-O2
- APP21-O3
- APP21-O7
- APP21-O8

#### Lessons

1. **Files, Descriptors and Async Operations** — Open, read, write and close a disposable local file with Node promise APIs; explain file descriptors, buffers and lifecycle ownership.

2. **Sync versus Async Filesystem Calls** — Compare synchronous and promise APIs in the context of a request-handling loop, demonstrating how blocking file work affects unrelated tasks.

3. **Errors and Context Preservation** — Classify missing files, permissions, conflicting paths and other I/O failures; preserve safe error codes and causes without leaking sensitive absolute paths to clients.

4. **Filesystem Paths, Symlinks and TOCTOU** — Parse only intended relative file identifiers, reject traversal, apply explicit allowlists, and reason about why simple string-prefix path checks are unsafe; describe links and race conditions in hostile directories; keep learner fixtures in disposable trusted trees rather than claiming a naive path check is a sandbox.

5. **Atomicity and Durable Writes** — Distinguish write completion from crash durability, temporary-file/rename patterns and whether a given filesystem provides the needed guarantees.

6. **Abort Signals and Resource Disposal** — Inspect an API's actual AbortSignal support, explain that cancellation can be best-effort and cannot necessarily roll back completed I/O.

7. **Bounded File Operations** — Impose fixture size and count limits, avoid unbounded `readFile` for large arbitrary files, and pick streaming when appropriate.

*Optional practice — I/O Failure Injection:* Reproduce an invalid-path or missing-file error with a local fixture, verify cleanup and test that no other files are touched.

### Module 5 — Buffers, Encodings and Data Interpretation

#### Outcomes

- APP21-O3
- APP21-O5
- APP21-O7

#### Lessons

1. **Bytes versus JavaScript Strings** — Explain Buffer as a byte sequence and why UTF-8 bytes, UTF-16 JS string code units and user-visible characters differ.

2. **Creating and Slicing Buffers** — Use explicit encodings, byte lengths and bounded allocations; distinguish view-like slicing and copying as appropriate to the active API.

3. **Multibyte Encoding and Protocol Boundaries** — Demonstrate decoding a split UTF-8 sequence with an incremental decoder rather than arbitrarily converting each chunk to a string; recognize when a file or HTTP body is bytes versus a declared text or JSON representation; validate encoding and stated media type rather than trust it.

4. **Network and Disk Payload Size** — Measure bytes actually received, enforce byte-based limits and explain why character counts and Content-Length alone cannot prove request-body safety.

5. **JSON and Error Semantics** — Parse a bounded JSON payload, distinguish malformed syntax from valid JSON with an unacceptable domain shape, and serialize explicit response contracts.

*Optional practice — Encoding Defect:* Repair a chunk-splitting or truncation bug with a fixture containing multibyte characters and a reproducible byte-count check.

### Module 6 — Streams, Backpressure and Pipelines

#### Outcomes

- APP21-O3
- APP21-O5
- APP21-O8
- APP21-O11

#### Lessons

1. **Readable, Writable, Duplex and Transform Streams** — Identify major Node stream abstractions and show where filesystem and HTTP messages expose readable/writable interfaces.

2. **Chunks, End and Destroy** — Distinguish stream data, completion and error/close states; explain what resource cleanup a consumer or producer must own.

3. **Backpressure and High-Water Marks** — Explain internal buffering, producer/consumer speed mismatch, `write()` returning false and waiting for `drain` without treating highWaterMark as a hard total-size limit.

4. **Pipelines and Error Propagation** — Use `node:stream/promises` pipeline for safe local copying/transformation, inspecting failure and cleanup behavior.

5. **Async Iteration of Streams** — Use `for await` with bounded work, explain cancellation and early exit consequences, and avoid unintentionally accumulating all chunks.

6. **Transforming Data Safely** — Apply a simple line or record transform to synthetic data while handling chunk boundaries and explicit encoding assumptions.

7. **Slow Consumer and Failure Injection** — Simulate a bounded slow writable target or rejected stream; inspect buffer growth and demonstrate propagation to the controlling promise.

*Optional practice — Backpressure Repair:* Diagnose a stream-copy implementation that ignores backpressure or drops an error; repair and retest using controlled local inputs.

### Module 7 — HTTP/1.1 Server and Request/Response Lifecycles

#### Outcomes

- APP21-O1
- APP21-O6
- APP21-O7
- APP21-O8

#### Lessons

1. **Request Method, Target and Headers** — Explain HTTP/1.1 request messages, response status and headers, request-target parsing, and why framework-style routing does not happen automatically.

2. **Building a Loopback HTTP Server** — Implement `node:http` `createServer`, listen on an ephemeral port at `127.0.0.1`, and close the server under explicit test ownership.

3. **Routing by Exact Path and Method** — Use `URL` with a known local base, match a bounded path/method table, and distinguish missing routes from method-not-allowed cases.

4. **Response Headers, Body and End** — Set correct response status and media type, end responses exactly once, and inspect behavior for HEAD and no-body response cases.

5. **Reading a Request Body Incrementally** — Consume request body chunks with an explicit byte limit; distinguish transfer framing, declared length and actual received bytes.

6. **Validation and Structured Failure Responses** — Separate malformed JSON, invalid domain input, unsupported methods/media type and internal failures into predictable response categories.

7. **Connection Reuse and Early Disconnect** — Observe persistent HTTP/1.1 connections, a disconnected client and already-sent response headers; do not attempt to send a new error body after a response has completed.

8. **Raw HTTP Service versus Framework API** — Document which repetitive routing/validation/error concerns APP3 Fastify will later help organize, without turning this course into an API framework tutorial.

*Optional practice — HTTP Trace:* Use a local Node client or equivalent tool to inspect a response sequence and repair an incorrect status, header or lifecycle handling issue.

### Module 8 — HTTP Security, Trust and Resource Limits

#### Outcomes

- APP21-O6
- APP21-O7
- APP21-O8
- APP21-O11

#### Lessons

1. **Trust Boundary for Untrusted Clients** — Threat-model request methods, targets, headers, body content and connection concurrency even when the exercise runs only on loopback.

2. **Bounded Request Bodies and Uploads** — Reject oversized incoming streams by actual bytes, handle partial/chunked arrivals and ensure the error path does not keep buffering forever.

3. **Method, Content-Type and Shape Policies** — Accept only explicitly documented methods/media types, validate parsed JSON and reject ambiguous or inconsistent inputs.

4. **Path Traversal and Unsafe File Serving** — Demonstrate how decoded paths, separators and untrusted identifiers can lead outside a content root; use a bounded allowlist or no file serving in the core assessment.

5. **Safe Errors and Output Encoding** — Return stable public errors without stack traces, environment variables, filesystem paths or secrets; use explicit content types to avoid ambiguous browser interpretation.

6. **Timeouts, Slow Clients and Response Limits** — Investigate Node server header/request/connection timeout settings with a documented version and enforce an application-level body limit rather than relying on defaults alone.

7. **Authentication and Authorization Boundary** — Explain why a loopback demo is not an authenticated Internet API. Introduce the need for authenticated identity and authorization without requiring APP3's full framework implementation.

8. **Trust of Proxies and Deployment Boundaries** — Recognize that forwarded headers and external TLS termination require a trusted proxy/deployment model; do not trust client-supplied origin or proxy headers as authoritative.

*Optional practice — Negative-Path Attack Fixture:* Inject malformed JSON, oversize input, wrong media type and an unauthorized-looking request; verify controlled behavior and clearly state protections not implemented.

### Module 9 — Errors, Timeouts, Cancellation and Cleanup

#### Outcomes

- APP21-O3
- APP21-O5
- APP21-O8
- APP21-O9

#### Lessons

1. **Error Taxonomy by Boundary** — Classify programmer exceptions, rejected promises, filesystem codes, aborted requests, stream errors and expected bad inputs.

2. **HTTP Response State and Error Mapping** — Map controlled client faults to stable status categories while preserving internal error context for local diagnostics; avoid always returning 500 or 200.

3. **Timeout Ownership and Deadlines** — Explain API-specific timeout behavior and why a timer expiration does not itself cancel an unrelated Promise, socket or file operation.

4. **AbortSignal Propagation** — Use AbortController only with supported consumers, distinguish an abort request from proof that I/O stopped or external side effects were undone.

5. **Stream and Socket Teardown** — Demonstrate pipeline failure and request/response close handling; avoid double-send/double-close bugs and swallowed cleanup exceptions.

6. **Unhandled Rejection and Fatal Error Policy** — Diagnose unhandled failures, distinguish recoverable request errors from process corruption and justify fail/exit behavior under a declared Node baseline.

7. **Cleanup with Finally and Ownership** — Use `finally` and idempotent cleanup for file handles, timers, connections and test fixtures, including the case where setup only partially succeeded.

*Optional practice — Cancellation Incident:* Inject a timeout and a late failure in a local operation, trace state transitions and prove the system does not leak its owned resources.

### Module 10 — Startup, Health, Shutdown and Operational Behavior

#### Outcomes

- APP21-O2
- APP21-O8
- APP21-O9
- APP21-O10

#### Lessons

1. **Service State Model** — Define startup, ready, draining, stopped and failed states; distinguish an open listening socket from readiness for the stated function.

2. **Configuration Validation Before Listen** — Check required data and environment settings before accepting traffic, and select safe local defaults for experimental service exposure.

3. **Health and Readiness Endpoints** — Implement a bounded status endpoint that avoids disclosing secrets and clearly states what it checks and what it cannot establish.

4. **Process Signals and Platform Variations** — Investigate supported SIGINT/SIGTERM handling, Windows/Unix differences and signal behavior; provide an explicit programmatic shutdown path for portable testing.

5. **Graceful HTTP Shutdown** — Stop accepting new connections, allow bounded in-flight requests to finish, define a forced-stop deadline and record the behavior of existing keep-alive connections for the declared Node version.

6. **Restart and Error Recovery** — Inject a startup failure or crashing handler, demonstrate controlled request-level errors when safe and document when a fresh process is required.

7. **Configuration and Secret Hygiene** — Use fabricated environment values; distinguish required configuration from sensitive material and prevent leakage into responses/logs.

*Optional practice — In-Flight Shutdown:* Begin a controlled local request, initiate shutdown and record whether it completes, fails deliberately or meets the stated deadline.

### Module 11 — Testing, Observability and Resource Diagnosis

#### Outcomes

- APP21-O4
- APP21-O6
- APP21-O7
- APP21-O8
- APP21-O10
- APP21-O11

#### Lessons

1. **Node Built-in Test Runner and Assertions** — Use `node:test` and strict assertions to test pure adapters, error mapping and lifecycle helpers; maintain the tests independently from main-service entry.

2. **Ephemeral-Port Integration Fixtures** — Create and close a loopback server from test setup, issue local HTTP client requests, and prevent port collisions and hanging handles.

3. **Protocol and Input-Failure Matrix** — Test valid JSON, malformed JSON, invalid methods, wrong content types, oversized/chunked bodies, missing paths, aborted requests and double-response hazards.

4. **Stream, Error and Shutdown Tests** — Inject a broken readable/writable, cancellation and an in-flight shutdown; assert cleanup, failure propagation and consistent response state.

5. **Structured Logging and Correlation** — Record synthetic request IDs, method, route class, duration and error code without logging bodies, secrets or full untrusted request data.

6. **Latency and Event-Loop Diagnostics** — Use monotonic timing and a supported event-loop delay metric; qualify clock noise, small samples, concurrent workload and CPU/event-loop contention.

7. **Memory, CPU and Active Handles** — Observe process memory/CPU metrics in a safe small local workload and explain why a single metric does not reveal heap leaks or production capacity.

8. **Bounded Load Investigation** — Run a small local-only load test with concurrency/time limits, compare a baseline and a deliberately blocking handler, and identify backpressure or event-loop starvation evidence.

*Optional practice — Incident Analysis:* Given fixture logs and measured traces, distinguish a slow client, slow disk, blocking callback and unhandled error, then defend one verified change.

### Module 12 — Integrated Framework-Free Service and Engineering Defense

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

1. **Define the Local Service Problem** — Select a bounded synthetic task queue, local note processor or inventory-report endpoint with clear success/failure behavior and no required database/framework.

2. **Publish Routes, Limits and Acceptance Criteria** — Document allowed methods/paths, input JSON shape, response statuses, maximum body bytes, concurrency policy, health checks and safe error shapes.

3. **Separate Domain Logic from Runtime Adapters** — Keep pure input/rule computations distinct from HTTP, filesystem and process entry points so behavior can be verified without opening a socket.

4. **Add Bounded I/O and Stream Processing** — Implement at least one real Node async filesystem or stream operation, including a controlled failure path and a declared resource bound.

5. **Wire a Raw HTTP Server** — Integrate a framework-free `node:http` service on loopback with explicit parsing, validation, response lifecycle and representative HEAD/unsupported-method policies.

6. **Diagnose Scheduling or Backpressure** — Reproduce a small event-loop delay, stream pressure or unintended serial/parallel work defect and document a verified repair.

7. **Test Bad Clients and Runtime Failures** — Run malformed, oversized, aborted and unusual method requests, late I/O failures, startup invalid configuration and controlled service shutdown.

8. **Produce Safe Operational Evidence** — Capture structured local logs, basic request count/latency samples, health/readiness observations and an in-flight shutdown trace without personal data.

9. **Clean Reproduction and Unfamiliar Change** — From a fresh local checkout, execute documented test/start/stop commands; implement a bounded new route/failure requirement and defend changes with regression evidence.

## Completion requirements

All **twelve required outcomes** are evaluated by the **five
required summative assessments** below. A single evolving
Node.js codebase can supply evidence to several assessments
when independent evaluation remains possible. Learners do
not need five unrelated HTTP servers. Lesson investigations,
sample fixtures and non-summative debugging exercises
are formative preparation, not hidden completion gates.

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
- Stream backpressure controls **flow**, not an absolute
  payload length by itself. Handle slow consumers, errors,
  aborted requests and early stream termination by the
  stated resource ownership policy. A timeout or abort
  signal does not automatically reverse completed file
  changes or guarantee a task's underlying work stopped.
- HTTP server and process lifecycle claims must cover
  startup failure, readiness, active requests, drain and
  shutdown under a declared runtime. Do not assume a
  response can be sent after headers have been committed,
  that close always waits forever, or that OS signals are
  identical on every platform.
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
  - Work: Investigate a supplied JavaScript/Node fixture that mixes synchronous computation, Node host APIs, promise reactions, `process.nextTick`, timers, `setImmediate` and local filesystem I/O. Separate language-defined behavior from Node runtime and OS mechanisms, record actual version/OS, predict only defensible ordering, introduce a bounded blocking callback and analyze event-loop response. Repair one scheduling/starvation defect while maintaining stated behavior. Demonstrate a reproducible startup/configuration error and explain the relevant resource ownership.
  - Criteria: The learner accurately separates V8/ECMAScript, libuv, OS and Node facilities; distinguishes I/O overlap from parallel JavaScript execution; qualifies ESM and timing-dependent callback order rather than asserting a universal timer sequence. Trace and event-loop delay observations match a documented environment, the bounded defect is reproduced and repaired, and the process exits cleanly after tests without hidden active handles.
  - Evidence: Versioned local fixture and startup commands, prediction-versus-observation table, timestamped/annotated ordering trace, event-loop delay evidence with limitations, before/after regression tests and mechanism-based rationale.

- **APP21-AS2** (required asynchronous file, byte and stream boundary)
  - Outcomes: APP21-O2, APP21-O3, APP21-O5, APP21-O7, APP21-O8, APP21-O11
  - Work: Build a local, bounded file-processing adapter that reads a synthetic text/record input asynchronously, handles non-ASCII bytes correctly across arbitrary chunk boundaries, and transforms or copies it to a slow local target using a backpressure-aware stream/pipeline. Validate file identifiers or use a fixed allowlist, enforce explicit total-byte limits and distinguish expected missing/invalid files from operational failures. Inject a stream failure, early abort and a slow consumer; demonstrate cleanup without building a Web server.
  - Criteria: Outputs are byte-correct and repeatable, including split multibyte characters; no unbounded accumulation or path traversal reaches unrelated files; the source/target pipeline respects writable backpressure and propagates failures. After a controlled abort or write failure owned handles are closed, partial artifacts follow a documented cleanup policy, and no unsupported claim is made that abortion undoes already-committed filesystem effects.
  - Evidence: Synthetic files and expected checksums/outputs, modular source, run/test commands, byte/stream/backpressure observations, invalid path/size/abort tests, recorded failure propagation and resource-cleanup evidence.

- **APP21-AS3** (required framework-free http contract and security review)
  - Outcomes: APP21-O6, APP21-O7, APP21-O8, APP21-O11
  - Work: Implement a minimal `node:http` loopback service supporting at least one read-only route and one bounded JSON-processing route, with declared methods, exact path matching, media type, status codes, response body shape, size limits and a controlled error mapping. Use a local Node client to test valid requests, wrong methods/content types, malformed JSON, oversized/chunked bodies, unsupported paths, disconnected clients and a late handler failure. Demonstrate why the service is not inherently authenticated or safe for public deployment.
  - Criteria: The actual route/method behavior matches a published request/response contract; bodies are limited by observed bytes, not trusted Content-Length alone, and oversized processing ceases according to documented policy. Unknown input is validated, malformed requests receive consistent nonsecret errors, no response is double-sent after headers are committed, and connection aborts do not create unhandled failures. No third-party framework or database is required.
  - Evidence: Runnable framework-free server and local client, route/response contract, negative-path matrix with status/body/header observations, validated request-size counters, failed-and-repaired tests, exposure/threat boundary notes.

- **APP21-AS4** (required service lifecycle, cancellation and observability drill)
  - Outcomes: APP21-O2, APP21-O4, APP21-O7, APP21-O8, APP21-O9, APP21-O10, APP21-O11
  - Work: Extend a disposable local Node service with documented configuration/startup validation, readiness and health semantics, structured privacy-aware diagnostic logs, bounded in-flight work, explicit timeout/abort policies and controlled shutdown. Inject one invalid startup configuration, one slow or aborted request, one late filesystem/stream failure and a shutdown during a request. Demonstrate a successful clean restart and qualified local latency/event-loop/resource measurements.
  - Criteria: Start/ready/drain/stop transitions are observable and justified; unsafe configuration fails before listen; shutdown bounds new/in-flight work under the declared Node/OS version and does not leave timers/sockets/test handles hanging. Timeouts do not masquerade as automatic cancellation; errors preserve internal diagnostic context while exposing stable safe client responses; logs contain no secrets or unredacted payloads. Measurements record method and environment and do not claim production capacity from a local experiment.
  - Evidence: Configuration/health contract, state diagram and signal or programmatic shutdown log, synthetic failure injection and clean restart results, local structured request correlation records, bounded latency/resource samples and test/limitation notes.

- **APP21-AS5** (required local http service engineering defense)
  - Outcomes: APP21-O1, APP21-O2, APP21-O3, APP21-O4, APP21-O5, APP21-O6, APP21-O7, APP21-O8, APP21-O9, APP21-O10, APP21-O11, APP21-O12
  - Work: Build or extend a cohesive framework-free HTTP/1.1 service that accepts bounded synthetic requests, validates data, performs a genuine nonblocking Node file/stream operation, handles expected and unexpected errors deliberately, records safe diagnostic signals, provides a constrained readiness status and supports controlled shutdown. Reuse qualifying APP21-AS1–AS4 artifacts rather than creating unrelated projects. From a clean checkout, demonstrate both successful and failed requests, a controlled failure/repair trace, a concurrency or backpressure analysis and a bounded unfamiliar change such as a new route, input limit or failure-policy requirement. Defend how the service uses runtime primitives and which responsibilities belong in later APP3 framework engineering.
  - Criteria: A reviewer can reproduce the service locally without privileged ports, paid services, TypeScript, React, a database or a framework. Published request/response, input, byte-limit, async, error, shutdown and logging requirements have matching tests and honest negative evidence. The implementation owns and closes local resources, has no unexplained connection or unhandled rejection, avoids sensitive error disclosure, and records actual runtime/OS boundaries. The unfamiliar change satisfies stated criteria without breaking previous cases; the learner explains event-loop/stream behavior, resource limitations and what security/operability guarantees are not provided.
  - Evidence: Version-controlled source and local synthetic fixtures, reproducible `node --test`/start/stop commands, route and acceptance matrix, normal/adverse integration logs, bounded workload results, before/after defect/change evidence, error/shutdown traces, README and a written/recorded/accessible technical defense.

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

APP21 enters the active catalog as an outcome-driven
OEE `v0.2.0` **draft**, not learner-tested or verified.
The previous APP18 curriculum and legacy APP3/APP9
course evidence retain their historical identities;
adding a required core course does not silently
upgrade old completion evidence. APP3 will separately
build on APP19, APP21 and APP4 to teach typed
framework API engineering; its assessment and
prerequisites are not rewritten by this PR.

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
