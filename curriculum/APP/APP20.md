# APP20 — React Application Engineering

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `core`
**Prerequisites:** [APP2](APP2.md) — Browser & Frontend Engineering
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (provisional; revise using learner and reviewer evidence)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Engineer maintainable, accessible and testable browser applications
with **React and TypeScript**, after learning the underlying Web,
JavaScript and framework-neutral DOM mechanisms. Build an accurate
mental model of function components, JSX, props, render/commit,
reconciliation, identity, state snapshots, Hooks and synchronization.
Apply those mechanisms to forms, shared state, routing, validated
async data, error and loading boundaries, accessibility, security,
testing, profiling and a coherent application-level technical defense.

**APP2 is the direct prerequisite.** Its prerequisite closure
already includes APP17 and APP19, with APP1 and APP18 earlier in
those paths. APP2 owns browser DOM/event/fetch/history behavior,
user-task requirements, accessibility/usability foundations and
browser security. APP19 owns TypeScript's type system, and APP18
owns JavaScript language plus basic Node/npm developer tooling.
APP20 applies those skills to **React-specific application design**
rather than teaching them all again.

The reference technologies are open-source **React**, its browser
renderer **React DOM**, TypeScript and a compatible local build/test
toolchain (for example Vite, with an open-source testing runner).
A maintained, mutually compatible release baseline and relevant
package versions must be declared and pinned for reproducibility.
Do not prescribe deprecated Create React App. A simple client-only
React project makes rendering and state boundaries inspectable;
production applications may use integrated frameworks, routing
or data-loading solutions as appropriate. Such frameworks are
reviewed as alternatives, **not hidden prerequisites**.

Node.js may execute the reference build and test tools, but APP21's
Node backend-runtime and HTTP server course is **not** required.
The assessed app runs in a standards-capable browser and uses
synthetic data with a supplied local fixture service or a
deterministic injectable transport. React Router or a compatible
alternative may be used for local navigation; no paid service,
public domain, backend database, API key, commercial analytics,
authentication provider, cloud deployment or third-party production
endpoint is mandatory. The React/React DOM/build dependencies
must be available after initial free installation or pre-provisioned
locally, so assessed execution can be reproduced from a clean
checkout without network access when the declared local artifacts
are supplied.

**Concepts must match actual React guarantees.** Rendering computes
a UI description; commit updates the host. A component's state
depends on type/position/key identity, not arbitrary object mutation.
State updates operate through render snapshots. Effects synchronize
with systems outside React; many derived values and event actions
do not need Effects. Development Strict Mode deliberately checks
purity and cleanup and is not a promise that production runs the
same checks. Error boundaries cover eligible rendering failures,
not all event handlers or asynchronous errors. Suspense only reacts
to supported suspending operations, not any promise created in an
Effect. Concurrent rendering and transitions do not create
extra JavaScript threads or guarantee a network request has
been canceled. Version-dependent behavior must be checked
against the pinned installed React release.

Accessibility, security and user research remain inspectable:
use native controls, verify focus and status through component/route
changes, validate unknown network data, avoid dangerous HTML
injection and client-side authorization claims, and label any
synthetic usability walkthrough as such. A browser screenshot,
green compiler check or one profiler trace is not sufficient
proof of user experience or security.

**Boundary with later APP:** APP3 teaches typed framework-based
backend APIs; APP5 integrates frontend/backend/data and identity;
APP6 and APP7 deepen quality, operations and release engineering;
APP10 (elective) covers advanced browser performance. APP20 teaches
relevant client-rendering versus SSR/hydration/server component
trade-offs conceptually but does not demand a production SSR
framework or a distributed backend.

The duration/workload are estimates, not an achieved readiness
status. Modules progress from worked mechanisms, through bounded
state and failure investigations, to increasingly independent
design. Lesson investigations are formative unless a required
summative assessment below explicitly includes their evidence.

## Learning outcomes

- **APP20-O1:** Reproduce a React and TypeScript browser project with a documented maintained runtime, React/React DOM versions, open-source build/test tooling and independently executable source; distinguish developer-tool execution from the browser runtime and React from the host DOM.
- **APP20-O2:** Design and implement typed React function components, JSX and composable public props/children contracts, using stable data flow and native semantic HTML without confusing JSX with an HTML string or a trusted input validator.
- **APP20-O3:** Predict and investigate React render/commit behavior, component identity, keyed list reconciliation, state preservation/reset and the effects of unstable keys; distinguish supported React behavior from undocumented implementation internals.
- **APP20-O4:** Implement correct event-driven state updates using state snapshots, functional updaters, batching as applicable, immutable data transformations and derived render-time values; diagnose stale closures, accidental mutation and redundant state.
- **APP20-O5:** Build accessible interactive forms with a justified controlled/uncontrolled input strategy, explicit validation and submission states, native keyboard and focus behavior, meaningful errors and protection against unintended duplicate actions.
- **APP20-O6:** Apply the Rules of Hooks and distinguish pure rendering, event logic and synchronization Effects; manage dependencies, cleanup and development Strict Mode behavior without hiding reactivity or leaking subscriptions.
- **APP20-O7:** Use refs and imperative integration only when appropriate, including DOM focus, resource handles and a bounded non-React widget; preserve cleanup, accessibility and state ownership through React-driven updates.
- **APP20-O8:** Choose appropriate component, reducer, context and custom Hook boundaries; explain local/shared/external state ownership, reduce unnecessary coupling and demonstrate a maintainable feature change without introducing a mandatory state library.
- **APP20-O9:** Integrate validated asynchronous data into React views with correct HTTP/network outcomes, request ownership, loading/empty/forbidden/error states, cache/mutation consistency and race/abort protection without treating TypeScript contracts as runtime validation.
- **APP20-O10:** Implement user-meaningful React navigation and route-level state while retaining deep-link behavior, Back/Forward navigation, access-error presentation, focus/title handling, clean teardown and declared host fallback behavior.
- **APP20-O11:** Use rendering error boundaries, deliberate loading/Suspense boundaries and appropriate scheduling or transition tools within their documented limits, distinguishing render failures from event/async failures and avoiding false assumptions about Suspense data fetching.
- **APP20-O12:** Demonstrate browser and React application security/privacy boundaries involving untrusted rendered data, dangerous HTML sinks, credentials, identity-scoped state and third-party dependencies, without claiming client checks or CORS provide server authorization.
- **APP20-O13:** Apply semantic, keyboard, focus, status-announcement, reflow, motion and usability criteria across React component and route transitions, preserving the APP2 interaction contract through rerenders and error recovery.
- **APP20-O14:** Design deterministic unit/component/integration and suitable local browser tests that establish externally visible behavior, error paths, async cleanup and accessibility; distinguish development-only effects from production behavior.
- **APP20-O15:** Investigate measured React performance, profiling render causes, stable identity and memoization trade-offs, avoiding premature optimization or relying on unverified React/compiler version behavior; explain conceptual client versus server rendering and hydration boundaries.
- **APP20-O16:** Deliver, reproduce, evolve and defend a cohesive TypeScript React browser application in response to a bounded user task and unfamiliar change, with trustworthy runtime validation, tests, accessibility evidence, failure investigation and technical trade-off reasoning.

## Modules

### Module 1 — React as a Browser UI Runtime and Reproducible Toolchain

#### Outcomes

- APP20-O1
- APP20-O2

#### Lessons

1. **From DOM Manipulation to Declarative React** — Starting from APP2 browser interaction competence, briefly situate React's component approach historically and explain what it owns versus JavaScript, native HTML/CSS, React DOM, browser event behavior and a backend.

2. **React, React DOM and Development Tooling** — Choose supported mutually compatible React, React DOM, TypeScript and free local build/test releases; record exact package/lockfile provenance and explain Node's build-time role versus JavaScript executed by the browser.

3. **A Root, Real Build and Safe Local Fixture** — Mount a typed root in a known DOM element, reproduce a missing-root or mismatched-renderer defect and inspect real browser output from a local served build rather than relying on type checking alone.

4. **Library versus Full-Stack Framework Responsibility** — Compare the chosen small client-only application with SSR, hydration, pre-rendering and framework-integrated approaches conceptually; justify the present boundary without requiring APP21, APP3, a hosted framework or deprecated Create React App.

*Optional practice — Setup Failure:* Diagnose incompatible renderer/dependency versions, failed JSX compilation or wrong browser import assumptions, then reproduce from a clean copy.

### Module 2 — JSX, Typed Components and Intentional Composition

#### Outcomes

- APP20-O1
- APP20-O2
- APP20-O12
- APP20-O13

#### Lessons

1. **JSX, React Elements and Executable Browser Output** — Trace a JSX expression into React elements and final DOM output, distinguishing JavaScript expression evaluation, JSX text escaping and HTML string injection.

2. **Function Components, Typed Props and One-Way Ownership** — Build correctly invoked typed function components with meaningful required/optional props, event callbacks and readonly parent-owned data; rely on APP19 typing rather than repeat its language course.

3. **Children, Composition and Semantic HTML** — Use children and cohesive components to share actual structure without overbuilding a configurable UI library; preserve native links, buttons, labels and fieldset behavior from APP17/APP2.

4. **Conditional UI and Meaningful Empty States** — Render intentionally defined empty, failed, pending and result variants, handling null and falsy values accurately rather than accidentally displaying a count or contradictory text.

5. **Safe Text, Attributes and Explicit HTML Trust** — Compare React's default text escaping with dangerouslySetInnerHTML; prove why user-controlled URLs, attributes and rendered trusted markup need separate context-sensitive validation and security decisions.

*Optional practice — Component Contract Review:* Refactor a monolithic static/reactive view into typed composable parts and verify its semantics and invalid-prop boundaries.

### Module 3 — Render, Commit, Keys and State Identity

#### Outcomes

- APP20-O2
- APP20-O3
- APP20-O4
- APP20-O15

#### Lessons

1. **Render, Commit and Browser Paint** — Predict React's render calculation and commit update without equating either with actual browser paint or assuming a single synchronous render.

2. **Pure Render and React-Owned DOM** — Reproduce a render-time mutation/side effect or manual React-owned DOM change and show the resulting corruption or repeated behavior, then repair it with correct ownership.

3. **Keyed Identity, Reorder and Form Preservation** — Use stable domain keys and type/position identity to reproduce lost/reassigned input state on insert/reorder and demonstrate intentional key-controlled reset, not random or list-index identity.

4. **Layout Changes, Component Position and Controlled Tests** — Move a subtree or change its type/key, predict which state and focus survives, then verify actual DOM behavior without relying on undocumented Fiber internals.

5. **Development Strict Mode Purity versus Production Semantics** — Observe development purity and setup/cleanup probes on a recorded React version, separate them from production guarantees and design an idempotent check that does not depend on a fixed render count.

*Optional practice — Identity Diagnosis:* Repair a list whose typed rows swap internal input values after reordering and provide a small regression demonstration.

### Module 4 — Render Snapshots, User Events and Correct State Updates

#### Outcomes

- APP20-O3
- APP20-O4
- APP20-O5

#### Lessons

1. **Event Handlers and Snapshot Semantics** — Explain which state each React event handler sees, preserve native event defaults and distinguish an intentional user action from a reactive synchronization process.

2. **Queued Updaters, Batching and Immutable Changes** — Diagnose a repeated-increment or array/object mutation defect; repair with functional updaters and immutable structural changes without assuming immediate setter results.

3. **Derived Values Instead of Redundant Effects** — Compute filtered/aggregated displays from props and state during render, correcting an effect-driven duplicate that becomes stale or triggers avoidable updates.

4. **Discriminated Transitions and Invalid States** — Represent actual UI phases with a tagged state model and a tested transition table rather than contradictory loading/success/error booleans.

5. **Ownership, Local Reset and User Intent** — Demonstrate a component identity or route change that intentionally resets one region while preserving unrelated drafts, selection or keyboard focus.

6. **State Repair under Unfamiliar Event Order** — Apply an unseen bounded sequence of events, predict the resulting render snapshot, reproduce the failure and verify a minimal correction with a behavior test.

*Optional practice — Stale Snapshot Repair:* Reproduce an incorrect double update or state mutation, write a behavior test, then fix it without introducing a spurious Effect.

### Module 5 — React Forms, Submission and Accessible Recovery

#### Outcomes

- APP20-O2
- APP20-O4
- APP20-O5
- APP20-O12
- APP20-O13

#### Lessons

1. **Native Form Semantics with Deliberate React Control** — Reuse APP17/APP2 form semantics and compare controlled value/onChange with defaultValue/refs/FormData; justify the source of truth for a real task rather than default to one method.

2. **Different Field Kinds and Actual Validation** — Model text, checkbox, select and file inputs without treating FileList as ordinary controlled text. Combine native validity with explicit runtime domain checks; a TypeScript type is not input validation.

3. **Pending, Duplicate and Uncertain Submission** — Use a bounded submission state machine to avoid accidental duplicate clicks and preserve draft content on recoverable errors; distinguish UI disablement from server idempotency or undoing an uncertain write.

4. **Field Errors, Status and Focus** — Associate labels/error messages/status text with real form controls; test keyboard navigation, appropriate focus movement and nonduplicated live announcements after React rerenders.

5. **React Form APIs and Supported-Version Decisions** — Compare standard event submission with installed-release supported action/form helpers when beneficial, without requiring an unverified experimental API or a framework server.

6. **An Adversarial Form Recovery** — Inject invalid domain input, late failure, route change or unmounted form and verify that meaningful draft/state and accessible recovery policies remain coherent.

*Optional practice — Form Defect:* Fix a lost draft, stale validation message or inadvertent repeated submit, then verify keyboard and negative-path behavior.

### Module 6 — Hooks, Refs and Owned External Synchronization

#### Outcomes

- APP20-O3
- APP20-O4
- APP20-O6
- APP20-O7
- APP20-O9
- APP20-O13
- APP20-O14

#### Lessons

1. **Rules of Hooks, Identity and Negative Cases** — Use state/effect/custom Hooks only at valid React component or custom Hook top levels; demonstrate one conditional-Hook/lint failure and correct rule adherence under changing props.

2. **Render Calculations, Events and True Effects** — Classify pure derivation, user-triggered work and external subscription or DOM integration; replace an unnecessary Effect with render/event logic and justify remaining synchronization.

3. **Reactive Dependencies and Strict Mode Setup/Cleanup** — Synchronize a mock external resource with truthful dependencies, demonstrate development setup-cleanup-setup probes and prove that current subscriptions do not leak or duplicate.

4. **Refs versus Render State and Focus Timing** — Use stable mutable refs for appropriate handles or DOM focus instead of UI data, distinguish when useLayoutEffect is justified for pre-paint measurement and qualify blocking/render implications.

5. **One Non-React Widget with Create/Update/Destroy** — Integrate a small supplied external widget, prove its instance is not recreated on every render, preserve React-owned DOM and dispose on prop change/unmount.

6. **Portals, DOM Placement and Interaction Semantics** — Use a justified overlay/portal, inspect React event ancestry versus DOM placement and demonstrate focus/keyboard behavior rather than assuming portal insertion makes a modal accessible.

7. **Cancellable Work and Stale-Effect Ownership** — Use an Effect only when it actually owns a request/subscription, abort or ignore outdated completions on dependency/identity change and explain why abort does not guarantee server rollback.

8. **A Small Custom Hook and Independent Instances** — Extract reusable behavior without sharing accidental global state, preserve dependency correctness, and test two separate component instances and cleanup.

9. **Synchronization Defect and Verified Repair** — Reproduce a stale closure, lingering widget or duplicate subscription; show failing-before/passing-after component behavior under the selected strict/development configuration and honest production limits.

*Optional practice — Effect Bug:* Repair a stale closure, subscription leak or dependency-suppression defect with a reproducible Strict Mode test and documented cleanup.

### Module 7 — Feature Boundaries, Reducers and Shared State

#### Outcomes

- APP20-O2
- APP20-O4
- APP20-O6
- APP20-O8
- APP20-O16

#### Lessons

1. **Local, Lifted and Shared State Responsibility** — Assign a draft, selection and user identity to the nearest justified owners; compare explicit props with lifted state and reject unjustified global mutable state.

2. **Feature Components and Pure Reducer Transitions** — Separate one feature's domain, view and transport contracts; use a reducer for a real multi-action transition problem and test illegal transitions independently.

3. **Context Scope, Re-Renders and Explicit Dependencies** — Use Context for a real scoped theme/service/identity dependency, diagnose wide-provider invalidation and compare a simpler local prop or smaller provider boundary.

4. **Custom Hooks and External Store Ownership** — Define one reusable feature Hook or provided external-store adapter, explain useSyncExternalStore only if an actual external source exists and avoid mandatory Redux/Zustand.

5. **State Immutability and Boundary Validation** — Validate incoming unknown data before trusted feature state, and trace why mutating a shared nested record causes consumer inconsistency despite TypeScript checks.

6. **Change-Cost Comparison and Architecture Defense** — Implement a small unfamiliar requirement twice conceptually or with scoped alternatives; demonstrate the chosen ownership's effect on coupling, testing and independent feature instances.

*Optional practice — Architecture Review:* Compare a broad context and an intentional feature-local reducer, make a defensible choice and test independent feature instances.

### Module 8 — React Async Data, Cache and Mutation Correctness

#### Outcomes

- APP20-O6
- APP20-O8
- APP20-O9
- APP20-O12
- APP20-O14

#### Lessons

1. **React Ownership of an APP2 Transport Boundary** — Use APP2's established Fetch/HTTP status and response contracts as an injected local adapter; show what React newly owns about render lifetime, pending state and identity changes.

2. **Runtime-Validated Responses and Distinct UI Outcomes** — Decode unknown data before typed domain use, including successful no-body, malformed JSON, HTTP errors versus network rejection, forbidden, empty and recoverable states.

3. **Late Results, Identity Changes and Unmounted Views** — Use controlled promise settlement to reproduce a stale response after prop/route/user change, then prove an obsolete result cannot overwrite current content even when abort is late.

4. **Cache Invalidation and Sensitive Scope** — Define key, freshness, eviction and user-identity partitioning for a bounded local cache, including logout; defend when a compatible declarative library/router loader would be safer than hand-coded Effect caching.

5. **Mutation, Optimism and Uncertain Commit** — Integrate a local synthetic mutation, explicit pending/rollback or reconciliation behavior, and a no-blind-retry rule for a side effect that may already have completed.

6. **React-Specific Race/Recovery Regression** — Use deterministic injected transport, independent rendered DOM observations and an unfamiliar failure to verify request ownership, state transition and correct focus/status output.

*Optional practice — Async Race:* Fix a user-switch stale-data leak under deterministic deferred responses and document a regression for the changed component identity.

### Module 9 — React Navigation, URL Contracts and Route Ownership

#### Outcomes

- APP20-O8
- APP20-O9
- APP20-O10
- APP20-O13

#### Lessons

1. **Router Choice and Host URL Responsibilities** — Choose a compatible free router or minimal adapter, distinguishing APP2's native URL/History promises from route-composed React components.

2. **Route Layouts, Identity and Search Parameters** — Use nested layout where justified, parse/validate path/search/hash and decide which provider/form/cache state persists or resets after navigation.

3. **Direct Link, Browser History and Native Link Behavior** — Verify actual direct URL reload under the supplied local static server, Back/Forward navigation and normal anchor/modifier behavior, not just a simulated router click.

4. **Focus, Title, Scroll and Failure Recovery** — Define intentional keyboard focus, title, scroll restoration and error/empty/forbidden state transitions for a route change without inventing a universal focus-reset law.

5. **Navigation, Request Ownership and Authorization Display** — Cancel/ignore stale route loads, clear identity-scoped content on logout and explain why hidden routes or client guards do not enforce backend authorization.

6. **A Real Direct-Load or History Defect** — Reproduce and repair a broken deep link, stale loader, lost draft or focus transfer with an actual browser/host observation and targeted regression.

*Optional practice — Navigation Failure:* Repair a direct-link reload, stale loader or lost focus and verify with real browser history interactions.

### Module 10 — React Render Errors, Suspense and Update Priorities

#### Outcomes

- APP20-O3
- APP20-O6
- APP20-O9
- APP20-O11
- APP20-O14

#### Lessons

1. **Eligible Render Errors and Boundary Scope** — Place a genuine rendering error boundary and fallback/reset around a feature and explain which React rendering-phase failures it can contain.

2. **Event, Async and Streaming Failure Distinctions** — Contrast an event-handler throw, rejected event/effect Promise and a supported React transition exception with a render failure; apply appropriate handling instead of promising that one boundary catches everything.

3. **Suspense for Supported Resources and Lazy Components** — Exercise a lazy-loaded React component with a real fallback; explain how a supported suspending resource can activate Suspense while arbitrary fetch inside an Effect cannot.

4. **Fallible Loading UI and Independent Error UI** — Keep pending loading, render exception, forbidden HTTP/data error and malformed response visibly distinguishable, including accessible focus/status recovery.

5. **Transitions, Deferred Values and Responsiveness** — Use startTransition/useTransition or useDeferredValue for one real nonurgent update where installed React supports it; compare an immediate-input path and reject false claims of CPU threads or automatic network cancellation.

6. **Version-Aware Optional Features and Boundary Tests** — Inspect the pinned version's supported actions/optimistic/suspending APIs as optional design alternatives, then test one genuinely unsupported assumption or incorrect catch/fallback pairing.

*Optional practice — Boundary Diagnosis:* Inject a render failure, an async rejection and a slow UI update; assign correct handling to boundary, event/error policy or transition and verify actual output.

### Module 11 — React-Specific Accessibility, Security and Human Evaluation

#### Outcomes

- APP20-O2
- APP20-O5
- APP20-O10
- APP20-O11
- APP20-O12
- APP20-O13

#### Lessons

1. **Native Semantics across Composition and Portals** — Verify native controls, label names, dialog/overlay keyboard behavior and focus return through React component/portal replacement instead of re-teaching APP17 label syntax.

2. **Pending, Error and Route-Change Announcements** — Test real dynamic status and error descriptions with visible and keyboard observations, and disclose what assistive-technology behavior was actually tested rather than inferred.

3. **Rendered Strings, HTML Sinks and User-Controlled URLs** — Prove React escapes text and why dangerouslySetInnerHTML, injected attributes or unvalidated href/src still require context-appropriate review; do not generalize text escaping to arbitrary DOM/script/URL contexts.

4. **Identity Privacy and Browser Security Boundaries** — Test a synthetic user switch for stale cached DOM/network values, sanitize diagnostics, avoid secrets in storage and explain why CORS and client-only guards cannot guarantee server authorization.

5. **Dynamic Reflow, Focus Visibility and User Preference Checks** — Recheck relevant WCAG 2.2 AA keyboard/focus/Focus Not Obscured, 320 CSS px reflow with exceptions and separate 200% text resizing; stress RTL/long text and reduced motion through real React state changes.

6. **Honest Usability Task and Repair Evidence** — Apply a repeatable task/failure rubric, explicitly distinguish synthetic persona or peer walkthrough from consenting participant evidence, repair one confusing outcome, and disclose untested scenarios without claiming WCAG certification.

*Optional practice — Trust and Accessibility Repair:* Repair a markup sink, persistent user-data flash or lost modal focus and collect clear negative-path evidence.

### Module 12 — Behavioral Testing, React Profiling and Optimization Limits

#### Outcomes

- APP20-O3
- APP20-O4
- APP20-O6
- APP20-O9
- APP20-O11
- APP20-O13
- APP20-O14
- APP20-O15

#### Lessons

1. **Behavior-First Component, Reducer and Hook Tests** — Test visible component outputs and actual user interactions with a maintained free compatible runner; check reducer transitions and public Hook behavior rather than implementation-specific hook invocation counts.

2. **Controlled Async, Strict Mode and Error Boundary Regressions** — Inject deferred request/race/identity changes, effect setup/teardown and real render/event errors with independent assertions; do not use arbitrary sleeps or development-only duplicate invocation as correctness criteria.

3. **Real Browser Route, Keyboard and Security Observations** — Verify direct-link reload, Back/Forward, focus/dialog status and unsafe-string handling in a local browser as distinct from jsdom/mocked component tests; report any inaccessible AT contexts.

4. **React Profiler and a User-Visible Bottleneck** — Record React/React DOM/browser/toolchain/build versions, device, fixture and comparable repeated render/interaction traces; connect a suspected slow update to real user work rather than counting rerenders alone.

5. **Memoization, React Compiler and Measured Alternatives** — Compare memo/useMemo/useCallback, context splitting and simpler workload reduction only for an observed bottleneck; React Compiler 1.0+ may automatically memoize in configured builds, so verify **whether it actually ran** rather than claiming manual memoization is always necessary.

6. **Before/After Correctness, Accessibility and Trade-off Defense** — Inspect variation and test whether the improvement preserves data, focus, navigation and failure recovery. Explain conceptual CSR/SSR/hydration/RSC ownership without requiring full-stack implementation.

*Optional practice — Performance Repair:* Fix a measured unnecessary render or expensive operation and defend the change with trace, correctness and accessibility evidence.

### Module 13 — One Integrated React Application and Independent Defense

#### Outcomes

- APP20-O1
- APP20-O2
- APP20-O3
- APP20-O4
- APP20-O5
- APP20-O6
- APP20-O7
- APP20-O8
- APP20-O9
- APP20-O10
- APP20-O11
- APP20-O12
- APP20-O13
- APP20-O14
- APP20-O15
- APP20-O16

#### Lessons

1. **One Task, Source and Accepted Evidence** — Choose a bounded synthetic multi-view React browser task and integrate the **same evolving project** evaluated in APP20-AS1–AS5; publish acceptance/error/privacy criteria and reference previous accepted evidence rather than build six unrelated apps.

2. **Compose State, Effects, Forms, Data and Navigation** — Complete coherent typed component identity, form recovery, properly synchronized external resources, validated async transport, user-safe caching and real route/focus behavior under an explicitly pinned compatible React/browser/toolchain.

3. **Security, Boundary and Performance Regression** — Verify genuine render error versus async/event failure handling, supported Suspense fallback, safe untrusted content/identity changes, accessibility and repeatable measured optimization; link previously accepted AS1–AS5 results where still valid.

4. **Unfamiliar Feature, Broken Assumption and Repair** — Address one new bounded React-specific feature or defect involving keys, state reset, render/effect cleanup, async navigation or a bad input; reproduce, correct and independently retest earlier contracts.

5. **Fresh Checkout, Toolchain and Technical Defense** — Build/serve/test in a documented free local offline-capable environment, provide one source/evidence index and defend React versus browser/framework/server boundaries, supported-version caveats, uncertainty and observed limits.

## Completion requirements

All **sixteen APP20 learning outcomes** require authentic evidence
through **six independently decidable summative assessments**.
APP20-AS1–AS5 inspect different rendering, state, synchronization,
network/navigation, boundary and performance competencies using
**one evolving local React project**; APP20-AS6 integrates their
accepted results with an unfamiliar bounded change and defense.
A reviewer may **reference already evaluated evidence** instead
of requiring six separate applications, duplicate traces or
a new project for each lesson. Formative investigations remain
optional preparation, not hidden completion gates.

| Required assessment | Required outcome coverage | Principal evidence |
| --- | --- | --- |
| `APP20-AS1` — Component, Render and Identity Investigation | APP20-O1, APP20-O2, APP20-O3, APP20-O4, APP20-O12, APP20-O13 | Versioned source/manifest/lockfile or local fixture provenance, compiler/build/test commands, component API notes, before/after key/identity trace and regression test, keyboard observation and concise design rationale |
| `APP20-AS2` — State, Forms, Hooks and Effect Lifecycle | APP20-O3, APP20-O4, APP20-O5, APP20-O6, APP20-O7, APP20-O8, APP20-O13, APP20-O14 | Feature source, transition table, accessibility observations, deterministic normal/error tests, Strict Mode subscription/teardown logs, before/after defect evidence and a short state/effect ownership explanation |
| `APP20-AS3` — React Data, Navigation and Race Recovery | APP20-O6, APP20-O8, APP20-O9, APP20-O10, APP20-O12, APP20-O13, APP20-O14 | Route and request contracts, synthetic fixture/adapter and response matrix, verified component integration tests with controlled promise order, focus/history observations, negative identity-cache tests, and a documented recovery/abort policy |
| `APP20-AS4` — Boundaries, Accessibility and Security Failure Audit | APP20-O2, APP20-O5, APP20-O7, APP20-O10, APP20-O11, APP20-O12, APP20-O13, APP20-O14 | Failure scenario matrix, rendered fallback/async regression tests, accessibility/keyboard-focus evidence and environment, safe rendering/privacy negative cases, a repaired defect history and explicitly bounded conformance observations |
| `APP20-AS5` — React Feature Architecture and Performance Decision | APP20-O3, APP20-O4, APP20-O6, APP20-O7, APP20-O8, APP20-O10, APP20-O13, APP20-O14, APP20-O15 | Before/after component/feature diagram, code diff and transition/contract tests, profiling environment and repeated trace summary, measured trade-offs, post-change keyboard/recovery checks and an architectural reflection |
| `APP20-AS6` — Integrated React Application and Independent Engineering Defense | APP20-O1, APP20-O2, APP20-O3, APP20-O4, APP20-O5, APP20-O6, APP20-O7, APP20-O8, APP20-O9, APP20-O10, APP20-O11, APP20-O12, APP20-O13, APP20-O14, APP20-O15, APP20-O16 | Version-controlled source, dependency/version/lockfile and offline fixture instructions, acceptance and state/route matrices, independent component/integration/browser tests, security/focus/a11y failure evidence, profiler measurements, clean-reproduction and change log, and a written/recorded/otherwise accessible technical defense |

### Shared execution, review and safety boundaries

- Use a documented compatible React/React DOM/TypeScript and
  open-source local build/test stack with recorded package
  versions, lockfile or equivalent pinned local artifacts,
  an ordinary unprivileged user and a supported browser.
  Validate that the example actually builds and runs,
  not merely type-checks. Reference Vite or another
  compatible build tool; do not rely on deprecated CRA.
- Required work uses locally served synthetic pages, local
  fixture responses or deterministic injected transports.
  Initial free toolchain installation/pre-provisioning may
  require Internet access, but no assessment must require
  a remote registry, paid environment, user login,
  public deployment or production backend. Do not make
  APP21 or APP3 an undeclared prerequisite.
- Follow the selected supported React API contract. Do not
  equate a render with DOM commitment or paint; treat key
  and position as component identity concerns. React
  implementation internals, specific scheduling timings,
  automatic compiler optimizations and development-only
  Strict Mode diagnostics are not universal runtime promises.
- Keep render pure. Calculate derived values **during render**
  and handle user intentions **in events** where appropriate;
  use appropriately cleaned-up Effects only for actual external
  synchronization with truthful dependencies. An arbitrary
  Effect-created Promise does not activate Suspense, and
  rendering error boundaries do not catch ordinary event
  handlers or every async failure. Abort/transition mechanisms
  never guarantee already-completed server work is undone.
- Validate untrusted JSON before constructing typed domain
  values. Inspect success, empty, malformed, forbidden,
  failed, aborted, stale and identity-changed outcomes as
  applicable. Untrusted HTML, unsafe link targets,
  browser storage and CORS do not replace safe API
  validation or server-side authorization.
- Ensure native semantics, keyboard use, focus management,
  understandable status/error announcements, reflow and
  reduced-motion behavior through component, route, error
  and loading transitions. Automated accessibility
  checks supplement but do not replace suitable manual
  inspection; disclose exactly what assistive-technology
  evidence was actually gathered.
- Performance investigations record browser/hardware,
  workload, React/React DOM/build and test versions,
  development/production configuration, whether React
  Compiler 1.0+ is **actually enabled and functioning**,
  and repeated trace variability. Do not count every
  re-render as a defect or present manual memoization as
  mandatory when automatic compiler optimization may
  already apply. Neither one Profiler trace nor a compiler
  configuration file proves user-visible speedup.
- Use synthetic users and sanitized local data. Never
  upload real secrets, private participant responses,
  cookies or production traffic into source, logs or
  public evidence. Distinguish a synthetic usability
  walkthrough from real user interviews, consented
  testing and verified product usability.
- An independent assessor may supply an unfamiliar
  bounded feature change, invalid fixture or relevant
  rendering defect, but not an unpublished proprietary
  tool, full-stack service or framework requirement.
  A written, recorded, live or equivalent accessible
  reviewable defense can satisfy the same public
  technical criteria.

### Required summative assessments

- **APP20-AS1** (required component, render and identity investigation)
  - Outcomes: APP20-O1, APP20-O2, APP20-O3, APP20-O4, APP20-O12, APP20-O13
  - Work: Begin **the one cumulative React project** from a small accessible APP2-style task view and a recorded compatible React/React DOM/TypeScript build. Establish typed props, children and semantic native controls, reproduce and repair a real key/position identity bug where rows swap draft/focus or unexpectedly reset, and compare actual browser render/commit output. Use safe React text rendering for a synthetic hostile string and separately check an externally controlled link/attribute context; explain why escaping an ordinary text child does not authorize arbitrary HTML/URL insertion.
  - Criteria: The clean checkout builds and renders under the recorded React/React DOM/compiler versions; public props and children types are sound; native control semantics and keyboard access remain usable. A stable-key and a deliberate-reset scenario behave correctly under add/remove/reorder, and a prior erroneous state/DOM association is reproduced and fixed. The learner distinguishes React element description, render and commit, and shows why untrusted text does not require unsafe `innerHTML` insertion.
  - Evidence: Versioned source/manifest/lockfile or local fixture provenance, compiler/build/test commands, component API notes, before/after key/identity trace and regression test, keyboard observation and concise design rationale.

- **APP20-AS2** (required state, forms, hooks and effect lifecycle)
  - Outcomes: APP20-O3, APP20-O4, APP20-O5, APP20-O6, APP20-O7, APP20-O8, APP20-O13, APP20-O14
  - Work: Extend **the same project** with a real multi-state form/editable feature, a chosen controlled/uncontrolled input policy and a meaningful reducer or justified local state. Repair a stale render snapshot, redundant Effect or lost draft/focus case. Use a documented external mock subscription or bounded non-React widget to exercise genuine Effect/ref ownership; show correct dependencies, setup/cleanup on prop change/unmount, and React development Strict Mode's setup-cleanup check without falsely asserting a fixed number of production executions. Test accessibility and both an invalid domain input and aborted/late completion path.
  - Criteria: Actual user action and form state follow the declared transition table with recoverable draft values, accessible errors and no unhandled duplicate submission. Stale snapshots/illegal transitions are repaired without DOM mutation or disabled dependency lint. The external adapter/ref is initialized/updated/disposed under explicit ownership, leaving **at most the intended active instance** after development Strict Mode checks and none after unmount. Native event and form semantics are preserved; TS-only validation or a development render-count assertion is insufficient.
  - Evidence: Feature source, transition table, accessibility observations, deterministic normal/error tests, Strict Mode subscription/teardown logs, before/after defect evidence and a short state/effect ownership explanation.

- **APP20-AS3** (required React data, navigation and race recovery)
  - Outcomes: APP20-O6, APP20-O8, APP20-O9, APP20-O10, APP20-O12, APP20-O13, APP20-O14
  - Work: Extend **the one React app** with a supplied/injected deterministic Fetch-compatible transport, runtime decoding and two real client routes. Test success/**204 no-body**, empty, 4xx/5xx fulfilled HTTP error, forbidden/conflict, malformed JSON, network rejection, abort and deliberately out-of-order responses. Prove a late result cannot expose former-user data or overwrite the latest route even where abort does not cancel underlying work; demonstrate cache invalidation and an uncertain mutation's explicit retry/rollback policy. Test **direct-link reload under the real local host**, Back/Forward, title/focus/scroll and route identity/teardown, not merely a mocked router navigation. No backend framework, identity service or cloud endpoint may be imposed.
  - Criteria: 204/no-body and HTTP status are handled without unsafe JSON assumptions, checked payloads do not silently become trusted TypeScript values and obsolete results never overwrite a changed route or identity. Data is cleared/partitioned at user switch; an uncertain write is not blindly replayed. Real direct-load/History behavior, focus/title/scroll, navigation cleanup and the chosen server's rewrite/fallback limitations match observed browser evidence; client guards are not called authorization.
  - Evidence: Route and request contracts, synthetic fixture/adapter and response matrix, verified component integration tests with controlled promise order, focus/history observations, negative identity-cache tests, and a documented recovery/abort policy.

- **APP20-AS4** (required boundaries, accessibility and security failure audit)
  - Outcomes: APP20-O2, APP20-O5, APP20-O7, APP20-O10, APP20-O11, APP20-O12, APP20-O13, APP20-O14
  - Work: Audit **the cumulative app** with (1) an actual eligible render failure and React error-boundary/reset behavior, (2) a distinct event-handler or ordinary async rejection that must be handled separately, and (3) a **genuinely supported Suspense trigger**, such as a lazy component, not a Promise started in an Effect. Add an overlay or route transition where focus/keyboard/status fails, then repair it and a context-sensitive unsafe HTML/URL or stale-identity presentation flaw. Scope WCAG 2.2 reflow/focus/announcements and actual assistive-tech evidence honestly; no fictitious participant testing or blanket conformance claim.
  - Criteria: Test evidence distinguishes **render/error-boundary, independent event/async failure and true Suspense fallback** with appropriate reset/recovery. The overlay/route is keyboard-operable with meaningful accessible name/status and intentional focus; applicable WCAG 2.2 reflow near 320 CSS px, separate 200% text resize and Focus Not Obscured are checked at realistic dynamic states. Unsafe HTML/URL contexts are prevented, identity-scoped data does not leak, and automated/keyboard/actual screen-reader observations are clearly differentiated without unsupported site-wide conformance claims.
  - Evidence: Failure scenario matrix, rendered fallback/async regression tests, accessibility/keyboard-focus evidence and environment, safe rendering/privacy negative cases, a repaired defect history and explicitly bounded conformance observations.

- **APP20-AS5** (required React feature architecture and performance decision)
  - Outcomes: APP20-O3, APP20-O4, APP20-O6, APP20-O7, APP20-O8, APP20-O10, APP20-O13, APP20-O14, APP20-O15
  - Work: Restructure **the evolving app** around justified component/reducer/context, custom Hook and ref ownership, compare a simpler baseline against a genuine change and test independent consumers. Identify **one user-visible measured bottleneck** under a recorded React/React DOM/browser/device/build/fixture; investigate a specific render or interaction cause with React Profiler or equivalent trace and repeated observations. Compare a proportionate fix with unnecessary memo/useMemo/useCallback, context splitting or compiler-assisted optimization. If React Compiler is used, demonstrate actual configured output; otherwise state that it is absent. Rerun functional, stale-data, keyboard/focus and error-path tests. Defend the client-rendering versus SSR/hydration/RSC responsibilities without implementing a production server framework.
  - Criteria: Reusable boundaries improve or justifiably preserve change/test cost without hiding invalid shared state, Effects or uncontrolled refs. Measurements identify an actual user-visible problem, comparable environment and variance; render count alone is not a pass. The learner discloses the **real compiler setting and observed effect**, not an assumed React release optimization; manual memoization is optional when no measurement warrants it. The optimization preserves function, identity, async and accessible user paths, and the broader client/server rendering alternatives are explained correctly.
  - Evidence: Before/after component/feature diagram, code diff and transition/contract tests, profiling environment and repeated trace summary, measured trade-offs, post-change keyboard/recovery checks and an architectural reflection.

- **APP20-AS6** (required integrated React application and independent engineering defense)
  - Outcomes: APP20-O1, APP20-O2, APP20-O3, APP20-O4, APP20-O5, APP20-O6, APP20-O7, APP20-O8, APP20-O9, APP20-O10, APP20-O11, APP20-O12, APP20-O13, APP20-O14, APP20-O15, APP20-O16
  - Work: Complete **the single cumulative React app** already judged through APP20-AS1–AS5. Integrate the accepted component, state, Effect/ref, form, data/route, error/Suspense, security, accessibility and performance behavior using source/fixtures and **references to previously accepted evidence**. Accept an unfamiliar but bounded changed identity, keyboard/focus, route, key/state, effect cleanup or async failure requirement, reproduce a defect and independently repair it without regressing earlier contracts. Verify a free local clean-checkout build, run and tests, then defend React-specific ownership and limits without adding a backend, paid framework or cloud requirement.
  - Criteria: A reviewer can reproduce the local app and observed behavior using documented compatible free tooling and synthetic fixtures, including real browser navigation, errors, correctly owned external resources and accessible user actions. The unknown change is repaired with explicit before/after evidence and no regression to previously accepted invariants. **AS6 integration cannot excuse a missing or failed APP20-AS1–AS5 decision.** Unsafe data exposure, inaccessible required action or unrepeatable build/flow blocks completion. The learner explains React guarantees versus DOM/TypeScript/APP3 server responsibilities and observed version/measurement limits.
  - Evidence: One versioned source/fixture bundle, recorded React/React DOM/TypeScript and build/test compatibility, local clean-start instructions, **an outcomes-to-prior-accepted-AS1–AS5 evidence index** instead of copied logs, unfamiliar-change source/regression trace, only necessary new integrated checks, explicit untested risks and a reviewable written, recorded or accessible technical defense.

### Completion decision, status and revision safety

Completion requires an inspectable acceptable review decision
on `APP20-AS1` through `APP20-AS6` that jointly demonstrates
`APP20-O1` through `APP20-O16`. Reused artifacts must be
evaluated under the *new* integrated change/failure criteria.
A working happy-path SPA, generated component code, a
type-check log or a single accessibility/performance
score does not establish all the stated capabilities.

Material violation of correctness, accessible recovery,
security/privacy boundaries, resource cleanup or clean
reproduction criteria requires repair before passing.
Review records should retain actual revision, assessment
IDs, source/evidence locations, environment and test
conditions, uncertainty and documented limitations
under [OEE Evidence Rules](../../spec/evidence-rules.md).

APP20 remains an OEE `v0.2.0` **draft**,
not learner-tested, independently verified or
accredited by a source-only curriculum review.
APP2 remains the distinct framework-neutral prerequisite;
the APP catalog **already includes** APP3, APP5 and APP9
with their own published integration and graduation
assessment contracts. This reassessment neither changes
those course outcomes nor automatically upgrades
historical learner completions, which remain tied to
their actual evaluated course/specification revisions.

### Public non-mandatory study references

These accessible references support precise inspection
of React and host behavior. All required outcomes,
work, criteria and evidence are published above; no
paid content or proprietary test platform is needed.

- [React Learn](https://react.dev/learn) for component,
  rendering, identity, state and effect mechanisms.
- [React Rendering Lists](https://react.dev/learn/rendering-lists)
  and [Preserving and Resetting State](https://react.dev/learn/preserving-and-resetting-state)
  for stable keys and component identity.
- [React Synchronizing with Effects](https://react.dev/learn/synchronizing-with-effects)
  and [You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect)
  for actual synchronization boundaries and cleanup.
- [React Component Error Boundaries](https://react.dev/reference/react/Component)
  and [React Suspense](https://react.dev/reference/react/Suspense)
  for rendering fault and loading boundaries.
- [React Hooks Reference](https://react.dev/reference/react/hooks)
  for version-specific Hooks and state contracts.
- [React Creating a React App](https://react.dev/learn/creating-a-react-app)
  for framework versus small client-only project choices.
- [React Router documentation](https://reactrouter.com/home)
  and [Vite guide](https://vite.dev/guide/) for one
  compatible open-source navigation/build reference.
- [TypeScript JSX reference](https://www.typescriptlang.org/docs/handbook/jsx.html)
  for TypeScript JSX configuration.
- [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
  and [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
  for properly scoped accessibility investigations.
