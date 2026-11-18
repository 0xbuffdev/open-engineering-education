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

### Module 1 — ECMAScript, Hosts and First Language Experiments

#### Outcomes

- APP18-O1
- APP18-O2
- APP18-O9

#### Lessons

1. **JavaScript's Place and First Local Program** — From prior SEF programming, inspect a short ES module with a supported local Node runtime; place JavaScript's browser origins and present-day uses in context while explaining why APP18 is neither browser DOM nor backend engineering.
2. **Language, Engine and Host Boundaries** — Classify syntax, ECMAScript semantics, engine execution and Node-provided process/filesystem/timer interfaces; contrast a portable expression with a host-only API using actual or supplied evidence.
3. **From Python Reasoning to JavaScript Semantics** — Translate a bounded, already-understood SEF computation; predict effects of nullish values, truthiness, equality, object aliasing and function binding before running examples rather than relearning general programming from zero.
4. **First Diagnostics and Reproduction** — Distinguish parse-time syntax errors from executed failures using a stack trace; record runtime/command and minimal fabricated inputs without installing remote packages or exposing secrets.

### Module 2 — Values, Equality, Precision and Text

#### Outcomes

- APP18-O2
- APP18-O3

#### Lessons

1. **Primitive Values and Bindings** — Distinguish undefined, null, Boolean, Number, BigInt, String and Symbol; inspect typeof's historical null behavior, let/const rebinding and mutation without treating typeof as complete validation.
2. **Equality, Truthiness and Missing Data** — Predict strict/abstract equality, falsy cases, optional chaining and nullish coalescing; explain where 0, false and empty text are legitimate rather than missing.
3. **Numeric Representation and Correctness** — Investigate binary floating-point precision, NaN, infinities, signed zero, safe-integer bounds and BigInt compatibility; choose explicit constraints instead of silently rounding identifiers or money.
4. **Text, UTF-16 and User-Visible Characters** — Compare UTF-16 code units, Unicode code points and grapheme clusters; show how naive string length/indexing can misinterpret user-visible text.
5. **Parsing and Conversion Boundaries** — Contrast explicit parsing and range checks with implicit numeric/string conversions, relational comparisons and accidental concatenation on realistic malformed input.
6. **Value-Model Investigation** — Given unseen value fixtures, predict, run, explain and repair at least one precision, coercion or Unicode defect; use version-specific host functionality only when disclosed.

### Module 3 — Control Flow, Abstraction and Functional Reasoning

#### Outcomes

- APP18-O3
- APP18-O10

#### Lessons

1. **Decisions and Unexpected Cases** — Use if, conditional expressions and switch with intentional fall-through and a published invalid-case policy; connect branches to acceptance criteria instead of syntax memorization.
2. **Iteration and Termination** — Choose bounded for, while and for-of loops; state termination/loop invariants and diagnose off-by-one behavior.
3. **Functions, Parameters and Result Contracts** — Use declarations, expressions and arrow functions with explicit returns, defaults, rest/destructured parameters as justified; test empty and invalid inputs.
4. **Higher-Order Transformations** — Pass functions as values; compare map/filter/reduce with a clear loop on the same dataset and defend behavior/readability rather than fashionable chaining.
5. **Recursion, Stack Depth and Alternatives** — Trace a recursive base case and failure boundary; select iteration when input depth or stack limits make recursion unsuitable.
6. **Decomposition and Pure Computation** — Separate deterministic domain transformations from logging, input and time; refactor an existing routine and check its unchanged behavior on a new case.

### Module 4 — Scope, Closures and Function Receivers

#### Outcomes

- APP18-O3
- APP18-O4
- APP18-O10

#### Lessons

1. **Lexical Binding and Initialization** — Trace block/function/module scope, shadowing and lexical declaration initialization, including the temporal dead zone and historical var behavior in a controlled example.
2. **Closures and Captured State** — Explain capturing bindings rather than value snapshots; build independent closures and reproduce a shared-state or loop-capture bug with observable feedback.
3. **Function Calls and this Binding** — Contrast method receiver binding, detached calls, call/apply/bind and arrow lexical this; predict a receiver failure before inspecting actual output.
4. **References, Parameters and Mutation** — Trace object identity, passed reference values and alias-visible mutation; avoid the incorrect claim that JavaScript arguments are passed by reference.
5. **Trace-Driven Scope Repair** — Use breakpoints or stacks to identify a closure/receiver/alias error, distinguish observation from speculation, and verify a minimal correction with independent tests.

### Module 5 — Objects, Prototypes, Copies and Classes

#### Outcomes

- APP18-O4
- APP18-O5
- APP18-O6

#### Lessons

1. **Object Properties and Absence** — Use literals, computed keys, destructuring and property lookup; distinguish absent own keys from inherited or present-with-undefined values.
2. **Identity, Mutation and Copy Semantics** — Compare aliases, object spread/shallow copying and a justified independent structured copy; detect nested-reference surprises using before/after observations.
3. **Prototype Lookup and Enumerability** — Trace own/inherited properties with Object.hasOwn, Object.keys and prototype chains; explain why enumeration and inherited mutable fields affect correct data handling.
4. **Classes and Delegation** — Explain class constructor/method/private-field mechanics as syntax over prototype-based behavior; compare a small class with composition without insisting on OOP for every task.
5. **Descriptors, Accessors and Trust** — Observe getter/setter side effects and property descriptors where they change iteration or data access; demonstrate that parsed data and inherited keys cannot be trusted without safe boundary rules.

### Module 6 — Collections, Iteration and Data Transformation

#### Outcomes

- APP18-O2
- APP18-O3
- APP18-O5
- APP18-O6
- APP18-O10

#### Lessons

1. **Arrays and Mutation Invariants** — Distinguish holes from explicit undefined elements, correct indexing and accumulation, and the effect of changing an array during traversal.
2. **Ordering, Search and Sorting** — Compare default string sort with explicit comparators, in-place versus copy-producing operations and deterministic handling of equal/duplicate values.
3. **Maps, Sets and Key Identity** — Choose arrays, plain records, Map or Set by required equality, iteration and uniqueness semantics; validate a surprising key-identity case.
4. **Iterables and Lazy Production** — Explain iterable/iterator protocols using for-of and a simple supplied generator; use lazy production only where its memory or sequencing effect matters.
5. **JSON Representation and Limits** — Explain parsing/serialization of structured records, including malformed JSON, unsupported values, cycles, surprising null/missing behavior and date/number representation constraints.
6. **Bounded Parsing and Aggregation** — Use a safe bounded regular expression only for suitable text and structured parsing for structured data; implement filtering/grouping or aggregation with a published deterministic result and boundary tests.

### Module 7 — Trust Boundaries, Runtime Contracts and Failures

#### Outcomes

- APP18-O5
- APP18-O6
- APP18-O10

#### Lessons

1. **Untrusted Data to Valid Domain State** — Design shape, allowed-key, type, range and relationship checks; distinguish absent, null, invalid and out-of-range values before trusting a parsed record.
2. **Prototype and Dynamic-Execution Hazards** — Show that JSON parsing alone does not cause prototype mutation, but unsafe merging/assignment can; protect domain keys with explicit allowlists or appropriate data structures, and reject eval or executable input.
3. **Error Classification and Diagnostic Context** — Use throw, try/catch/finally and error causes to separate malformed input, recoverable domain failure and programming defects; redact sensitive details from public diagnostics.
4. **Partial Batch Policy and Atomic Results** — Choose reject-all, collected errors or declared partial success for a data operation; test which valid state survives a failed member and avoid unsupported transactional claims.
5. **Contract-Preserving Revision** — Modify an input contract or implementation and verify existing successful and invalid cases, documenting any intentional incompatible change rather than swallowing exceptions.

### Module 8 — ES Modules, Interfaces and Cohesive Design

#### Outcomes

- APP18-O7
- APP18-O9
- APP18-O10

#### Lessons

1. **ES Modules and Live Bindings** — Build an export/import pair, explain strict semantics and module scope, and trace why an imported live binding is not an assignable local variable.
2. **Module Graphs and Initialization** — Inspect module evaluation and one cyclic dependency/early-access failure; remove an unnecessary cycle while preserving the public result.
3. **Public Interfaces and Side-Effect Ownership** — Choose minimal cohesive exports, place validation/domain logic behind a predictable API and isolate host-dependent I/O so consumers and tests can run independently.
4. **Resolution and CommonJS Boundaries** — Investigate Node ESM relative paths, package exports and a limited CommonJS interoperability case; distinguish runtime resolution from ECMAScript-defined module semantics.
5. **Modular Refactor and Contract Tests** — Split one bounded monolithic program into domain, validation and host-adapter modules; compare observable behavior and consumer tests before and after, with a deliberate misuse case.

### Module 9 — Node Project Tooling and Offline Reproduction

#### Outcomes

- APP18-O1
- APP18-O7
- APP18-O9
- APP18-O10

#### Lessons

1. **Supported Runtime and Package Manifest** — Choose and document a maintained Node baseline, ESM package identity, entry points and safe scripts; distinguish Node-host APIs from ECMAScript semantics.
2. **Dependency and Lockfile Decisions** — Explain zero-dependency built-in facilities versus reviewed local dependencies, version ranges, resolved lockfile behavior and the limits of offline reproducibility.
3. **Install-Script and Configuration Safety** — Inspect scripts/dependency provenance, synthetic configuration and environment variables; recognize untrusted installation hooks, avoid real secrets and do not require network on assessed execution.
4. **CLI Execution and Local Tests** — Run an ordinary-user Node module with a defined fixture and built-in test/assertion tools; compare documented exit behavior and command failure modes.
5. **Independent Clean-State Reproduction** — Recreate setup, scripts and tests from a fresh local copy, record versions and diagnostic evidence, and identify an intentionally missing export or configuration defect.

### Module 10 — Promises, Scheduling and Bounded Asynchrony

#### Outcomes

- APP18-O4
- APP18-O6
- APP18-O8
- APP18-O10

#### Lessons

1. **Call Stacks and Language versus Host Scheduling** — Predict synchronous execution and distinguish ECMAScript promise reaction jobs from browser/Node timer, I/O and task scheduling; avoid asserting universal event-loop phase ordering.
2. **Promise Settlement and Chains** — Trace pending, fulfilled and rejected promise states, then/catch/finally and propagated results; investigate a returned-versus-forgotten promise bug.
3. **Async and Await as Structured Promise Use** — Rewrite a chain with async/await while keeping errors and cleanup visible; explain that async functions yield promises rather than synchronous values.
4. **Sequential, Overlapping and CPU Work** — Compare repeated sequential awaits, controlled overlap and CPU parallelism; promises do not create threads or guarantee completion order.
5. **Composition, Early Failure and Noncancellation** — Choose Promise.all or allSettled by policy, show that Promise.all rejects early without canceling outstanding work, and distinguish settled-result order from completion order.
6. **Cancellation, Timeouts and Ownership** — Demonstrate a supported host cancellation signal with a cooperative local fixture; distinguish a timer/race from actual operation cancellation and locate detailed Node I/O cancellation in APP21.
7. **Deterministic Failure and Scheduling Repair** — Use manually controlled deferred promises to expose swallowed rejections, lost cleanup and unbounded concurrent work; repair with a bounded in-flight policy and deterministic tests rather than sleeps.

### Module 11 — Testing, Debugging and Change Reasoning

#### Outcomes

- APP18-O3
- APP18-O5
- APP18-O6
- APP18-O7
- APP18-O8
- APP18-O10

#### Lessons

1. **Behavioral Tests and Test Doubles** — Use built-in Node test/assertion facilities to inspect exported functions; choose test cases from required behavior, not source-line counts.
2. **Boundary, Invalid and Invariant Evidence** — Design empty, missing, duplicate, Unicode, numeric, nested-copy and malformed cases and check what an invariant can actually establish.
3. **Deterministic Async Verification** — Test fulfilled, rejected, out-of-order and abandoned work by controlled promise settlement without relying on arbitrary timing sleeps.
4. **Debugger-Guided Root Cause Analysis** — Inspect stack traces and variables, form a falsifiable hypothesis, reproduce a seeded defect, repair it and retain failing-before/passing-after evidence.
5. **Complexity and Measurement Limits** — Use established SEF algorithmic reasoning to justify representative time/space costs; qualify noisy local measurements rather than claiming production benchmarks.
6. **Compatible Evolution** — Change a module contract for an unfamiliar bounded requirement; distinguish compatible changes from breaking ones and re-run the independently relevant regression cases.

### Module 12 — One Modular JavaScript Utility and Technical Defense

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

1. **One Public Problem and Acceptance Contract** — Choose a bounded synthetic-record utility or equivalent; publish expected outputs, invalid/duplicate policies, resource limits and acceptance cases before altering code.
2. **Cohesive Modules and Verified Data Rules** — Integrate language-model corrections, validated transformations, objects and explicit error policies into the **same** evolving program assessed in APP18-AS1–AS4, referencing accepted evidence instead of rebuilding independent projects.
3. **Controlled Asynchronous Work** — Add a small local, bounded asynchronous feature with defined order, rejection and cleanup behavior; explain language versus host guarantees.
4. **Adversarial Change and Repair** — Take an unfamiliar bounded requirement or counterexample, predict effects, reproduce a failure, make a narrow correction and verify existing invariants.
5. **Independent Reproduction and Defense** — From a clean local checkout, execute the documented project and tests; present relevant evidence references and defend semantics, modularity, failure cases, performance limits and unresolved uncertainty.

## Completion requirements

All **eleven required course outcomes** must be demonstrated through
**five separately decidable summative assessments**, with one evolving
modular local JavaScript utility as the principal assessed artifact.
APP18-AS1 can begin as a supplied diagnostic fixture; APP18-AS2–AS4
can extend and investigate the same source; APP18-AS5 integrates those
verified results and requires a new bounded change and defense.
Reviewers may **reference previously accepted evidence**, not demand
five unrelated applications, repeated log packets or standalone labs
for every lesson. Formative exploration never silently gates completion.

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
  - Work: Investigate a supplied event-order example and a small asynchronous data workflow, preferably extending the AS2 utility. Predict synchronous stack order, ECMAScript promise reaction jobs and separately identified Node-host scheduling observations. Reproduce a swallowed rejection, unbounded overlap or unintended sequential-work defect and repair it using a bounded in-flight policy. Test differing settlement order, one failed item, and an abandoned operation using a **documented cooperative host mechanism**. In a separate controlled example, demonstrate that **`Promise.all` early rejection does not cancel other started operations**, and contrast this with `Promise.allSettled` outcome collection.
  - Criteria: Predictions distinguish language-level promise semantics from Node host facilities; a correct `Promise.all` counterexample shows in-flight work continuing after aggregate rejection, while claiming no automatic cancellation or CPU parallelism. The chosen work/failure policy is explicit, bounded and deterministically reproducible, with no unhandled rejections in assessed paths. A timeout or abandoned result is not falsely described as guaranteed cancellation of underlying work. Errors preserve safe context.
  - Evidence: Same-module or shared-utility source, annotated order/settlement/failure timeline, controlled deferred-promise tests **without arbitrary sleeps**, before/after failure and bounded-work observations, qualified host-specific cancellation notes and the runtime/version needed to reproduce them.

- **APP18-AS4** (required node tooling, modules, and maintainability review)
  - Outcomes: APP18-O1, APP18-O7, APP18-O9, APP18-O10
  - Work: Package **the evolving AS2/AS3 utility** as an ES module project with a clear README, `package.json` scripts and appropriate lockfile evidence **only if third-party dependencies are justified**. Explain ECMAScript-versus-Node module resolution, a relevant package `exports` or relative-path boundary, and the risk of dependency install scripts. Reproduce and repair one seeded module/resolution/version problem; verify clean local execution/tests **without a registry fetch** using built-ins or supplied reviewed fixtures.
  - Criteria: Entrypoints and exports behave as documented in a fresh checkout; declared scripts and test command work under the recorded supported runtime; no hidden global dependency or secret is required. Package/dependency decisions, lockfile significance (or justified built-in-only choice), module-resolution diagnostics and recorded command safety are explained accurately.
  - Evidence: Complete project source/manifest, tests and execution log from clean state, relevant lockfile/local fixture or rationale for zero dependencies, version data, a traced module defect and its fix.

- **APP18-AS5** (required modular JavaScript utility and independent defense)
  - Outcomes: APP18-O1, APP18-O2, APP18-O3, APP18-O4, APP18-O5, APP18-O6, APP18-O7, APP18-O8, APP18-O9, APP18-O10, APP18-O11
  - Work: Complete **the one cumulative local utility** developed in APP18-AS1–AS4, processing synthetic records through at least two cohesive modules with runtime validation, a documented result/error policy, proportionate tests and a bounded asynchronous operation. Cite qualifying prior accepted evidence instead of resubmitting separate implementations. Handle an **unfamiliar, reasonably scoped rule change or supplied counterexample**, demonstrate a correction and regression result, then independently reproduce and defend the implementation, including its language/host boundary, constraints and technical limitations.
  - Criteria: Every stated required input/output rule is supported by reproducible tests and inspectable output; unsafe data cannot bypass required validation; async errors are handled without silent loss; bounded resource-use decisions match the fixture's needs; documented npm/Node setup works as claimed. The learner can explain a concrete value/scope/prototype or object behavior, the host boundary, a normal/failure trace, complexity, a verified repair and remaining limitations. The unfamiliar change is correctly incorporated without regressing published invariants; unnecessary networking, external accounts, or framework use is not demanded.
  - Evidence: A single version-controlled source/fixture package with clean local README commands, an indexed acceptance/outcome map **referencing prior evaluated AS1–AS4 evidence**, the unfamiliar-change counterexample and repair/regression trace, necessary runtime/host observations, material limits and a reviewable written, recorded or accessible defense. No second program or duplicate evidence bundle is required.

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

This course remains a `v0.2.0` **draft**, not learner-tested
or independently educationally verified. The APP catalog already
contains separate TypeScript (APP19), browser (APP2), Node service
(APP21), React (APP20), backend (APP3) and capstone (APP9) course
definitions; their distinct competencies remain outside this
JavaScript language-and-local-tooling course. Historical learner
decisions remain attributable to the source/specification
revision under which they were evaluated, without automatic
equivalence or retroactive completion judgments.

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
