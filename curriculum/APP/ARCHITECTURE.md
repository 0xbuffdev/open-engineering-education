# Application Engineering — Migration Architecture Decision

**Decision status:** Approved migration architecture **upon merge of this decision PR**. **Implementation status:** planned and incremental, tracked in [Issue #30](https://github.com/0xbuffdev/open-engineering-education/issues/30). **The current [APP catalog](README.md) and course files remain authoritative until separate curriculum PRs merge.**

The current authoritative program, course codes, prerequisites, and graduation
requirements remain in [APP README](README.md) and its linked course files
until separately reviewed migration pull requests change them. This document records the **temporary program migration decision**; it is not another normative OEE specification, authoring format, or course-completion contract. Once implementation is complete, reconcile the decision into the canonical APP catalog and retain only the historical rationale needed for traceability.

The objective is a curriculum that starts at first principles, teaches
individual engineering capabilities deeply, and remains navigable for
independent study and for OEE Workspace/0xNAND. No course needs an arbitrary
module count, lesson count, assessment quota, or universal duration.

## 1. Decisions and boundaries

1. **Keep APP1 as the completed first-principles foundation.** It explains
   the Internet, DNS, HTTP/TLS, hosting, browser architecture, document
   parsing, layout, and rendering; it does **not** become an HTML/CSS,
   JavaScript, React, or backend-implementation course.
2. **Separate HTML/CSS, JavaScript, and TypeScript.** Each is a
   substantial capability with different learning outcomes, practical
   evidence, and prerequisites. Do not write a combined JS/TS course.
3. **Teach browser engineering before frameworks.** DOM events, browser APIs,
   accessibility, networking, application state, async work, debugging,
   and performance need a framework-independent foundation.
4. **Teach React in its own course.** React-specific reconciliation,
   component boundaries, state, effects, routing/data integration, testing,
   and architectural trade-offs are not generic browser fundamentals.
   Modern React application tooling requires basic Node.js/npm literacy:
   provide that within APP18 rather than making the full backend
   foundations course APP21 a prerequisite for React.
5. **Separate Node.js/backend fundamentals from backend framework
   engineering.** The former explains runtime/event loop, asynchronous
   I/O, HTTP service primitives, streams, process behavior, security,
   and testing; the latter teaches framework-level API composition and
   maintainable service architecture. Use **Fastify as a reference
   framework candidate**, not a new normative OEE dependency.
6. **Keep database engineering a distinct capability.** Teach SQL,
   relational modeling, indexes, transactions, schema evolution, and
   data correctness before treating a database as a framework plugin.
   PostgreSQL is an appropriate open reference implementation.
7. **Integrate only after the component capabilities exist.** Full-stack
   architecture, quality, deployment, production evolution, and capstone
   should reuse work rather than reteach syntax or prescribe unnecessary
   technology complexity.
8. **Keep electives optional.** Advanced frontend performance, distributed
   backend, realtime systems, mobile, edge, cross-language integration,
   and platform engineering are extensions, not hidden graduation gates.

The program's core remains an integrated Application Engineering pathway.
The **fourteen-course core capability structure is the approved migration target**, not an arbitrary course-count constraint or an immediate change to graduation requirements. Course durations, learning outcomes and any justified later split/merge must follow documented competency, prerequisite, workload and evidence review. Such changes require another explicit program-level decision.

## 2. Course identity is not course sequence

Existing identifiers `APP1`–`APP16` are already published in OEE
v0.2.0. Renumbering existing courses merely to make the new pathway look
contiguous would silently change the meaning of identifiers used by
prerequisites, assessments, OEE Workspace, resource maps, citations, and
future learner history.

**Adopted migration policy (effective upon merge):** preserve existing course identities
where the underlying capability remains recognizable, revise course
scope/version explicitly, and allocate **new IDs APP17–APP21** for five
new core capabilities. The course catalog's **ordered rows** are the
learner sequence; the numeric suffix is an identifier, not a
prerequisite level or an implicit sort key.

The existing `APP2` and `APP3` titles/scopes would be narrowed:
`APP2` retains the browser/frontend engineering capability; `APP3`
retains service/API engineering but makes the framework boundary
explicit. No old `APP2` completion automatically satisfies a new
framework-specific course outcome, and no old completion record is
reinterpreted without an explicit migration review.

The trade-off is nonsequential IDs in the displayed learning order.
That is preferable to silently making `APP2` mean HTML/CSS only
or making the historical `APP10` elective mean a new required course.
A future machine-readable export must expose **catalog order**
independently of course code and must not infer core/elective status
from number ranges.

## 3. Target core course progression

The table records the **approved target architecture**, not a live program catalog. The new course files, dependencies and classifications take effect only through separately reviewed migration PRs.

| Sequence | Code | Target course | Public exit capability | Target direct prerequisites |
| --- | --- | --- | --- | --- |
| 1 | APP1 | Web & Internet Foundations | Diagnose a complete network-to-pixels Web visit | SEF10 |
| 2 | APP17 | HTML & CSS Engineering | Author semantic, accessible, responsive documents and styles | APP1 |
| 3 | APP18 | JavaScript Programming | Build and debug JavaScript programs, including basic Node/npm tooling | APP1 |
| 4 | APP19 | TypeScript Programming | Design and verify useful static type contracts over JavaScript behavior | APP18 |
| 5 | APP2 | Browser & Frontend Engineering | Build framework-neutral, accessible, interactive browser applications | APP17, APP19 |
| 6 | APP20 | React Application Engineering | Engineer a maintainable React application with tested state and data behavior | APP2 |
| 7 | APP21 | Node.js & Backend Foundations | Build a secure, observable HTTP service using runtime primitives | APP19 |
| 8 | APP4 | Databases & Data Modeling | Model and query durable relational data and reason about transactions | APP1 |
| 9 | APP3 | Backend Framework Engineering | Build a validated, authorized, maintainable API service using a backend framework | APP21, APP4 |
| 10 | APP5 | Full-Stack Application Architecture | Integrate frontend, services, relational data, and cross-layer failure handling | APP20, APP3 |
| 11 | APP6 | Software Quality & Engineering Operations | Apply system-level tests, CI, observability, reliability and debugging | APP5 |
| 12 | APP7 | Deployment, Cloud & DevOps | Deploy, secure, observe, restore, and roll back an application | APP5, APP6 |
| 13 | APP8 | Production Application Architecture | Evaluate capacity, resilience and architecture changes with evidence | APP5, APP6, APP7 |
| 14 | APP9 | Application Engineering Capstone | Deliver and defend a substantial reproducible integrated product | Complete all preceding core capabilities |

This display order is a **recommended linear reading path**, not a
requirement to study all of its courses strictly serially. Once
APP1 is complete:

- HTML/CSS (APP17), JavaScript (APP18), and SQL/data modeling (APP4)
  can be studied in parallel where workload permits.
- After APP19, the backend runtime path (APP21) and the
  browser/frontend path (APP2 after APP17) can progress independently.
- Backend framework engineering (APP3) needs runtime/service
  understanding and data-modeling competencies; it does not
  require React first.
- React (APP20) needs browser/frontend and TypeScript knowledge,
  plus basic Node.js/npm development-tooling literacy gained in APP18;
  it does **not** require APP21 backend-runtime engineering or
  backend framework engineering first.
- Full-stack architecture (APP5) is the intentional integration
  boundary where the paths converge.

**Prerequisites are capability dependencies, not marketing gates.**
A learner who already demonstrates a required capability may qualify
through an appropriate public diagnostic route; the evidence must
be comparable to the published prerequisite outcome.

## 4. Exact ownership boundaries

### APP17 — HTML & CSS Engineering

Owns semantic HTML, document structure, forms, accessibility
fundamentals, CSS syntax/cascade, specificity, typography,
layout systems, responsive design, media queries, maintainable
styles, progressive enhancement, and accessible interface
inspection. Its project is a robust document/interface,
not a full JavaScript application.

Does **not** re-teach the Internet stack, JavaScript language
semantics, or framework components. APP1 already explains
what the DOM/CSSOM are; APP17 teaches constructing and
reasoning about real markup and styles.

### APP18 — JavaScript Programming

Owns values, types and coercion, control flow, scopes,
functions/closures, objects/prototypes, modules, exceptions,
collections/iteration, asynchronous promises and scheduling,
testing, debugging, and program design. Include enough
language runtime reasoning to prevent cargo-culted async code.

**Also owns basic Node.js development tooling**, without becoming a
backend course: installing and selecting a Node.js version,
running JavaScript with Node, using npm or a compatible package
manager, understanding `package.json`, dependency installation,
lockfiles, package scripts, ES modules, environment variables,
and local development/build commands. Practical evidence should
include reproducing a small JavaScript project from a clean checkout,
installing its declared dependencies, running a script/test, and
explaining the distinction between development tooling and code
that actually executes in a browser.

APP18 does **not** require implementing HTTP servers, streams,
production process lifecycle management, React, or TypeScript's
type system. Those belong to later capabilities.

### APP19 — TypeScript Programming

Owns structural typing, inference, narrowing, union/
intersection types, generics, mapped/conditional utility
types at appropriate depth, module/type declarations,
configuration, unknown data validation and type/runtime
boundaries, typed API surfaces, and useful tooling.
TypeScript is *not* a replacement for JavaScript
understanding; `APP18` is an explicit prerequisite.
Advanced library type design may continue in elective
APP15 without being needed for core graduation.

### APP2 — Browser & Frontend Engineering

Owns vanilla browser DOM APIs, event propagation,
forms/interaction, client-side routing concepts,
fetch/error handling, browser state, accessibility,
responsive application behavior, browser security
boundaries, structured UI state, testing, and measured
loading/interaction performance. Use JS/TS without
assuming React.

Relocate the current APP2's complete HTML/CSS teaching
to APP17, introductory JavaScript to APP18, TypeScript
language teaching to APP19, and React-specific
component models to APP20. Preserve valuable browser
performance/testing evidence in APP2 without
prematurely turning it into the APP10 elective.

### APP20 — React Application Engineering

Owns component composition, rendering/state transitions,
effects and synchronization, data fetching, forms,
client-side navigation/routing, accessibility,
testing, error boundaries, performance investigation,
and React application architecture. Explain where
React's model differs from browser primitives.

APP20 **uses** the Node.js/npm toolchain knowledge established
in APP18, including `package.json`, reproducible installs,
scripts and lockfiles. Teach creating/running/building a
React application with a modern open frontend toolchain
such as Vite, and how the resulting browser application
differs from the Node-hosted development/build process.
APP20 may refresh this setup, but must not duplicate an
entire Node.js programming curriculum.

React-specific server-side features may be evaluated
in later architecture/integration work if required
by genuine outcomes, not imported by default. A
React browser application is not inherently a Node.js
HTTP service.

### APP21 — Node.js & Backend Foundations

Owns Node's event loop and task scheduling, modules,
process/runtime lifecycle, asynchronous filesystem
and networking APIs, streams/backpressure, basic
HTTP servers without a full framework, input/response
handling, cancellation, configuration, error
boundaries, security, local testing and diagnostic
observability.

This is not an introductory second JavaScript course,
and is **not a prerequisite for APP20 React**. It develops
backend-runtime understanding beyond APP18's package-manager
and script-runner familiarity. It should demonstrate a
reliable small service using already acquired JS/TS skills
before layering on a framework or application persistence.

### APP4 — Databases & Data Modeling

Retains relational modeling, SQL, constraints,
indexes, transactions, isolation, migrations,
query analysis, security, backup/recovery
fundamentals, and measured data decisions.
PostgreSQL is an open reference database;
general correctness outcomes are not
PostgreSQL-locked. Database knowledge can be
studied in parallel with frontend/backend
runtime work rather than requiring APP3 first.

### APP3 — Backend Framework Engineering

Retains API service engineering, validation,
authentication and authorization, domain
boundaries, transactions, async/background
work, structured errors, contract/version
compatibility, tests, observability,
security review and operational behavior.

Its **reference framework candidate** is Fastify
with TypeScript, used to apply the concepts
after APP21 and APP4. Public outcomes should
describe portable service-engineering
capabilities; framework-specific instructions
are a supported example, not a proprietary
requirements gate.

### APP5–APP9 — Integration and production sequence

Retain the existing responsibilities with
v0.2.0 outcome-driven restructuring when
their migration begins:

- **APP5 Full-Stack Application Architecture:** UI/service/data
  composition, authenticated flows, async operations,
  caching and external integration failure boundaries.
- **APP6 Software Quality & Engineering Operations:** risk-based
  tests, CI, observability, dependency safety, reliability,
  performance verification and incident reasoning.
- **APP7 Deployment, Cloud & DevOps:** portable release/build,
  secret management, TLS/networking, health checks,
  monitoring, rollback, backups and cost-aware deployment.
- **APP8 Production Application Architecture:** scaling,
  queues, caching, consistency trade-offs, resilience,
  availability and evidence-based architectural revision.
- **APP9 Application Engineering Capstone:** one
  substantial, versioned, independently defended product,
  integrating the required core competencies. A
  capstone need not force excessive distributed-system
  complexity merely to count technologies.

## 5. Elective preservation

The existing seven electives retain their IDs and
optional graduation classification. Their recommended
new prerequisite links will be reviewed after core
migration; none should gate APP9.

| Existing code | Specialization | Proposed relevant foundation |
| --- | --- | --- |
| APP10 | Advanced Frontend Performance | APP20, APP6 |
| APP11 | Advanced Backend Architecture | APP3, APP4, APP6 |
| APP12 | Realtime Systems | APP3, APP5, APP6 |
| APP13 | Mobile Application Engineering | APP19, APP3; APP20 where the chosen mobile stack requires it |
| APP14 | API Gateways & Edge Delivery | APP3, APP7 |
| APP15 | Advanced TypeScript/Rust Application Development | APP19, APP21, APP6, relevant SEF systems competence |
| APP16 | Platform Engineering | APP6, APP7 |

Do not make advanced framework-specific knowledge or Rust
interoperability necessary for a learner who is not
studying the corresponding elective.

## 6. Coverage and overlap review

Before writing replacement curricula, maintain a temporary
ownership matrix in the architectural migration issue,
cross-checking the supplied roadmaps, open language
documentation, reference implementation docs and
the OEE course outcomes. At a minimum, verify:

| Competency family | Primary owner | Supporting/revisited in |
| --- | --- | --- |
| Internet, DNS, TLS, HTTP, browser engines, rendering model | APP1 | APP2, APP7 |
| Semantic HTML, CSS, responsive layout, foundational accessibility | APP17 | APP2, APP20 |
| JavaScript language/async semantics and basic Node/npm tooling | APP18 | APP2, APP19, APP20, APP21 |
| TypeScript language/type design | APP19 | APP2, APP20, APP21 |
| Browser APIs, events, accessibility verification, client-side failures | APP2 | APP20, APP10 |
| React components/state/data architecture and Vite-based frontend builds | APP20 | APP5, APP10 |
| Node backend runtime and raw HTTP-service fundamentals | APP21 | APP3 |
| Relational database and SQL correctness | APP4 | APP3, APP5 |
| API framework, security, backend service correctness | APP3 | APP5, APP11 |
| Integrated application architecture | APP5 | APP8, APP9 |
| Tests, reliability, CI and observability | APP6 | Every implemented project; APP7–APP9 |
| Deployment, operations, recovery | APP7 | APP8, APP9 |
| Scaling and failure-driven architecture | APP8 | APP9, relevant electives |

The matrix is a **planning aid**, not a second
machine-readable curriculum source. The canonical
course files remain the source of each actual
outcome and assessment after review.

Audit sources from [Issue #30](https://github.com/0xbuffdev/open-engineering-education/issues/30):
[roadmap.sh](https://roadmap.sh/roadmaps),
[web.dev Learn](https://web.dev/learn),
[MDN](https://developer.mozilla.org/en-US/docs/Web),
[TypeScript documentation](https://www.typescriptlang.org/docs/),
[React documentation](https://react.dev/learn),
[Node.js Learn](https://nodejs.org/en/learn),
[Fastify documentation](https://fastify.dev/docs/latest/),
and [PostgreSQL documentation](https://www.postgresql.org/docs/).
These are reference/benchmark inputs, never
a mandatory paid curriculum dependency.
Detailed coverage comparison is an outstanding
authoring review, not a completed claim.

## 7. Migration protocol

**No mass renaming or ID reassignment in this proposal.**
Implement the approved architecture in short,
independently reviewable stages:

1. **Architecture decision:** adopt the competency boundaries, preserve existing APP1–APP16 identities, and reserve APP17–APP21 for the five new core capabilities as recorded here; effective when this PR merges. Course migration remains separate.
2. **Validator/catalog preparation — completed in [PR #44](https://github.com/0xbuffdev/open-engineering-education/pull/44):** use explicit catalog classification and validated **ordered program rows** rather than assuming APP1–APP9 are always core and APP10–APP16 are always elective. Preserve historical course validation while migrating. A numeric ID must not imply order or elective status.
3. **First new foundations:** add APP17 HTML/CSS, APP18
   JavaScript and APP19 TypeScript as distinct
   v0.2.0 draft courses, with outcomes, public
   evidence, and appropriate prerequisites.
4. **Two independent implementation paths:** migrate
   APP2 to browser/frontend engineering and add
   APP20 React; add APP21 Node.js foundations;
   migrate APP4 database dependencies as needed,
   then narrow APP3 to backend framework engineering.
5. **Integration and capstone:** migrate APP5–APP9
   to the final prerequisite graph and proportional
   public summative assessments; update elective
   dependencies APP10–APP16 without turning
   electives into core graduation gates.
6. **Consumer migration:** update the OEE Workspace
   course index, resource/book mappings, 0xNAND
   integrations, links, exported order, and
   learner-progress version handling. References
   must not be silently rewritten to different
   capabilities.
7. **Release control:** record course ID additions,
   identity-preserving scope revisions, changed
   prerequisites, and completion-contract revisions
   in release notes. Determine the appropriate
   subsequent repository version before publishing
   the revised program. Do not move the published
   `v0.2.0` tag.

The required catalog-driven validator changes **are already merged** in PR #44. Each curriculum PR must demonstrate that existing and newly added course files coexist without weakening legacy checks, required prerequisite closure, or explicit classification.
A future machine-readable course index can
express explicit order, but this proposal
does not create that serialization contract.

## 8. Decision record and implementation gates

**Decision date:** 2026-11-07 (effective only when this decision PR merges).

**Scope:** APP program design, public reference curriculum boundaries and
migration sequencing; this decision changes **no normative OEE v0.2.0 rule**.
The [APP catalog](README.md) remains authoritative for learners until the
individual course migration PRs merge.

### Accepted decisions

1. **Core architecture:** adopt the fourteen capability/course boundaries in
   Section 3 as the target for reviewable implementation, without treating the
   number fourteen as a normative constraint or a guarantee of fixed duration.
   Course-specific evaluation may justify a later separately recorded revision.
2. **Stable identities:** keep the meaning of existing `APP1`–`APP16`
   course identifiers wherever recognizable. Assign `APP17`–`APP21`
   to HTML/CSS, JavaScript, TypeScript, React and Node.js/backend foundations,
   respectively. **Catalog row order**, not numeric course suffix, is the
   learning-order authority.
3. **Course ownership:** preserve APP1 unchanged. Relocate legacy APP2
   language, HTML/CSS and framework introduction into the correct new
   courses; narrow APP2 to framework-neutral browser/frontend engineering
   and APP3 to backend framework engineering. APP4 keeps relational/data
   engineering and no longer needs APP3 as a prerequisite after migration.
4. **Reference technologies:** React is the core open-source frontend
   framework subject, following framework-neutral browser work. Fastify
   with TypeScript is the open reference **candidate** for APP3, and
   PostgreSQL is an open reference for APP4. Publish transferable
   capabilities and criteria; avoid a proprietary-service completion gate.
   A further recorded decision is required if the reference framework
   choice materially changes a required course outcome.
5. **Graduation competencies:** the required core must cover web diagnosis;
   accessible documents and styles; JavaScript and TypeScript correctness;
   browser interaction; React application design; backend runtime and
   framework services; relational data; full-stack integration; testing,
   CI and observability; deployment/recovery; evidence-based production
   architecture; and APP9's reproducible engineering defense.
6. **Optional specializations:** keep APP10–APP16 elective. Advanced frontend
   optimization, distributed/backend systems, realtime, mobile, edge,
   cross-language interoperation and platform engineering do not become
   hidden APP9 graduation prerequisites.
7. **Dependency model:** use the direct prerequisites in Section 3.
   After APP1, APP17, APP18 and APP4 can proceed independently; APP19
   follows APP18. APP2 needs APP17 and APP19; APP20 follows APP2.
   APP21 follows APP19, and APP3 needs APP21 and APP4.
   APP5 converges APP20 and APP3. APP6, APP7 and APP8 follow the
   dependencies in Section 3. APP9 must cover **all core courses**
   through the validated prerequisite closure, with no elective required.
8. **Versioned migration:** never reinterpret a previously recorded course
   completion as meeting a newly revised course's assessment contract.
   Track the course/spec revision, maintain stable references, update
   workspace/resource/0xNAND consumers explicitly, and document breaking
   prerequisite or completion changes in the subsequent release. Do not
   move the published `v0.2.0` tag.

### Implementation gates

- **Before first course PR:** the dual-format APP validator and
  catalog-driven classification/order checks must be present; met by PR #44.
- **For each new or migrated course:** include explicit
  `**Specification:**` metadata with value `v0.2.0`, stable required outcome and
  assessment IDs, public assessment criteria/evidence, a substantive
  outcome-coverage review, realistic prerequisite justification, and
  appropriate practical work without fixed test/lab quotas.
- **For APP17–APP21 introduction:** update the authoritative catalog
  in the same course PR so the course has an explicit classification,
  correct study order and prerequisites; preserve validation for legacy
  courses. Unchanged course definitions must not be relabeled as
  v0.2.0-conforming.
- **For existing course dependency changes:** update the affected course
  metadata and catalog together, and preserve a passing APP9
  all-core prerequisite closure. Stage downstream adaptations
  deliberately rather than silently changing historical learner records.
- **Before declaring program migration complete:** conduct the coverage
  audit against the open reference sources listed in Issue #30, verify
  substantive assessment quality and free/public reproducibility, align
  consumer mappings and recorded revisions, and publish a release with
  the migration impact explained.
- **For readiness claims:** all new and migrated course definitions
  remain `draft` until learner evidence and independent review satisfy
  the OEE status requirements. Automated validation alone is not a
  conformance or educational-quality finding.

The next implementation PR should introduce **APP17 — HTML & CSS
Engineering** under this architecture, without editing APP1. Subsequent
reviewable PRs introduce APP18 and APP19 before narrowing APP2 or
adding the framework- and backend-specific courses.
