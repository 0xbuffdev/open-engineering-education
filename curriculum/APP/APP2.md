# APP2 — Browser & Frontend Engineering

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `core`
**Prerequisites:** [APP17](APP17.md) — HTML & CSS Engineering, [APP19](APP19.md) — TypeScript Programming
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (provisional; calibrate against learner evidence)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Engineer interactive browser applications **without first depending
on a UI framework**. Begin with user tasks and acceptance criteria,
then make semantic, responsive documents interactive through
browser DOM and event APIs. Model typed state and validation,
handle asynchronous data and network failures, preserve user
intent across transitions and navigation, protect browser trust
boundaries, evaluate accessible interaction and usability,
and diagnose a measured performance or lifecycle defect.
Finish with a reproducible, tested application and an
independent engineering defense.

This is the **browser interaction** course, not a second
course in HTML/CSS, JavaScript or the TypeScript language.
[APP17](APP17.md) already teaches semantic markup, native
forms, accessibility foundations and responsive CSS.
[APP18](APP18.md) and [APP19](APP19.md) supply language,
asynchrony, module, testing and static type competencies;
APP19 also depends on APP18. APP2 teaches their application
to browser host APIs, DOM ownership, interactive components,
asynchronous views, client-side navigation and user needs.

**Framework-neutral is a real assessment boundary.**
Use TypeScript and standard browser DOM/Fetch/History APIs,
not React component lifecycles, framework routers,
framework-specific state management or server rendering.
Those belong to [APP20](APP20.md) — React Application Engineering. Likewise, designing a
production API, implementing authorization on a server,
building Node HTTP infrastructure, database engineering,
distributed caching and infrastructure deployment belong
to APP3, APP21, APP4, APP8 or other specialized courses.

A locally served static document and compiled browser JavaScript
are sufficient for the core project. Use a supplied local
HTTP fixture server, deterministic injected transport adapter,
or equivalent free mock responses to model real request
outcomes; students are **not required to implement a backend**.
The direct prerequisites are APP17 and APP19; APP1/APP18
are satisfied transitively. A compiler and supported browser
with development tools can be installed or provided before
the assessments. The implemented project must remain
reproducible with local synthetic data and no required
public endpoint, remote test harness, paid tool, domain,
proprietary accessibility software, account, API key or
production identity system.

User research and accessibility evidence must be honest.
A synthetic persona is a design hypothesis, not a human
interview. A keyboard-only review or automated audit is
not proof that a screen-reader user tested the interface.
Actual participant feedback is optional where access or
consent is unavailable; publish what was observed, not
fictional conclusions. Do not collect or publish private
user data to satisfy an OEE assessment.

Browser guarantees must also be accurately bounded.
`fetch()` normally **fulfills** for an HTTP 404 or 500
response, but rejects for a network or abort-related
failure; successful TypeScript checking does not validate
JSON at runtime. `history.pushState()` does not itself
emit `popstate`. Client-side route and permission checks
do not replace server-side authentication/authorization;
CORS restricts browser script access, not who is allowed
to use an API. Avoid claiming a fixed rendering interval,
universal cache policy or complete WCAG certification
from one synthetic environment.

Duration and workload are estimates, not proof of educational
quality. Modules organize authentic explanations,
investigations, failure analysis and progressively less
scaffolded implementation. Only the explicitly required
assessments below establish summative completion evidence;
other module activities are formative.

## Learning outcomes

- **APP2-O1:** Translate a bounded user task into observable interaction requirements, acceptance criteria, data/privacy assumptions and state-transition scenarios, distinguishing supplied assumptions from genuine user-research findings.
- **APP2-O2:** Implement predictable, semantic DOM updates using standard browser APIs and TypeScript, explaining browser-owned versus application-owned state, safe content rendering, and differences between DOM properties and HTML strings.
- **APP2-O3:** Explain and correctly handle browser event propagation, delegation, defaults and listener lifecycles; preserve keyboard, pointer, focus and cleanup behavior through dynamic interface changes.
- **APP2-O4:** Investigate browser task/microtask scheduling, rendering opportunities and work on the main thread; choose appropriate updates and cleanup strategies for timing-sensitive interactions without assuming exact frame or network timing.
- **APP2-O5:** Implement accessible interactive forms with native semantics, explicit domain validation and useful field-level error/recovery behavior, and distinguish client checks from server trust and authorization.
- **APP2-O6:** Model typed UI inputs and state transitions with reusable framework-independent components and discriminated states, validating untrusted runtime values before presenting them and preventing unsupported actions.
- **APP2-O7:** Implement and diagnose browser Fetch API workflows, distinguishing HTTP failure status from rejected network operations, response decoding, abort/cancellation limits, origin/credentials rules and data trust boundaries.
- **APP2-O8:** Manage asynchronous view state, request races, stale results, simple cache validity, mutations and recovery without losing user intent, replaying unsafe actions, or exposing stale private content.
- **APP2-O9:** Provide usable client-side navigation with meaningful URLs, History API behavior, direct-link fallback, back/forward correctness, and intentional keyboard focus, title and scroll behavior.
- **APP2-O10:** Identify and mitigate representative browser application security and privacy risks, including untrusted DOM content, origin/CORS misconceptions, credential exposure, client storage limits and unauthorized UI data handling.
- **APP2-O11:** Audit and repair dynamic accessibility behavior using keyboard interaction, focus management, accessible names/status announcements, semantic controls, responsive reflow and reasonable assistive-technology inspection or disclosed equivalent evidence.
- **APP2-O12:** Evaluate a representative interaction against explicit usability, localization and human-centered requirements, accounting for user feedback provenance, error comprehension, input methods, reduced motion and variable text direction or length.
- **APP2-O13:** Design deterministic browser integration and negative-path tests, reproduce real DOM/network/focus defects, and measure a bounded loading or interaction bottleneck without mistaking a noisy trace for universal performance evidence.
- **APP2-O14:** Deliver, reproduce, maintain and defend a cohesive framework-neutral browser application with accessible user flows, typed and validated state, resilient data access, security boundaries, automated verification and an unfamiliar bounded change.

## Modules

### Module 1 — User Tasks, Browser Capabilities and Interaction Contracts

#### Outcomes

- APP2-O1
- APP2-O2
- APP2-O12

#### Lessons

1. **A Browser Task and Its Host Boundary** — Given a realistic but fictional user request, distinguish APP17 semantic HTML/CSS and APP18/APP19 JavaScript/TypeScript preparation from browser-owned DOM/events, storage, Fetch and History capabilities. Situate browser interactivity briefly in its historical evolution while defining a concrete user task and the client/server trust boundary.

2. **Observable State, Failure and Acceptance Criteria** — Map relevant idle, editing, loading, empty, success, rejected, forbidden, stale and recovery transitions to observable actions and accessible acceptance tests; discard irrelevant template states rather than require every possible label.

3. **Assumptions, User Research and Data Provenance** — Distinguish synthetic personas, supplied stakeholder requirements, consenting participant observations and independent research; explain what each can and cannot prove, and minimize any recorded personal data.

4. **An Initial Task-Based Walkthrough** — Apply a repeatable task/expected-outcome rubric to a supplied interface, expose a misleading happy path, confusing recovery instruction or inaccessible flow, and record honest limitations before implementation.

*Optional practice — task-mapping review:* Inspect a misleading happy-path-only interface specification and identify absent error, focus and authorization outcome cases.

### Module 2 — DOM Ownership, Safe Rendering and Predictable Updates

#### Outcomes

- APP2-O2
- APP2-O3
- APP2-O6
- APP2-O10

#### Lessons

1. **From Parsed DOM to Owned Mutations** — Select stable elements with querySelector, construct nodes, append or replaceChildren and handle missing targets; distinguish DOM properties, rendered CSS and application state without repeating APP1 parsing theory.

2. **Untrusted Data and Context-Safe Rendering** — Demonstrate why textContent or text nodes are appropriate for untrusted **ordinary text**, not a universal sanitizer for script/style contents or dangerous URL/attribute contexts. Validate URLs and attribute semantics separately and reject unsafe innerHTML interpolation.

3. **Properties, Attributes and Live Control State** — Contrast input.value, checked and serialized attributes; inspect when live input state diverges from authored markup and must not be reset by rerenders.

4. **Scoped Rerendering and User-Intent Preservation** — Update only necessary regions, preserve selection, draft values, focus and accessible names, and explain when DOM replacement invalidates owned element references.

5. **Meaningful Loading, Empty, Failed and Result Content** — Render semantic content for actual request/state outcomes, including appropriate status/focus information, without smuggling component framework lifecycles into simple DOM code.

*Optional practice — DOM security defect:* Replace an unsafe dynamic HTML insertion with safe DOM construction and assert both displayed content and absence of injected executable elements.

### Module 3 — Events, Native Interaction and Resource Lifetime

#### Outcomes

- APP2-O2
- APP2-O3
- APP2-O4
- APP2-O11

#### Lessons

1. **Capture, target and bubble phases** — Trace event propagation with explicit DOM structure and explain capture/bubble ordering without treating every event as bubbling.

2. **Event delegation and dynamic nodes** — Attach delegated handlers to a stable parent, interpret event.target/currentTarget and choose closest/contains checks.

3. **Default Actions, Pointer and Keyboard Parity** — Preserve link/form/button native behaviors, Enter/Space and pointer/touch activation; use preventDefault only with an equivalent justified action, not as a blanket interception mechanism.

4. **Focus Through Dynamic UI Changes** — Trace document.activeElement, focus order, disclosure/dialog activation and the suitable destination for focus after a component is dismissed or replaced; do not impose a universal focus jump on every change.

5. **Listener Ownership, AbortSignal and Stale Nodes** — Reproduce duplicate delegated listeners or a removed-node reference; repair with correctly owned removal/AbortSignal and disposal, and prove two component instances do not share accidental handlers.

6. **Custom Event Contracts Where Justified** — Demonstrate a bounded CustomEvent payload and propagation policy between components, then compare it with a simpler direct callback; do not require a global event bus when local events suffice.

*Optional practice — interaction repair:* Reproduce a duplicate-action or lost-focus bug, provide failing test evidence and demonstrate a corrected listener lifecycle.

### Module 4 — Main-Thread Scheduling and Lifecycle Constraints

#### Outcomes

- APP2-O3
- APP2-O4
- APP2-O13

#### Lessons

1. **Tasks, Microtasks and Interaction Delays** — Reproduce a bounded long synchronous task and compare promise jobs, event tasks and host scheduling opportunities using a browser trace. Apply APP18 scheduling knowledge without claiming a universal rendering/frame sequence.

2. **Animation Frames and Layout Read/Write Effects** — Use requestAnimationFrame for a justified visual update and inspect forced-layout patterns and the effect of grouping reads/writes; recognize that rAF is not a fixed-rate timer.

3. **Debouncing and Preserving the Last Intent** — Use bounded debounce/throttle semantics for a real search/resize interaction and demonstrate that the final user input is not silently discarded. Correctness tests must not depend on fragile arbitrary sleep durations.

4. **Hidden Documents and Scheduled Work** — Explain tab visibility/background timer limitations and check the lifecycle of a hidden/suspended interface; do not treat background timers as durable application jobs.

5. **Cancel and Discard Owned Work** — Cancel owned frames/timers/listeners/requests during teardown, distinguish cancellation signals from already-completed work or server rollback, and reproduce a repeated-mount cleanup failure.

*Optional practice — scheduling trace:* Predict an interaction trace, collect actual browser observations, repair one ordering or responsiveness fault and state unproven timing assumptions.

### Module 5 — Dynamic Forms, Domain Validation and Recovery

#### Outcomes

- APP2-O1
- APP2-O3
- APP2-O5
- APP2-O11

#### Lessons

1. **Native Forms Meet Validated Domain Input** — Apply APP17 accessible labels, fieldsets and native constraints, then use actual browser validity APIs and JavaScript domain validation for missing, malformed, range and business-rule cases. TypeScript annotations are not runtime checks.

2. **Submission, Pending and Duplicate-Action Policy** — Transition explicitly between editing, pending, success and failed submission; prevent unsupported duplicate actions without leaving an inaccessible, indefinitely disabled form.

3. **Accessible Field Errors and Clear Status** — Associate per-field guidance and error messages with controls, signal important state transitions proportionately and demonstrate sensible focus/keyboard recovery without overstating guaranteed screen-reader announcements.

4. **Conditional Steps, Draft Values and User Recovery** — Preserve meaningful input across multi-step forms, validation errors and local retry, and state precisely whether drafts are in memory, deliberately persisted or not retained.

5. **Progressive Enhancement and the Server Trust Boundary** — Justify any custom client-side form behavior against robust native fallback; explain that client checks, displayed success and a hidden control cannot validate server authorization or guarantee an accepted write.

*Optional practice — form audit:* Inject missing and invalid values and repair a misleading success banner, hidden error or lost in-progress input.

### Module 6 — Framework-Independent Components and Typed State Transitions

#### Outcomes

- APP2-O2
- APP2-O5
- APP2-O6
- APP2-O13

#### Lessons

1. **Browser-Executable TypeScript and Component Ownership** — Produce browser-compatible JavaScript from documented APP19 tooling and define a minimal typed render/update/dispose contract; distinguish compiler diagnostics from actual DOM and runtime validation.

2. **Discriminated States from Domain Requirements** — Model only relevant idle/editing/loading/success/empty/error/forbidden variants with state-specific data instead of contradictory flags; align each state with visible/accessible output.

3. **Action and Completion Transitions** — Build an explicit transition table for user actions, asynchronous results, cancellations and navigation, with invalid transitions rejected or ignored according to a documented policy.

4. **Single Source of Truth and Derived DOM** — Identify canonical application state versus temporary DOM-owned control state, and repair a stale duplicate that would overwrite current user intent.

5. **Untrusted Fixture to Typed View Model** — Validate an unknown JSON-like fixture against the actual domain contract before presentation; demonstrate a malformed counterexample not protected by erased TypeScript types.

6. **Two Instances and Independent Teardown** — Exercise multiple component instances to prove isolated state, handlers and caches, including a remount/cancel scenario; avoid hiding accidental singleton behavior.

*Optional practice — state refactor:* Turn an ad-hoc conditional UI into a typed transition-driven component and demonstrate corrected invalid-state behavior.

### Module 7 — Browser Fetch, Response Contracts and Origin Limits

#### Outcomes

- APP2-O6
- APP2-O7
- APP2-O10

#### Lessons

1. **Fetch Fulfillment and HTTP Status Contracts** — Handle Request/Response and status/ok semantics, explicitly distinguishing a fulfilled 404/500 from network rejection and handling 204/no-body without blindly calling response.json; define domain error cases separately from HTTP status.

2. **Decode and Validate Untrusted Bodies** — Check appropriate media type and decode fallibility, reject wrong/missing/invalid JSON shapes as unknown and present errors through safe ordinary-text sinks rather than executable HTML.

3. **Abort Controllers, Body Consumption and Side Effects** — Reproduce abort before and after response headers but before a body is consumed; distinguish rejected consumption, stale-result suppression and the fact that an abort cannot be assumed to undo a server mutation.

4. **Same-Origin, Preflight and CORS's Actual Scope** — Contrast browser origin enforcement, credentialed cross-origin conditions, preflight and response readability with the separate server authorization decision; CORS is not an API access-control system.

5. **Cookies, Credentials and Cross-Site Request Risks** — Inspect fetch credential modes and relevant cookie/SameSite assumptions with a synthetic fixture; identify why some cross-site requests can still be sent and why CSRF authorization belongs to the server.

6. **Deterministic Local HTTP and Injected Transport Fixtures** — Provide reproducible local success/204/4xx/5xx/malformed/offline responses or a deterministic injected fetch-compatible adapter; require real browser DOM observations separately without forcing a learner-written Node backend.

*Optional practice — network matrix:* Simulate 200/204/400/401/403/404/409/500, malformed JSON, aborted fetch and offline cases; compare the visible UI to its documented failure policy.

### Module 8 — Async View Consistency, Cache Ownership and Mutation Safety

#### Outcomes

- APP2-O1
- APP2-O6
- APP2-O7
- APP2-O8
- APP2-O10

#### Lessons

1. **Explicit Remote and Local View State** — Separate remote authoritative records from local selection/draft state; represent unrequested, empty, pending, failed, forbidden and resolved results truthfully, not by one overloaded boolean.

2. **Late Completion and Latest-Intent Protection** — Reproduce out-of-order responses with controlled deferred operations and show an identity/version guard preventing old results from overwriting a newer query or a changed user.

3. **Cache Keys, Freshness and Identity Isolation** — Define cache key, expiration/invalidation and memory limits; reject permanently valid responses and clear or partition identity-scoped data at sign-out/authorization change.

4. **Optimistic Changes, Conflict and Rollback** — Use optimistic updates only where domain policy supports them; demonstrate a failed mutation, visible rollback/reconciliation and a preserved user draft.

5. **Retries, Idempotency and Uncertain Results** — Classify retriable reads versus uncertain side-effecting writes, use bounded retry/backoff where justified and avoid automatic replay of a potentially committed mutation.

6. **Paginated and Partial Data Recovery** — Represent cursor/offset and partial-success cases with stable IDs and deterministic merging; diagnose duplicates or missing records on a fixture where page contents change.

*Optional practice — race and cache defect:* Reproduce a stale authorized result or duplicate mutation, repair it and write a deterministic regression test without network sleep timing.

### Module 9 — History, URLs, Deep Links and Accessible Navigation

#### Outcomes

- APP2-O1
- APP2-O3
- APP2-O9
- APP2-O11

#### Lessons

1. **Route Inputs and Direct-Link Hosting** — Use URL APIs to validate pathname/search/hash inputs, choose ordinary native navigation where possible, and verify a real direct-link static-host fallback or explicit route strategy instead of assuming every static server rewrites paths.

2. **History Entries, popstate and Initial State** — Use pushState/replaceState and Back/Forward correctly, noting that calling them does **not** fire popstate; include initial/null history state and content restoration in a deterministic route trace.

3. **Native Anchors and Interception Boundaries** — Preserve modifier-click, copying links, context menus and normal anchor defaults, intercepting only safe same-origin navigations that the application actually owns.

4. **Focus, Title, Scroll and Draft Context** — Define appropriate title/heading/focus/scroll behavior for routes and browser history, protecting relevant drafts and keyboard continuity without moving focus by arbitrary blanket rules.

5. **Route Teardown and Reproducible Navigation Failures** — Demonstrate direct-load, Back/Forward or stale-request failure, dispose route-owned listeners and in-flight work, repair the cause and recheck that restricted data cannot flash on route changes.

*Optional practice — deep-link incident:* Demonstrate a failure when loading a route directly or pressing Back, fix the environment/routing policy and record keyboard behavior.

### Module 10 — Browser Security, Storage and User-Identity Boundaries

#### Outcomes

- APP2-O2
- APP2-O7
- APP2-O8
- APP2-O10

#### Lessons

1. **Trust Model and Context-Sensitive DOM XSS** — Identify attacker-controlled URL, response and stored values, test a safe synthetic injection/unsafe HTML-sink counterexample, and explain why textContent is appropriate only for ordinary text (not executable script/style content or unchecked URL destinations).

2. **Same-Origin, CORS, CSRF and Authorization** — Contrast browser read restrictions and cross-site request abilities with authoritative server access control, token/cookie protections and CSRF defenses; never treat a hidden button or CORS header as proof of authorization.

3. **Storage and Credential Lifetime** — Compare in-memory state, sessionStorage, localStorage and IndexedDB by retention and threat properties; avoid persisting secrets or private responses without an explicit justified policy, and understand XSS exposure.

4. **CSP as Defense in Depth** — Explain a restrictive Content Security Policy, safe script practices and why CSP does not substitute for correct output handling, runtime data validation or server authorization.

5. **Sign-Out, Cache Separation and Negative Authorization Paths** — Test sign-out/forbidden flows and stale memory/storage/cache/rendered content under two synthetic identities; verify that cross-identity data is not exposed after transition.

*Optional practice — security and privacy test:* Repair untrusted text rendering or an identity-scoped stale-cache leak, and state server-side protections that APP2 cannot prove.

### Module 11 — Inclusive Dynamic Accessibility and User-Task Evaluation

#### Outcomes

- APP2-O1
- APP2-O3
- APP2-O5
- APP2-O9
- APP2-O11
- APP2-O12

#### Lessons

1. **Native Semantics and Chosen Interactive Patterns** — Apply APP17's native semantic controls and inspect justified dialog/disclosure or composite behavior from WAI-ARIA APG; do not replace built-in interactions with ARIA role labels that lack keyboard functionality.

2. **Keyboard Journey, Visibility and Focus Ownership** — Trace Enter/Space/Escape/tab behavior, focus order and restoration after modal/route changes, distinguishing hidden, inert and disabled elements; test WCAG 2.2 Focus Not Obscured (Minimum) where applicable.

3. **Accessible Names, Field Errors and Async Status** — Inspect real name/description/role/state relationships and appropriate status/live announcements for loading, validation and results; distinguish manual/automated indications from confirmed assistive-technology behavior.

4. **Reflow, Text Zoom and Dynamic State Stress** — Inspect interactive failure/success/dialog states near 320 CSS pixels for reflow (with genuine two-dimensional exceptions), and separately test 200% text resize/zoom, sticky focus obstruction and touch/keyboard operation; do not repeat APP17 introductory CSS instruction.

5. **Localization, Long Text, Bidirectionality and Motion** — Use suitable Intl number/date formatting in a real workflow, stress long and RTL strings without corrupting data meaning, and respect reduced-motion/contrast preferences with understandable non-animated state changes.

6. **A Scoped WCAG and Assistive-Technology Audit** — Select relevant WCAG 2.2 AA checks and WAI-ARIA patterns, compare automated warnings, keyboard inspection and feasible actual screen-reader observations; label untested assistive technologies and never infer site-wide conformance.

7. **Repeatable Usability Task, Guidance and Provenance** — Have a supplied synthetic/consenting participant or clearly labeled reviewer attempt a defined task and failure recovery; record observed comprehension and input-mode difficulties, improve one message or transition and limit claims to the evidence actually collected.

*Optional practice — accessibility defect triage:* Repair a focus trap, missing error announcement or inaccessible async status and show the before/after behavior in the same environment.

### Module 12 — Measured Interaction, Regression Testing and Independent Defense

#### Outcomes

- APP2-O1
- APP2-O2
- APP2-O3
- APP2-O4
- APP2-O5
- APP2-O6
- APP2-O7
- APP2-O8
- APP2-O9
- APP2-O10
- APP2-O11
- APP2-O12
- APP2-O13
- APP2-O14

#### Lessons

1. **Reproducible Browser Performance Conditions** — Choose a user-visible slow interaction/load and record browser, device, throttle, warm/cold cache and bounded fixture size; inspect relevant long tasks, layout shifts or load/interaction observations without inventing a universal performance threshold.

2. **Root-Cause Trace and Bounded Correction** — Use actual DevTools/Performance observation to attribute a DOM update, layout read/write, retained handler or oversized response bottleneck, make a narrow correction and report repeated before/after measurements and variance.

3. **Correctness and Accessibility after Optimization** — Verify that measured improvements do not lose user input, violate async authority, remove focus visibility, break reduced-motion behavior or create confusing status announcements.

4. **Deterministic State, Transport and Real Browser Tests** — Combine pure state transition tests and controlled HTTP responses with at least one real local-browser DOM/keyboard/history integration observation; do not claim a stub alone proves all browser host behavior.

5. **Negative-Path and Lifetime Regression Matrix** — Inspect invalid forms, HTTP error/204, malformed body, aborted/late response, forbidden identity, Back/Forward restoration, unsafe text and remount cleanup, linking already accepted evidence instead of redoing every full assessment.

6. **One Cumulative Framework-Neutral User Flow** — Integrate the same semantic APP17 source and APP19-typed components, validation, route, local data adapter, accessible form, measured interaction and secure identity handling into **one** coherent browser app from APP2-AS1–AS5.

7. **Unfamiliar Change, Clean Build and Technical Defense** — Respond to a bounded changed user need, browser failure, unsafe DOM value or race scenario, reproduce and repair it without regressions, then build/serve/test from a clean local checkout and defend choices and declared limits.

## Completion requirements

All **fourteen required course outcomes** must be demonstrated in
**six independently decidable summative assessments**, normally
using **one evolving locally served browser application**.
APP2-AS1–AS5 each assess a distinguishable interaction,
state/transport, accessibility/security or performance
competence; APP2-AS6 integrates their accepted work with
an unfamiliar bounded change and independent defense.
Previously accepted source, fixtures and test observations
may be **referenced** rather than rebuilt or resubmitted as
six unrelated applications. Optional formative investigations
do not create extra completion decisions.

| Required assessment | Required outcome coverage | Principal evidence |
| --- | --- | --- |
| `APP2-AS1` — User-task Requirements and Framework-Neutral DOM Interaction | APP2-O1, APP2-O2, APP2-O3, APP2-O4, APP2-O6 | Requirements/task table, typed DOM component source, synthetic fixtures, event/timing and focus traces, before/after cleanup test, security-negative test for untrusted text, and a concise mechanism-based rationale |
| `APP2-AS2` — Accessible Form and Typed State-Transition Investigation | APP2-O1, APP2-O3, APP2-O5, APP2-O6, APP2-O11, APP2-O12 | Form HTML/TypeScript component, state diagram, acceptance and invalid-input matrix, keyboard/focus/error recordings or equivalent annotated observations, regression tests, and a short task-evaluation limitations note |
| `APP2-AS3` — Asynchronous Data, Cache, and Navigation Recovery | APP2-O6, APP2-O7, APP2-O8, APP2-O9, APP2-O10, APP2-O13 | Typed transport and state code, locally reproducible fixture/adapter and versioned response scenarios, deterministic race/abort tests, route/history and focus traces, cache invalidation tests, and a failure-policy explanation |
| `APP2-AS4` — Dynamic Accessibility, Usability and Browser Security Audit | APP2-O1, APP2-O2, APP2-O5, APP2-O9, APP2-O10, APP2-O11, APP2-O12 | Audit scope and WCAG-criterion references, test environments, failing/passing examples, DOM/security regression tests, focus/status observations, representative localized/reflowed interaction, usability-task notes and remaining-risk statement |
| `APP2-AS5` — Browser Performance and Regression Diagnosis | APP2-O3, APP2-O4, APP2-O8, APP2-O11, APP2-O13 | Fixture and runnable app, before/after profiler trace or bounded observation log, reproducible procedure and timing summaries, identified cause, diff and normal/negative regression tests, and performance/accessibility trade-off rationale |
| `APP2-AS6` — Framework-Neutral Browser Application and Technical Defense | APP2-O1, APP2-O2, APP2-O3, APP2-O4, APP2-O5, APP2-O6, APP2-O7, APP2-O8, APP2-O9, APP2-O10, APP2-O11, APP2-O12, APP2-O13, APP2-O14 | Versioned source, static assets and local fixture recipe, TypeScript build steps, task/acceptance and state-transition matrices, scripted and browser test results, negative request and DOM security evidence, keyboard/focus and usability notes, performance measurements, clean-checkout verification, changed code history and accessible written/recorded/otherwise reviewable defense |

### Shared assessment, reproducibility and safety boundaries

- Use a supported standards-capable browser and current free
  TypeScript/JavaScript tooling from APP19/APP18. Record browser
  and tool versions, build/start/test commands and local origin.
  Serve local pages on loopback rather than relying on
  `file://` restrictions or a paid/public deployment.
- Use a synthetic dataset and **supplied local fixture responses**
  or a deterministic injected Fetch-compatible adapter: creating
  APP21/APP3 backend source is not a hidden prerequisite.
  For actual browser host behavior, include independent local
  browser inspection: isolated mocks do **not** alone establish
  focus, History, CORS or real network-layer semantics.
  A direct-link strategy must actually work with the chosen
  local static server rather than assume an unconfigured
  history-fallback rewrite.
- Use semantic APP17 HTML/CSS and browser-compatible
  JavaScript output from TypeScript without a React,
  component framework or paid bundler dependency. Do not
  falsely claim types exist at runtime. Validate actual
  response payloads before the internal model.
- Evaluate success, **204/no-body**, empty, malformed,
  unauthorized/forbidden, transient HTTP failures, rejected
  network operations, abort **including after headers but
  before body consumption**, and late completion where
  applicable. An HTTP 4xx/5xx response commonly **fulfills**
  `fetch()` with `ok=false`; it is not a transport rejection.
  Abort does not guarantee reversal of server actions.
  Never replay uncertain non-idempotent writes automatically.
- Preserve native semantics, keyboard and focus behavior,
  real accessible error/status presentation and route
  navigability through failure and success. Where relevant,
  check **reflow near 320 CSS pixels** (with legitimate
  two-dimensional exceptions), **200% text resize separately**,
  dynamic names/status and **WCAG 2.2 AA Focus Not Obscured
  (Minimum)**. Report actually inspected assistive technologies
  and criteria; never claim whole-site WCAG conformance from
  a limited review.
- Do not expose secrets, cookies, tokens or personal data
  in code, fixtures, local logs or assessment material.
  CORS, browser storage and hidden UI controls cannot
  substitute for server authorization. Display untrusted
  **ordinary text** using safe DOM text nodes/`textContent`,
  but do **not** treat textContent inside script/style
  elements or unvalidated URL/attribute assignments as
  universally safe; apply context-specific restrictions.
- A provided synthetic persona/task, peer inspection,
  heuristic evaluation and actual participant usability
  observations are different kinds of evidence. Label
  their source truthfully and avoid manufacturing user
  interviews. If involving real participants, use
  consent and proportionate data minimization.
- For performance, record browser/device, network/CPU
  profiles, workload, warm/cold cache conditions and
  comparable before/after traces. A single performance
  score or noisy millisecond reading is not a reliable
  general production claim. Retest accessibility and
  correctness after optimizations.
- Include an appropriately scoped unseen fault or
  maintenance request aligned with the published
  outcomes. A technical defense can be written,
  recorded, synchronous or another equivalently
  accessible reviewable format; no hidden proprietary
  environment or additional backend course may be
  imposed by an evaluator.

### Required summative assessments

- **APP2-AS1** (required user-task requirements and framework-neutral DOM interaction)
  - Outcomes: APP2-O1, APP2-O2, APP2-O3, APP2-O4, APP2-O6
  - Work: Begin **the same cumulative app** with an explicit fictional user task, accepted/rejected states and honest source assumptions, starting from APP17-style semantic markup. Add APP19-typed DOM update behavior and intentional event delegation/handler ownership; preserve keyboard defaults and focus through a real component replacement. Display synthetic hostile **ordinary text** through suitable safe DOM nodes, and separately validate any user-controlled destination URL/attribute rather than asserting all textContent uses or assignments are safe. Trace one task/microtask/visual-update case with qualified browser observations and verify cleanup after unmount.
  - Criteria: The user/task brief identifies normal, invalid and recovery paths without inventing genuine interview evidence; the UI meets all published action, state and focus criteria and does not use an unsafe HTML injection sink for untrusted content. Event behavior distinguishes target/currentTarget and default actions, does not duplicate listeners on reinitialization, and supports keyboard input. Timing claims are consistent with documented browser observations rather than assumed exact frame ordering.
  - Evidence: Requirements/task table, typed DOM component source, synthetic fixtures, event/timing and focus traces, before/after cleanup test, security-negative test for untrusted text, and a concise mechanism-based rationale.

- **APP2-AS2** (required accessible form and typed state-transition investigation)
  - Outcomes: APP2-O1, APP2-O3, APP2-O5, APP2-O6, APP2-O11, APP2-O12
  - Work: Extend **the same app** with a native semantic form and a justified typed transition model for editing, invalid, pending, accepted, failed and retry paths. Validate actual runtime input against specific domain rules; preserve drafts across failure, prevent conflicting duplicate actions without trapping keyboard users, and expose actionable per-field guidance plus proportionate accessible status/focus behavior. Perform one repeatable task-based usability walkthrough with explicitly labeled synthetic, peer or consenting participant evidence; no real user data submission is required.
  - Criteria: The declared transition table has no reachable contradictory states or unhandled submission path, valid input produces expected results, and invalid input does not falsely show success or erase values. Keyboard-only operation and semantic label/error association work; live announcements are proportionate and nonduplicative; source types do not substitute for runtime validation. Feedback is disclosed accurately as synthetic/peer/observed, without exaggerated user research or accessibility certification claims.
  - Evidence: Form HTML/TypeScript component, state diagram, acceptance and invalid-input matrix, keyboard/focus/error recordings or equivalent annotated observations, regression tests, and a short task-evaluation limitations note.

- **APP2-AS3** (required asynchronous data, cache, and navigation recovery)
  - Outcomes: APP2-O6, APP2-O7, APP2-O8, APP2-O9, APP2-O10, APP2-O13
  - Work: Extend **the same app** with an injected fetch-compatible transport or supplied local HTTP fixture, explicit route/history behavior, and typed state transitions. Test successful results, **204/no-body**, 4xx/5xx fulfilled error responses, malformed/unknown bodies, rejected transport, abort during body consumption and out-of-order completions; prove an old response cannot overwrite a newer request or switched identity even when abort arrives too late. Test cache ownership/invalidation and a bounded non-idempotent mutation or supplied uncertainty counterexample, with truthful retry/rollback policy. Verify direct-link behavior under the **actual chosen local host**, Back/Forward including initial/null history state, and that `pushState` does not itself dispatch `popstate`; test titles, focus and cleanup. No learner-written backend is required.
  - Criteria: `Response.ok`/status and response body-handling are interpreted separately (including **not parsing a no-content response as JSON**); HTTP errors are distinguished from transport rejection, and abort signal handling does not imply server-side rollback. Request identity guards prevent stale/mixed-user results; uncertain writes are not replayed blindly. Actual direct navigation and Back/Forward, URL input validation, `popstate` semantics, title/focus/scroll and component teardown match an explicit policy. CORS and credential observations are not misrepresented as authoritative access control.
  - Evidence: Typed transport and state code, locally reproducible fixture/adapter and versioned response scenarios, deterministic race/abort tests, route/history and focus traces, cache invalidation tests, and a failure-policy explanation.

- **APP2-AS4** (required dynamic accessibility, usability and browser security audit)
  - Outcomes: APP2-O1, APP2-O2, APP2-O5, APP2-O9, APP2-O10, APP2-O11, APP2-O12
  - Work: Audit **the cumulative app** for demonstrable focus/keyboard, accessible name and status/error, unsafe DOM content, privacy/storage and changed-identity issues. Select applicable WCAG 2.2 criteria: test dynamic failure states and focus visibility/not-obscured, **reflow near 320 CSS pixels with justified exceptions, and 200% text resize as a separate observation**. Challenge a long/RTL/localized or reduced-motion user journey and repair an actual confusing transition. Record any automated, actual assistive-technology and synthetic/consenting user observations separately without inventing interviews or whole-site conformance claims.
  - Criteria: Real and negative-path keyboard/focus/status behaviors are observed before and after repair. Untrusted text is rendered with **context-appropriate** safe DOM operations; no malicious destination/HTML sink, client-only permission gate, CORS or storage setting is misrepresented as server authorization. Applicable reflow, resize, Focus Not Obscured and dynamic name/status checks are documented without overstating untested screen-reader results. Localized or RTL text does not hide essential controls; reduced motion does not erase status information. Usability evidence is labeled by provenance and limits.
  - Evidence: Audit scope and WCAG-criterion references, test environments, failing/passing examples, DOM/security regression tests, focus/status observations, representative localized/reflowed interaction, usability-task notes and remaining-risk statement.

- **APP2-AS5** (required browser performance and regression diagnosis)
  - Outcomes: APP2-O3, APP2-O4, APP2-O8, APP2-O11, APP2-O13
  - Work: Reproduce a user-visible slow load or interaction **in the same app**, capturing comparable local browser traces under disclosed conditions. Attribute a DOM/layout/event or request cause, apply one justified correction and compare repeated before/after observations with variance and user-task interpretation. Test a distinct retained-listener, stale-state or perceived-delay defect as appropriate, and re-run keyboard/focus/status, async and negative-path regressions instead of pursuing unmeasured optimizations.
  - Criteria: The identified bottleneck is supported by trace or timing evidence rather than an invented universal threshold; repeat measurements disclose variance and browser conditions. The corrected behavior preserves user task completion, accessible focus/status and correct data state; no evidence depends solely on a synthetic audit score. Resource/listener cleanup and repeated interaction paths are testable and there is no unsupported claim of production-wide speedup.
  - Evidence: Fixture and runnable app, before/after profiler trace or bounded observation log, reproducible procedure and timing summaries, identified cause, diff and normal/negative regression tests, and performance/accessibility trade-off rationale.

- **APP2-AS6** (required framework-neutral browser application and technical defense)
  - Outcomes: APP2-O1, APP2-O2, APP2-O3, APP2-O4, APP2-O5, APP2-O6, APP2-O7, APP2-O8, APP2-O9, APP2-O10, APP2-O11, APP2-O12, APP2-O13, APP2-O14
  - Work: Deliver **the single evolving local browser app** previously evaluated across APP2-AS1–AS5, with semantic APP17 markup/CSS, APP19-checked TypeScript compiled to browser JavaScript, owned DOM/event components, accessible form/navigation, bounded fixture-driven Fetch, visible state and real safe untrusted content handling. **Reference** accepted prior observation/test artifacts rather than rebuild five new apps. Demonstrate a new unfamiliar but bounded route, focus, identity, request-race or user-task change, diagnose and correct the resulting defect, check impacted regressions and defend the design from a clean, offline-capable build and local host without React, new server coursework or paid tooling.
  - Criteria: A reviewer can build and launch the app from a clean checkout with free local tools and fixture data without React, paid cloud, proprietary accessibility platform, authentication provider or a real backend service. All documented user-task and failure criteria are reproducibly met with tests that include lost focus, malformed/late response, unsafe text, lifecycle cleanup and navigation. The unfamiliar change does not regress stated invariants; the learner accurately explains browser scheduling, TypeScript/runtime validation, Fetch response semantics, CORS/security limits, user feedback provenance and measurement uncertainty.
  - Evidence: A single versioned local app/source and synthetic fixture package, clean TypeScript build/host/test commands, an outcome-to-accepted-AS1–AS5 **evidence index** rather than duplicate logs, the unfamiliar change and targeted before/after regression observations, remaining support/accessibility/measurement limitations and a reviewable written, recorded or otherwise accessible technical defense.

### Completion decision, readiness and revision safety

APP2 completion requires an inspectable acceptable decision
for `APP2-AS1` through `APP2-AS6` that jointly
establishes `APP2-O1` through `APP2-O14`. A working
demo, one successful network request, an automatic
accessibility report or a TypeScript check alone
does not prove independent interaction-engineering
competence. Materially incorrect security boundaries,
loss of user intent, inaccessible recovery or
unreproducible work must be repaired before passing.

Record the current course/spec revision, evaluated
assessment/outcome IDs, environment and fixture
assumptions, tested and untested cases, observations,
defect traces, review decisions, and acknowledged
limitations according to
[OEE Evidence Rules](../../spec/evidence-rules.md).

This course remains an outcome-driven OEE `v0.2.0`
**draft**, not learner-tested or independently
verified merely because its source validator passes.
It retains APP17 + APP19 as its direct prerequisites:
APP1 and APP18 are already met transitively. This
competency-first review does not reclassify prior
APP2 learner decisions or assume their equivalence
to the current source/specification revision.
APP20 already exists as a separate React core course;
optional APP10 owns deeper frontend performance
specialization. Neither is silently required here.

### Public non-mandatory study references

These free sources support inspection of actual browser
behavior and relevant public standards. They do not
replace the requirements and criteria stated above.

- [MDN DOM introduction](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
  and [MDN Events](https://developer.mozilla.org/en-US/docs/Web/Events)
  for element ownership, event propagation and cleanup.
- [MDN Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
  for HTTP status, response streams, abort and credentials.
- [MDN History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API/Working_with_the_History_API)
  for navigation and `popstate` semantics.
- [MDN web security](https://developer.mozilla.org/en-US/docs/Web/Security)
  for origin policy, injection, credentials and client-side limits.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
  and [WAI ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
  for tested interaction accessibility patterns.
- [MDN browser performance](https://developer.mozilla.org/en-US/docs/Web/Performance)
  and [web.dev performance](https://web.dev/learn/performance)
  for profiling, responsiveness and qualified interpretation.
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
  for static contracts; APP19 owns complete language instruction.
