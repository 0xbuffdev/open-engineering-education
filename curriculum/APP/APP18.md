# APP18 — JavaScript Programming

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `core`
**Prerequisites:** [SEF10](../SEF/SEF10.md) — Software Engineering Foundations
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (provisional; calibrate with learner evidence)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Develop a precise working model of JavaScript as a general-purpose
programming language and use it to build maintainable, testable programs.
Beginning with SEF programming competence (primarily Python), learn
the ECMAScript execution model, values and conversions, control flow,
functions, lexical scope, closures, object/prototype behavior,
collections, modules, explicit data contracts, errors, promises,
asynchronous scheduling, debugging and program design.

Learn the tools required to reproduce JavaScript programs from a clean
checkout using a supported local Node.js runtime, ES modules,
`package.json`, package scripts and an appropriate dependency
strategy. Node is the **local execution and development-tooling
host**, not an assumption that JavaScript equals Node. Compare
language-defined behaviors with host-provided operations and explain
which results are portable.

This course is **not** a browser DOM, HTML/CSS, React, TypeScript,
Node HTTP-service, or backend-framework implementation course.
Browser interaction belongs to APP2; TypeScript's static type
system to APP19; React to APP20; Node service/runtime engineering to
APP21; framework API engineering to APP3. APP1's Web mechanisms and
APP17's markup competence remain complementary but do not gate
general JavaScript programming; SEF10 is the required entry course.

A working local Node.js runtime and text editor are sufficient.
Use synthetic or sanitized local files and tests. No remote registry,
public endpoint, proprietary account, paid textbook, browser framework,
production cloud deployment, credential, or internet-connected
application is necessary for required assessment execution. Toolchain
installation may use a normal public download or a preinstalled
runtime; required project behavior must be reproducible without
network access after setup. Where a package demonstration is useful,
use built-in libraries or a reviewed local dependency fixture
rather than forcing a supply-chain download.

JavaScript has standard-language semantics defined by ECMA-262,
while `process`, filesystem operations, timers and the Node test
runner are host-provided facilities. Teach the stable principles
used by this course rather than treating an experimental
proposal, engine optimization or one runtime version's behavior
as universal language behavior.

Duration is a planning estimate, **not** proof of readiness.
Learners should develop explanations, guided experiments, testable
designs and independent change-handling, with gradually decreasing
scaffolding. Practice in modules is formative unless explicitly
included in a required assessment below.

## Learning outcomes

- **APP18-O1:** Distinguish the ECMAScript language from JavaScript host environments, execute and inspect a small program in a supported local runtime, and explain which behavior is specified by the language versus supplied by Node.js or a browser.
- **APP18-O2:** Predict and verify JavaScript value, equality, coercion, arithmetic, string/Unicode and conditional behavior; repair representative defects involving missing values, numeric precision and implicit conversion.
- **APP18-O3:** Implement and test correct functions and control flow using expressions, parameters, recursion or iteration as appropriate, and justify decomposition, edge-case handling and termination.
- **APP18-O4:** Explain and debug lexical scope, closures, call-time context, function forms and mutation/aliasing; demonstrate the practical consequences of `this`, captured state and reference identity.
- **APP18-O5:** Represent and transform data using objects, prototypes, arrays, maps, sets and iteration protocols; distinguish own versus inherited properties and shallow versus independent data copies.
- **APP18-O6:** Define and enforce runtime input/output contracts, parse untrusted structured data safely, distinguish recoverable errors from programming defects, and test explicit failure paths without swallowing errors or exposing sensitive information.
- **APP18-O7:** Design maintainable JavaScript modules and functional boundaries with explicit exports, cohesive responsibilities, predictable side effects and independent tests; explain module loading and compatibility assumptions.
- **APP18-O8:** Explain event-loop scheduling and promise settlement, implement controlled asynchronous workflows with `Promise` and `async`/`await`, and diagnose propagation, ordering and bounded-work failures using reproducible observations.
- **APP18-O9:** Establish and reproduce a small Node.js/ES module project with a declared runtime baseline, `package.json`, npm scripts, dependency and lockfile reasoning, safe local build/test steps, and a clear distinction between development tooling and application runtime.
- **APP18-O10:** Select and implement proportionate automated tests and debugging investigations, covering normal, boundary and malformed cases; reproduce a defect, verify a repair, and reason about a program's algorithmic cost.
- **APP18-O11:** Deliver, modify and independently defend a small modular JavaScript application or utility against published functional, reliability and evidence criteria, including reproducible execution and an unfamiliar bounded change.

## Modules

### Module 1 — From SEF Programming to JavaScript

#### Outcomes

- APP18-O1
- APP18-O2
- APP18-O9

#### Lessons

1. **Course Orientation and the Web's Programming Language** — Recall prior SEF programming and explain why JavaScript emerged for Web scripting, how general-purpose use expanded, and where APP18 ends before browser/React and backend-service courses.

2. **ECMAScript, Engines, and Hosts** — Separate language syntax/semantics, engine execution, runtime host APIs and surrounding tools; identify an example that works in Node but not without adaptation in a browser.

3. **First Local Program** — Run a small ES module using an installed supported Node runtime; inspect standard output, process exit status and an intentionally triggered stack trace.

4. **From Python Concepts to JavaScript Behavior** — Translate a bounded computation from SEF Python while recording meaningful differences in booleans, nullish values, equality, iterables, mutation and function binding.

5. **Reading Source and Diagnostics** — Use a text editor and runtime diagnostic output to locate syntax and runtime errors; distinguish parser errors from errors in reachable execution paths.

6. **Runtime Readiness and Safe Fixtures** — Record runtime version and execution command, run from an ordinary user account, and use synthetic local data rather than secrets or remote service credentials.

7. **Formative Investigation: Host or Language?** — Classify representative APIs and predict what happens under another host; independently verify one assumption with documentation and a runnable example.

### Module 2 — Values, Conversion, Numbers, and Strings

#### Outcomes

- APP18-O2
- APP18-O3

#### Lessons

1. **Primitive Values and Type Inspection** — Distinguish undefined, null, Boolean, Number, BigInt, String and Symbol values; explain `typeof null` as historical behavior and why `typeof` is not a general validation strategy.

2. **Bindings and Expressions** — Use `const` and `let`, distinguish rebinding from mutating referenced objects, and explain expression evaluation and assignment order.

3. **Equality, Truthiness, and Nullish Defaults** — Predict strict versus loose equality in representative cases; distinguish falsy, missing and intentionally zero/empty values; use `??` and `?.` when their semantics match the requirement.

4. **Number Representation and Precision** — Explain binary floating-point limitations, `NaN`, infinities, safe integers, signed zero and `BigInt`; reject incorrect currency or identifier calculations rather than relying on accidental rounding.

5. **String and Unicode Semantics** — Distinguish code units, code points and grapheme clusters; explain why indexing and simple `length` cannot count user-visible characters in every case.

6. **Conversion and Comparison Boundaries** — Inspect numeric/string conversions, relational comparisons, and accidental concatenation; apply explicit parsing and range checks to an input-processing problem.

7. **Dates, Time Zones, and Localization Limits** — Explain timestamps versus local display, the risk of ambiguous date parsing, and when a host's internationalization facilities are presentation tools rather than business-domain logic.

8. **Formative Debugging: Surprising Values** — Predict outputs for adversarial value fixtures, run them, explain mismatches and produce a corrected implementation with tests.

### Module 3 — Control Flow, Functions, and Problem Decomposition

#### Outcomes

- APP18-O3
- APP18-O10

#### Lessons

1. **Branching and Exhaustive Cases** — Use conditional expressions, `if` and `switch` with deliberate fall-through decisions; handle unexpected cases instead of silently selecting a default.

2. **Loops and Termination** — Select `for`, `while` or for-of iteration by data shape; reason about invariants, boundaries, off-by-one errors and termination.

3. **Function Signatures and Parameters** — Distinguish declarations, expressions and arrow functions; implement defaults, rest parameters, destructuring and explicit return values without obscuring contracts.

4. **Higher-Order Functions** — Pass functions as values and use map/filter/reduce where they clarify a transformation; compare against an explicit loop for correctness and readability.

5. **Recursion and Iteration Trade-offs** — Trace the call stack and base case of a recursive task; choose an iterative alternative when depth and resource bounds warrant it.

6. **Pure Functions and Side Effects** — Separate deterministic computations from logging, input, mutable state and time; test pure functions against explicit examples and counterexamples.

7. **Readable Decomposition and Complexity** — Decompose a data transformation into named operations; reason about representative linear, quadratic and lookup costs without optimizing prematurely.

8. **Formative Change: New Rule, Same Invariants** — Extend an existing function for one changed requirement and verify earlier behavior with regression cases.

### Module 4 — Lexical Scope, Closures, and Call Context

#### Outcomes

- APP18-O3
- APP18-O4
- APP18-O10

#### Lessons

1. **Lexical Environment and Shadowing** — Trace identifier lookup and block/function/module scope; distinguish lexical binding from object property lookup.

2. **Initialization and Temporal Dead Zones** — Explain declaration instantiation, `var` versus `let`/`const`, and why using a lexical binding before initialization fails.

3. **Closures and Private State** — Build a closure over state, explain captured bindings versus captured values, and test independent instances with no accidental shared state.

4. **Call Context and `this`** — Distinguish ordinary-function dynamic receiver binding, method calls, explicit `call`/`apply`/`bind`, and lexical `this` in arrows; inspect detached-method failures.

5. **Arguments, References, and Aliasing** — Explain parameter passing of values that may refer to objects; investigate mutation visible through several aliases without claiming pass-by-reference semantics.

6. **Callbacks and Captured Loop Variables** — Reproduce a closure timing or loop-binding defect, repair it, and explain when callback invocation occurs.

7. **Stack Frames and Debugging** — Walk a nested call/closure stack trace, inspect locals and captured variables, and explain why a log statement cannot prove every execution path.

8. **Formative Closure Review** — Review a small callback-heavy program, write a prediction, run it, and fix one state or receiver bug without masking it.

### Module 5 — Objects, Prototypes, and Classes

#### Outcomes

- APP18-O4
- APP18-O5
- APP18-O6

#### Lessons

1. **Object Shapes and Property Access** — Use computed keys, object literals, optional properties and destructuring; distinguish absent properties from those present with undefined values.

2. **References and Copying** — Demonstrate shallow spread, nested aliasing and explicit structured data copying; avoid claiming that spread is a deep clone.

3. **Own, Inherited, and Enumerable Properties** — Inspect `Object.hasOwn`, `Object.keys`, descriptors, and prototype-chain lookup; explain consequences for untrusted key iteration.

4. **Prototypes and Delegation** — Trace property lookup through a prototype and demonstrate why shared inherited mutable data can surprise learners.

5. **`class` and Instance Semantics** — Use constructors, methods, private fields where appropriate and composition alternatives; explain how JavaScript classes relate to prototypes.

6. **Getters, Setters, and Descriptors** — Describe property accessors and descriptor flags; avoid unexpected side effects during logging, serialization or iteration.

7. **Data Parsing and Prototype Boundaries** — Test a record with keys such as `__proto__` and distinguish parsing from unsafe merging into application objects; prefer explicit allowlists and safe data structures.

8. **Formative Object Repair** — Diagnose a bug in copying, method binding, or inherited fields and provide executable regression tests.

### Module 6 — Collections, Iteration, and Structured Data

#### Outcomes

- APP18-O2
- APP18-O3
- APP18-O5
- APP18-O6
- APP18-O10

#### Lessons

1. **Arrays and Representation Invariants** — Distinguish sparse positions from explicit undefined entries, choose indexing and append operations, and trace mutation during traversal.

2. **Search, Sort, and Stable Expectations** — Write an explicit comparator, account for default string ordering and distinguish in-place sorting from non-mutating transformations.

3. **Maps and Sets** — Choose Map/Set versus plain objects and arrays; demonstrate key identity, insertion-order expectations and duplicates.

4. **Iterables, Iterators, and Generators** — Explain iterable and iterator protocols; implement a small generator and reason about lazy production versus eager allocation.

5. **String, JSON, and Data Shapes** — Parse and serialize JSON with explicit representation limits; identify unsupported values, cyclic structures and schema drift.

6. **Regular Expressions and Parsing Trade-offs** — Use bounded regular expressions for a suitable task while recognizing escaping, partial matches and the risk of pathological patterns; choose structured parsing for structured formats.

7. **Data Transformation Contracts** — Define invariants for filtering, grouping, deduplication or aggregation; check missing fields, duplicate keys and deterministic output.

8. **Formative Dataset Investigation** — Compare an array/object implementation with a Map/Set alternative and explain correctness, complexity and iteration effects on a synthetic fixture.

### Module 7 — Runtime Contracts, Errors, and Defensive Design

#### Outcomes

- APP18-O5
- APP18-O6
- APP18-O10

#### Lessons

1. **Static Assumptions versus Runtime Data** — Explain that a JavaScript type check is not a complete domain validator; separate untrusted input from the program's validated internal representation.

2. **Shape and Domain Validation** — Implement explicit validation for record shape, length, range, allowed keys and relationships; distinguish missing fields, null, wrong type and out-of-range values.

3. **Error Categories and Exceptions** — Use `throw` and `try`/`catch`/`finally` appropriately; distinguish programmer defects, expected invalid input and transient operational failures.

4. **Error Messages and Causes** — Preserve diagnostic context and error causes without leaking secrets or raw untrusted payloads into user-facing output.

5. **Safe Data Boundaries** — Avoid `eval`, unchecked dynamic execution and merging arbitrary object keys; apply allowlists to accepted inputs and outputs.

6. **Partial Processing and Atomicity** — Define the behavior when one dataset item fails: reject all, collect structured errors or proceed with documented partial results; test the decision.

7. **Refactoring without Behavioral Drift** — Reorganize code while retaining published input/output semantics, supported error categories and regression coverage.

8. **Formative Negative-Path Review** — Inject malformed JSON, unexpected fields, invalid numbers and duplicates; demonstrate failures remain controlled and observable.

### Module 8 — Modules, Interfaces, and Reusable Packages

#### Outcomes

- APP18-O7
- APP18-O9
- APP18-O10

#### Lessons

1. **ES Modules and Strict Semantics** — Export a small API, import it into a consumer and explain file/module scope, live bindings and strict-mode behavior.

2. **Module Evaluation and Cycles** — Trace a simple dependency graph, evaluation order and why cyclic module initialization can be confusing; refactor to avoid unnecessary cycles.

3. **Public API versus Implementation** — Define minimal exports, cohesive module responsibilities and a test seam; keep configuration and side effects outside pure domain logic.

4. **Resolution and Host Differences** — Explain how Node resolves local ESM paths and package export maps, and why imports that work under one host/build setup may not work in another.

5. **CommonJS Interoperability Boundaries** — Recognize legacy `require`/exports and selected ESM/CJS interoperability constraints without requiring a full dual-package publication system.

6. **Dependency Selection and Maintenance** — Distinguish runtime/development dependencies, package scripts and third-party supply-chain risk; prefer built-in tools when they meet requirements.

7. **Refactoring a Monolith** — Split an existing script into source, input validation and CLI adapter modules; compare independent unit tests before/after.

8. **Formative Interface Review** — Create a separate consumer for a small module and test misuse, missing exports and version-sensitive assumptions.

### Module 9 — Node.js Developer Tooling and Reproduction

#### Outcomes

- APP18-O1
- APP18-O7
- APP18-O9
- APP18-O10

#### Lessons

1. **Node Runtime Selection** — Choose a documented maintained runtime baseline and distinguish installed runtime, package manager and application execution host without prescribing a particular proprietary installer.

2. **Project Manifest and Scripts** — Create `package.json` with `type: module`, entry points and safe `scripts`; explain how scripts execute in a local working directory.

3. **Versions, Dependencies, and Lockfiles** — Explain version ranges versus resolved versions, package-lock provenance and why clean installation can differ from an unlocked install.

4. **Offline-Ready Fixture Strategy** — Use a built-in-only example or a supplied local package fixture to make required assessment execution reproducible without paid hosting, remote registries or account login.

5. **Install Scripts and Supply-Chain Risk** — Explain that package installation and scripts can execute untrusted code; audit declared scripts and use reviewed local inputs for required demonstrations.

6. **Environment and Configuration** — Separate harmless test fixtures from credentials, avoid committing secrets and compare host environment variables to JavaScript program arguments.

7. **Clean-Checkout Verification** — Document version, setup command, test command, input fixtures and known limitations; test from a fresh directory and explain dependency/tool mismatch symptoms.

8. **Formative Build Failure** — Investigate a missing module, incorrect package export or lockfile mismatch without rewriting version history to hide the cause.

### Module 10 — Asynchronous JavaScript and Scheduling

#### Outcomes

- APP18-O4
- APP18-O6
- APP18-O8
- APP18-O10

#### Lessons

1. **Synchronous Call Stacks** — Trace one stack from entry point to return or exception; distinguish language call semantics from host scheduling.

2. **Tasks, Microtasks, and Host Facilities** — Use observable examples to distinguish promise reaction jobs from selected host task scheduling; qualify ordering claims that depend on Node/browser APIs.

3. **Promise States and Composition** — Explain pending, fulfilled and rejected states, then/catch/finally behavior, returned promises and chaining errors.

4. **`async` and `await`** — Refactor a promise chain into `async`/`await` while preserving error propagation, returned results and cleanup.

5. **Parallelism versus Concurrency** — Contrast sequential awaits, bounded overlapping operations and CPU parallel execution; avoid claiming promises create threads or guarantee completion order.

6. **`Promise.all`, `allSettled` and Failure Policies** — Select coordination behavior for independent local tasks, identify early rejection versus settled results, and retain failures instead of swallowing them.

7. **Timeouts, Cancellation, and Ownership** — Explain that timeouts and AbortSignal are host/framework facilities rather than automatic promise cancellation; document resource ownership and when deeper service cancellation belongs to APP21.

8. **Uncaught Errors and Unhandled Rejections** — Reproduce and diagnose one sync throw and one async rejection; demonstrate an explicit error boundary and exit policy.

9. **Formative Event-Order Investigation** — Predict logged steps, execute the fixture, distinguish guaranteed from host-dependent ordering and explain a concurrency bug.

### Module 11 — Testing, Debugging, and Software Evolution

#### Outcomes

- APP18-O3
- APP18-O5
- APP18-O6
- APP18-O7
- APP18-O8
- APP18-O10

#### Lessons

1. **Assertions and Test Design** — Use Node's built-in test runner and assertions to organize tests around behavior rather than implementation details.

2. **Equivalence Classes and Boundaries** — Choose normal, empty, missing, malformed, duplicated, extreme and Unicode cases; explain why superficial line coverage alone does not prove correctness.

3. **Async Tests and Reproducibility** — Test fulfilled/rejected results and scheduling using deterministic deferred promises and test doubles rather than arbitrary sleeps.

4. **Runtime Diagnostics and Breakpoints** — Read stack traces and use debugger inspection to compare hypotheses with observed state; preserve reproducible steps.

5. **Property-Oriented Checks and Invariants** — Check simple invariants over generated or table-driven inputs and diagnose counterexamples without demanding an external property-testing framework.

6. **Performance and Complexity** — Estimate time/space growth and measure a bounded workload with appropriate noise disclosure; distinguish a microbenchmark from a production claim.

7. **Maintenance and Compatibility** — Apply a scoped new requirement to an existing module, protect public contracts and explain breaking versus backward-compatible changes.

8. **Formative Defect Investigation** — Reproduce a seeded data-processing or async defect, add a failing test, fix the root cause and explain the regression evidence.

### Module 12 — Integrated JavaScript Engineering and Defense

#### Outcomes

- APP18-O1
- APP18-O2
- APP18-O3
- APP18-O4
- APP18-O5
- APP18-O6
- APP18-O7
- APP18-O8
- APP18-O9
- APP18-O10
- APP18-O11

#### Lessons

1. **Selecting a Bounded Domain Problem** — Choose a local synthetic-record processor, task scheduler or similar program with deterministic data rules, identifiable users and a clear non-network execution boundary.

2. **Requirements and Acceptance Cases** — Document functional inputs/outputs, malformed records, duplicate behavior, performance bounds, error policy and change acceptance before implementation.

3. **Domain and Host Architecture** — Separate pure computation, stateful orchestration, local input/output and command-line entry points; explain what depends on ECMAScript versus Node.

4. **Incremental Implementation and Verification** — Build a feature slice, write representative negative tests, debug one actual failure and preserve failing-before/passing-after evidence.

5. **Asynchronous Integration** — Add one bounded asynchronous workflow using local/synthetic operations, with specified ordering, rejection propagation and cleanup behavior.

6. **Reproducibility and Security Review** — Verify a fresh checkout with recorded runtime and package steps; inspect dependency scripts, input validation, sensitive data handling and unsupported assumptions.

7. **Unfamiliar Change and Technical Defense** — Handle a new bounded rule or supplied counterexample, verify regressions and defend language semantics, module boundaries, performance and limitations against inspected code.

## Completion requirements

All **eleven required course outcomes** must be demonstrated through
the **five required summative assessments** below. Each assessment
has an explicit outcome scope and independent public success
criteria. A learner may extend the same evolving program across
assessments; five unrelated applications are **not** required.
The formative lesson investigations are not separate completion
checkpoints simply because they are listed.

| Required assessment | Required outcomes | Principal evidence |
| --- | --- | --- |
| `APP18-AS1` — JavaScript Semantics and Debugging Investigation | APP18-O1, APP18-O2, APP18-O3, APP18-O4 | Versioned source/fixtures, a prediction-versus-observation table, commands/runtime version, failing and passing regression cases, and a concise explanation of corrections and uncertainty |
| `APP18-AS2` — Data Contract and Collection Transformation | APP18-O2, APP18-O3, APP18-O5, APP18-O6, APP18-O7, APP18-O10 | Public data contract, ES module and local fixtures, negative/positive automated tests, a demonstrated malformed input, one maintained compatibility scenario, and written representation/complexity reasoning |
| `APP18-AS3` — Asynchronous Scheduling and Failure Diagnosis | APP18-O4, APP18-O6, APP18-O8, APP18-O10 | Runnable asynchronous fixture, event-order diagram/table, deterministic tests without timing-flaky sleeps, before/after defect reproduction, failure-policy notes and versioned runtime details |
| `APP18-AS4` — Node Tooling, Modules, and Maintainability Review | APP18-O1, APP18-O7, APP18-O9, APP18-O10 | Complete project source/manifest, tests and execution log from clean state, relevant lockfile/local fixture or rationale for zero dependencies, version data, a traced module defect and its fix |
| `APP18-AS5` — Modular JavaScript Utility and Engineering Defense | APP18-O1, APP18-O2, APP18-O3, APP18-O4, APP18-O5, APP18-O6, APP18-O7, APP18-O8, APP18-O9, APP18-O10, APP18-O11 | Version-controlled source and synthetic test data, README with runtime/commands, case-to-test matrix, normal and failure execution logs, meaningful regression test history, clean-checkout reproduction, change/diagnosis evidence, concise technical rationale and written/recorded/accessible defense |

### Shared execution, integrity, and review boundaries

- Use a documented maintained local Node.js baseline, an ordinary
  unprivileged account, a plain-text editor and freely available
  built-in test/assertion facilities. Record exact runtime and
  package-manager versions where their behavior matters.
- Required execution uses local synthetic or sanitized inputs,
  reviewed fixture dependencies and no mandatory external
  registry, credentials, paid tool, production account, or cloud
  deployment. Explain any initial toolchain installation separately
  from reproducible program execution and tests.
- Treat JavaScript `Promise` behavior as language-level; distinguish
  host-specific timers, event-loop phases, filesystem and
  `AbortSignal` implementation. Do not claim all Node/browser
  scheduling is identical or that a promise can inherently be
  canceled.
- Test normal, boundary and malformed values where applicable.
  Avoid relying on truthiness for values where 0, empty strings,
  false, null and absence have different domain meanings. Verify
  numeric precision, Unicode, copying and prototype assumptions
  when relevant to the chosen work.
- Do not use `eval` or execute data as commands; never include
  real secrets, tokens, private user data or unexplained third-party
  install scripts. External runtime inputs are not trustworthy
  merely because a test fixture is well formed.
- Automated test success does not demonstrate an understanding of
  closure capture, async ordering, failure policy or engineering
  trade-offs. Include reviewable predictions, inspected failures
  and concise mechanism-based explanations where assessed.
- A live presentation is not mandatory: provide a written,
  recorded or otherwise accessible defense against the same
  published outcome criteria. A reviewer may select an equivalent
  unforeseen bug or bounded change without imposing a hidden
  language, platform or account requirement.

### Required summative assessments

- **APP18-AS1** (required javascript semantics and debugging investigation)
  - Outcomes: APP18-O1, APP18-O2, APP18-O3, APP18-O4
  - Work: Given a small runnable project and a set of deliberately misleading examples, predict and then investigate coercion/equality, nullish/default handling, number precision, Unicode strings, lexical scope, closures, method receivers and parameter/object aliasing. Correct at least two genuine defects without altering unrelated behavior. Contrast at least one language-defined rule with a Node host facility.
  - Criteria: The predicted and observed results agree after reasoned correction; each identified issue is explained using accurate ECMAScript and host distinctions; fixes handle normal and boundary inputs; no silent numeric/Unicode data corruption is introduced. At least one closure or `this` defect and one conversion/precision defect have a reproducible before/after explanation.
  - Evidence: Versioned source/fixtures, a prediction-versus-observation table, commands/runtime version, failing and passing regression cases, and a concise explanation of corrections and uncertainty.

- **APP18-AS2** (required data contract and collection transformation)
  - Outcomes: APP18-O2, APP18-O3, APP18-O5, APP18-O6, APP18-O7, APP18-O10
  - Work: Implement a small reusable JavaScript module that validates and transforms synthetic JSON records. Publish the accepted input fields, missing/null/invalid-field policy, duplicate identity behavior, deterministic output contract and error shapes. Use a justified mix of object/array/Map/Set operations, with an explanatory test of shallow copying and inherited keys. Add one realistic requirements change without sacrificing prior cases.
  - Criteria: Valid records produce the stated deterministic output; unknown or malformed JSON/values are rejected or reported according to the specified policy; prototype-like keys cannot modify application behavior unexpectedly; duplicate, Unicode and numeric boundary cases are covered; sorting/comparison and aggregate computations behave as documented. The public export is testable independently, and complexity/representation trade-offs match the implementation.
  - Evidence: Public data contract, ES module and local fixtures, negative/positive automated tests, a demonstrated malformed input, one maintained compatibility scenario, and written representation/complexity reasoning.

- **APP18-AS3** (required asynchronous scheduling and failure diagnosis)
  - Outcomes: APP18-O4, APP18-O6, APP18-O8, APP18-O10
  - Work: Inspect a supplied event-ordering example and an asynchronous multi-item processing workflow. Explain call-stack, promise reaction and host scheduling boundaries; reproduce a swallowed rejection or unintended sequential/overlapping work defect; repair it with explicit failure propagation and bounded asynchronous coordination. Show the behavior when one item fails, when results settle in a different order, and when an operation is deliberately abandoned under an identified host mechanism.
  - Criteria: Scheduling predictions correctly qualify Node-specific behavior; no assumption confuses promise concurrency with CPU threads or promises with automatic cancellation. The repaired workflow has bounded in-flight work, deterministic test control, explicit success/rejection policy and no unhandled rejection in the tested paths; validation errors retain useful context without exposing secrets.
  - Evidence: Runnable asynchronous fixture, event-order diagram/table, deterministic tests without timing-flaky sleeps, before/after defect reproduction, failure-policy notes and versioned runtime details.

- **APP18-AS4** (required node tooling, modules, and maintainability review)
  - Outcomes: APP18-O1, APP18-O7, APP18-O9, APP18-O10
  - Work: Package the reusable component in an ES module project with a precise README, `package.json` scripts, a suitable supplied/generated lockfile when dependencies are used, and reproducible tests. Explain one host/module-resolution boundary, the implications of running dependency install scripts, and a real or seeded module/resolution/version defect. Reproduce the program from a new clean directory using free local tooling; no remote account or network is necessary during the assessment.
  - Criteria: Entrypoints and exports behave as documented in a fresh checkout; declared scripts and test command work under the recorded supported runtime; no hidden global dependency or secret is required. Package/dependency decisions, lockfile significance (or justified built-in-only choice), module-resolution diagnostics and recorded command safety are explained accurately.
  - Evidence: Complete project source/manifest, tests and execution log from clean state, relevant lockfile/local fixture or rationale for zero dependencies, version data, a traced module defect and its fix.

- **APP18-AS5** (required modular javascript utility and engineering defense)
  - Outcomes: APP18-O1, APP18-O2, APP18-O3, APP18-O4, APP18-O5, APP18-O6, APP18-O7, APP18-O8, APP18-O9, APP18-O10, APP18-O11
  - Work: Build or extend one substantial but bounded local JavaScript utility that processes synthetic records, exposes at least two cohesive modules, validates untrusted input and performs a controlled asynchronous task. Include a published acceptance-case matrix, normal and malformed input paths, explicit error/result policy, testable output and recorded algorithmic/representation decisions. Reuse qualifying results from APP18-AS2–AS4 rather than producing unrelated duplicate projects. Demonstrate an unfamiliar scoped change or counterexample, complete a clean-checkout reproduction and defend the chosen design in a reviewable format.
  - Criteria: Every stated required input/output rule is supported by reproducible tests and inspectable output; unsafe data cannot bypass required validation; async errors are handled without silent loss; bounded resource-use decisions match the fixture's needs; documented npm/Node setup works as claimed. The learner can explain a concrete value/scope/prototype or object behavior, the host boundary, a normal/failure trace, complexity, a verified repair and remaining limitations. The unfamiliar change is correctly incorporated without regressing published invariants; unnecessary networking, external accounts, or framework use is not demanded.
  - Evidence: Version-controlled source and synthetic test data, README with runtime/commands, case-to-test matrix, normal and failure execution logs, meaningful regression test history, clean-checkout reproduction, change/diagnosis evidence, concise technical rationale and written/recorded/accessible defense.

### Completion decision and revision safety

Completion requires a documented acceptable decision for each of
`APP18-AS1` through `APP18-AS5` with inspectable evidence,
collectively demonstrating `APP18-O1` through `APP18-O11`.
When the integrated assessment reuses an earlier artifact, the
reviewer must evaluate the *integrated and changed* behavior
rather than counting previous activity checkmarks as proof.

Failures that violate stated functional, safety, error-handling or
reproduction criteria require repair before a passing decision.
Other limitations must be honestly recorded and bounded; a
flawed language-model explanation cannot be replaced by a green
unit-test log alone. Preserve the applicable source revision,
assessment IDs, evidence locations and review decisions in
accordance with [OEE Evidence Rules](../../spec/evidence-rules.md).

This course is a `v0.2.0` **draft**, not learner-tested or
independently educationally verified. Its implementation adds
one new core capability to the current APP catalog; legacy APP
courses and historical learner records retain the meanings and
prerequisites attached to their own recorded revisions.
The eventual TypeScript, browser, Node backend and capstone
migrations require separate reviewed course changes.

### Public non-mandatory study references

These free references support investigation; they do not
replace the public course outcomes, assessments or criteria:

- [ECMA-262 language standard](https://ecma-international.org/publications-and-standards/standards/ecma-262/)
  for precise JavaScript language behavior.
- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
  for language mechanisms, reference examples and explanations.
- [MDN JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
  for script/module semantics and host distinctions.
- [Node.js Learn](https://nodejs.org/en/learn)
  for runtime behavior, package management, and diagnostics.
- [Node.js API documentation](https://nodejs.org/api/)
  for host-specific modules, package manifests and the built-in test runner.
