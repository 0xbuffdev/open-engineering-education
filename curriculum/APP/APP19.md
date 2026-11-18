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

### Module 1 — TypeScript's Static Contract and First Program

#### Outcomes

- APP19-O1
- APP19-O2
- APP19-O9

#### Lessons

1. **Why TypeScript Exists and Where It Stops** — Apply APP18 JavaScript competence to a short type-checked function; situate TypeScript's motivation and use briefly, distinguish source types from executable JavaScript, and define the non-browser/non-service course boundary.

2. **Compiler Diagnostics versus Runtime Evidence** — Predict a static rejection and a runtime failure in the same small utility; inspect a `tsc` diagnostic and actual JavaScript output without claiming type checking executes or protects the program.

3. **A Real Strict Toolchain** — Run a strict locally available TypeScript compiler with a declared version and compare type-only `--noEmit` checking with deliberate executable JavaScript emission; record an offline-capable reproduction route.

4. **Language, Host and Declaration Assumptions** — Trace which observed effects come from ECMAScript, Node, TypeScript checks or supplied declarations; test a false type assumption against an actual runtime value and document its limitation.

### Module 2 — Inference, Literal Models and Missing Values

#### Outcomes

- APP19-O1
- APP19-O2
- APP19-O5

#### Lessons

1. **Contextual Inference and Explicit API Types** — Choose inference for local expressions and annotations for meaningful public boundaries; compare predicted inferred types with compiler feedback.

2. **Primitive, Array and Tuple Contracts** — Model JavaScript primitives, arrays, fixed-position tuples and readonly views without assuming immutability at runtime.

3. **Widening, Literals and Discriminants** — Compare widened variables with preserved literal values and union alternatives; use a specific domain rather than defining dozens of unrelated literal types.

4. **Null, Undefined and Optional State** — Explain meaningful absent versus undefined/null/zero/empty values under strict null checks and distinguish required properties from optional ones.

5. **Unions, Intersections and Unreachable Combinations** — Represent alternative states and combined requirements, diagnose an impossible intersection and compare an explicit domain union with an overly broad shape.

6. **`unknown`, `any`, `never` and Safe Assertions** — Explain why unknown demands evidence, any suppresses checks and never denotes unreachable cases; compare `as const`, `satisfies` and an unsound cast in one compiler/runtime counterexample.

### Module 3 — Structural Object Contracts and Assignment Limits

#### Outcomes

- APP19-O2
- APP19-O3
- APP19-O5

#### Lessons

1. **Types, Interfaces and Structural Assignability** — Model a genuine record API with type aliases/interfaces and explain structural compatibility rather than nominal identity or automatic runtime schema checks.

2. **Fresh Literals, Variables and Excess-Property Checks** — Predict which excess fields are rejected on a fresh literal and why the same value assigned through a variable can be structurally acceptable; verify that neither case validates external data.

3. **Required, Optional, Readonly and Nested Shapes** — Express presence, nested constraints and readonly intent; demonstrate readonly's static limitation and the difference between absent and explicit undefined.

4. **Index Signatures, Records and Known Keys** — Select explicit fields, Record, index signatures or a Map by actual domain-key requirements; use a constrained key example and inspect unsafe overly broad lookup assumptions.

5. **Class Contracts and Runtime Members** — Compare implements/visibility checks with APP18's prototype/class runtime behavior and distinguish TypeScript private from ECMAScript runtime-private members; do not require an unnecessary class hierarchy.

### Module 4 — Control-Flow Narrowing and Exhaustive States

#### Outcomes

- APP19-O2
- APP19-O4
- APP19-O5
- APP19-O11

#### Lessons

1. **Narrowing with Observable JavaScript Checks** — Trace typeof, equality, null, in and instanceof guards on real values; identify edge cases such as null and inherited keys rather than treating a type guard as magic.

2. **Discriminated Result and State Models** — Replace loosely related optional flags with a meaningful tagged result union whose variants have distinct required fields and domain actions.

3. **Truthiness and Control-Flow Limits** — Show why truthy checks can discard valid zero/empty values and why assignment, mutable aliases or callback boundaries may invalidate a prior assumption.

4. **Exhaustiveness with `never`** — Make a variant consumer exhaustively decidable at compile time, add a new variant and verify that the expected missing branch is flagged.

5. **Predicates, Assertions and Unsound Signatures** — Compare a truthful user-defined type predicate or assertion function against one that merely promises a type; verify both with actual counterexample data.

6. **Variant Migration and Runtime Recovery** — Introduce an unfamiliar bounded state change, repair static consumers and protect malformed-input behavior with runtime regression tests.

### Module 5 — Functions, Callback Compatibility and Typed Async Results

#### Outcomes

- APP19-O5
- APP19-O6
- APP19-O10

#### Lessons

1. **Function Boundaries and Optional Inputs** — Model parameter, return, optional, default, rest and receiver signatures that correspond to actual JavaScript behavior and supported call paths.

2. **Callbacks, Contextual Types and Variance** — Predict callback assignability under strict function checking; investigate a narrowed-parameter counterexample and qualify method-position exceptions rather than promising universal soundness.

3. **Overload versus Union versus Generic** — Compare representations of one bounded API and justify which preserves an actual caller-specific input/output relationship; check implementation and consumers.

4. **Promises and Error-Aware Result Contracts** — Type a local async result and rejection-handling boundary, distinguishing `Promise<T>` fulfillment type from unchecked thrown/rejected values and host behavior already learned in APP18.

5. **Independent Function Consumer Checks** — Exercise valid and invalid calls from a separate consumer, test runtime behavior and demonstrate that declarations can omit or misdescribe important execution facts.

### Module 6 — Generics and Proportionate Type Transformations

#### Outcomes

- APP19-O3
- APP19-O6
- APP19-O7
- APP19-O8

#### Lessons

1. **Generic Input/Output Relationships** — Use type parameters to preserve a meaningful relationship, comparing a generic signature with unknown or union alternatives on concrete consumer calls.

2. **Inference, Constraints and Defaults** — Derive a parameter from actual arguments, add a necessary extends bound and choose a default only when it clarifies rather than obscures the public API.

3. **Related Keys and Values** — Implement a safe generic lookup with `keyof`, indexed access and optional-key considerations; demonstrate valid and rejected key/value pairs.

4. **Reusable Typed Collections or Results** — Design one modest generic result container, record index or callback interface with explicit invariants, not a generic framework for its own sake.

5. **Utility and Mapped Transformations** — Use suitable Partial, Pick, Omit or Readonly and derive one small mapped transformation; explain shallow static modifiers and the real contract being transformed.

6. **Conditional Selection, Distribution and `infer`** — Explain a bounded conditional relationship, the effect of a distributive type parameter versus tuple wrapping, and inspect inference only where a public consumer benefits.

7. **Template-Literal Contracts Where Appropriate** — Derive or inspect a small string-key or event-name relationship from declared keys; verify compiler-accepted and rejected names and explain when ordinary literals are clearer.

8. **Type Complexity and Independent Consumer Tests** — Compare a sophisticated type with a simpler domain union/interface; use positive and negative `tsc` consumer cases to justify the smallest sufficient relationship.

### Module 7 — Compiler, Module and Typed API Delivery

#### Outcomes

- APP19-O1
- APP19-O3
- APP19-O5
- APP19-O9
- APP19-O10

#### Lessons

1. **Strict Project Definition and Type Precision Flags** — Create a scoped `tsconfig.json` with strict diagnostics; examine noUncheckedIndexedAccess and exactOptionalPropertyTypes on concrete indexed/optional inputs without assuming they are always enabled.

2. **Checking, Target, Ambient Libraries and Emission** — Separate `--noEmit` checks, emitted JavaScript, source maps and the target/lib distinction: an ambient DOM/ES API declaration does not install a runtime API or polyfill.

3. **Node Type Stripping as a Limited Host Path** — Compare a supported erasable TypeScript case against compiler-emitted JavaScript; verify that Node's native stripping does not type-check, transform arbitrary TS syntax, honor tsconfig or resolve paths for you.

4. **ESM Resolution and Type-Only Imports** — Investigate module/moduleResolution, a local relative specifier and an import type versus runtime value distinction; reproduce one erased-import or host-resolver failure.

5. **Public Modules and Declaration Surfaces** — Export a cohesive typed interface, inspect a .d.ts declaration and distinguish compile-time claims from executable values and trustworthy implementation behavior.

6. **JavaScript Interoperation and Package Contracts** — Consume a bounded APP18-style JavaScript module using suitable declarations or incremental checking; qualify CommonJS/ESM and package exports under the declared host baseline.

7. **Consumer Compatibility and Breaking Changes** — Change a required/optional property, callback or result variant and inspect compiler and runtime effects on two local consumers; avoid claiming a passing type check implies deployed behavioral compatibility.

8. **Clean Local Build and Diagnostic Repair** — Reproduce type checks, chosen JavaScript execution and independent tests from pre-provisioned local tools; repair a relevant configuration/resolution defect without online registries, secrets or private CI.

### Module 8 — Untrusted Runtime Data and Checked Domain Boundaries

#### Outcomes

- APP19-O4
- APP19-O5
- APP19-O10
- APP19-O11

#### Lessons

1. **Erasure, `unknown` and Boundary Ownership** — Accept fabricated JSON/filesystem data as unknown, not as a trusted TypeScript domain value; show exactly how a cast and an external declaration can be wrong at runtime.

2. **Shape, Value, Missing and Optional Policies** — Validate actual record presence, type, finite range, allowed tags, null/undefined and optional fields; distinguish accepted absence from fabricated or invalid values.

3. **Truthful Predicates and Validated Constructors** — Build a predicate/decoder from executable checks and test a deceptive signature against a counterexample; construct a typed internal value only after validation.

4. **Schema Evolution and Exhaustive Version Handling** — Accept or reject a changed version with explicit policy, compiler-supported variant handling and negative runtime fixtures; do not silently reinterpret an older payload.

5. **Untrusted Keys, Prototype and Error Privacy** — Reuse APP18 prototype/key security knowledge to protect typed indexing/merges and redact raw sensitive payloads; distinguish domain rejection from unexpected program defects.

6. **Adversarial Validation and Consumer Recovery** — Use malformed, extra-field, nested, duplicate and version-shifted synthetic fixtures to prove rejected inputs never reach a typed operation as though validated.

### Module 9 — Incremental JavaScript Migration and Dual Verification

#### Outcomes

- APP19-O1
- APP19-O7
- APP19-O9
- APP19-O10
- APP19-O11
- APP19-O12

#### Lessons

1. **A Bounded APP18 Migration Slice** — Identify implicit input/output assumptions in a tested prior JavaScript module and choose a meaningful subset for typing; preserve existing runtime acceptance cases.

2. **JSDoc, `checkJs` and TypeScript Files** — Compare a locally checkable JSDoc boundary with a .ts conversion; explain which migration steps preserve emitted behavior and which require extra host setup.

3. **Compiler-Negative and Consumer Tests** — Write stable compiler expectations for invalid calls/variants; independently exercise correct consumers without relying on one transcript of successful compilation.

4. **Runtime Tests for Valid and Adversarial Inputs** — Retain and strengthen Node tests for malformed input, version drift, promise rejection and actual behavior that erased TypeScript cannot guarantee.

5. **Trace, Regress and Explain a Change** — Use source/output/stack evidence to fix a deliberate type/host mismatch, explain unsafe declarations or type holes and record when a public interface change is breaking.

### Module 10 — One Typed Library, Real Evolution and Defense

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

1. **A Real Contract and One Cumulative Artifact** — Select a bounded typed library or local utility with genuine consumers, external synthetic input and explicit acceptance policy; plan to reuse inspected APP19-AS1–AS4 artifacts and evidence rather than produce unrelated projects.

2. **Static Models and Runtime Data Gates** — Integrate a discriminated state model, checked unknown boundary, relational generic and one proportionate advanced type transformation; expose documented live module exports.

3. **Independent Consumers and Failure Evidence** — Verify positive/negative compiler examples and runtime consumers separately, including a malformed/changed input and declared toolchain/module assumptions.

4. **Unfamiliar Contract or Variant Change** — Respond to a bounded external change, reproduce its static and runtime consequences, repair domain and consumer behavior and check existing acceptance criteria.

5. **Clean Reproduction and Engineering Defense** — Deliver one offline-capable source/test bundle, references to prior accepted outcome evidence, a reproducible change trace and a reviewable explanation of soundness limitations, type/runtime ownership and remaining uncertainty.

## Completion requirements

All **twelve required outcomes** must be established through
**five independently decidable summative assessments**. These
may use **one evolving local typed-library or utility source**:
APP19-AS1 diagnoses source semantics, AS2 establishes validated
state and runtime boundaries, AS3 builds a genuinely relational
typed API, AS4 verifies migration and compiler/module behavior,
and AS5 evaluates the integrated artifact and an unfamiliar
bounded change. Previously accepted evidence may be **referenced**
rather than copied or rebuilt. Neither five separate libraries
nor an assessment for every lesson is required. Formative
investigations remain optional preparation, not hidden gates.

| Required assessment | Outcomes evaluated | Principal evidence |
| --- | --- | --- |
| `APP19-AS1` — Static Modeling and Structural Compatibility Review | APP19-O1, APP19-O2, APP19-O3, APP19-O5, APP19-O9 | TS source, compiler configuration and diagnostics, a prediction-versus-observation table, executable JS tests or counterexamples, repaired definitions and a concise distinction between checking and execution |
| `APP19-AS2` — Discriminated State and Runtime Validation Investigation | APP19-O2, APP19-O4, APP19-O5, APP19-O11 | Union and validation source, negative/normal fixture matrix, compiler diagnostics before/after the new variant, executable tests, and explanation of type predicates, `never` and the runtime trust boundary |
| `APP19-AS3` — Generic API and Type Transformation Review | APP19-O3, APP19-O6, APP19-O7, APP19-O8, APP19-O10 | One relational generic API; justified utility/mapped, conditional and bounded template-literal type checks; two consumers; compiler-positive/negative and runtime evidence; proportionate complexity defense |
| `APP19-AS4` — Compiler, Module, and JavaScript Migration Audit | APP19-O1, APP19-O5, APP19-O9, APP19-O10, APP19-O12 | Migrated APP18 source, separate compiler and executable-JavaScript evidence, declared toolchain and module assumptions, clean local reproduction, diagnosed resolver/configuration failure |
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

- **APP19-AS3** (required generic API and type transformation review)
  - Outcomes: APP19-O3, APP19-O6, APP19-O7, APP19-O8, APP19-O10
  - Work: Develop a small reusable data-processing, event or result module **within the evolving library**. Demonstrate one relational generic API with constrained `keyof`/indexed access, a justified standard utility and a small mapped type, a bounded conditional type (including an illustrative distributivity check), and a **meaningful template-literal key/name relationship**. A compact isolated consumer example is sufficient when the latter would overcomplicate the public API; do not mandate type gymnastics in the shipped interface. Include a typed callback or async result with explicit runtime failure handling, two independent local consumers, and intentionally invalid static calls.
  - Criteria: Different concrete callers preserve their generic input/output relationships; utility/mapped, conditional and template-literal examples have correct compiler-positive and negative expectations, with limitations on actual runtime validation understood. The published API stays proportionate, required/optional/readonly meanings are not silently changed, consumer misuse is rejected by strict checking, and valid callback/async behavior is runtime-tested. No `any` cast masks a fundamental boundary. The learner can **reject unnecessary advanced types** in the exported API while still demonstrating and explaining their semantics in bounded checked examples.
  - Evidence: Typed module, a focused mapping of each O8 type family to an accepted/rejected static example, two local consumer fixtures, separately recorded type-check and runtime results, callback/async tests, and a concise decision explaining the domain need or deliberate exclusion of an advanced type. Prior AS1/AS2 evidence may be linked rather than repeated.

- **APP19-AS4** (required compiler, module and JavaScript migration audit)
  - Outcomes: APP19-O1, APP19-O5, APP19-O9, APP19-O10, APP19-O12
  - Work: Move a bounded, already-tested APP18 JavaScript module into an appropriately checked TypeScript boundary, preserving its documented runtime behavior and ideally extending the AS2/AS3 library. Define strict compiler options and `module`/`moduleResolution` appropriate to the actual host, distinguish type-only imports and declaration-only exports from live values, and compare **explicit type-only checking with a separately documented runnable JavaScript path**. A `tsc`-emitted output or appropriately versioned erasable-type Node execution may satisfy the runnable path; native type stripping must not be described as `tsconfig` evaluation or a checker. Diagnose and repair an erased-import, relative-path, package-exports or configuration mismatch, then reproduce from pre-provisioned free local tools.
  - Criteria: A real `tsc` run produces meaningful static feedback under the recorded compiler baseline, including an intentionally failing invalid consumer; documented executable behavior matches prior APP18 regression cases and the declared Node/module environment. No checked type or `.d.ts` is mistaken for actual runtime validation, and no `lib` declaration is mistaken for an installed API. The identified module/configuration failure has a causal, verified correction. No private compiler, remote grading account, live registry or unreviewed install script is required.
  - Evidence: Reused or migrated source and original behavior fixtures, minimal `tsconfig.json`, separately identified **static** diagnostic and **runtime** test/inspection outputs, one broken/fixed module or resolution case, exact material tool versions and clean local setup. Evidence from AS1–AS3 may be referenced.

- **APP19-AS5** (required typed library evolution and engineering defense)
  - Outcomes: APP19-O1, APP19-O2, APP19-O3, APP19-O4, APP19-O5, APP19-O6, APP19-O7, APP19-O8, APP19-O9, APP19-O10, APP19-O11, APP19-O12
  - Work: Complete **one coherent cumulative** local typed library or utility with a documented live API and at least two independent consumers. Integrate the validated `unknown` input boundary, exhaustive result states, justified generic and type-transform relationships, runtime error policy, strict checking and executable tests from APP19-AS1–AS4. Reference **previously evaluated** evidence rather than duplicate projects. Implement an **unfamiliar bounded state, field or caller-contract change**, observe the static and runtime effects, repair them and independently reproduce and defend the result. Do not add hidden browser, React, HTTP server, paid platform or external-data requirements.
  - Criteria: Published domain cases, compiler-positive and compiler-negative expectations, live value exports and runtime failure scenarios are supported by inspectable evidence, not casts or declaration claims. Malformed external data cannot silently enter domain operations as validated. The new change has traceable impact, verified consumer revisions and no unaddressed breaking behavior relative to the stated compatibility policy. The learner explains inference, structural typing limits, trustworthy narrowing, generic/type transformation trade-offs, compiler/host boundaries and observed limitations. A successful compilation alone cannot pass.
  - Evidence: One versioned local source/fixture package, concise public type/runtime API documentation, independently runnable consumer/test commands, a **references-first** evidence map for AS1–AS4, the new contract/variant change and static/runtime regression results, compatibility limitations, and a reviewable written, recorded or other accessible technical defense.

### Completion decision and revision safety

Completion requires an inspectable decision for each of
`APP19-AS1` through `APP19-AS5` and authentic evidence
for every `APP19-O1` through `APP19-O12`. **One evolving**
source is sufficient where the five decisions remain distinct:
AS5 integration does not excuse unproved AS1–AS4 outcomes.
Previously judged evidence may be linked, not re-submitted.
A passing compiler/test command, cosmetic typing, unchecked
cast, excessive type complexity or lesson-attendance checkbox
cannot substitute for domain understanding or runtime safety.

The evaluator must check both type-system claims and the
runtime behavior actually asserted, ask for repair of
materially invalid cases, and record uncertainty and
limitations without inflating what the evidence shows.
Preserve applicable course/spec revision, assessment IDs,
evidence references and decisions according to
[OEE Evidence Rules](../../spec/evidence-rules.md).

APP19 remains a `v0.2.0` **draft**, not a learner-tested,
independently accredited or educationally verified course.
The APP catalog already includes APP19 in the required core
path and APP9 graduation prerequisite closure; APP2, APP3,
APP20 and optional APP15 consume TypeScript competence at
different depth. This reassessment neither alters their
course contracts nor silently re-evaluates historical APP18
or other learner decisions, which remain tied to their
actual assessed source/specification revisions.

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
