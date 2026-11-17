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

### Module 1 — React in the Application Engineering Pathway

#### Outcomes

- APP20-O1
- APP20-O2
- APP20-O15

#### Lessons

1. **Course Orientation and React's Role** — Locate React in the history of interactive UIs and explain why the component model addresses coordination and change, not replacement of Internet, HTML/CSS, JavaScript or browser mechanics.

2. **Browser Foundations and React Runtime Boundaries** — Review native DOM/events, form semantics, user journeys, fetch failure, client history and focus management; identify React-specific decisions to learn here; distinguish React's declarative model and state update APIs, the browser renderer `react-dom`, JSX transformation and actual DOM APIs.

3. **Choose and Record the Reference Toolchain** — Prepare an explicitly versioned open-source React/TypeScript project using a simple local build tool such as Vite, or an equivalent compatible toolchain; document React and React DOM versions.

4. **Developer Tool versus Browser Runtime** — Trace what Node/npm do during development/build versus what a delivered bundle executes in a browser; APP21 server implementation is not a prerequisite.

5. **A Minimal Root and Clean Bootstrap** — Render a typed root into a known DOM container, detect missing mounts and verify output with a local server, without a proprietary deployment target.

6. **React Frameworks versus React Library** — Explain why production-scale React apps may use integrated frameworks; justify using a small client-only project for mechanism study and reserve full-stack server frameworks for later courses.

7. **Deprecations and Supported APIs** — Avoid relying on deprecated Create React App or accidental experimental API behavior; compare the current official React API contract with installed package versions.

*Optional practice — Setup Failure:* Diagnose incompatible renderer/dependency versions, failed JSX compilation or wrong browser import assumptions, then reproduce from a clean copy.

### Module 2 — JSX, Typed Components and Composition Contracts

#### Outcomes

- APP20-O1
- APP20-O2
- APP20-O12
- APP20-O13

#### Lessons

1. **JSX as JavaScript Syntax** — Trace compilation to React elements and distinguish JSX expressions from HTML source strings or a template engine that can execute injected markup.

2. **Function Components and Naming** — Build reusable component functions with accurate names, explicit inputs and consistent return shapes rather than calling components as ordinary imperative functions.

3. **Typed Props and Children** — Create type-safe required/optional props, callback signatures and composable children with justified React type definitions, without repeating the entire APP19 type system.

4. **Props, Data Direction and Ownership** — Follow one-way data flow through a component tree and explain why a child should not mutate parent-owned props.

5. **Conditional Rendering** — Use readable branching, `null` and explicit status variants; avoid accidentally rendering numerical or falsey sentinel values as misleading UI.

6. **List Rendering and Stable Keys** — Map bounded data to elements with genuine stable identities and test addition/removal/reordering; do not use random or index keys where identity matters.

7. **Component Composition and Slots** — Compare children, composition helpers and small feature components with overly generic configurable abstractions; favor accessible native controls where available.

8. **Safe Text and Intentional HTML** — Demonstrate React's normal escaping of rendered strings and define a narrow, reviewed policy for any genuinely necessary `dangerouslySetInnerHTML` case.

*Optional practice — Component Contract Review:* Refactor a monolithic static/reactive view into typed composable parts and verify its semantics and invalid-prop boundaries.

### Module 3 — Render, Commit, Identity and Reconciliation

#### Outcomes

- APP20-O2
- APP20-O3
- APP20-O4
- APP20-O15

#### Lessons

1. **Render and Commit as Conceptual Phases** — Explain rendering as React calculating UI output and commit as applying necessary DOM changes; distinguish later browser paint from React's own commit.

2. **Pure Render Logic** — Reproduce a bug from mutating external variables or making a network call while rendering and repair it without assuming renders run exactly once.

3. **Position, Keys and Component State Identity** — Trace which component identity preserves state across parent rerenders and which type/position changes cause reset; demonstrate resetting a form by changing a key deliberately versus accidentally resetting every row with unstable identity.

4. **Reordering, Controlled Tests and DOM Observations** — Observe list reorder with stable versus index keys and explain visible wrong-value/focus consequences without depending on private Fiber details.

5. **Development Strict Mode Checks** — Inspect development-only render purity and effect setup/cleanup stress behavior; avoid claiming every extra observation occurs in production.

6. **React Element Identity versus DOM Mutation** — Explain why a React element value is a description and why directly mutating React-owned DOM can be overwritten on a subsequent commit.

7. **State Preservation across Dynamic Layout** — Move a subtree and evaluate whether intended draft, focus or selection state should survive; document the chosen identity mechanism.

*Optional practice — Identity Diagnosis:* Repair a list whose typed rows swap internal input values after reordering and provide a small regression demonstration.

### Module 4 — State Snapshots, Events, Updates and Derived Data

#### Outcomes

- APP20-O3
- APP20-O4
- APP20-O5

#### Lessons

1. **State as a Render Snapshot** — Explain why an event handler observes the state captured by its render and why a setter requests a future render rather than mutating a local variable.

2. **Event Handlers and React Event Props** — Apply React-supported handlers to native controls, preserve default actions intentionally, and distinguish React event callbacks from manual DOM listeners.

3. **Functional State Updaters** — Repair repeated incremental updates by deriving the next state from the queued previous value; inspect outcomes under batching.

4. **Immutable Object and Array Updates** — Copy just the state path that changes, avoid mutating prior snapshots and distinguish deep identity changes from shallow spreads.

5. **Derived State during Render** — Compute filtered lists, labels and summaries directly during render when possible instead of syncing redundant state through an Effect.

6. **Avoid Contradictory Booleans** — Use a discriminated UI status for mutually exclusive workflows; do not store simultaneously impossible loading, success and failure flags.

7. **Event Actions versus Reactive Synchronization** — Put a user-initiated request or message in the event that knows its intent, not an Effect that later guesses why state changed.

8. **State Lifetime and Reset** — Reset a scoped feature intentionally on identity or navigation changes while preserving unrelated drafts and accessible focus.

*Optional practice — Stale Snapshot Repair:* Reproduce an incorrect double update or state mutation, write a behavior test, then fix it without introducing a spurious Effect.

### Module 5 — Accessible React Forms and Submission Lifecycles

#### Outcomes

- APP20-O2
- APP20-O4
- APP20-O5
- APP20-O12
- APP20-O13

#### Lessons

1. **Native Form Semantics in React** — Reuse APP17/APP2 label, fieldset, input type, keyboard and submit behavior; avoid custom controls when native ones satisfy the task.

2. **Controlled and Uncontrolled Inputs** — Choose `value`/`onChange`, `defaultValue`, refs and native FormData by desired source of truth and performance, rather than declaring one approach universally superior.

3. **Text, Checkbox, Select and File Semantics** — Model multiple input kinds accurately, including immutable FileList constraints and when a form control cannot be treated as a controlled text input.

4. **Validation at Form and Domain Boundaries** — Combine relevant native constraints with explicit runtime domain rules; TypeScript does not make user input or remote data trusted.

5. **Pending, Success and Recoverable Errors** — Represent submission status honestly, keep draft input after recoverable failures and avoid disabling every control indefinitely.

6. **Duplicate Submission and Uncertain Outcomes** — Handle repeated submit clicks and late responses; distinguish UI suppression from true server-side idempotence or exactly-once guarantees.

7. **Accessible Errors and Focus Recovery** — Associate field errors and status messages with controls, move focus when justified and verify useful announcements without flooding live regions.

8. **React Version-Specific Form APIs** — Inspect whether the installed maintained React version supports action-based form mechanisms; compare with standard event submission without making unverified new APIs mandatory.

*Optional practice — Form Defect:* Fix a lost draft, stale validation message or inadvertent repeated submit, then verify keyboard and negative-path behavior.

### Module 6 — Hooks Rules, Effects and Synchronization

#### Outcomes

- APP20-O4
- APP20-O6
- APP20-O7
- APP20-O9
- APP20-O14

#### Lessons

1. **Rules of Hooks and Component Boundaries** — Use Hooks at the top level of React components or custom Hooks, not in loops, conditions, callbacks or arbitrary utilities; show a negative static/lint case.

2. **Distinguish Render, Event and Effect Logic** — Classify calculations, user-intent actions and external system synchronization, refactoring an unnecessary `useEffect` into render or event logic.

3. **Effect Setup and Dependency Correctness** — Use `useEffect` to synchronize external subscriptions or APIs; list reactive dependencies honestly rather than suppress lint to force a desired lifetime.

4. **Cleanup and Identity Changes** — Subscribe and unsubscribe correctly on dependency change/unmount; implement idempotent cleanup of event listeners, timers and local mock connections.

5. **Strict Mode Development Stress Test** — Demonstrate setup-cleanup-setup behavior under a selected React development configuration; ensure repeated setup cannot create duplicate live subscriptions.

6. **Effects and Fetch Race Ownership** — When teaching a minimal effect-based fetch, abort or ignore obsolete results and test late completions; explain why mature data routing/caching solutions can be preferable.

7. **Effect Timing and Layout Effects** — Contrast `useEffect` and `useLayoutEffect` when a justified DOM measurement requires a pre-paint adjustment, noting visual and performance costs.

8. **Custom Hook as Shared Behavior** — Extract reusable stateful behavior while preserving Rules of Hooks, dependency correctness and independent hook instance state.

*Optional practice — Effect Bug:* Repair a stale closure, subscription leak or dependency-suppression defect with a reproducible Strict Mode test and documented cleanup.

### Module 7 — Refs, Imperative Escape Hatches and Non-React Integration

#### Outcomes

- APP20-O3
- APP20-O6
- APP20-O7
- APP20-O13

#### Lessons

1. **Ref Identity and Mutable Handles** — Distinguish `useRef` stable holder values from state-triggered rendering; do not mutate refs during render to smuggle visible state changes.

2. **Focus and Selection after Updates** — Apply refs to native focus or selection behavior with correct timing and preserve APP2's keyboard interaction requirements.

3. **Managing Timers and Abort Controllers** — Own cancellable work using refs or effect-local resources as appropriate and document who releases each resource.

4. **Interacting with a Non-React Widget** — Wrap a small mock map/chart/editor in a bounded adapter, describe its create/update/destroy protocol and keep React-owned DOM separate.

5. **Version-Aware Ref Passing** — Use ref patterns supported by the selected React release, distinguishing React 19 ref-as-prop behavior from legacy forwarding APIs when reviewing older code.

6. **React Portal Semantics** — Create a dialog-like overlay using a portal when justified; inspect event ancestry, focus trapping and stacking without assuming portal placement alone ensures accessibility.

7. **Synchronizing a Third-Party Instance** — Avoid reinitializing a widget on every render; update it through a justified Effect and tear it down cleanly.

*Optional practice — Integration Leak:* Reproduce duplicate widget creation, stale focus or a lingering external callback, then repair with verified lifecycle evidence.

### Module 8 — React Feature Architecture and State Ownership

#### Outcomes

- APP20-O2
- APP20-O4
- APP20-O6
- APP20-O8
- APP20-O16

#### Lessons

1. **Local State versus Shared State** — Choose nearest component ownership for a draft, selection or modal; lift state only when more than one participant truly needs synchronization.

2. **Component and Feature Boundaries** — Decompose a user task into cohesive domain, view and data-adapter layers, avoiding a single global feature component or excessive prop drilling.

3. **Custom Hooks for Behavior, not Presentation** — Package repeated app behavior with an explicit API and testable dependencies while retaining clear DOM/UI ownership.

4. **Reducers for Complex Transition Logic** — Use `useReducer` for a justified multi-event state machine and test transitions as pure functions.

5. **Context for Dependency Distribution** — Use `createContext`/`useContext` to distribute an appropriate stable service/theme or scoped user identity; avoid treating context as free global cache infrastructure.

6. **Context Changes and Render Scope** — Explain how provider value changes affect consumers and when splitting contexts or placing providers locally reduces unnecessary coupling.

7. **External Stores and Integration** — Recognize `useSyncExternalStore` as a version-aware integration tool for an actual external store; no Redux/Zustand or other specific library is required.

8. **Immutable Domain State and Validation** — Preserve type-safe state transitions and runtime data validation across component boundaries without introducing brittle casts.

9. **Maintainability and Change Cost** — Implement a bounded new feature in one component tree and justify whether reuse reduced or increased coupling and test burden.

*Optional practice — Architecture Review:* Compare a broad context and an intentional feature-local reducer, make a defensible choice and test independent feature instances.

### Module 9 — React Data Integration, Loading and Mutation Recovery

#### Outcomes

- APP20-O6
- APP20-O8
- APP20-O9
- APP20-O12
- APP20-O14

#### Lessons

1. **From APP2 Fetch to React Data Lifetimes** — Reuse Fetch/HTTP response correctness, async races, typed input validation and identity-scoped caches; focus here on React ownership and render synchronization.

2. **Validated Transport and Typed Domain Models** — Keep raw response parsing external to presentational components and return a checked result/typed error rather than asserting unknown JSON.

3. **Pending, Empty, Forbidden, Error and Success UI** — Render distinct status variants with appropriate accessible announcements, route behavior and recovery actions.

4. **Race Safety Across Prop and Identity Changes** — Demonstrate stale request completion after a key/user/route change; abort/ignore obsolete responses and prove no incorrect user data appears.

5. **Cache Keys, Freshness and Eviction** — Choose a bounded local cache policy, invalidation scope and identity separation; explain the limits of handwritten effect-based caching.

6. **Mutation State and Optimistic Presentation** — Apply a mutation with known recovery, visible pending status and rollback/uncertainty policy; do not reissue non-idempotent mutations blindly.

7. **Server-State Libraries and Router Loaders** — Compare a small hand-authored adapter to optional open-source declarative data fetching or router data APIs; no named library beyond React is a mandatory educational gate.

8. **Request Cancellation Limitations** — Explain that abort may stop browser-side work but not reverse already completed server mutations; keep feedback truthful after uncertain network outcomes.

*Optional practice — Async Race:* Fix a user-switch stale-data leak under deterministic deferred responses and document a regression for the changed component identity.

### Module 10 — React Routing, Navigation and User Context

#### Outcomes

- APP20-O8
- APP20-O9
- APP20-O10
- APP20-O13

#### Lessons

1. **Browser Routing versus React Rendering** — Explain that URL/History behavior remains a browser contract while React is responsible for route-driven component composition and state ownership.

2. **Choose a Documented Router Strategy** — Use a compatible open-source React router (for example a documented React Router release) or an equivalent small adapter for a bounded client-only app; no full-stack framework or vendor account is required.

3. **Nested Routes, Layouts and State Lifetime** — Decide which layout/content persists as routes change and when feature state resets; test identity and keyed boundaries.

4. **Navigation with Deep Links** — Support direct route loads with local server fallback, Back/Forward, meaningful links and correct handling of unrecognized routes.

5. **Route Params and Search Inputs** — Parse and validate untrusted parameters, separate navigation intent from accepted domain input and avoid constructing unsafe links.

6. **Focus, Title and Announcements** — Implement intentional document title and focus strategy after route changes, including errors/empty states and keyboard-only traversal.

7. **Route-Aware Requests and Cleanup** — Abort/ignore obsolete route data, prevent old identity-state flashes and verify cleanup when moving between pages.

8. **Authorization Display versus Actual Policy** — Present forbidden/unauthenticated states honestly while stating that client-side route guards cannot enforce server permissions.

*Optional practice — Navigation Failure:* Repair a direct-link reload, stale loader or lost focus and verify with real browser history interactions.

### Module 11 — React Error Boundaries, Suspense and Scheduling

#### Outcomes

- APP20-O3
- APP20-O6
- APP20-O9
- APP20-O11
- APP20-O14

#### Lessons

1. **Rendering Errors and Recovery Boundaries** — Place an error boundary around a meaningful feature region to prevent a localized render failure from blanking unrelated UI; show a safe fallback and reset path.

2. **What Error Boundaries Do Not Catch** — Demonstrate that ordinary event-handler errors, asynchronous callbacks and server-side rendering failures require appropriate separate handling; qualify version-specific transition exceptions.

3. **Loading Fallbacks versus Error Fallbacks** — Differentiate pending input/data, an unexpected render failure and a recoverable request rejection; use honest user-visible statuses.

4. **Suspense Contract and Scope** — Explain Suspense boundaries for React-supported suspending resources, lazy components or compatible frameworks; do not claim arbitrary async work in an Effect automatically suspends.

5. **Lazy Loaded Components** — Load a feature component lazily with React's supported mechanism and a focused Suspense fallback, with testable local chunk delivery.

6. **Transitions and Responsiveness** — Use version-supported `startTransition`/`useTransition` for a justified nonurgent update; explain that transitions are scheduler hints, not threads or automatic network prioritization.

7. **Urgent Input versus Deferred Views** — Compare an immediately updated input with a heavy derived view, including when `useDeferredValue` is justified and when simpler work reduction is preferable.

8. **React Version-Specific Async Actions** — Inspect documented installed-release capabilities such as action state/optimistic helpers where available; classify optional enhancements separately from required stable React guarantees.

*Optional practice — Boundary Diagnosis:* Inject a render failure, an async rejection and a slow UI update; assign correct handling to boundary, event/error policy or transition and verify actual output.

### Module 12 — Accessibility, Browser Security and Privacy in React

#### Outcomes

- APP20-O2
- APP20-O5
- APP20-O10
- APP20-O11
- APP20-O12
- APP20-O13

#### Lessons

1. **Semantic Components versus Styled Divs** — Review the native link/button/form semantics inherited from APP17/APP2 and check they survive component abstraction.

2. **Focus, Portals and Dynamic Updates** — Audit focus restoration on dialog close, route update or error reset; check that a portal alone does not create a valid modal focus pattern.

3. **Status Announcements and Pending States** — Associate dynamic error/status messages and progress with accessible names and live regions without duplicate/late announcements.

4. **Keyboard and Reflow Regression** — Test component controls under keyboard-only, zoom/reflow, reduced motion and longer text in the actual React-rendered app.

5. **Safe Default Escaping and Dangerous HTML** — Explain normal React text rendering and why dangerous HTML insertion requires a trusted, context-appropriate sanitization/design policy.

6. **Trusted Attributes, Links and URLs** — Validate navigation targets and externally derived URLs; avoid unsafe patterns or user-controlled script destinations.

7. **Credentials and Identity-Sensitive State** — Prevent storing personal secrets in test fixtures/logs, wipe user-scoped caches on identity changes and explain why CORS or hidden buttons are not server authorization.

8. **Error and Telemetry Privacy** — Use stable nonsecret error labels and synthetic request IDs; avoid logging raw responses or sensitive payloads during diagnostics.

9. **Usability Evidence and Provenance** — Evaluate a provided task with honest synthetic, peer or participant observations; document consent and limits when any real-person testing occurs.

*Optional practice — Trust and Accessibility Repair:* Repair a markup sink, persistent user-data flash or lost modal focus and collect clear negative-path evidence.

### Module 13 — React Testing, Debugging and Performance Decisions

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

1. **Behavior-Focused Component Testing** — Test rendered output and real user actions with a maintained open-source React-compatible test library or equivalent environment, avoiding assertions about internal hook implementation.

2. **Reducer and Custom Hook Unit Tests** — Test pure state transitions and exposed feature contracts with invalid events and boundary inputs.

3. **Integration Tests with Controlled Data** — Inject deterministic HTTP/async results, including network failures, malformed payloads, late completions and identity changes without brittle timer sleeps.

4. **Development Strict Mode and Cleanup Tests** — Verify a mounted/unmounted component cleans up external subscriptions and side effects without taking development-only double-invocation as a user-visible invariant.

5. **Error Boundary and Route Tests** — Trigger actual render failures, deep-link reloads, Back/Forward navigation and fallback recovery with appropriate test infrastructure.

6. **Keyboard and Screen Reader Evidence** — Document real keyboard focus/announcements; use automated checks as a supplement and disclose whether actual assistive-technology inspection was conducted.

7. **React DevTools and Profiler Evidence** — Capture bounded component render costs and causes, record version/build conditions and avoid equating all re-renders with performance problems.

8. **Memoization and Stable Identity** — Evaluate `memo`, `useMemo`, `useCallback` and context splitting only where a measured issue warrants it; explain semantic correctness independent of caching.

9. **React Compiler and Automatic Optimizations** — Describe version-conditioned compiler support and its limits; do not demand manual memoization or compiler enablement without verifying toolchain behavior.

10. **Reproducible Load and Interaction Experiment** — Record device/browser/throttling and before/after traces, then rerun functional, async and accessible user-task checks.

*Optional practice — Performance Repair:* Fix a measured unnecessary render or expensive operation and defend the change with trace, correctness and accessibility evidence.

### Module 14 — React Application Integration, Delivery and Defense

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

1. **Choose a Bounded React Product Slice** — Define an accessible multi-view, user-task-driven React feature such as a local request dashboard or library catalog with synthetic data, explicit privacy and recovery requirements.

2. **Publish Requirements and Component Boundaries** — State task acceptance, component/route responsibilities, data contracts, permissions presentation and testable failure behavior before choosing state libraries.

3. **Plan and Build the Reference Project** — Configure compatible React, React DOM and TypeScript versions, review dependency and lockfile provenance and produce a clean local build without deprecated scaffolding.

4. **Explain Rendering Strategy Alternatives** — Compare client rendering, SSR, hydration, pre-rendering and server components conceptually and identify when a framework is appropriate; do not claim these all occur in the required client-only project.

5. **Integrate State, Forms and Reusable Components** — Build a stable key-aware component hierarchy with typed props, appropriate local/shared state and accessible form/recovery flows.

6. **Integrate Route and Data Workflows** — Implement local multi-route navigation, reliable async fixture-backed data, identity-safe cache handling, errors and retry status.

7. **Exercise Suspense, Boundary and External Synchronization** — Use a justified lazy/Suspense loading boundary, one appropriate render error boundary and correctly cleaned-up Effect; trace distinct error categories.

8. **Verify Security, Accessibility and Usability** — Use a reviewed negative-path matrix for unsafe content, wrong identity, keyboard/focus and task comprehension, preserving honest evidence provenance.

9. **Measure and Improve a Real Bottleneck** — Capture repeatable component/perceived interaction measurements, apply one justified optimization and verify unaffected functional/accessibility behavior.

10. **Reproduce and Defend an Unfamiliar Change** — Start from a clean checkout, apply a bounded new feature or defect fix, demonstrate regression safety and defend the chosen React mechanisms and remaining limitations.

## Completion requirements

**All sixteen APP20 learning outcomes** must be demonstrated
through the **six required summative assessments** below.
Their artifacts can form one evolving React application; six
separate products are not required. Lesson investigations,
exploration and formative feedback are preparation rather
than extra independent graduation requirements.

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
- Keep render pure and put external synchronization in
  appropriately cleaned-up Effects. Do not suppress actual
  dependencies to force behavior, claim timers/abort undo
  past mutations, or treat an Effect-created promise as
  automatically triggering Suspense. Explicit event and
  async error handling is required where rendering error
  boundaries do not apply.
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
- Performance investigations use documented browser,
  hardware, data volume, development/production build,
  compiler behavior and repeat measurement conditions.
  Profiler output and caching hints support limited
  engineering arguments, not an unsupported guarantee
  of global speedup or safety.
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
  - Work: Given an accessible static APP2-style task view, build a small typed React/React DOM project from a documented local toolchain. Refactor repeated markup into coherent props/children components, then reproduce and repair a keyed-list or position-dependent state-reset defect. Demonstrate pure rendering, correct React text escaping of supplied untrusted strings, intentional element semantics, and explain the render/commit boundary using actual browser output without relying on React internal implementation details.
  - Criteria: The clean checkout builds and renders under the recorded React/React DOM/compiler versions; public props and children types are sound; native control semantics and keyboard access remain usable. A stable-key and a deliberate-reset scenario behave correctly under add/remove/reorder, and a prior erroneous state/DOM association is reproduced and fixed. The learner distinguishes React element description, render and commit, and shows why untrusted text does not require unsafe `innerHTML` insertion.
  - Evidence: Versioned source/manifest/lockfile or local fixture provenance, compiler/build/test commands, component API notes, before/after key/identity trace and regression test, keyboard observation and concise design rationale.

- **APP20-AS2** (required state, forms, hooks and effect lifecycle)
  - Outcomes: APP20-O3, APP20-O4, APP20-O5, APP20-O6, APP20-O7, APP20-O8, APP20-O13, APP20-O14
  - Work: Implement a typed multi-state form or editable workflow with deliberate controlled/uncontrolled choices, a reducer or justified local-state alternative, accessible pending/invalid/success/recovery views and an external mock subscription or non-React widget requiring an Effect/ref. Reproduce and repair stale state, an unnecessary Effect, duplicated subscription under development Strict Mode or a lost focus/draft fault, and verify correctly bounded setup/cleanup on dependency changes and unmount.
  - Criteria: Submission behavior follows a published transition matrix; keyboard, focus, field labels/errors and recovery are usable; stale closures, mutation and duplicate listener bugs are prevented with correct state ownership. Hooks follow their rules and dependencies are not falsified to suppress warnings. An effect actually synchronizes with an external system, survives Strict Mode's development checks without duplicate active subscriptions, and disposes only resources it owns. A successful type check alone does not substitute for runtime input and cleanup tests.
  - Evidence: Feature source, transition table, accessibility observations, deterministic normal/error tests, Strict Mode subscription/teardown logs, before/after defect evidence and a short state/effect ownership explanation.

- **APP20-AS3** (required react data, navigation and race recovery)
  - Outcomes: APP20-O6, APP20-O8, APP20-O9, APP20-O10, APP20-O12, APP20-O13, APP20-O14
  - Work: Integrate synthetic HTTP-like data through an injected adapter or supplied free local fixture service into a multi-view React feature. Verify loading, empty, forbidden, conflict, malformed, network-rejected, timeout/abort and success outcomes; validate unknown data at runtime, not by assertion. Add two route-like views through a documented compatible open-source client router or equivalent adapter, test deep links, Back/Forward, title/focus behavior and identity-scoped cache/late-response safety. Demonstrate an uncertain mutation without blindly replaying it.
  - Criteria: Correctly distinguishes HTTP error Responses from rejected fetch, and validates data shapes before presenting domain values. Obsolete results never overwrite a newer route or identity, even if abort is late; private prior-user data does not flash during context changes. Route behavior and focus/title transitions match stated policy, including refresh fallback, and retry/optimistic actions preserve honest uncertainty. No learner-built Node server, database or authenticated cloud service is needed.
  - Evidence: Route and request contracts, synthetic fixture/adapter and response matrix, verified component integration tests with controlled promise order, focus/history observations, negative identity-cache tests, and a documented recovery/abort policy.

- **APP20-AS4** (required boundaries, accessibility and security failure audit)
  - Outcomes: APP20-O2, APP20-O5, APP20-O7, APP20-O10, APP20-O11, APP20-O12, APP20-O13, APP20-O14
  - Work: Audit a representative React feature with an intentional rendering exception, a separate event-handler or async failure, a lazy-loaded/Suspense component and a focus-sensitive overlay or route transition. Implement meaningful React rendering error isolation, distinguish nonboundary failures, and repair accessible status/focus and unsafe DOM/data handling. Use scoped WCAG 2.2/accessibility criteria, manual keyboard inspection, free automated checks where available, and feasible screen-reader review or a transparent untested disclaimer.
  - Criteria: The error boundary contains an eligible render error without falsely claiming to catch all event/async exceptions; the lazy component shows an appropriate Suspense fallback rather than relying on an arbitrary useEffect promise. Fault and recovery states are named, nonsecret and testable. Overlay/route interactions preserve keyboard and focus behavior, dynamic status is meaningful, untrusted text/links and identity-scoped data do not leak into unsafe UI, and evidence distinguishes tested criteria from unverified accessibility claims.
  - Evidence: Failure scenario matrix, rendered fallback/async regression tests, accessibility/keyboard-focus evidence and environment, safe rendering/privacy negative cases, a repaired defect history and explicitly bounded conformance observations.

- **APP20-AS5** (required react feature architecture and performance decision)
  - Outcomes: APP20-O3, APP20-O4, APP20-O6, APP20-O7, APP20-O8, APP20-O10, APP20-O13, APP20-O14, APP20-O15
  - Work: Refactor or extend an existing typed React feature with justified component, reducer/context, custom Hook and ref boundaries, rejecting unnecessary global state and manual memoization. Investigate a measurable rendering or interaction problem with a declared browser/device/build workload and React Profiler or equivalent traces; apply one defensible optimization, compare repeated baseline and changed runs, and test that navigation, async recovery, keyboard usability and correctness remain intact. Explain how client rendering differs conceptually from SSR/hydration and what additional framework/server capability would be required, without implementing a production SSR service.
  - Criteria: State ownership and public API choices reduce or justify coupling; component identity and Effects remain correct under changed props/route conditions. An actual measured bottleneck—not simple render count or a single synthetic score—supports the optimization, and observed variance, React/compiler versions and possible automatic optimization are disclosed. No caching hint is treated as a semantic guarantee; functional/negative/accessibility regression tests still pass. The learner correctly identifies which rendering strategies are outside this client-only course.
  - Evidence: Before/after component/feature diagram, code diff and transition/contract tests, profiling environment and repeated trace summary, measured trade-offs, post-change keyboard/recovery checks and an architectural reflection.

- **APP20-AS6** (required integrated react application and independent engineering defense)
  - Outcomes: APP20-O1, APP20-O2, APP20-O3, APP20-O4, APP20-O5, APP20-O6, APP20-O7, APP20-O8, APP20-O9, APP20-O10, APP20-O11, APP20-O12, APP20-O13, APP20-O14, APP20-O15, APP20-O16
  - Work: Deliver one cohesive, versioned React/TypeScript browser application solving a bounded user problem, with composable typed components, stable identity, explicit state and form contracts, correctly owned Effect/ref work, multiple navigable views, runtime-validated asynchronous data from free local fixtures, usable errors/empty/loading/forbidden/retry states, intentional render/Suspense boundaries, accessible keyboard/focus behavior, safe identity/data handling and measurable interaction diagnosis. Reuse qualifying prior assessments rather than creating six unrelated applications. Prove clean-checkout build/run/test behavior, demonstrate a controlled failure and repair, accept an unfamiliar bounded user requirement or bug, and defend React-specific decisions without making APP3, a server framework, cloud deployment or elective technology prerequisites.
  - Criteria: A reviewer with the recorded compatible open-source local toolchain can reproduce the app, fixture data, tests and at least one failure/recovery exercise without hidden paid/vendor access. Published task acceptance and negative paths are visibly met; validation, stale-data protection, focus/navigation and render boundary policies function as described. React mechanisms (render/commit, keyed identity, snapshots, Effects, refs, data loading and error handling) are explained accurately, with bounded security and performance claims. The unfamiliar change preserves prior correctness and accessibility; limitations, untested contexts and dependency/version risks are explicit.
  - Evidence: Version-controlled source, dependency/version/lockfile and offline fixture instructions, acceptance and state/route matrices, independent component/integration/browser tests, security/focus/a11y failure evidence, profiler measurements, clean-reproduction and change log, and a written/recorded/otherwise accessible technical defense.

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

APP20 is introduced as an OEE `v0.2.0` **draft**
course, not a learner-tested or independently verified
course. Adding it to the program core expands the
APP9 prerequisite closure but does not retroactively
change historical learner completions or certify
earlier evidence. APP2's framework-neutral browser
assessment contract remains distinct and unchanged.
The eventual APP3, APP5 and APP9 migrations will
address their own integration and production
assessment obligations separately.

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
