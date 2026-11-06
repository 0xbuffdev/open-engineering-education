# APP Frontend Foundations — Architecture and Coverage Audit

> **Status:** Proposal for review (2026-11-06). **Tracking:** [Issue #28](https://github.com/0xbuffdev/open-engineering-education/issues/28).  
> **Scope:** APP1–APP4 redesign and impact assessment for APP5–APP16.  
> **Authority:** Non-normative review note. The existing [APP catalog](../../curriculum/APP/README.md), course IDs, prerequisites, and OEE [course format](../../spec/course-format.md) remain authoritative until a reviewed implementation PR is merged.

## 1. Decision to evaluate

APP currently assumes a single nine-week frontend course can introduce HTML, CSS, JavaScript/TypeScript, browser APIs, frontend architecture, accessibility, data integration, and performance. That is not an adequate **instructional decomposition** for the intended SEF-to-APP progression.

**Proposed architecture:**

1. **APP1 — Web & Internet Foundations:** web mechanisms and diagnostics, without requiring learners to implement a backend service or write JavaScript before instruction.
2. **APP2 — HTML & CSS Engineering:** semantic HTML, native behavior and forms, CSS fundamentals and modern layout, responsive design, accessibility and static-page verification.
3. **APP3 — JavaScript & TypeScript Programming:** the JavaScript language and runtime model, then the TypeScript type system, toolchain, safe boundaries, tests and substantial language-focused practice.
4. **APP4 — Frontend Application Engineering:** DOM/events/browser APIs, asynchronous browser interaction, UI state, components, framework abstractions, frontend security, API consumption, testing, performance and shipping.
5. **APP5 onward — Backend and downstream courses:** backend starts in its own course; later courses are not rewritten during this first audit.

Course names/codes are **provisional**, not adopted. No arbitrary module count or duration target should determine the eventual instructional decomposition.

## 2. Evidence from the current files

| Existing course | Current shape | Initial concern | Required investigation |
| --- | --- | --- | --- |
| [APP1](../../curriculum/APP/APP1.md) — Web & Internet Foundations | 8 modules; 7 weeks | Module 5 includes Fetch API, promises and asynchronous failure before APP teaches JS. Final lab builds an HTTP service, crossing into backend implementation. | Separate conceptual web/network understanding from JS-dependent browser coding and server development; preserve useful HTTP conceptual knowledge. |
| [APP2](../../curriculum/APP/APP2.md) — Frontend Engineering | 9 modules; 9 weeks | Module 2 condenses CSS layout; Module 3 begins with one broad `JavaScript/TypeScript in the browser` lesson; Module 5 assumes typed component contracts; the course also covers accessibility, APIs and performance. | Split HTML/CSS, JS/TS language, and browser application concerns into separately assessable courses. |
| [APP3](../../curriculum/APP/APP3.md) — Backend Engineering & API Design | 9 modules; 9 weeks | Current prerequisite is APP1. Its conceptual prerequisites include HTTP and programming, but any browser-framework prerequisite would be artificial. | Keep backend implementation exclusively here (proposed APP5); reevaluate entry requirements after JS/TS is established. |
| [APP4](../../curriculum/APP/APP4.md) — Databases & Data Modeling | 8 modules; 8 weeks | Existing modules combine broad SQL subjects. Not part of the frontend rewrite, but identifier and prerequisite changes will propagate here. | Defer pedagogical rewrite to the backend/database audit; preserve links during migration. |

**Observed boundary failures:**

- APP1 Module 5 `Fetch API, promises, and asynchronous failure` presupposes language/runtimes not systematically established in APP1.
- APP1 final `HTTP Service` is a backend engineering exercise inside web foundations.
- APP2 Module 1 introduces semantic HTML and forms, but does not provide a dedicated HTML progression.
- APP2 Module 2 compresses CSS cascade, layouts, intrinsic sizing and responsive images into a short sequence.
- APP2 Module 3 `JavaScript/TypeScript in the browser` gives neither language its own foundational sequence.
- APP2 Module 5 teaches typed component contracts, state machines and runtime validation as frontend design concerns without first teaching TypeScript comprehensively.
- APP2 mixes framework/application concerns with platform and language foundations, increasing cognitive load and reducing diagnosability of prerequisite gaps.

**Important qualification:** An OEE curriculum file is a public learning-and-assessment contract, not a complete textbook or lecture script. The goal is precise, independently teachable and assessable lesson boundaries, explicit practical expectations, and sufficient public instructions—not artificially increasing word counts.

## 3. Exit competencies and boundaries

### APP1 — Web & Internet Foundations

**Entry:** SEF10 or demonstrated SEF-equivalent competence.

**Learner must be able to:**

- Trace a navigation from URL through name resolution, transport, TLS, HTTP exchange and response processing.
- Interpret HTTP methods, status codes, headers, cookies, caching semantics, redirects and origin/security boundaries.
- Reproduce, inspect and classify DNS, transport, TLS, origin-policy, HTTP and application-level failures.
- Explain browser loading and client/server interactions at a conceptual level using network inspection or supplied HTTP fixtures.

**Exclusions:** requiring the learner to author a backend HTTP service, implement JavaScript Fetch programs, or build a frontend framework application.

**Possible exit lab:** diagnose a supplied website/API fixture using browser network tools and CLI HTTP tooling, collect a request/response trace, reproduce failures, explain expected behavior and suggest fixes. A prebuilt server may serve as a **lab fixture**, not required backend implementation.

### APP2 — HTML & CSS Engineering

**Entry:** APP1 (and SEF foundations); **JavaScript must not be required**.

**Learner must be able to:**

- Produce valid, semantic, accessible HTML documents with metadata, links, navigation, tabular content, native controls and forms.
- Explain the accessibility tree, accessible names, keyboard interaction and browser-native form behavior.
- Explain CSS matching, cascade, layers, specificity, inheritance, computed values, box model and layout constraints.
- Implement robust Flexbox/Grid layouts, responsive images and typography, zoom/reflow behavior, internationalization-aware layout and accessible motion choices.
- Inspect, debug and verify HTML/CSS behavior across viewports, input methods and supported browsers.

**Exclusions:** DOM scripting, JavaScript application state, server-side form processing and backend code.

**Possible exit lab:** a standards-compliant, multi-page responsive site with accessible native forms and media; evidence from keyboard testing, zoom/reflow checks, browser inspection, contrast and compatibility review.

### APP3 — JavaScript & TypeScript Programming

**Entry:** SEF programming foundations and web-foundations context. APP2 is a **recommended sequence predecessor**, not necessarily a *technical* prerequisite; review whether APP2 needs to be a formal requirement.

**Learner must be able to:**

- Predict JavaScript value/type/coercion behavior, scopes, binding and mutation; explain functions, closures, objects, prototypes, classes and modules.
- Use arrays, iterables, collections, error handling and asynchronous constructs, including promises and the event loop.
- Write, debug and test independent JavaScript programs with documented runtime assumptions.
- Explain TypeScript's compile-time checks, inference, narrowing, object/function types, generics, module resolution and compiler configuration.
- Distinguish types from runtime validation; reject malformed external input explicitly.

**Exclusions:** required DOM/framework knowledge, HTTP server/API architecture, backend persistence or deployment.

**Possible exit lab:** a tested TypeScript CLI or reusable package that parses untrusted inputs, implements a meaningful workflow, exposes typed contracts, reports errors predictably and has independent runtime tests.

### APP4 — Frontend Application Engineering

**Entry:** APP1 + APP2 + APP3.

**Learner must be able to:**

- Manipulate the DOM and reason about events, rendering, cleanup, asynchronous browser lifecycles and browser security.
- Develop accessible, interactive components and explain framework abstractions over native browser behavior.
- Manage UI state, routing, network requests, caching/mutations, client persistence and authorization-sensitive views.
- Test visual, functional, async failure and accessibility behavior; diagnose production browser performance with controlled measurements.
- Build a production-grade browser application that consumes an existing HTTP API and survives negative-path tests.

**Exclusions:** requiring learners to implement the backend API or production server as part of frontend course completion. Use provided local fixtures or an externally supplied API when suitable.

**Possible exit lab:** an accessible TypeScript frontend against a provided running API, with typed and runtime-validated response boundaries, loading/empty/error/denied states, cancellation and stale-response recovery, tests and measured performance improvements.

### APP5 — Backend Engineering & API Design (proposed renumbering)

Begin backend implementation, service boundaries, API design, authentication and authorization, persistence integration, operational failure handling and backend testing here. **Do not silently require frontend-framework expertise** when the skill is not needed; distinguish program order from technical prerequisites.

## 4. Preliminary coverage matrix

**Labels:** `Primary` = initial in-depth instruction and assessment owner; `Reinforce` = subsequent use/extension. Primary ownership does not imply only one course may mention the subject.

| Competency area | Primary owner | Reinforcement / boundary | Coverage benchmark |
| --- | --- | --- | --- |
| URL structure, DNS, IP, transport, TLS, HTTP semantics | APP1 | APP4 browser traces; APP5 server implementation | [APP1](../../curriculum/APP/APP1.md), HTTP standards |
| Origin policy, cookies, request/response concepts | APP1 conceptual | APP4 programmatic browser security | [web.dev privacy](https://web.dev/learn/privacy), MDN |
| HTML document structure, metadata, headings, semantics | APP2 | APP4 dynamic document correctness | [Learn HTML](https://web.dev/learn/html) |
| Hyperlinks, navigation, lists and tables | APP2 | APP4 routing and dynamic navigation | [Learn HTML](https://web.dev/learn/html) |
| Native forms, labels, constraints, autofill | APP2 | APP4 JavaScript-assisted forms | [Learn Forms](https://web.dev/learn/forms) |
| Accessible names, native focus, semantic controls | APP2 | APP4 dynamic focus and announcements | [Learn Accessibility](https://web.dev/learn/accessibility) |
| Images, SVG, audio/video, responsive media | APP2 | APP4 asset loading and measured performance | [Learn Images](https://web.dev/learn/images) |
| CSS box model, cascade, selectors, inheritance, layers | APP2 | APP4 component styling boundaries | [Learn CSS](https://web.dev/learn/css) |
| Positioning, stacking, intrinsic sizing, flex and grid | APP2 | APP4 UI rendering/debugging | [Learn CSS](https://web.dev/learn/css) |
| Responsive design, media/container queries, reflow | APP2 | APP4 dynamic responsive interfaces | [Learn Responsive Design](https://web.dev/learn/design) |
| Typography, color, design tokens, logical properties | APP2 | APP4 scalable component systems | [Learn CSS](https://web.dev/learn/css) |
| Motion, transitions, reduced motion and CSS diagnostics | APP2 | APP4 interaction feedback and performance | [Learn CSS](https://web.dev/learn/css) |
| JavaScript values, coercion, equality, operators | APP3 | APP4 browser programming | [Learn JavaScript](https://web.dev/learn/javascript) |
| JavaScript scope, closures, functions, objects/prototypes | APP3 | APP4 components and lifecycle | [Learn JavaScript](https://web.dev/learn/javascript), MDN |
| Iterables, collections, modules, tooling and tests | APP3 | APP4 application organization | [Learn JavaScript](https://web.dev/learn/javascript), MDN |
| Promises, async/await, task/microtask order | APP3 | APP4 Fetch, cancellation and UI races | MDN JavaScript |
| TS inference, object types, narrowing and generics | APP3 | APP4 typed components and API data | [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) |
| TS emit/compiler settings, module boundaries, runtime validation | APP3 | APP4 frontend contracts | TypeScript Handbook |
| DOM querying, mutation, events and delegation | APP4 | APP2 provides static semantic substrate | MDN Web APIs |
| Fetch, browser storage, origin and permissions APIs | APP4 | APP1 conceptual network; APP3 async language | MDN Web APIs |
| Components, rendering, state, framework abstractions | APP4 | APP3 modularity and typed contracts | Framework-neutral competence |
| Routing, forms, loading/empty/error and server state | APP4 | APP5 owns actual API implementation | [Learn Forms](https://web.dev/learn/forms) |
| Browser privacy and client security | APP4 | APP1 origin concepts, APP2 safe markup | [Learn Privacy](https://web.dev/learn/privacy) |
| Frontend tests and accessibility audits | APP4 | APP2 HTML/CSS checks; APP3 language tests | [Learn Testing](https://web.dev/learn/testing), [Learn Accessibility](https://web.dev/learn/accessibility) |
| Critical rendering path, Web Vitals, profiling | APP4 | APP2 resource/layout fundamentals | [Learn Performance](https://web.dev/learn/performance) |
| Service workers, offline and installability | APP4 | Follow-on PWA specialization possible | [Learn PWA](https://web.dev/learn/pwa) |
| Browser feature support and progressive enhancement | APP2 foundations | APP4 runtime enhancement | [Web Platform Baseline](https://web.dev/baseline) |
| AI-assisted and web AI features | Optional later specialization | Not a foundational graduation dependency | [Learn AI](https://web.dev/learn/ai) |

This is a **coverage ownership matrix**, not a claim of 100% parity with web.dev or of OEE readiness. Check subtopics and authored lesson outcomes during each course PR.

## 5. Proposed instructional decomposition, not final module counts

### APP2: HTML/CSS learning progression

- HTML syntax, browser parsing and document structure; metadata and document language.
- Content semantics, headings, lists, links, navigation, tables and embedded media.
- Forms: inputs, labels, grouping, validation attributes, autocomplete, native interaction and accessibility.
- Accessibility: semantic landmarks, accessible names/descriptions, focus/keyboard, zoom and assistive technology observation.
- CSS syntax, selector matching and specificity; origins, cascade layers and computed values.
- Box model, flow, sizing, positioning, stacking, overflow and painting.
- Flexbox, Grid, intrinsic sizing and responsive layout.
- Typography, color, custom properties, logical properties, media/container queries and responsive images.
- Transitions, animations, reduced motion, compatibility and browser devtools.
- Final HTML/CSS integration work with reproducible acceptance checks.

**Example broad-title split:** `CSS cascade, inheritance and specificity` should be separated into selector matching, cascade origin/order, cascade layers, specificity, inheritance/defaults, and devtools fault diagnosis, with a dedicated evidence-producing stylesheet repair task.

### APP3: language learning progression

- JavaScript runtime vs language, values and primitive types, coercion, equality, declarations, expressions.
- Control flow, functions, parameter/return behavior, lexical environments, closures, objects, prototypes, class syntax.
- Arrays, Map/Set, iterators, generators, string/number/date/error handling, modules and packages.
- Async programming: callbacks, promise state/chains, microtasks, async/await, cancellation patterns and failure propagation.
- Tests, debugging, compatibility and project/package tooling.
- TypeScript basics, inference and strict mode, unions, narrowing, objects, function types, generics.
- Type operators, mapped/conditional types, module resolution, declarations and interop as appropriate to core competence.
- Runtime validation, contract evolution, compiler behavior and safe external data boundaries.
- Independent JavaScript/TypeScript integration lab without browser-framework dependency.

### APP4: frontend learning progression

- Browser documents and rendering, native DOM, event propagation, input and accessible dynamic interactions.
- Fetch, client security, browser storage, lifecycle, cancellation, navigation and network fault handling.
- Components, rendering ownership, view/state separation, UI architecture and framework comparisons.
- Forms, routing, server-state caches, mutations, race conditions, typed component boundaries.
- Internationalization, accessibility audits, performance budgeting and profiling, test boundaries.
- Progressive enhancement, service workers/PWA behavior, production build/diagnostics and integration lab.

## 6. Prerequisites and recommended study sequence

**Recommended learner sequence:** SEF → APP1 → APP2 → APP3 → APP4 → backend.

**Proposed *technical* edges:**

`SEF10 → APP1`

`APP1 → APP2` and `APP1 → APP3`

`APP2 + APP3 → APP4`

`APP1 + APP3 → APP5 (backend)` is a plausible technical minimum, with program sequencing to be evaluated. Do not invent a framework prerequisite for backend engineering.

Rationale: knowing HTML/CSS is not a fundamental prerequisite for understanding JavaScript language semantics. It is sensible to recommend HTML/CSS first, but a false hard prerequisite weakens independent study flexibility. The program catalog should clarify this distinction before finalizing identifiers.

## 7. Identifier migration and downstream impact

Current APP contains 9 required courses (including the APP9 capstone) and 7 electives = **16 courses**. The proposed frontend split adds two required courses = **11 required courses + 7 electives = 18 courses**, if the number of electives remains unchanged.

**Candidate sequential mapping (not approved):**

| Current | Proposed | Notes |
| --- | --- | --- |
| APP1 | APP1 | Retain identity, revise scope |
| APP2 | APP4 | Existing frontend course becomes frontend application engineering; new APP2 and APP3 are authored |
| APP3 | APP5 | Backend |
| APP4 | APP6 | Databases |
| APP5 | APP7 | Full-stack architecture |
| APP6 | APP8 | Software quality and operations |
| APP7 | APP9 | Deployment |
| APP8 | APP10 | Production architecture |
| APP9 | APP11 | Capstone |
| APP10–APP16 | APP12–APP18 | Seven electives |

**High-risk changes:** cross-course `Prerequisites` links, `curriculum/APP/README.md` table/graph, `curriculum/README.md` totals, `scripts/check-app-curriculum.py` hard-coded course ranges, CI assumptions, links from other programs, OEE Workspace references and resource mappings in external content. Course IDs are currently documented as stable references. **Do not migrate IDs until the impacted consumers are inventoried and a compatibility plan is approved.**

Alternatives worth reviewing: preserve existing code identifiers and append new courses with explicit learning order, or introduce machine-readable stable course identifiers independent of display codes. Both have trade-offs; avoid a casual breaking renumber.

## 8. Assessment and effort policy

For each authored module, reviewers should be able to follow **outcome → required concepts → instruction → practice → test/lab → observable evidence**.

- A lesson should contain a coherent, independently explainable concept or closely related group; separate concepts with genuinely different prerequisites or failure modes.
- Each required test must identify an outcome and a way to evaluate understanding, not just a title.
- Labs follow OEE's required fields: objective, prerequisites, environment, procedure, expected result, verification, evidence and failure analysis.
- Final labs must integrate course outcomes. Do not mandate paid products or a particular proprietary framework.
- Default to mechanism-first explanations; language/framework syntax alone is not mastery.
- Estimate guided study, independent implementation, debugging, testing and assessment workload before assigning weeks; retain `draft` until actual validation evidence exists.
- **No arbitrary minimum or maximum module/lesson counts.** Use course outcomes and reasonable cognitive scope to determine length.

## 9. PR sequence and review gates

1. **This review-only PR:** validate course boundaries, coverage ownership, prerequisites and migration options. **No live catalog or course file edits**.
2. **APP1 boundary correction:** retain web/network foundations, remove premature backend service requirements and move JS-dependent browser-programming work.
3. **New APP2:** write HTML/CSS course with SEF-level learning decomposition, outcomes, tests and reproducible labs.
4. **New APP3:** write standalone core JavaScript/TypeScript programming course, retaining a framework-independent scope.
5. **New APP4:** rebuild existing frontend course as application engineering; reuse suitable work and tests from [PR #27](https://github.com/0xbuffdev/open-engineering-education/pull/27), without merging the obsolete nine-module design first.
6. **Identifier migration:** as a coordinated, separately reviewed migration when new courses are ready; repair catalog, validator, links and downstream consumers.
7. **APP5+ audits:** backend/data/etc. depth reviews as independent curriculum improvements.

**PR #27 is currently open:** Its assessment work is valuable, but its unchanged old APP2 structure is in conflict with the proposed decomposition. Hold the merge; reuse the parts that remain pedagogically appropriate in APP2/APP4. This document neither closes nor supersedes it automatically.

## 10. Review acceptance criteria

- [ ] APP1–APP4 boundary decisions are explicit and approved.
- [ ] Critical APP1/APP2 prerequisite inversions have an agreed resolution.
- [ ] Each major web.dev track has a plausible primary owning course; omissions are noted explicitly.
- [ ] JS and TS fundamentals have a distinct course separate from browser/framework instruction.
- [ ] HTML/CSS is independent of JavaScript and has a substantial learning/assessment plan.
- [ ] Frontend consumes a supplied API rather than requiring backend implementation.
- [ ] Proposed identifier and consumer migration are reviewed before breaking changes.
- [ ] Course readiness remains `draft`; no false claims of course or learner verification.
- [ ] Authoring follows existing OEE specification; normative changes, if needed, get a separate RFC.

## 11. Reference baseline (reviewed 2026-11-06)

- [web.dev learning catalog](https://web.dev/learn)
- [web.dev HTML](https://web.dev/learn/html), [CSS](https://web.dev/learn/css), [JavaScript](https://web.dev/learn/javascript)
- [web.dev Forms](https://web.dev/learn/forms), [Responsive Design](https://web.dev/learn/design), [Images](https://web.dev/learn/images)
- [web.dev Accessibility](https://web.dev/learn/accessibility), [Testing](https://web.dev/learn/testing), [Performance](https://web.dev/learn/performance)
- [web.dev Privacy](https://web.dev/learn/privacy), [PWA](https://web.dev/learn/pwa), [Baseline](https://web.dev/baseline)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [OEE course format](../../spec/course-format.md), [OEE evidence rules](../../spec/evidence-rules.md)

This mapping draws on external references as **coverage benchmarks**, not mandatory proprietary course texts or paid dependencies. Topic ownership remains a curriculum design decision supported by review.
