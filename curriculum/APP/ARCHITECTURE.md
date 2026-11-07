# Application Engineering — Course Architecture Proposal

**Status:** Proposed program-level architecture for review in [Issue #30](https://github.com/0xbuffdev/open-engineering-education/issues/30). **Not an adopted or published course catalog.**

The current authoritative program, course codes, prerequisites, and graduation
requirements remain in [APP README](README.md) and its linked course files
until separately reviewed migration pull requests change them. This document
is a **temporary migration design**, not another normative OEE specification,
authoring format, or course-completion contract. Retire it or reconcile it
into the canonical program catalog once migration is complete.

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
The **fourteen-course proposal is provisional**; final course counts and
durations follow audited capabilities, prerequisite load, and evidence,
not an arbitrary target.

## 2. Course identity is not course sequence

Existing identifiers `APP1`–`APP16` are already published in OEE
v0.2.0. Renumbering existing courses merely to make the new pathway look
contiguous would silently change the meaning of identifiers used by
prerequisites, assessments, OEE Workspace, resource maps, citations, and
future learner history.

**Preferred migration policy:** preserve existing course identities
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

## 3. Proposed core course progression

The table is **prospective**. None of the new titles, dependencies,
new files, or classifications is yet implemented.

| Sequence | Code | Proposed course | Public exit capability | Proposed direct prerequisites |
| --- | --- | --- | --- | --- |
| 1 | APP1 | Web & Internet Foundations | Diagnose a complete network-to-pixels Web visit | SEF10 |
| 2 | APP17 | HTML & CSS Engineering | Author semantic, accessible, responsive documents and styles | APP1 |
| 3 | APP18 | JavaScript Programming | Build and debug programs using JavaScript language and async semantics | APP1 |
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
  but it does not require backend framework engineering first.
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
language runtime reasoning to prevent cargo-culted
async code, but not a compulsory React/Node.js framework
or TypeScript type system.

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
React-specific server-side features may be evaluated
in later architecture/integration work if required
by genuine outcomes, not imported by default.

### APP21 — Node.js & Backend Foundations

Owns Node's event loop and task scheduling, modules,
process/runtime lifecycle, asynchronous filesystem
and networking APIs, streams/backpressure, basic
HTTP servers without a full framework, input/response
handling, cancellation, configuration, error
boundaries, security, local testing and diagnostic
observability.

This is not an introductory second JavaScript course.
It should demonstrate a reliable small service using
already acquired JS/TS skills before layering on a
framework or application persistence.

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
| JavaScript language/async semantics | APP18 | APP2, APP21 |
| TypeScript language/type design | APP19 | APP2, APP20, APP21 |
| Browser APIs, events, accessibility verification, client-side failures | APP2 | APP20, APP10 |
| React components/state/data architecture | APP20 | APP5, APP10 |
| Node runtime and raw HTTP-service fundamentals | APP21 | APP3 |
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

1. **Architecture decision:** review this proposal against the
   current APP catalog, competency map and Issue #30.
   Settle whether retaining old IDs and appending APP17–APP21
   is acceptable before creating course files.
2. **Validator/catalog preparation:** remove the current
   fixed assumption that APP1–APP9 are core and
   APP10–APP16 are electives. Use explicit catalog
   classification and a validated **ordered program list**;
   preserve the old validation behavior until each
   course is migrated. A numeric ID must not silently
   imply completion order or elective status.
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

The validator changes must be merged **before**
introducing the new core IDs, otherwise current
APP CI will fail by design. Curriculum PRs must
prove existing and newly added courses coexist
without weakening checks for historical files.
A future machine-readable course index can
express explicit order, but this proposal
does not create that serialization contract.

## 8. Review and decision record

Pending decisions before migration:

- Confirm the fourteen-course core *capability
  structure*, or identify independent capabilities
  that warrant merging/splitting after workload review.
- Confirm stable-ID preservation and APP17–APP21
  allocation, accepting that numeric IDs do not
  directly indicate study sequence.
- Confirm React as the dedicated frontend
  framework and Fastify as an **open reference
  candidate** for backend framework engineering.
- Confirm minimum core graduation outcomes and
  which advanced deployment/performance topics
  belong in electives or later courses.
- Confirm the prerequisite DAG and a
  non-disruptive consumer/resource migration path.

**No approval, migration, or renumbering is
implied by publishing this proposal.**
All new and migrated course definitions remain
`draft` until the OEE status evidence rules
support a different label.
