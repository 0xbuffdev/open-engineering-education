# APP19 — TypeScript Programming

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `core`
**Prerequisites:** [APP18](APP18.md) — JavaScript Programming
**Duration:** 10–14 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (provisional; revise with learner and reviewer evidence)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Turn JavaScript programming competence into the ability to reason
precisely about static contracts for maintainable application code.
Model values and objects, understand TypeScript's structural
compatibility, use narrowing and discriminated unions, create
reusable generic APIs, and configure the compiler so the static
guarantees are demonstrable. Cross the type/runtime boundary
deliberately: data from JSON or other external sources must be
validated with actual JavaScript behavior, not merely asserted to
have a TypeScript type.

[APP18](APP18.md) already teaches JavaScript semantics, async
promises, error handling, ES modules, tests and basic Node/npm
development tooling. APP19 builds on those competencies rather
than re-teaching them. A learner should be able to explain why
TypeScript improves developer feedback yet **does not change**
JavaScript's runtime values, guarantee safe execution, validate
unknown data, or substitute for testing and review.

Use the TypeScript compiler and free local tooling to build a
small typed library or application slice. Teach selected advanced
type operations only where they clarify a meaningful data
contract; avoid type-level tricks whose complexity overwhelms
the underlying engineering problem. Build and examine usable
public modules and declarations, including the limits of
declaration accuracy and version compatibility.

This is **not** a React, DOM, CSS, Node HTTP-service, backend
framework, Rust or large library-publication specialization.
Browser engineering belongs to APP2, React to APP20,
Node.js backend runtime to APP21, framework services to APP3,
and advanced TypeScript–Rust interoperability to optional APP15.
A Node runtime is used for local execution and developer tooling,
not as a required server implementation.

TypeScript compiler installation may use an accessible public
download or a provided/preinstalled local toolchain. Required
exercises must run and be reviewable after setup with synthetic
files, local modules, fixtures and tests; no remote registry
access, login, paid textbook, production host or proprietary
service is mandatory. If a chosen test fixture includes a
dependency, document how the exact artifact can be made
available locally and inspected. Separate tooling setup
limitations from assertions about runtime behavior.

Modern Node versions may strip some erasable TypeScript syntax
and execute the remaining JavaScript, but this **does not**
type-check a program or implement `tsconfig.json` semantics.
Teach a documented `tsc` checking workflow and a separate
verified JavaScript execution path. Avoid tying outcomes to
an experimental feature or a specific tool release when an
open, reproducible equivalent exists.

Workload and duration are planning estimates, not evidence of
course effectiveness. Build from worked examples through
bounded changes, compiler investigations and runtime
counterexamples toward an independently explained interface.
Module activities are formative unless the completion section
explicitly requires their evidence.

## Learning outcomes

- **APP19-O1:** Explain TypeScript's relationship to JavaScript, distinguish type checking from JavaScript emission and execution, and investigate why a successful type check cannot establish runtime correctness or input safety.
- **APP19-O2:** Model representative JavaScript values and state with inferred, annotated, literal, union, intersection, tuple and immutable-facing types; explain widening, optionality and assignment constraints.
- **APP19-O3:** Define and evaluate structural object contracts using type aliases, interfaces, optional and readonly members, index signatures and excess-property checks; identify what those checks do not guarantee at runtime.
- **APP19-O4:** Construct discriminated unions and implement control-flow narrowing with exhaustive case analysis; demonstrate a safe change when a new union variant or missing-state case is introduced.
- **APP19-O5:** Distinguish evidence-based narrowing from assertions and unsound predicates; apply `unknown`, `never` and appropriately justified `any` while identifying type holes and their operational consequences.
- **APP19-O6:** Type functions, callbacks, generic async results and error-aware APIs; reason about call signatures, overloads, parameter compatibility and variance without replacing JavaScript runtime error handling.
- **APP19-O7:** Design reusable generic functions and data structures using inference, constraints and `keyof`/indexed-access relationships; preserve connections between inputs and outputs without unnecessary assertions.
- **APP19-O8:** Apply appropriate utility, mapped, conditional and template-literal types to express bounded transformations of existing contracts; diagnose when type complexity obscures domain intent or introduces unsafe assumptions.
- **APP19-O9:** Configure a strict TypeScript project, distinguish compiler diagnostics from runtime exceptions, explain relevant module/target/resolution settings, and reproduce either type-only checking or emitted JavaScript behavior on a declared toolchain.
- **APP19-O10:** Design, import and evolve public typed module and package interfaces, including type-only imports, declaration files, JavaScript interoperability and compatibility limitations; distinguish types from runtime exports.
- **APP19-O11:** Validate untrusted runtime data before granting it an internal TypeScript type, test malformed and version-shifted inputs, and defend the boundary between an external payload and a checked domain value.
- **APP19-O12:** Improve a small existing JavaScript/TypeScript application or library through a maintained typed contract, meaningful tests, clean reproduction, an unfamiliar bounded change and a reviewable technical defense.

## Modules

### Module 1 — From JavaScript to TypeScript

#### Outcomes

- APP19-O1
- APP19-O2
- APP19-O9

#### Lessons

1. **Course Orientation and History** — Situate TypeScript as a typed development layer over JavaScript, from its motivations to modern use; identify why language and tooling evolution does not change the JavaScript runtime contract.

2. **Review of APP18 JavaScript Semantics** — Recall objects, closures, promises, ESM, runtime validation and tests before introducing annotations; inspect an existing JavaScript utility and its verified failure cases.

3. **Types, Type Checking and JavaScript Execution** — Observe type errors independently of running code; compare `tsc --noEmit`, emitted JavaScript, and Node's limited type stripping where supported.

4. **The Compiler, Language Service and Host** — Differentiate the compiler's static analysis, editor language services, JavaScript output and execution host; identify assumptions from external declaration files.

5. **First Strict TypeScript Program** — Write a typed function, run a real type check with a locally available TypeScript compiler and execute the intended JavaScript output or supported erasable syntax.

6. **Prediction Before Compilation** — Predict which operations type-check and which fail, then verify; distinguish diagnostics from actual JavaScript exceptions and value changes.

7. **Study and Toolchain Boundaries** — Record a compiler/runtime baseline, avoid real credentials and online-only tooling, and explain how type-checking dependencies can be reproduced with provided local files.

### Module 2 — Inference, Everyday Types and Literal Precision

#### Outcomes

- APP19-O1
- APP19-O2
- APP19-O5

#### Lessons

1. **Annotations and Contextual Inference** — Use meaningful inference for local values and explicit annotations for public contracts; observe contextual typing in functions and collections.

2. **Primitive, Array and Tuple Models** — Represent strings, numbers, booleans, optional elements, tuples, arrays and readonly array views with correct mutation assumptions.

3. **Literal Types and Widening** — Distinguish a broad `string` from specific literal unions; observe assignment behavior under `let`, `const` and explicit contexts.

4. **Null and Undefined Under Strict Checking** — Use `strictNullChecks` and meaningful optionality; do not confuse absence, `undefined`, `null`, empty string and zero.

5. **Union and Intersection Meaning** — Explain alternatives versus combined requirements using nontrivial domain examples; identify impossible intersections rather than treating them as runtime merging.

6. **`unknown`, `any` and `never`** — Compare the guarantees and hazards of each, including `any` propagation, untrusted `unknown` and impossible/exhausted states.

7. **`as const` and `satisfies`** — Distinguish expression-level literal preservation, validating assignment to a target type, and unsafe assertion; demonstrate where none supplies runtime validation.

8. **Formative Investigation: Inference Gone Wrong** — Repair a widening or nullability bug and explain a compiler warning without papering it over with `any` or a non-null assertion.

### Module 3 — Structural Object Contracts and Compatibility

#### Outcomes

- APP19-O2
- APP19-O3
- APP19-O5

#### Lessons

1. **Types and Interfaces** — Define complementary object shapes and compare extension and intersection without declaring the constructs universally interchangeable.

2. **Structural Compatibility** — Inspect why a value with additional fields can satisfy a structural contract; distinguish this from nominal identity and runtime schema validation.

3. **Fresh Object Checks and Assignment** — Reproduce excess-property behavior for fresh literals versus variables; explain why a passing assignment is not an allowlist for external data.

4. **Required, Optional and Readonly Members** — Specify presence semantics and readonly access, noting that TypeScript's `readonly` does not necessarily freeze an object at runtime.

5. **Nested Objects, Tuples and Recursive Shapes** — Model a bounded nested configuration or tree with meaningful identifiers and optional branches; identify representational edge cases.

6. **Index Signatures and Records** — Choose explicit property shapes, `Record`, index signatures or Maps by use case; investigate the consequences of unrestricted keys.

7. **Classes, Implements and Visibility** — Explain compile-time `implements` and access modifiers versus runtime behavior; prefer composition where it produces clearer contracts.

8. **Formative Contract Review** — Review an object type with contradictory optionality or a hidden excess-property assumption and create a failing type expectation.

### Module 4 — Control-Flow Analysis and Exhaustive State Modeling

#### Outcomes

- APP19-O2
- APP19-O4
- APP19-O5

#### Lessons

1. **Union Narrowing with Runtime Checks** — Trace `typeof`, equality, null checks, `in` and `instanceof` on actual JavaScript values including null and inherited properties.

2. **Discriminated Unions** — Encode a request lifecycle or domain result with distinct tags and variant-specific data; avoid a bag of loosely related optional fields.

3. **Truthiness and Empty Values** — Show how broad truthiness guards can lose valid zero or empty-string data and how precise checks preserve contract meaning.

4. **Narrowing Across Assignments and Callbacks** — Inspect when control-flow facts are invalidated or maintained and why mutable aliasing can undermine a simplifying assumption.

5. **Exhaustiveness with `never`** — Write a `switch` that checks unreachable cases and demonstrate an appropriate compiler failure when a new variant is added.

6. **Assertions, Type Predicates and Assertion Functions** — Build a sound predicate from actual runtime checks; demonstrate that a predicate signature alone cannot prove a runtime condition.

7. **Error and Result Shapes** — Distinguish expected validation errors from exceptional programming faults; model honest success/error outcomes without depending on TypeScript for runtime catching.

8. **Formative Variant Migration** — Add a new state to an existing union, locate affected consumers, and repair the code while retaining negative-path tests.

### Module 5 — Functions, Callbacks and Asynchronous Contracts

#### Outcomes

- APP19-O5
- APP19-O6
- APP19-O10

#### Lessons

1. **Typed Parameters, Returns and Function Values** — Declare callable contracts and understand how inference works across implementations and consumers.

2. **Optional, Default and Rest Parameters** — Distinguish omitted values and defaults from callable overload contracts; test behavior as well as assignability.

3. **Contextual Typing of Callbacks** — Use callback contracts for array operations, events or local abstractions; inspect accidental implicit-any surfaces.

4. **Parameter Compatibility and Variance** — Explain soundness risks involving callback parameter narrowing and why strict checking matters; contrast function parameters with method positions as necessary.

5. **Overloads, Unions and Generics** — Choose overloads only when they express real input/output relationships better than a union or generic; verify the implementation supports them.

6. **Generic Promise and Async Result Types** — Type promise-producing APIs, expected errors and result unions; demonstrate runtime rejection paths beyond TypeScript's return type.

7. **`this` Parameters and Class Methods** — Model receiver-sensitive methods appropriately without hiding APP18's JavaScript call-context behavior.

8. **Formative Callback Repair** — Diagnose a consumer/compiler mismatch and one runtime error in an async callback; retain both static and runtime tests.

### Module 6 — Generic Abstractions and Relational Type Design

#### Outcomes

- APP19-O3
- APP19-O6
- APP19-O7

#### Lessons

1. **Why Generic Parameters Exist** — Preserve a relationship between input and output types; contrast `unknown`, a union and a generic for a concrete operation.

2. **Inference and Explicit Type Arguments** — Observe inferred type parameters from calls and use explicit arguments only where they convey information the compiler cannot infer.

3. **Constrained Generics** — Apply `extends` constraints to object keys, records or collections without assuming they validate runtime values.

4. **`keyof` and Indexed Access** — Write type-safe property lookup preserving the relationship between a key and its value while considering optional keys.

5. **Generic Collections and Result Containers** — Implement a small typed index, page of results or error-bearing container with clear invariants and tests.

6. **Type Parameter Defaults and Inference Limits** — Review when defaults and multiple type parameters improve an API and when they increase complexity.

7. **Safe Reuse versus Assertions** — Compare a well-typed generic implementation against an `as any` shortcut and explain what actually breaks in the latter.

8. **Formative Generic Refactor** — Replace duplicated record functions with a bounded generic implementation and verify both caller-specific static expectations and runtime behavior.

### Module 7 — Type Transformations and Useful Utility Types

#### Outcomes

- APP19-O3
- APP19-O7
- APP19-O8

#### Lessons

1. **Mapped Utility Types** — Use `Partial`, `Required`, `Readonly`, `Pick` and `Omit` as transformations of existing definitions; acknowledge their compile-time nature.

2. **Key Remapping and Modifiers** — Create an understandable mapped type involving optional or readonly modifiers, justified by an actual library requirement.

3. **Conditional Type Relationships** — Represent a bounded type selection based on a generic parameter; distinguish type-level branching from JavaScript runtime conditionals.

4. **Distributive Conditional Types** — Demonstrate how a naked generic parameter distributes over a union and how a tuple wrapper changes behavior.

5. **`infer` and Standard Utility Types** — Inspect `ReturnType`, `Parameters` and an appropriate inference example without building an unnecessary type-level programming language.

6. **Template Literal and Indexed Types** — Express a small constrained event-name or message-key contract and assess readability/maintenance costs.

7. **When Not to Use Advanced Types** — Compare a complex conditional/mapped type to a clear interface or explicit domain union; select the simplest design that preserves correctness.

8. **Formative Type Evolution** — Introduce a versioned field, examine type transformation behavior, and fix a misleading type-level abstraction.

### Module 8 — Compiler Configuration, Emission and Diagnostics

#### Outcomes

- APP19-O1
- APP19-O5
- APP19-O9

#### Lessons

1. **The `tsconfig.json` Project Model** — Explain config discovery, included/excluded files, project directories and the risks of relying on editor-only settings.

2. **Strict Checking and Diagnostic Categories** — Use `strict`, null checks and implicit-any diagnostics; evaluate `noUncheckedIndexedAccess` and `exactOptionalPropertyTypes` with concrete trade-offs.

3. **Target, Library and JavaScript Output** — Distinguish syntax emission targets and ambient library declarations from available runtime APIs; show why `lib` does not install a polyfill.

4. **`noEmit` versus Compiled JavaScript** — Compare an independent type-check step with emitting executable JavaScript; verify an actual output and explain the behavior of erased types.

5. **Modules and Resolution Modes** — Explain Node ESM, `module`/`moduleResolution`, file extensions and package export maps; do not assume every environment resolves the same specifiers.

6. **Native Node Type Stripping** — Inspect supported erasable syntax in a declared Node baseline, why Node does not read `tsconfig` or type-check, and when a regular `tsc` workflow is required.

7. **Type Imports, Declaration-only Outputs and Source Maps** — Distinguish `import type`, value exports, `.d.ts` artifacts and debugging source positions; avoid treating declarations as runtime code.

8. **Formative Configuration Failure** — Repair a mismatched target/module setting or phantom runtime API after recording the original diagnostic and observed runtime behavior.

### Module 9 — Typed Modules, Public APIs and JavaScript Interoperability

#### Outcomes

- APP19-O3
- APP19-O6
- APP19-O9
- APP19-O10

#### Lessons

1. **Designing a Public Typed Surface** — Use named exports, cohesive modules and a public contract that consumers can exercise without seeing private implementation details.

2. **Type-only and Value Imports** — Demonstrate the distinction with a local ESM module and identify a runtime failure caused by treating erased symbols as values.

3. **Declarations and Ambient Assumptions** — Inspect generated or hand-authored `.d.ts` declarations; explain that a declaration describes expected types, not guaranteed live behavior.

4. **Consuming a JavaScript Module** — Type a bounded existing JavaScript API with a declaration or suitable migration strategy and verify it against actual JavaScript behavior.

5. **Package Boundaries and Exports** — Explain a documented `package.json` export surface, relative import specifiers and consumer support under a chosen host/module target.

6. **API Evolution and Compatibility** — Evaluate a change to required/optional fields or result variants against static consumers, runtime fixtures and prior behavior.

7. **Structural Types versus Trusted Implementations** — Explain why a consumer may conform structurally yet fail domain validation; use contract tests to reinforce trust boundaries.

8. **Formative Consumer Repair** — Create two independent local consumers, change the public API and diagnose both compile-time and runtime consequences.

### Module 10 — Runtime Data Boundaries and Security

#### Outcomes

- APP19-O4
- APP19-O5
- APP19-O10
- APP19-O11

#### Lessons

1. **Types Are Erased at Runtime** — Show that a cast, interface, generic or successful `tsc` run does not validate an HTTP-like JSON payload or filesystem data.

2. **`unknown` as the Entry Boundary** — Parse a synthetic JSON value as `unknown`, validate presence, types, lengths, finite numbers and allowed tags before constructing a domain value.

3. **Missing versus Optional versus Null** — Evaluate omitted fields, `undefined`, `null` and schema-version changes with explicit policies rather than accidental narrowing.

4. **Safe Predicates and Assertion Contracts** — Demonstrate an intentionally unsound type guard and repair it using executable tests and an actual runtime check.

5. **Compatibility and Versioned Data** — Support a declared version migration or reject unsupported versions with a testable, nonambiguous error rather than asserting an old payload is new.

6. **Error Propagation and Privacy** — Return useful typed errors, avoid logging sensitive raw values and distinguish recoverable bad input from an internal programming failure.

7. **Prototype and Key Safety** — Check suspicious object fields, inherited properties and arbitrary keys before merging or indexing untrusted records; use explicit allowlists and safe maps.

8. **Formative Adversarial Fixture** — Apply malformed, additional-field, duplicate and wrong-type fixtures to a typed parser; show that runtime acceptance matches the documented policy.

### Module 11 — Gradual JavaScript Migration, Testing and Maintainability

#### Outcomes

- APP19-O1
- APP19-O7
- APP19-O9
- APP19-O10
- APP19-O11
- APP19-O12

#### Lessons

1. **Audit an Existing JavaScript Program** — Start from a tested APP18-style module, identify implicit contracts, input sources, undefined behavior and an appropriately small migration boundary.

2. **JSDoc and Incremental Typing** — Compare checkable JavaScript/JSDoc with moving selected files to TypeScript; explain why a migration can proceed without rewriting all modules.

3. **Third-party and Missing Declarations** — Classify legitimate ambient type packages versus unsafe ad-hoc declarations, and identify risks of treating third-party declarations as ground truth.

4. **Static Negative Tests** — Write compiler-expectation tests or captured diagnostics for a deliberate misuse; distinguish asserting a type failure from testing runtime behavior.

5. **Runtime and Contract Tests** — Retain Node tests for normal, invalid and async rejection paths; demonstrate a type-safe module with a runtime-invalid payload.

6. **Debugging and Source Mapping** — Trace a failure across TS source, emitted JS and host stack traces with documented tooling conditions, and explain misleading error locations.

7. **Refactoring Without Changing Semantics** — Preserve JS runtime behavior while improving module types, avoid `as any` suppression, and record a justified compatibility decision.

8. **Formative Maintenance Request** — Implement a bounded feature in a partially typed codebase, verify a regression and explain unresolved type holes.

### Module 12 — Integrated TypeScript Library and Engineering Defense

#### Outcomes

- APP19-O1
- APP19-O2
- APP19-O3
- APP19-O4
- APP19-O5
- APP19-O6
- APP19-O7
- APP19-O8
- APP19-O9
- APP19-O10
- APP19-O11
- APP19-O12

#### Lessons

1. **Define a Small Typed Library Problem** — Choose a self-contained command processor, typed configuration parser or event/result processing library with synthetic inputs, explicit clients and a meaningful trust boundary.

2. **Publish Domain Types and Acceptance Cases** — Specify input/output contracts, invalid data, optional fields, versioning and observable state transitions before implementing types.

3. **Compose Narrowing and Generics** — Build cohesive reusable data-processing operations with structural contracts, bounded generic relationships and exhaustively checked state variants.

4. **Validate before Trusting** — Implement actual runtime parsing/validation from `unknown` and demonstrate a malicious or malformed example that a cast would falsely accept.

5. **Verify Compilation and Runtime Independently** — Run strict static checks, normal and negative runtime tests and a clean-install or pre-provisioned/offline verification path with recorded tool versions.

6. **Evolution and Consumer Compatibility** — Add a new variant or data field and demonstrate which type-level and runtime consumers need amendment, using a structured compatibility note.

7. **Unfamiliar Change and Technical Defense** — Respond to a new bounded client request, repair one broken assumption and defend compile-time versus runtime guarantees, API design, and recorded limits.

## Completion requirements

All **twelve required course outcomes** must be demonstrated
through the **five required summative assessments** below.
The assessments share a coherent set of typed module and
consumer artifacts where appropriate. Formative investigations
and lesson activities are preparation, not separate mandatory
completion evidence merely because they are listed.

| Required assessment | Outcomes evaluated | Principal evidence |
| --- | --- | --- |
| `APP19-AS1` — Static Modeling and Structural Compatibility Review | APP19-O1, APP19-O2, APP19-O3, APP19-O5, APP19-O9 | TS source, compiler configuration and diagnostics, a prediction-versus-observation table, executable JS tests or counterexamples, repaired definitions and a concise distinction between checking and execution |
| `APP19-AS2` — Discriminated State and Runtime Validation Investigation | APP19-O2, APP19-O4, APP19-O5, APP19-O11 | Union and validation source, negative/normal fixture matrix, compiler diagnostics before/after the new variant, executable tests, and explanation of type predicates, `never` and the runtime trust boundary |
| `APP19-AS3` — Generic API and Type Transformation Review | APP19-O3, APP19-O6, APP19-O7, APP19-O8, APP19-O10 | Typed module, two local consumer fixtures, compiler-positive and compiler-negative test evidence, runtime tests for callback/async behavior, public API contract and justification of type complexity and limitations |
| `APP19-AS4` — Compiler, Module, and JavaScript Migration Audit | APP19-O1, APP19-O5, APP19-O9, APP19-O10, APP19-O12 | Migrated source, original JS behavior fixtures, `tsconfig |
| `APP19-AS5` — Typed Library Evolution and Engineering Defense | APP19-O1, APP19-O2, APP19-O3, APP19-O4, APP19-O5, APP19-O6, APP19-O7, APP19-O8, APP19-O9, APP19-O10, APP19-O11, APP19-O12 | Versioned source and interface documentation, fixture and consumer matrix, reproducible `tsc`/runtime commands and test results, migration/change diff, negative-path reproduction, compatibility note, and written/recorded/otherwise accessible technical defense |

### Shared environment, assessment and trust boundaries

- Use a declared supported TypeScript compiler and a maintained
  local JavaScript runtime. Record relevant compiler, Node,
  module and configuration versions, working directory,
  execution commands, and assumptions about input data.
- Run **static** compiler checks and **runtime** tests
  separately: `tsc --noEmit` (or equivalent local compiler
  invocation) does not execute code, and successful Node
  execution or native TypeScript type stripping does not prove
  static correctness. If emitting JavaScript, inspect the output.
- Use locally stored synthetic datasets and independent local
  consumers. A paid cloud service, real user account, public
  endpoint, live customer data, remote test harness or
  proprietary editor must not be required for passing evidence.
- Define which inputs are trusted, which enter as `unknown`,
  and which are accepted only after runtime validation.
  Test empty/missing/null cases, malformed values, duplicate
  identities, unexpected tags, and compatibility changes when
  those scenarios are meaningful to a given contract.
- A type assertion, declaration file, assertion function or
  user-defined type predicate **does not by itself check**
  the data it describes. Reject misuse of `any` that makes
  the required assessment impossible to evaluate. Do not
  equate structural compatibility with security validation.
- Avoid executable untrusted package scripts and real
  credentials in examples. Do not require an online registry
  at the point of assessment; document a preinstalled
  compiler or supplied verified local toolchain and any
  necessary optional dependencies.
- Different valid module or execution configurations may
  satisfy the same outcome. Explanations must describe the
  actual documented baseline rather than assume Node
  implements every compilation or module-resolution feature.
- Static diagnostics, positive/negative runtime tests and
  technical explanation have **different evidentiary roles**.
  A clean compiler result cannot replace malformed-input
  runtime tests or proof of independent understanding.
- The learner may give the technical defense in a written,
  recorded, synchronous or equivalent accessible form
  against the same public criteria. An unfamiliar variant
  may be selected, but must not introduce an unpublished
  framework, vendor or language prerequisite.

### Required summative assessments

- **APP19-AS1** (required static modeling and structural compatibility review)
  - Outcomes: APP19-O1, APP19-O2, APP19-O3, APP19-O5, APP19-O9
  - Work: Starting with supplied JavaScript record and callback examples, predict static acceptance/rejection for annotated versus inferred values, literals, nullish fields, structural objects, excess properties, readonly views, tuples and `unknown`/`any`. Implement a small domain model and repair at least two cases where an asserted or overly broad type gives a misleading guarantee. Execute the corresponding JavaScript to compare static and runtime behavior.
  - Criteria: Predictions and compiler observations are consistent with a stated strict `tsconfig`; type definitions preserve missing/null/optional and literal distinctions; structural compatibility is explained accurately; `readonly` is not claimed to freeze runtime objects, and fresh-literal excess property checks are not misrepresented as runtime validation. At least one intentionally incorrect assertion and one runtime-invalid case are documented and corrected.
  - Evidence: TS source, compiler configuration and diagnostics, a prediction-versus-observation table, executable JS tests or counterexamples, repaired definitions and a concise distinction between checking and execution.

- **APP19-AS2** (required discriminated state and runtime validation investigation)
  - Outcomes: APP19-O2, APP19-O4, APP19-O5, APP19-O11
  - Work: Implement a typed result/state model with success, invalid input and explicitly recoverable failure variants for a local synthetic request or transaction. Define a validator that accepts `unknown` JSON and returns a validated internal value or a documented structured error. Inject an additional union variant and a schema version mismatch, then update the consumers so exhaustiveness and runtime behavior remain correct.
  - Criteria: No invalid payload is trusted solely through an `as` cast or unsound type guard; malformed, missing, null, extra-field and wrong-version cases follow a documented acceptance/rejection policy. Control-flow narrowing is valid, new variants produce a meaningful compile-time exhaustiveness signal, and negative runtime tests demonstrate controlled failure without leaking sensitive test data.
  - Evidence: Union and validation source, negative/normal fixture matrix, compiler diagnostics before/after the new variant, executable tests, and explanation of type predicates, `never` and the runtime trust boundary.

- **APP19-AS3** (required generic api and type transformation review)
  - Outcomes: APP19-O3, APP19-O6, APP19-O7, APP19-O8, APP19-O10
  - Work: Create a small reusable TypeScript module/library for a bounded data-processing or typed-event task. Provide one genuinely relational generic API, constrained keys/indexed access, and a justified utility/mapped/conditional type. Include an asynchronous or callback-consuming function with explicit result/error semantics. Supply two independent consumers and deliberately attempt invalid uses to demonstrate the boundary of the declared interface.
  - Criteria: Input/output generic relationships hold for representative different concrete types; selected transformations preserve intended required/optional and readonly semantics without obscuring runtime assumptions. Misuse cases are rejected by strict checking, valid consumers run as documented, callback or async behavior remains correct at runtime, and no `any` assertion masks a fundamental library defect. The learner defends why simpler types were or were not sufficient.
  - Evidence: Typed module, two local consumer fixtures, compiler-positive and compiler-negative test evidence, runtime tests for callback/async behavior, public API contract and justification of type complexity and limitations.

- **APP19-AS4** (required compiler, module, and javascript migration audit)
  - Outcomes: APP19-O1, APP19-O5, APP19-O9, APP19-O10, APP19-O12
  - Work: Migrate an existing bounded APP18 JavaScript project or module to a checked TypeScript boundary without changing supported JavaScript behavior. Document `strict` configuration, appropriate `module`/`moduleResolution` choice, import type behavior, declaration output or a justified `noEmit` workflow, and a reproducible type-check command. Show a compiler-success/runtime-failure counterexample and diagnose an intentionally broken resolution or erased-type import. Verify a clean state with local compiler/toolchain availability.
  - Criteria: Static checks run under a declared compiler version and fail on an intentional incompatible consumer; executable output works in the declared Node host and existing regression tests continue to pass. Type-only values are not imported as runtime objects; declarations are not treated as validation, and Node's native type stripping is not credited with `tsc` checking or `tsconfig` execution. No hidden global installation, unreviewed network dependency or proprietary account is needed for reproducible evaluation.
  - Evidence: Migrated source, original JS behavior fixtures, `tsconfig.json`, toolchain and local package recipe, type-check output, runtime test log, a repaired module/configuration defect, and migration/compatibility notes.

- **APP19-AS5** (required typed library evolution and engineering defense)
  - Outcomes: APP19-O1, APP19-O2, APP19-O3, APP19-O4, APP19-O5, APP19-O6, APP19-O7, APP19-O8, APP19-O9, APP19-O10, APP19-O11, APP19-O12
  - Work: Deliver a maintainable TypeScript library or local application slice exposing a documented typed interface and at least two consumers. Integrate a validated `unknown` external input boundary, discriminated state handling, a justified generic abstraction, meaningful error behavior, strict checks and runtime tests. Reuse qualifying work from earlier assessments rather than build five unrelated products. Perform one unfamiliar bounded request such as a new result variant, data field, or changed consumer contract; prove backward-compatibility or explicitly document a breaking change. Rebuild and defend the system without requiring a browser, React, a backend HTTP service or a third-party cloud account.
  - Criteria: Required contracts and variant behavior satisfy published acceptance cases; malformed data cannot reach typed domain operations unchecked; compiler and runtime tests verify different claims; consumers resolve actual values and type declarations correctly. The new request is implemented with a traceable contract impact and passing regression suite. The learner can explain structural typing, sound narrowing, a meaningful generic transformation, compiler configuration, the difference between emitted JS and type annotations, and remaining limitations with inspected evidence.
  - Evidence: Versioned source and interface documentation, fixture and consumer matrix, reproducible `tsc`/runtime commands and test results, migration/change diff, negative-path reproduction, compatibility note, and written/recorded/otherwise accessible technical defense.

### Completion decision and revision safety

Completion requires an inspectable acceptable decision on
`APP19-AS1` through `APP19-AS5` and evidence establishing
`APP19-O1` through `APP19-O12`. Reusing one evolving
codebase across assessments is encouraged when reviewers
can still distinguish the outcomes demonstrated. A passing
test command, cosmetic typing, unsupported cast or
unreviewed activity checkbox cannot establish competence.

The evaluator must check both type-system claims and the
runtime behavior actually asserted, ask for repair of
materially invalid cases, and record uncertainty and
limitations without inflating what the evidence shows.
Preserve applicable course/spec revision, assessment IDs,
evidence references and decisions according to
[OEE Evidence Rules](../../spec/evidence-rules.md).

APP19 is introduced as a `v0.2.0` **draft**, not a
learner-tested or independently verified course.
The active APP catalog and APP9's current core prerequisite
closure include APP19 only when the reviewed source PR
merges. Existing APP18 and legacy APP course evidence
retain their recorded historical interpretation.
APP2, APP3, APP20 and optional APP15 remain distinct,
separately reviewed future migrations.

### Public non-mandatory study references

These accessible references are for independent reading
and verifying mechanisms; all required assessment work
and criteria are published above.

- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
  for everyday types, narrowing, object types, functions,
  generics, type manipulation and modules.
- [TypeScript TSConfig reference](https://www.typescriptlang.org/tsconfig/)
  for compiler flags, strictness, module resolution and emission.
- [TypeScript module reference](https://www.typescriptlang.org/docs/handbook/modules/reference.html)
  for module formats and interoperable imports/exports.
- [Node.js TypeScript documentation](https://nodejs.org/api/typescript.html)
  for host-native type stripping and its explicit limitations.
- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
  for underlying runtime language semantics.
