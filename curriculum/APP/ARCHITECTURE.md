# Application Engineering — Migration Architecture Decision

**Decision record:** Approved program migration target, academically amended
on 2026-11-16 in [PR #78](https://github.com/0xbuffdev/open-engineering-education/pull/78).

**Implementation status:** Partially implemented. APP1, APP17, APP18,
APP19, APP4 and APP21 are published as `v0.2.0` drafts. APP2 is being
migrated in a separate course PR. APP20 and other unrevised course
boundaries/dependencies remain **targets**, not current learner
requirements. The [active APP catalog](README.md) and linked course
files remain authoritative until individually amended.

**Authority:** This is a non-normative, program-specific architecture
decision. It does not revise OEE's [Course Format](../../spec/course-format.md),
[Evidence Rules](../../spec/evidence-rules.md), [Conformance](../../spec/conformance.md),
or readiness thresholds; only OEE governance can change those requirements.
It is not a second authoring format, assessment rubric, learner-completion
contract, or machine-readable course catalog.

**History:** The original design was adopted on 2026-11-07 through
[APP architecture PR #49](https://github.com/0xbuffdev/open-engineering-education/pull/49).
[Issue #30](https://github.com/0xbuffdev/open-engineering-education/issues/30)
records the historical discussion, and
[issue #55](https://github.com/0xbuffdev/open-engineering-education/issues/55)
tracks course-by-course execution. This amendment keeps the original
capability boundaries where defensible and corrects dependencies,
professional competency ownership, assessment sequencing, and the
TypeScript/Rust elective boundary before further APP migration.

## 1. Educational objective and accepted design principles

The intended APP graduate can interpret a real application problem,
establish testable requirements, design its interfaces and data,
implement and maintain the solution, test and secure it, deploy and
observe its operation, investigate failure, make a bounded unfamiliar
change, and defend decisions with reproducible evidence.

Design the program around those capabilities, not a list of fashionable
tools or a predetermined module, lesson, exercise, or course duration.

1. **Mechanisms precede tools.** APP1 teaches Internet/Web/browser
   mechanisms. APP17 teaches semantic HTML and CSS authoring. APP18
   and APP19 separately teach JavaScript and TypeScript. APP2 teaches
   browser application behavior before APP20 applies React.
2. **Meaningful course boundaries.** APP21 teaches Node.js runtime
   and framework-free service primitives; APP3 teaches typed,
   framework-based API and service engineering. APP4 teaches data
   modeling independently of a backend framework. APP5 integrates
   these competencies.
3. **Independent pathways remain independent.** After SEF10,
   learners can begin APP1, APP18, or APP4 independently. Requiring
   Web fundamentals to learn JavaScript or relational modeling adds
   an unnecessary gate. Node.js runtime concepts require JavaScript,
   not prior TypeScript language mastery.
4. **An explicit reference stack, not a false universal standard.**
   React is the open-source core frontend framework subject;
   Fastify with TypeScript is the APP3 reference-framework candidate;
   PostgreSQL is the APP4 reference database. Framework-specific
   assessments may test what those courses teach, while general
   engineering outcomes should remain transferable. No proprietary
   paid service may be the sole path to required competence.
5. **Professional engineering is taught throughout.** Requirements,
   accessibility, usability, security, privacy, maintainability,
   testing, operational diagnosis, and communication need named
   teaching ownership and appropriately repeated practice.
6. **Assessment follows competence.** Start with explanations and
   bounded guided investigations; fade scaffolds as learners gain
   capability; assess integration, unfamiliar diagnosis, and a
   defensible technical decision where those are genuine outcomes.
   A passing code test alone does not establish independent judgment.
7. **Integrate only after prerequisites exist.** APP5–APP9 build
   toward full-stack operation and a reproducible project defense.
   They should not re-teach foundational syntax or introduce
   arbitrary distributed complexity to meet an activity quota.
8. **Electives remain genuinely optional.** APP10–APP16 provide
   specialized depth, never a hidden APP9 or core-graduation gate.
   Rust fundamentals and C/Rust comparison are owned by SYS, not
   APP15; the precise SYS course prerequisite remains provisional
   until SYS is redesigned.
9. **Historical evidence is not silently reinterpreted.** Keep
   stable identifiers where the competency identity remains
   recognizable. A new course scope, prerequisite, assessment, or
   revision does not retroactively upgrade a learner's historical
   completion record.

The **14-course core target** is an architectural decision, not a
normative count or proof that each duration is appropriate. A future
split or merger must follow a separately recorded capability,
prerequisite, workload, and assessment review.

## 2. Course identity is not course sequence

The existing APP1–APP16 course codes are published identifiers;
most associated course files still use a legacy authoring format.
Renumbering them to make the path appear sequential would change
identities referenced by prerequisites, evidence, curriculum exports,
OEE Workspace, content mappings, and 0xNAND.

Preserve recognizable existing identities. APP2 remains browser/frontend
engineering, and APP3 remains API/service engineering with a narrower
framework boundary. New APP17–APP21 codes represent HTML/CSS,
JavaScript, TypeScript, React, and Node.js/backend foundations.

**Catalog row order**, not code suffix, determines the recommended
learning sequence. Core/elective classification must also be explicit,
not inferred from numeric ranges. No old APP2 or APP3 completion
automatically satisfies a new or materially revised assessment contract.

## 3. Amended target core progression

This is the **proposed target prerequisite graph**, not the currently
published learner pathway. A course and the authoritative APP catalog
must be updated together in a reviewed migration PR before these
changes become active.

| Display sequence | Code | Target course | Public exit capability | Direct prerequisites |
| --- | --- | --- | --- | --- |
| 1 | APP1 | Web & Internet Foundations | Investigate a network-to-pixels Web visit and defend observed versus inferred causes | SEF10 |
| 2 | APP17 | HTML & CSS Engineering | Author and inspect a semantic, accessible, responsive static interface | APP1 |
| 3 | APP18 | JavaScript Programming | Write, test, debug, and package JavaScript programs using basic Node/npm tools | SEF10 |
| 4 | APP19 | TypeScript Programming | Design useful static contracts, validate real runtime data, and explain type/runtime boundaries | APP18 |
| 5 | APP4 | Databases & Data Modeling | Model relational data; verify queries, integrity, transactions, and schema changes | SEF10 |
| 6 | APP2 | Browser & Frontend Engineering | Build and investigate accessible interactive browser applications without relying on a framework | APP17, APP19 |
| 7 | APP21 | Node.js & Backend Foundations | Implement and diagnose a bounded HTTP service using Node runtime primitives | APP18 |
| 8 | APP20 | React Application Engineering | Build and verify a maintainable React application, distinguishing React behavior from browser mechanisms | APP2 |
| 9 | APP3 | Backend Framework Engineering | Implement and defend a secure, testable, maintainable typed API/service using a framework | APP19, APP21, APP4 |
| 10 | APP5 | Full-Stack Application Architecture | Integrate UI, services, persistent data, identity, and partial-failure behavior | APP20, APP3 |
| 11 | APP6 | Software Quality & Engineering Operations | Improve quality, CI, observability, maintainability, and reliability with evidence | APP5 |
| 12 | APP7 | Deployment, Cloud & DevOps | Deploy, observe, restore, and roll back a secure application reproducibly | APP5, APP6 |
| 13 | APP8 | Production Application Architecture | Investigate capacity, failure, and data trade-offs; defend measured architectural evolution | APP5, APP6, APP7 |
| 14 | APP9 | Application Engineering Capstone | Deliver, reproduce, improve, and defend an integrated application | APP8; verified transitive closure must cover every preceding core course |

**Why the graph changes:**

- **APP18: APP1 → SEF10.** JavaScript concepts build on SEF
  programming and engineering foundations, not DNS or browser
  internals. APP1 is still needed later through APP17/APP2.
- **APP4: APP1 → SEF10.** Relational modeling and SQL are independently
  useful; APP3 later requires APP4 before applying persistence in a
  framework service.
- **APP21: APP19 → APP18.** Node.js runtime fundamentals build on
  JavaScript and its async semantics. APP19 remains essential for
  the typed APP3 reference implementation, not for understanding
  event loops, streams, and HTTP servers in APP21.
- **APP3: APP21 + APP4 → APP19 + APP21 + APP4.** TypeScript language
  competence is made explicit for the planned typed reference
  framework; this does not change the subject to TypeScript syntax.
- **APP2, APP20, and APP3 remain separate.** React does not require
  backend Node.js service design. Backend frameworks do not require
  React. APP5 is the intentional point of integration.

**Recommended display order is not forced serial enrollment.** APP1,
APP18, and APP4 can run in parallel after SEF10. APP17 follows APP1;
APP19 and APP21 follow APP18. APP2 needs both APP17 and APP19;
APP20 follows APP2. APP3 needs APP19, APP21, and APP4. APP5 joins
the two implementation branches. APP9's direct APP8 link is sufficient **only if** the validated
transitive prerequisite closure includes all 13 preceding core
identities; a future prerequisite change must rerun this check.
No elective may enter the closure.

A publicly available, outcome-equivalent diagnostic may establish
prerequisite competence in place of repeating instruction, without
silently changing the assessment requirements of the later course.

## 4. Exact course ownership boundaries

These boundaries identify **what future course authoring must clarify**.
The course files themselves, not this decision, will publish the actual
learning outcomes and assessments.

### APP1 — Web & Internet Foundations (already migrated)

Owns connected devices, packets, routing, transport, DNS, hosting,
HTTP/TLS, browser engines, HTML/CSS parsing, layout, rendering,
security boundaries, and evidence-based failure diagnosis as one
network-to-pixels explanatory capability. It does not teach production
JavaScript, React, APIs, or database implementation.

Preserve the already published `v0.2.0` source; do not rewrite
it to support prerequisite changes unrelated to APP1.

### APP17 — HTML & CSS Engineering (already migrated)

Owns semantic documents, accessible navigation and forms, CSS
cascade and layout, responsive design, progressive enhancement,
and meaningful static-interface inspection. It produces a robust
static deliverable, not a JavaScript application.

Preserve its completed migration. APP2 extends accessibility to
dynamic interaction; APP20 applies it to React.

### APP18 — JavaScript Programming

Owns JavaScript language semantics, coercion, control flow, scopes,
functions/closures, prototypes, collections, modules, error handling,
promises and scheduling, testing, debugging, and maintainable program
design. Teach common failure modes, not just syntax demonstrations.

Also owns **basic Node.js development tooling**: installing and
selecting a runtime, executing scripts, npm/package management,
`package.json`, lockfiles, ESM, dependency reproducibility, and
test/build scripts. A clean-checkout JavaScript program is an
appropriate exit demonstration.

It does **not** teach full Node HTTP services, process lifecycle,
advanced streams, React, TypeScript's type system, or backend
frameworks. Introduce normal-path and malformed-input testing,
debugging, and readable maintenance before learners reach APP6.

### APP19 — TypeScript Programming

Owns structural typing, inference, unions and intersections,
narrowing, generics, conditional/mapped types at justified depth,
module/type declarations, compiler configuration, typed APIs,
unknown input validation, and the limits of static checking at
runtime. Require evidence that learners know when a type assertion
does **not** validate external data.

APP18 is the language foundation. APP3 and APP20 use TypeScript;
they do not repeat a full TypeScript language course. Advanced
library type design can be deepened in APP15 without gating core
graduation.

### APP4 — Databases & Data Modeling

Owns requirements-to-data modeling, relational structure,
normalization trade-offs, SQL and query correctness, constraints,
indexes, transactions/isolation, migrations, query planning,
data integrity, access controls, and basic recovery evidence.

Use PostgreSQL as an open reference but assess transferable
relational and transactional reasoning. Independent local
database investigations must be possible before any API
framework is taught. Application-specific repositories and
transaction orchestration are revisited in APP3/APP5.

### APP2 — Browser & Frontend Engineering

Owns browser DOM/event APIs, dynamic forms, application state,
fetch and HTTP failure behavior, browser security, structured
async UI states, client-side navigation principles, accessibility
verification, and measured interaction performance.

**Add explicit interaction and user-centered engineering:** translate
a scoped user workflow into observable behavior; model loading,
empty, validation, authorization, offline/error and recovery states;
use keyboard and assistive-technology inspection; evaluate a
representative task's usability with ethical, minimal-data feedback.
The goal is usable, explainable interaction, **not** a standalone
visual-design degree or a React course.

HTML/CSS belongs to APP17; language fundamentals to APP18/APP19;
React components and effects to APP20; deep performance tuning
to elective APP10. An unfamiliar browser interaction defect is
a suitable assessment scenario.

### APP21 — Node.js & Backend Foundations

Owns Node process/runtime behavior, event loop, async filesystem and
network I/O, streams, backpressure, cancellation, error boundaries,
configuration, HTTP servers without a framework, request parsing,
resource limits, security basics, local testing, and diagnostic
observability.

APP18's JavaScript plus package tooling is sufficient preparation.
TypeScript **may be used** as an extension or chosen implementation
language, but is not a required conceptual prerequisite for
Node event-loop and HTTP mechanisms. This course does not repeat
JavaScript syntax or build a production framework architecture.

The exit task is a small, bounded, tested and observable HTTP
service with intentional malformed inputs and failure recovery.

### APP20 — React Application Engineering

Owns React component composition, rendering and reconciliation
concepts, state ownership, effects and synchronization, routing,
data integration, accessibility, testing, error boundaries,
performance diagnosis, and maintainable React application design.

Use APP18's Node/npm tooling for local React builds (for example,
Vite) without importing APP21 backend-runtime requirements.
Distinguish browser runtime behavior from developer-tool runtime
behavior. Apply APP2's user-flow, usability, and accessibility
competence rather than re-teaching introductory browser APIs.

React-specific architectural outcomes are legitimate because the
course explicitly teaches React; broader application engineering
outcomes should not be framed as if React were the only possible
implementation.

### APP3 — Backend Framework Engineering

Owns requirements-to-API contracts, validated inputs, authentication,
**server-side authorization**, domain invariants, service boundaries,
transaction use, structured errors, async work, contract evolution,
testing, observability, failure behavior, and service maintenance.

Apply APP19 TypeScript, APP21 runtime knowledge, and APP4 database
competence in a framework-based reference service; Fastify with
TypeScript remains the **reference candidate**. Teach portable API
reasoning and defensible framework trade-offs, not framework
vocabulary alone. Require negative-path and cross-tenant
authorization scenarios appropriate to the chosen project.

APP3 introduces requirements traceability for API behavior and
maintenance of an existing contract. APP5 owns cross-layer
requirements and integration, while APP9 evaluates the full
problem-to-product process.

### APP5 — Full-Stack Application Architecture

Owns tracing a specified user journey through browser, service,
domain and data layers; coherent service boundaries; authenticated
end-to-end flows; external dependency and async-work handling;
caching, file/storage integration; and partial-failure behavior.

**Add cross-layer requirements ownership:** convert stakeholder
needs into testable flows, acceptance criteria, privacy/identity
constraints and error/recovery expectations. Evaluate contracts,
integration, change impact, and a working vertical slice rather
than introducing new JavaScript or framework syntax.

### APP6 — Software Quality & Engineering Operations

Owns risk-based test strategy, CI, reproducible builds, regression
investigation, dependency and supply-chain checks, maintainability
trade-offs, logging/metrics/traces, service-level signals,
incident diagnosis, and evidence-based reliability improvement.

**Do not postpone testing until APP6.** APP18 and every subsequent
implementation course already teach and require proportional
testing, debugging and change explanation. APP6 deepens these
into system-level strategy, quality governance, observability,
maintenance and repeatable investigation, rather than introducing
a learner's first automated test.

### APP7 — Deployment, Cloud & DevOps

Owns safe configuration and secrets, network/TLS exposure, artifact
build and delivery, CI/CD release controls, deployment environments,
health checks, monitoring, operational access, rollback, backup
and recovery tests, infrastructure reproducibility, and cost.

APP6 addresses quality signals and incident *diagnosis*; APP7
makes actual release, operational recovery, and deployment
responsibility assessable. A paid cloud account, public domain,
or proprietary service must not be the only assessment path;
appropriately constrained local/simulated evidence is acceptable.

### APP8 — Production Application Architecture

Owns measured load/capacity investigation, performance budgets,
queues/workers, caching, idempotency, data/consistency trade-offs,
failure containment, reliability, and reversible architectural
evolution with explicit operational cost.

APP8 tests whether added complexity addresses a demonstrated
constraint. It is not a requirement to build distributed
microservices merely to demonstrate seniority. APP11 and SYS
may deepen different distributed-systems subjects.

### APP9 — Application Engineering Capstone

Owns an integrated, independently reproducible and defended
application solving a bounded user problem. Evidence should show
requirements and user/ethical constraints, architecture decisions,
implementation, security/privacy considerations, testing,
deployment/recovery, observability, a measured trade-off,
and maintenance or an unfamiliar scoped change.

The public assessment definition must distinguish the required
deliverables and defense from optional stretch features. Supplied
stakeholder briefs and transparently synthetic usability feedback
are valid preparation where appropriate; they must not be
misrepresented as verified field research with real users. Provide
accessible review/defense routes, protect learner data and
credentials, and accept appropriately equivalent free local
environments. A team-style exercise or solo simulation must not
be presented as proof of actual collaborative team experience.

## 5. Electives, Rust, and cross-program boundaries

Keep APP10–APP16 as seven **optional** specializations. Their
prerequisites are targets for their own reviewed migration PRs,
not automatic edits to the active catalog.

| Code | Proposed specialization | Proposed foundation or boundary |
| --- | --- | --- |
| APP10 | Advanced Frontend Performance | APP20, APP6; deep rendering, memory, interaction and performance governance beyond APP2 |
| APP11 | Advanced Backend Architecture | APP3, APP4, APP6; backend evolution, isolation and coordination without duplicating the SYS discipline |
| APP12 | Realtime Systems | APP3, APP5, APP6; application-level connection lifecycle, event ordering, synchronization and recovery |
| APP13 | Mobile Application Engineering | APP19, APP3; APP20 only if a chosen implementation needs its React model |
| APP14 | API Gateways & Edge Delivery | APP3, APP7; advanced edge policy, identity propagation, caching and measured delivery |
| APP15 | TypeScript–Rust Application Interoperability | APP19, APP21, APP6 **plus demonstrated Rust competence**; precise SYS course link deferred until SYS redesign |
| APP16 | Platform Engineering | APP6, APP7; self-service workflows, policy, platform reliability and developer experience |

**APP15 amendment:** Its unique exit capability is to design, implement,
validate, version, test, operate and measure a TypeScript-facing
application feature with an appropriately bounded Rust component.
Focus on process/API boundaries first; FFI/shared memory is a
deliberate advanced alternative with safety analysis, not a
mandatory implementation gimmick. Do not re-teach introductory Rust,
C/Rust ownership comparisons, or all of SYS concurrency within APP15.

**SYS ownership is provisional until review:** Rust language foundations,
ownership/borrowing, lifetimes, low-level memory/safety mechanisms,
and explicit C-versus-Rust systems comparisons belong to the
redesigned SYS program. Do **not** hardcode the current legacy
SYS2 identifier into APP15's future catalog prerequisite before
SYS architecture and its assessments are approved. A public,
outcome-equivalent Rust readiness diagnostic can serve as an
alternative when the eventual SYS prerequisite is specified.

Advanced TypeScript library/package design may remain relevant in
APP15, but does not justify a second complete TypeScript foundations
course. No APP elective is required by APP9, any other core course,
or core graduation requirements.

## 6. Program-wide competency ownership review

This table is an **editorial coverage matrix**, not normative OEE
serialization or an additional source of truth. Future course PRs
must publish their actual required outcomes and assessments in
the respective course definitions under the OEE specification.

| Competency | Primary instructional owner | Applied/revisited and evidenced in |
| --- | --- | --- |
| Internet/DNS/TLS/HTTP and browser rendering mechanisms | APP1 | APP2, APP7 |
| Semantic HTML/CSS, native forms and static accessibility | APP17 | APP2, APP20 |
| JavaScript programming, errors, async semantics and basic tooling | APP18 | APP19, APP2, APP21 |
| TypeScript contracts versus runtime data | APP19 | APP2, APP20, APP3 |
| Data requirements, SQL correctness, constraints and transaction isolation | APP4 | APP3, APP5 |
| User journeys, dynamic UX states, usability and accessible interaction | APP2 | APP20, APP9 |
| Browser APIs, client security and framework-neutral behavior | APP2 | APP20, APP5 |
| React-specific rendering/state/data architecture | APP20 | APP5, APP10 |
| Node runtime, streams, HTTP primitives and diagnostics | APP21 | APP3 |
| API requirements, server authorization, secure service contracts | APP3 | APP5, APP6, APP9 |
| Cross-layer requirements, domain integration, contract evolution and partial failures | APP5 | APP6, APP8, APP9 |
| Reproducible testing, debugging and code maintenance | APP18 onwards, proportionate to each subject | APP6 (system strategy), APP9 |
| CI, supply chain, observability, reliability and incident diagnosis | APP6 | APP7, APP8, APP9 |
| Secure configuration, deployed boundaries, backups and rollback | APP7 | APP8, APP9 |
| Performance/capacity, resilience and cost-driven evolution | APP8 | APP9, relevant electives |
| Privacy and data minimization in product/system requirements | APP2, APP3, APP5 as applicable | APP7, APP9 |
| Technical reasoning and communication | SEF practice, then each APP implementation course | APP9's defense |
| Genuine collaborative work when offered and observed | Optional accessible learning arrangements | Do not claim team competence from solo simulation alone |

**Security progression:** APP1 explains Web trust mechanisms; APP17
establishes safe markup and accessible native form boundaries; APP2
covers browser origins, untrusted data, client state and exposure;
APP4 covers data access/constraints; APP21 covers runtime,
resource-bound and HTTP failure surfaces; APP3 covers application
authentication, server-side authorization and contract validation;
APP5 covers end-to-end identity, privacy, and cross-layer failure;
APP6 covers secure dependencies and quality checks; APP7 covers
secrets, deployment and operational access; APP9 assesses the
appropriate integrated risk argument.

This is *ordinary application security*, not a substitute for the
specialized SEC program. Security verification examples may
reference OWASP ASVS and NIST SSDF; accessible Web interaction
examples may reference WCAG 2.2. Use these as benchmarks for
reasoned criteria, not automatically binding requirements or
a demand to memorize whole standards.

**Overlap audit before course implementation:**

- APP1 explains Web/browser mechanisms; APP17 authors static
  documents; APP2 implements framework-neutral dynamic behavior;
  APP20 adds React-specific mechanisms and trade-offs.
- APP18 teaches the JavaScript language and Node/npm *tooling*;
  APP21 teaches Node as a backend *runtime*; APP3 teaches typed
  API implementation through a backend *framework*.
- APP4 teaches database mechanisms; APP3 applies them in an
  authorized service; APP5 integrates them across client/service
  boundaries.
- APP6 owns quality/reliability strategy and incident diagnosis;
  APP7 owns deployment and operational rollback/recovery; APP8
  owns measured architectural evolution.
- APP8 remains core application architecture. APP11 is optional
  advanced backend architecture; SYS owns deeper systems and
  language-level mechanisms.

Preserve substantive labs and useful outcomes from legacy APP
courses while relocating duplicated foundations to their
designated owners. Do not delete evidence obligations merely
because a capability is taught elsewhere; instead specify the
new, higher-level application in the appropriate later course.

## 7. Learning progression, assessments and workload

**Binding rules remain in OEE Course Format and Evidence Rules.**
This section gives the APP authoring/review strategy; it does not
introduce a new universal assessment quota, activity-kind taxonomy,
mandatory exam delivery method, or rule for unrelated programs.

### Teaching-to-evidence progression

| Stage | Instructional emphasis | Example inspectable evidence |
| --- | --- | --- |
| Web, documents and language foundations | Mechanisms, worked examples, prediction, guided diagnostics | Explain and reproduce a browser trace, accessible markup, or a JavaScript failure |
| Browser, runtime and database capabilities | Decreasing scaffolds, independent bounded changes and misuse cases | Implement a contract, debug malformed input, demonstrate data-integrity behavior |
| Frontend/backend application design | Maintainability, user flows, change impact and secure integrations | Tests against published requirements, authorization negative paths and failure recovery |
| Quality, deployment and production architecture | Realistic operational constraints, controlled incidents and measured alternatives | Reproducible pipeline, release recovery, traces, before/after trade-off analysis |
| APP9 capstone | Learner-owned problem framing, integrated delivery, independent change and defense | Clean reproduction, acceptance evidence, scoped unfamiliar modification, accessible technical defense |

Formative exercises and feedback should prepare learners for the
assessments; they must not silently become mandatory summative work.
Different outcomes need different evidence. Prefer fewer substantive
evaluations to a mechanical checkpoint-and-lab count. Where an
unfamiliar problem is used to establish independent transfer, its
criteria must still assess the public outcome, and an accessible
equivalent task must remain possible.

### Per-course authoring and review protocol

For **each** new or migrated APP course, reviewers should confirm:

1. **Entry competence:** prerequisites correspond to skills actually
   used at the start; no needless Web/framework gate or
   unacknowledged Rust/TypeScript requirement.
2. **Clear boundary:** one primary exit capability, distinct from
   neighboring courses and reasonable for the estimated workload.
3. **Instructional depth:** progressive lessons explain mechanisms,
   demonstrations, likely misconceptions, limitations, use cases,
   debugging, and authentic practice, not just headings or tool
   commands. Advanced recurrence adds new competence rather than
   repeating identical material.
4. **Outcome traceability:** stable `APPn-Ox` outcomes and
   `APPn-ASx` required assessments with credible direct
   evaluation of each claimed outcome under OEE v0.2.0.
5. **Assessment quality:** public work, criteria, evidence, environment
   and risk constraints; distinguish formative feedback from
   required completion evidence. Include negative-path,
   reproducibility and independent explanation when appropriate.
6. **Safety and independence:** local/free reproducible routes,
   accessibility, data minimization, learner privacy and
   proportional evidence. No required proprietary vendor,
   secret disclosure, paid book or public deployment.
7. **Workload calibration:** estimate reading, guided practice,
   debugging, revision and required assessment effort. Keep
   duration provisional, and address overloaded courses by
   competency analysis rather than arbitrary lesson reduction.
8. **Version and review:** structural validation plus substantive
   technical/editorial review, documented prior outcomes changed,
   assessment-ID/revision impact, source PR and downstream
   consumers. A green linter is not pedagogical conformance.

Module and lesson depth should be driven by these requirements,
not identical counts across courses. A learning *objective* can
have many supporting concepts without each becoming a new
course or a separate assessed submission.

### APP9 graduation evidence

APP9 must actually integrate the **core** capability graph,
not merely cite its course IDs. The project definition should
provide a reasonable problem space, milestones, user or
stakeholder requirements, data/privacy constraints, necessary
deliverables, verification and recovery criteria, and an
appropriate reviewable defense.

Require an independent reproduction and a justified scoped
change or unfamiliar diagnosis **when those are explicitly
defined APP9 outcomes**; this checks engineering ownership
rather than presentation quality alone. Do not require
unnecessary distributed components, public production
accounts, a paid hosting service, or an elective language.

Successful testing of software behavior does not itself
establish authorship, correct requirement selection, safe
operations, or collaboration. An accessible written,
recorded, synchronous or equivalent defense may establish
the appropriate reviewable reasoning.

### Readiness, status and ethics

All courses remain `draft` until the published OEE status
thresholds are met with actual learner/reviewer evidence;
migration or automated parse success does not promote them
to `tested`, `verified`, or program conformance. Never
publish unreviewable private learner data or imply that
a simulated team exercise proved real collaboration.

## 8. Migration, dependency and consumer protocol

**No automatic schema conversion or historical completion
reinterpretation.** Use short, separately reviewable public
course PRs. The catalog is changed only when a corresponding
course definition is actually merged.

1. **Architecture amendment — completed:** the revised dependency
   graph, ownership matrix, learning/assessment review gates and
   APP15–SYS boundary were adopted in [PR #78](https://github.com/0xbuffdev/open-engineering-education/pull/78).
   Track staged implementation in [issue #55](https://github.com/0xbuffdev/open-engineering-education/issues/55).
2. **Preserve preparation already done:** catalog-driven
   classification and ordering checks merged in
   [PR #44](https://github.com/0xbuffdev/open-engineering-education/pull/44).
   APP1, APP17, APP18, APP19, APP4 and APP21 are published
   `v0.2.0` course drafts; avoid rewriting them just to recreate
   earlier work.
3. **Foundation PRs:** APP18 was introduced in [PR #82](https://github.com/0xbuffdev/open-engineering-education/pull/82)
   and APP19 in [PR #84](https://github.com/0xbuffdev/open-engineering-education/pull/84).
   APP4's independent data/SQL migration was merged in [PR #86](https://github.com/0xbuffdev/open-engineering-education/pull/86),
   using SEF10 rather than the old APP3 prerequisite. APP21's
   framework-free Node runtime course followed APP18 through
   [PR #87](https://github.com/0xbuffdev/open-engineering-education/pull/87).
   APP2's browser engineering scope follows APP17 + APP19 in
   its separate reviewed migration PR, with catalog updates
   matched to the authoritative course file.
4. **Separate implementation branches:** APP21 follows APP18;
   APP2 follows APP17 and APP19; APP20 follows APP2;
   APP3 follows APP19, APP21 and APP4. Publish valid outcomes,
   assessments and genuine overlap relocation on each PR.
   APP21 and APP2's introductions do **not** change the still-legacy
   APP3 course prerequisites or its assessment contract.
5. **Integration and production:** APP5 after APP20 and
   APP3; then APP6, APP7, APP8; APP9 after complete
   required-core prerequisite closure and substantive
   review of the capstone evidence design.
6. **Elective migration:** APP10–APP16 receive independent
   scope/prerequisite/assessment review. APP15's exact Rust
   foundation link stays unresolved until the reviewed
   SYS redesign; do not invent a current SYS prerequisite
   or treat Rust as a hidden APP core skill.
7. **Downstream consumers:** for changed outcomes,
   assessments, course codes, dependencies or revisions,
   explicitly review OEE Workspace course/resource pins,
   content/book mappings, 0xNAND integrations and learner
   evidence identity. Never auto-remap stale evidence to
   a different educational requirement.
8. **Publication and readiness:** record migration impacts
   and decide the next appropriate repository release.
   Do not retag published `v0.2.0`. Run applicable
   structural, link and Markdown checks and obtain
   substantive review; keep course status truthful.

**Release gate:** The program is not migrated until each
core and elective course has its own reviewed and merged
source change, intended outcomes and summative coverage
have been examined, the authoritative catalog and
prerequisite closure match the merged source, and
consumer/revision obligations have identified owners.
"Implemented in source" is not equivalent to educational
validation or official conformance.

## 9. Decision history and implementation gates

**Original target decision:** 2026-11-07, through APP
architecture PR #49. Kept the 14 core competency identities,
new APP17–APP21 allocations, ordered catalog, core/elective
separation, framework/browser/runtime boundaries and public
reference-technology choices.

**Academic amendment accepted:** 2026-11-16,
[PR #78](https://github.com/0xbuffdev/open-engineering-education/pull/78).
The recorded target decisions are:

1. Remove unnecessary APP1 prerequisites from APP18 and APP4:
   both begin after SEF10.
2. Remove unnecessary TypeScript prerequisite from APP21:
   JavaScript/APP18 is enough. Add explicit APP19 to APP3's
   target prerequisites for its TypeScript reference path.
3. Establish named instructional ownership for
   requirements engineering, interaction/UX, security,
   privacy, testing, maintenance and technical defense.
4. Adopt progressive, outcome-aligned assessments that
   evaluate independent competence while respecting
   OEE's existing non-prescriptive activity and evidence rules.
5. Narrow elective APP15 to TypeScript–Rust application
   interoperability; give SYS ownership of Rust
   foundations and C/Rust comparisons, with the exact
   SYS dependency deferred until SYS architecture review.
6. Preserve APP1/APP17 source, all stable course IDs,
   optional electives, APP9 core closure, and immutability
   of published historical revisions.

**Approval boundaries:**

- This amendment is a curriculum *architecture* decision;
  it does not edit `spec/` or create binding OEE-wide rules.
  If future course design requires normative changes, use
  the public RFC/governance process separately.
- Course-specific outcomes, linked assessments, learner
  completion requirements, durations and actual prerequisites
  require their own reviewed curriculum-and-catalog PRs.
  This document cannot prematurely activate them.
- The current content-revision tag and previously assessed
  historical evidence are immutable and must retain their
  original interpretation.
- For a subsequent course PR, check curriculum format,
  expected prerequisite closure, course/catalog consistency,
  public evidence, no hidden paid dependency, and
  recorded changes to downstream pinned consumers.
- The editorial matrix, external reference guidance and
  examples here remain non-normative; they must not be
  misrepresented as additional v0.2.0 conformance rules.

**Current implementation snapshot:** APP1, APP17, APP18, APP19,
APP4 and APP21 are published in the outcome-driven `v0.2.0`
draft format; APP2's framework-neutral browser course is under
review in its separate migration PR. APP20 and the remaining
legacy course migrations, elective revisions and independent
APP evidence review remain future work. Use the
[current APP catalog](README.md) for active learner requirements;
planned dependencies are not live until the relevant course PR merges.

## 10. Non-binding review references

Use the following sources as background for coverage and
instructional design, not as hidden completion requirements:

- [OEE Curriculum Design Guide](../DESIGN-GUIDE.md)
  for capability boundaries, workload and lesson depth.
- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web),
  [web.dev Learn](https://web.dev/learn) and
  [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for Web,
  interaction and accessibility review.
- [JavaScript documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript),
  [TypeScript Handbook](https://www.typescriptlang.org/docs/),
  [React Learn](https://react.dev/learn),
  [Node.js Learn](https://nodejs.org/en/learn) and
  [Fastify documentation](https://fastify.dev/docs/latest/)
  for reference-language and runtime scope.
- [PostgreSQL documentation](https://www.postgresql.org/docs/)
  for database behavior and reproducible SQL study.
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
  and [NIST SSDF](https://csrc.nist.gov/Projects/ssdf) for
  appropriately scoped secure-engineering checks.
- [ACM/IEEE CS2023](https://csed.acm.org/) for broad
  academic competency comparison, not OEE certification.
