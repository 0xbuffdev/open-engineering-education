# APP9 — Application Engineering Capstone

**Program:** APP — Application Engineering
**Type:** `project`
**Classification:** `core`
**Prerequisites:** [APP1](APP1.md), [APP2](APP2.md), [APP3](APP3.md), [APP4](APP4.md), [APP5](APP5.md), [APP6](APP6.md), [APP7](APP7.md), [APP8](APP8.md), [APP17](APP17.md), [APP18](APP18.md), [APP19](APP19.md), [APP20](APP20.md), [APP21](APP21.md)
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; requires independent calibration)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

**Independently define, build, deploy, evaluate, improve and defend one coherent application** integrating the full Application Engineering core. The capstone is a graduation project, **not** a retest of every previous lab or a collection of screenshots. Engineering independence is shown through responsible problem selection, substantive personally defensible implementation, factual evidence, ethics, actual software behavior and an independent unfamiliar change or diagnosis.

**Complete required core:** The explicit prerequisites cover APP1–APP8 and APP17–APP21. They encompass first-principles web/Internet and HTML/CSS; JavaScript, TypeScript and the Node runtime; framework-neutral browser and React; data/SQL and typed backend service engineering; integrated application, quality/CI, actual deployment/recovery and measured production architecture. The capstone integrates **relevant transferable capabilities** in the *same product* without requiring an artificial demonstration of every prior topic, lab or elective. Authentic predecessor-course completion is a **separate entry requirement**, while APP9 requires new, independently evaluated product performance. Simply citing completed course IDs does not establish APP9 mastery. Optional APP10–APP16 electives, SYS/Rust and proprietary or paid services are **not** required.

**Acceptable product problem spaces:** An accessible education tool, multi-user business workflow, developer platform/tool, document/resource system or other bounded authenticated application with real user tasks, persistent state, authorization boundaries and a justified asynchronous or simulated external side effect. The product must include frontend, typed service, PostgreSQL, quality and a real locally operated deployment. A modular monolith is sufficient when evidence does not justify distribution. Avoid mandatory AI features, public hosting, microservice fleets or a commercial identity provider.

**Ownership and reuse:** Learners may build on earlier APP5–APP8 work or suitable starter templates, libraries and AI assistance, with clear attribution and independent explanation. There must be a **substantive capstone-owned change**—a new or materially revised user workflow, product requirement, security boundary, operating capability or architecture decision—and the learner must implement and defend it. Unmodified old coursework or a generated project that the learner cannot explain is insufficient. Solo projects are valid; collaboration must not be fabricated.

**Research integrity and equitable access:** If actual stakeholders or participants are available, use voluntary informed consent, appropriate minimization and ethical low-risk task observation. If not, cite relevant public evidence or perform explicitly labeled heuristic/synthetic task analysis. Neither synthetic personas nor fictitious interviews prove real demand. The required capability is thoughtful, reviewable research, bounded interpretation and a reasoned product decision, not access to personal networks or paid research panels.

**Integrated engineering:** The UI must demonstrate semantic, responsive, accessible React and sound browser state. A real TypeScript/Node/Fastify service must validate runtime inputs and enforce session/resource/tenant/action/property authorization independently of hidden UI controls. Actual PostgreSQL data must implement credible relational constraints and transactional concurrency. An asynchronous or external interaction must have honest accepted/completed/uncertain states, bounded retries and a defensible idempotency policy. Security and privacy also apply to cached resources, files, background jobs and logs according to features used.

**Engineering quality and operation:** Design real multi-layer tests and reproducible local CI, including normal/invalid/forbidden/concurrent failure cases. Deploy using free local APP7-compatible processes/containers and isolated synthetic data with genuinely verified local HTTPS, controlled release identity, secrets isolation and actual real-database restore. Investigate one injected running-service failure, then perform a reproducible workload or reliability/architecture decision comparing sensible options using measured results, financial assumptions and limitations. One laboratory run cannot certify public uptime, cloud security, global scalability or market demand.

**Independent evaluation:** A reviewer must be able to reproduce actual behavior from a clean environment with documented free provisioned dependencies, ask a bounded unfamiliar requirement or fault within published outcomes, inspect the learner's corrective evidence and challenge design alternatives. Technical defense may be live, written, recorded or equivalently accessible. The reviewer must not impose private criteria, unpublished technologies or paid systems.

**Duration and completion:** 12–16 weeks at 10–15 focused hours/week is provisional, not an evidence-backed workload guarantee. This course uses **eight cumulative summative assessments** with one evolving project. All ordinary lessons and planning milestones are formative unless explicitly used as evidence for a required assessment; no hidden attendance or checkmark gates apply.

### Verified prerequisite closure and capstone integration

Before starting Module 1, verify independently assessed completion decisions for **all thirteen** directly required APP core courses—APP1–APP8 and APP17–APP21—or separately approved, genuinely assessed outcome-equivalent preparation. Record each course code, actually assessed course/spec revision, decision and safe evidence reference; do not copy sensitive student records or substitute attendance, a passed unassessed diagnostic, a portfolio label or the capstone itself. A missing, unknown or rejected predecessor decision **blocks capstone entry** and must be resolved through that prerequisite's evaluation or governed equivalence process.

The prerequisite register and the project integration map answer **different questions**: prior completion establishes admission readiness; the project shows how applicable earlier competence transfers to one real product. Directly applied skills should point to actual product evidence; a bounded explanation may establish relevant conceptual transfer; a prior topic not naturally needed by the selected product does **not** justify manufacturing an unrelated feature. Mark such integration as not applicable while retaining its **required prior completion**. A course titled `draft` may still have legitimately evaluated individual learner work; source readiness status and learner completion are not interchangeable.

This is an entry and graduation-verification procedure, **not a ninth APP9 summative assessment** and not permission to regrade historic course revisions under new outcomes. The eight required APP9 assessments still evaluate APP9's own sixteen outcomes. Self-directed study may retain an inspectable evidence register, but a self-written completion claim without an actual assessed decision does not satisfy the admission requirement.

## Learning outcomes

- **APP9-O1:** Independently select, bound and justify a feasible application problem, identify affected users or stakeholders, competing needs, evidence provenance and realistic constraints without fabricating product demand.
- **APP9-O2:** Evaluate a consequential product assumption with ethically sourced consented, secondary or clearly labeled synthetic evidence, acknowledge methodological limits, and make a reasoned scope or interaction decision.
- **APP9-O3:** Translate the problem into prioritized user journeys, measurable normal/negative acceptance rules, domain invariants, privacy/accessibility needs, nonfunctional criteria and traceable incremental delivery.
- **APP9-O4:** Design and defend a coherent browser, React/TypeScript, Node/Fastify, PostgreSQL, authenticated, asynchronous and deployed architecture, including alternatives, trust boundaries, ownership and justified simplicity.
- **APP9-O5:** Deliver an accessible and usable responsive browser/React client with correct navigation, forms and observable empty, pending, invalid, expired, conflict, forbidden, failure and recovery states.
- **APP9-O6:** Deliver typed, runtime-validated service and HTTP contracts with real authentication and server-authoritative action, object, property and tenant authorization, verified by independent direct HTTP tests.
- **APP9-O7:** Model, migrate and operate relational PostgreSQL data with key and foreign-key constraints, transactions, concurrent-write invariants, query-plan awareness and independent durable-state verification.
- **APP9-O8:** Integrate justified asynchronous or external work with explicit authority, durable intent or bounded alternative, idempotent retry, user-visible progress and truthful reconciliation when completion is uncertain.
- **APP9-O9:** Identify and mitigate critical application privacy and security threats across sessions, API, database, caches, files, job status, dependencies, logs and deployments; verify least privilege and meaningful retention/deletion behavior.
- **APP9-O10:** Establish a risk-based independent test architecture, deterministic fixtures, meaningful accessibility/security negatives, source/dependency review, reproducible build and least-privilege CI that fails on a seeded material defect.
- **APP9-O11:** Release and operate an inspectable local deployment with correctly verified HTTPS, secret/environment isolation, trusted artifact identity, controlled promotion and safe stateful client/schema compatibility.
- **APP9-O12:** Use user-centered signals to detect, investigate, contain and recover from an actual local injected release/dependency incident; verify a real isolated PostgreSQL restore and qualified recovery point/time.
- **APP9-O13:** Design and interpret a reproducible user-task capacity/load experiment, detecting tail latency, failure and bottleneck/generator limits and validating a proportionate architecture or overload response.
- **APP9-O14:** Compare meaningful product and architecture options against measured user behavior, data/security requirements, performance, reliability, maintenance effort and resource/operational cost; justify changing or retaining the simpler design.
- **APP9-O15:** Maintain accurate inspectable requirements, changes, research provenance, architecture decisions, source authorship/assistance, review, operational/user documentation, failures, limitations and retrospective, claiming collaboration only when genuine.
- **APP9-O16:** Reproduce and explain the learner's substantive product contribution from clean state, respond to an unfamiliar bounded requirement or fault with observed tests/change, preserve critical invariants and defend alternatives and limits accessibly.

## Modules

The seven modules below are **cumulative project stages**, not another course sequence reteaching APP1–APP8 or APP17–APP21. **Instructional sufficiency** requires a clear mechanism and rationale, a worked or observable example, an authentic application, a failure counterexample and actionable feedback **before** an independent assessed decision where a new capstone problem demands them. Prior competence is reused, but product-specific reasoning and unfamiliar transfer are never assumed. Formative stage practice is not a hidden graduation gate. Refer to previously accepted `APP9-AS1`–`APP9-AS8` evidence rather than rebuilding the same product or reports.

### Module 1 — Charter, Ethical Inquiry and Feasible Scope

#### Outcomes

- - APP9-O1
- - APP9-O2
- - APP9-O3
- - APP9-O9
- - APP9-O15

#### Lessons

1. **Authentic admission, learner ownership and reuse** — Verify all thirteen genuine predecessor assessment decisions with exact course/spec revisions or approved equivalence before starting. Identify what is prior, third-party, collaborative or AI-assisted and name the *substantial capstone-owned* new user capability, architecture decision or security/operating correction that the learner will personally implement and defend. This entry check is not another APP9 assessment.

2. **Real problem and affected people** — Describe a specific user task, stakeholder constraints and credible provenance; distinguish a supplied brief from observed demand and state whose interests and data are at risk.

3. **Ethically valid inquiry and falsifiable question** — Select a consequential user-task assumption and an appropriate consented, secondary or transparently synthetic heuristic method, recording consent/storage boundaries, bias, confounders and what the chosen evidence cannot establish; paid panels and participant access are not required.

4. **Compare evidence and change a genuine decision** — Interpret actual, sourced or synthetic findings without turning generated personas into user observations; test an alternative explanation, document feedback that could disprove the claim and revise a specific product requirement or scope decision.

5. **Observable normal, denied and recoverable task contracts** — Define prioritized user outcomes, tenant/object/property and database invariants, accessible keyboard/focus, identity switch and pending/uncertain committed state. Set an independently checkable negative case for each significant failure condition.

6. **Constraints, exclusions and milestones** — Bound the smallest coherent product, plan its dependency-aware development, and record unimplemented features and assumptions rather than concealing them.

7. **Critique and revise the charter** — Expose the charter to a counterexample or independent review, revise a weak assumption, and preserve the reasoned decision; this is formative unless the published assessment evaluates the result.

### Module 2 — Architecture, Trust and Reproducible Design

#### Outcomes

- - APP9-O3
- - APP9-O4
- - APP9-O6
- - APP9-O7
- - APP9-O8
- - APP9-O9
- - APP9-O14
- - APP9-O15

#### Lessons

1. **One product and its boundaries** — Draw context and component views for browser, typed React client, Node/Fastify service, PostgreSQL and any genuinely required worker or external fixture; justify a modular monolith where sufficient.

2. **One task across user, HTTP, database and external effect** — Trace one protected user action from React request through credential proof, server authorization, Fastify validation, PostgreSQL commit and any durable job to truthful UI reconciliation. Work through a denied action and a post-commit lost-response counterexample.

3. **Verified identity, property policy and lifecycle privacy** — Define authorized principal, tenant/resource/action/read-write-property checks and lifetime/retention across HTTP, cached values, private files and worker status where applicable; demonstrate a client-forged tenant claim or revoked-session failure in the design review.

4. **Data model and concurrency contract** — Define entities, keys, relational constraints, transactions, query assumptions and schema compatibility, including two conflicting writers and durable outcomes.

5. **Contract and asynchronous boundaries** — Specify runtime validation, HTTP status/error semantics, replay safety, background intent, status visibility and client reconciliation without promising exactly-once side effects.

6. **Alternatives, challenged trust boundary and feedback** — Compare a modular monolith and an actual feasible alternative on correctness, privacy, access, operational load and cost. Challenge an unverified assumption or attacker-controlled input with a worked trace; change or reject the design based on concrete evidence.

### Module 3 — Implement the Protected Application Journey

#### Outcomes

- - APP9-O4
- - APP9-O5
- - APP9-O6
- - APP9-O7
- - APP9-O8
- - APP9-O9

#### Lessons

1. **Semantic and accessible client skeleton** — Implement responsive HTML/CSS, meaningful navigation, forms, focus and named controls for the selected task; verify keyboard and failure-state access rather than repeating basic HTML instruction.

2. **React client state, late identity and accessible failure** — Use typed React state and validated HTTP to make empty/pending/invalid/expired/forbidden/conflict/recovered states observable; reproduce one stale response after route/user change, then verify keyboard/focus and truthful status after repair.

3. **Backend contracts with authoritative direct-request denial** — Implement Fastify runtime schemas and actual trusted credentials, apply server-side action, object, read/write-property and tenant authorization, then issue independent guessed-resource/forged-role requests and inspect HTTP *and* PostgreSQL consequences.

4. **Relational schema and durable integrity** — Implement a PostgreSQL schema and versioned migrations with keys and constraints for the product's actual user task; inspect invalid-input rejection and authoritative persisted state using an independent SQL oracle.

5. **Two real writers, one invariant and uncertain replay** — Coordinate actual PostgreSQL-backed simultaneous HTTP operations, verify final committed rows, revision/constraint conflict and idempotent duplicate behavior, then intentionally lose a successful response and reconcile without duplicating the effect.

6. **Durable intent, worker restart and real completion** — Connect a justified recorded local external/worker operation to authoritative durable state, simulate a failed dependency or duplicate delivery and prove restart/retry bounds; distinguish HTTP accepted, DB committed, worker pending and actually completed user state.

7. **Privacy-safe auxiliary resources** — Use caching or file workflows only when necessary for the product; demonstrate appropriate authorization, retention and invalidation without making unrelated features graduation requirements.

8. **Worked failure across the actual product journey** — Walk one user task through success, permission denial, lost result and partial external failure; compare UI/status with independent HTTP/PostgreSQL/job facts, diagnose why a misleading success or stale result appears and repair it before summative judgment.

### Module 4 — Independent Quality, Security and Corrective Evidence

#### Outcomes

- - APP9-O5
- - APP9-O6
- - APP9-O7
- - APP9-O8
- - APP9-O9
- - APP9-O10
- - APP9-O15

#### Lessons

1. **Risk-led verification plan** — Translate the actual product risks into domain, browser, API, database, contract, accessibility and deployment checks; avoid a test-count quota and independent-oracle circularity.

2. **Authorization and data-integrity attacks** — Attempt invalid, cross-tenant, cross-role, replayed and concurrent actions through direct client and HTTP paths; inspect both response and authoritative database state.

3. **Dynamic accessibility and privacy-state observation** — Test keyboard/focus, relevant zoom/reflow, status announcements and usable error recovery under genuine React state changes. Inspect sensitive DOM, client cache and sanitized logs; distinguish actual assistive-tech checks from untested contexts without claiming WCAG certification.

4. **Deterministic execution and fault controls** — Use declared fixtures, seeds, controlled time, process and network faults, isolated databases and teardown to make failure claims reproducible.

5. **Secure build and CI decisions** — Publish reproducible build steps, dependency review, scoped CI privileges and meaningful fail-closed tests; document where the free local equivalent differs from a hosted provider.

6. **A material seeded defect with independent repair evidence** — Seed an actual authorization, schema, async state, accessible-error or concurrency flaw. Show a failing external/user/DB oracle before code changes, correct the cause, rerun material negative regressions and explain source attribution, CI limits and untested risk.

### Module 5 — Release, Observe and Recover the Same Product

#### Outcomes

- - APP9-O9
- - APP9-O10
- - APP9-O11
- - APP9-O12
- - APP9-O15

#### Lessons

1. **Reproducible operational package** — Start the same full-stack system from versioned source and isolated synthetic data; identify immutable artifact versions, startup/shutdown health and service boundaries.

2. **Verified HTTPS and secret isolation** — Demonstrate local certificate/hostname verification, trusted proxy headers, runtime configuration isolation and denied unauthorized environmental access.

3. **Compatible application and database release** — Stage old/new client, service and schema combinations; justify rollback versus forward repair for a persistent change and retain the tested artifact identity.

4. **Signals for user-visible service health** — Collect privacy-safe request, data and release observations that distinguish green process health from a broken protected user journey.

5. **Local running-service incident and stateful recovery** — Inject a real bounded release/proxy/dependency defect in the running service; capture safe browser, HTTP, DB and job observations, discriminate between plausible causes, repair and independently verify authorized/denied user behavior rather than simply seeing a green health response.

6. **Clean separate PostgreSQL restoration and permission proof** — Restore real populated test data into a separately named clean disposable PostgreSQL instance, account for global roles/privileges missing from a single-database logical dump, inspect actual schema/invariants and allowed/denied task outcomes, measure local recovery time/point and disclose missing private files, worker/external effects and non-PITR limitations.

7. **Operational handoff and limitations** — Publish clear setup, monitoring, release/recovery and shutdown instructions, unsafe assumptions and what the local exercise does not establish about public-cloud production.

### Module 6 — Measured Evolution, Product Revision and Economics

#### Outcomes

- - APP9-O1
- - APP9-O2
- - APP9-O3
- - APP9-O4
- - APP9-O12
- - APP9-O13
- - APP9-O14
- - APP9-O15

#### Lessons

1. **Re-evaluate the original task assumption without invented users** — Challenge the initial product assumption with ethically consented observations where actually available, otherwise cited public/secondary sources and labeled synthetic heuristic evaluation. Note selection bias and decide a meaningful revision, justified no-change or responsible further study.

2. **Capacity and correctness hypothesis** — Choose a measured latency, resource, saturation, or failure claim tied to a real task, protected data and an operational constraint rather than benchmark theater.

3. **Representative workload and bias** — Record task/tenant mix, data scale, warm-up, request arrival, environment, trials and generator limits; distinguish throughput, tail latency, failures and unmeasured effects.

4. **Locate the causal bottleneck** — Correlate browser/API/Node/SQL and dependency observations; challenge simplistic averages, coincidental correlations and unvalidated optimization claims.

5. **Compare at least two credible decisions** — Evaluate remove-work/no-change, caching/queue/concurrency or appropriate architectural alternatives against correctness, privacy, availability, cost and maintenance burden.

6. **Measured improvement or defensible no-change decision** — Repair one measured query, task, overload or architectural defect when warranted; if not, explicitly defend preserving the simpler baseline. Repeat comparable observations and ensure real tenant security, data invariants, accessible recovery and supported user tasks remain correct.

7. **Revise, document and hand off** — Revisit acceptance, user guidance, costs, energy/operational implications and original assumptions; identify bias, limitations, unsatisfied requests and next safe iteration.

### Module 7 — Independent Reproduction, Unfamiliar Challenge and Graduation Defense

#### Outcomes

- - APP9-O1
- - APP9-O2
- - APP9-O3
- - APP9-O4
- - APP9-O5
- - APP9-O6
- - APP9-O7
- - APP9-O8
- - APP9-O9
- - APP9-O10
- - APP9-O11
- - APP9-O12
- - APP9-O13
- - APP9-O14
- - APP9-O15
- - APP9-O16

#### Lessons

1. **Accepted prerequisites versus capstone outcomes** — Freeze authentic thirteen-course prior decisions and the **separate** accepted APP9-AS1–AS7 evidence map with actual revision/artifact references; avoid resubmitting or retesting all predecessor courses, or inventing past assessment decisions.

2. **Fresh local application, security and operational reproduction** — From a clean documented free fixture, exercise one complete protected React/API/Postgres/async workflow, forbidden direct HTTP and independently inspected restored data, referencing accepted AS3–AS5 traces rather than reproducing seven unrelated projects.

3. **Assessor-supplied unfamiliar bounded engineering challenge** — Accept a previously unseen role/field, stale UI, retry/concurrency, proxy/dependency or workload constraint from public outcomes. Predict a failure and construct independent before-fix evidence instead of delivering a memorized patch.

4. **Independent correction and regression protection** — Implement or causally diagnose the new issue, produce failing-before/passing-after observed user/HTTP/SQL evidence, and rerun relevant prior invariants, accessible paths, API compatibility and deployment effects without duplicating whole completed assessments.

5. **Authorship, evidence integrity and alternatives** — Defend personal work, third-party/license/AI assistance, actual versus synthetic research, security/privacy/accessibility, operational and cost choices and remaining uncertainty without fictional teamwork or inflated product validation.

6. **Accessible technical defense and final independent judgment** — Answer critical reviewer questions through live, written, recorded or equivalent accessible evidence under common public criteria; APP9-AS8 cannot excuse missing AS1–AS7 and an earlier course pass cannot substitute for new capstone performance.

## Completion requirements

### One coherent graduation product and required deliverables

The following describe **supporting project deliverables** for
the eight publicly defined assessments below; they are not
eight more independent summative gates or a demand for
a separate app for every previous course. Authentic completion
of all thirteen prerequisite courses is verified separately
before entry and remains necessary for APP graduation.

- **Product and inquiry:** bounded problem, attributed
  stakeholder/public-evidence task, hypothesis, ethical
  evaluation, user requirements, realistic scope and
  acceptance criteria for success and material failure.
- **Engineering design:** maintained context/component,
  state and data-flow diagrams; coherent architecture
  and alternatives/ADRs; domain and SQL model; trust,
  roles/permissions, privacy classification and
  retention/deletion limits; requirements-to-tests map.
- **Real integrated product:** accessible HTML/CSS,
  responsive React/TypeScript UI; actual Node/Fastify
  runtime input validation and authenticated API;
  PostgreSQL relational constraints and concurrency;
  meaningful user operation and justified async/external
  work with correct retry and reconciliation. Include
  file/cache mechanisms only where the chosen product
  needs them, with proportionate private access.
- **Quality and operation:** independent layered
  tests, accessibility and security negative cases,
  reproducible source/build and least-privilege CI,
  actual free local HTTPS deployment, meaningful
  release identity, controlled incident and recovery,
  real separate-target PostgreSQL restore and
  verifiable user/data correctness after restoration.
- **Evidence-based evolution:** representative workload,
  measurable resource/performance or fault constraint,
  comparison of alternatives including no-change,
  honest cost/operating analysis, tested change or
  justified decision, and versioned product learning.
- **Independent handoff:** clean-checkout build and
  synthetic setup, user help and operator runbook,
  source/reuse/collaboration attribution, assessment
  evidence, unresolved-risk register, retrospective,
  unfamiliar bounded requirement/fault and technical
  defense through an accessible reviewable medium.

A free local React, TypeScript, Node, Fastify and
PostgreSQL environment with synthetic users,
controlled worker/external fixture and scoped
test CA is sufficient. Paid hosting, public DNS,
unnecessary distributed infrastructure, electives,
proprietary grading or a mandatory participant
research panel are not required.

### Formative project milestones

The seven project-work stages below are **planning and feedback
checkpoints**, not additional mandatory evaluations.
Artifacts may contribute to a named required assessment
if they satisfy its published criteria. Iteration and
overlap are expected; alternative ordering is acceptable
if required outcomes and dependency safety are retained.

| Milestone | Suggested sequence | Reviewable progress | Related summative |
| --- | --- | --- | --- |
| M1 — Charter and inquiry | Early | Problem, evidence provenance, ethical scope, acceptance and risk | APP9-AS1 |
| M2 — Architecture and trust | Early–middle | System/data/identity design, alternatives, runtime contracts and test plan | APP9-AS2 |
| M3 — Protected vertical slice | Middle | Accessible React, typed API, genuine session/SQL and durable async state | APP9-AS3 |
| M4 — Quality and correction | Middle | Independent negative tests, deterministic CI, seeded fault and proven fix | APP9-AS4 |
| M5 — Operated release and recovery | Middle–late | Verified TLS, actual incident/recovery and separate PostgreSQL restore | APP9-AS5 |
| M6 — Measured evolution and product revision | Later | Representative capacity evidence, design/cost decision, responsible product evaluation and handoff | APP9-AS6, APP9-AS7 |
| M7 — Independent graduation defense | Final | Clean reproduction, unfamiliar bounded change, attribution and defense | APP9-AS8 |

### Required assessments and outcome coverage

All **sixteen APP9 outcomes** require **eight independently
decidable assessments** on one evolving product.
`APP9-AS1`–`APP9-AS7` inspect distinct inquiry, design,
implementation, quality, operations, evidence-based
architecture and responsible evaluation; `APP9-AS8`
assesses clean reproduction, **new unfamiliar transfer**
and technical defense. Previously accepted artifacts
may be referenced without resubmitting all earlier
work. A mapped outcome ID is not sufficient evidence.

| Assessment | Required outcome coverage | Principal evidence |
| --- | --- | --- |
| `APP9-AS1` — Problem Charter, Ethical Research and Feasible Scope | APP9-O1, APP9-O2, APP9-O3, APP9-O9, APP9-O15 | Product charter and provenance, research question/method/consent or secondary-source statement, documented actual observations or cited public evidence, scope/versioned requirements, acceptance and risk matrix, ethical data-handling plan and decision rationale |
| `APP9-AS2` — Architecture, Core Integration Plan and Threat Defense | APP9-O3, APP9-O4, APP9-O6, APP9-O7, APP9-O8, APP9-O9, APP9-O14, APP9-O15 | Architecture diagrams and request/failure sequences, API contracts, domain/relational and state models, authorization/data-retention matrix, threat/risk register, change/ADR alternatives and requirement-to-test/outcome traceability |
| `APP9-AS3` — Accessible, Secure, Durable Full-Stack Product | APP9-O3, APP9-O4, APP9-O5, APP9-O6, APP9-O7, APP9-O8, APP9-O9, APP9-O10 | Versioned product and local fixture source, browser/accessibility task traces, published runtime APIs and auth matrix, independent normal/negative HTTP tests, SQL schema/migrations and concurrent row checks, async state/replay simulation, observed errors/recovery and contribution attribution |
| `APP9-AS4` — Quality, Security, Privacy and Independent Corrective Test | APP9-O3, APP9-O5, APP9-O6, APP9-O7, APP9-O9, APP9-O10, APP9-O15 | Risk-and-layer test map, deterministic setup/teardown, CI YAML/local execution and toolchain/lockfile, real DB/API/security/browser tests, accessibility observation records, synthetic seeded defect and before/after transcript, review and residual-risk note |
| `APP9-AS5` — Operated Deployment, Release Incident and Restored State | APP9-O9, APP9-O10, APP9-O11, APP9-O12, APP9-O15 | Versioned deployment/proxy/config/runner, artifact digest/approvals and HTTPS verification, synthetic user/data, release/test logs and causal incident timeline, executed recovery/rollback, backup/restore commands, independent DB/HTTP tests, recovery numbers and operator runbook |
| `APP9-AS6` — Measured Architecture, Capacity and Operational Cost Decision | APP9-O1, APP9-O4, APP9-O7, APP9-O8, APP9-O12, APP9-O13, APP9-O14 | Workload scripts/data seeds and matched runs, tail/error/throughput resource and SQL traces, client capacity bias analysis, competing bottleneck hypotheses, source/architecture diff or no-change proof, security regression, ADR and transparent cost model |
| `APP9-AS7` — Product Evaluation, Revision and Responsible Handoff | APP9-O1, APP9-O2, APP9-O3, APP9-O5, APP9-O9, APP9-O14, APP9-O15 | Initial/final product assumption, consented anonymized or cited secondary evidence with methodology, findings and uncertainty, updated acceptance and decision record, bounded change and regression or no-change defense, privacy/user docs and retrospective |
| `APP9-AS8` — Independent Reproduction, Unfamiliar Change and Graduation Defense | APP9-O1, APP9-O2, APP9-O3, APP9-O4, APP9-O5, APP9-O6, APP9-O7, APP9-O8, APP9-O9, APP9-O10, APP9-O11, APP9-O12, APP9-O13, APP9-O14, APP9-O15, APP9-O16 | Single versioned source/product and complete outcome/evidence index, clean-run/fixture transcript, independent browser/API/PostgreSQL/security and deployed recovery traces, assessor's bounded scenario and source/test changes, product/architecture/cost decisions, evidence-limited reflections and accessible recorded/written/live defense |

### Project-wide ethics, independence and technical guardrails

- All source, application and learner-evidence
  claims must be accessible to a legitimate
  evaluator. Record precise project/OEE revision,
  code/toolchain version, risk-based assessment
  coverage, synthetic environment and privacy
  redactions. Avoid public release of actual
  user data or any secret.
- Research with humans requires voluntary
  consent, minimization and protected notes.
  Without participants, public secondary or
  heuristic/synthetic work is valid **when
  described accurately**; it cannot be
  portrayed as observed user behavior,
  representative adoption or a randomized
  usability study.
- Prior coursework, third-party packages,
  prebuilt templates and AI-assisted changes
  can be reused with attribution and
  demonstrable learner understanding. A
  meaningful independently designed new or
  revised protected user capability, design
  choice or operational behavior is required.
  No unmodified old coursework passes APP9.
- Use actual protected HTTP, real PostgreSQL,
  client-visible state and a deployed local
  service wherever claiming those properties.
  Browser UI hiding, mock authentication,
  static types, CORS, scripted success logs
  or a database diagram do not prove
  server authority, transactional safety or
  authentic recovery.
- Evaluate wrong-user/resource/field actions,
  invalid inputs, competing writes, session
  expiry, retries, inaccessible error states,
  asynchronous uncertainty, a failed
  dependency or release and repaired state.
  Tests and review oracles must be credible
  and independently inspectable; include
  actual negative DB and HTTP consequences.
- Actual local HTTPS must verify a
  correctly scoped test CA/hostname trust,
  not use an insecure bypass or claim
  public certificate authority acceptance.
  Release approvals, secrets and trusted
  artifact identity remain independent
  controls; don't expose credentials in
  source/static assets/images/CI artifacts.
- Real backups require independent
  restore into an explicitly disposable
  database with integrity/permission
  checks. Distinguish measured local RPO
  and RTO from production targets or
  complete backup of files and jobs.
- Workload reports require a declared
  environment, traffic/data mix, generator
  limitations, samples, errors/timeouts
  and appropriate tail measurements.
  Financial and performance statements
  disclose assumptions and uncertainty.
  A simple modular-monolith solution
  may correctly outperform an unjustified
  distributed design in engineering value.
- Perform all security, load and fault
  exercises on owned localhost/isolated
  synthetic resources only. Do not
  scan external systems, use real
  personal information or destroy
  shared databases as project evidence.
- A reviewer may select an unfamiliar
  but **bounded publicly defined**
  fault or change within listed outcomes.
  This must not impose a paid platform,
  specific private stack, surprise
  elective language or hidden grading
  criterion. An accessible written,
  recorded, live or equivalent defense
  must satisfy identical decision rules.
- Solo project work is legitimate and
  reviewable. A synthetic team scenario
  is **not evidence of collaboration**;
  real teamwork, code review and source
  attribution should be described only
  if actually experienced.

### Core capability-to-APP9 evidence mapping

This is an *explanatory integration map*,
not an extra independent assessment, a proof
of the earlier course-completion decisions or a
substitute for observing new APP9 outcomes.
A topic not naturally implemented in this specific
product retains its earlier independently assessed
prerequisite evidence; unnecessary feature insertion
is not a graduation requirement.

| Core course | Integrated capstone evidence |
| --- | --- |
| APP1 — Internet/Web | Real HTTP/origin/TLS behavior in APP9-AS2, APP9-AS3, APP9-AS5 |
| APP17 — HTML/CSS | Semantic responsive interface and keyboard/focus/error evidence in APP9-AS3, APP9-AS4 |
| APP18 — JavaScript | Correct browser/Node runtime behavior and async reasoning in APP9-AS3, APP9-AS8 |
| APP19 — TypeScript | Typed source and runtime validation boundaries in APP9-AS2, APP9-AS3 |
| APP21 — Node.js | Backend process, async runtime and bounded work in APP9-AS3, APP9-AS5 |
| APP2 — Browser/frontend | Network, navigation, client state and inclusive UI in APP9-AS3, APP9-AS4 |
| APP20 — React | Components, server state, forms and accessible failure modes in APP9-AS3, APP9-AS4 |
| APP4 — Data/SQL | Relational constraints, concurrent transactions, schema and restore in APP9-AS3, APP9-AS5 |
| APP3 — Backend framework | Fastify HTTP contract, runtime schemas and server-held authorization in APP9-AS2, APP9-AS3 |
| APP5 — Full-stack integration | Protected journey, durable async state and partial failure in APP9-AS3, APP9-AS8 |
| APP6 — Engineering quality | Testing, CI, signals, security/performance evidence in APP9-AS4–APP9-AS6 |
| APP7 — Deployment | Verified local operation, controlled release, data restoration in APP9-AS5 |
| APP8 — Production architecture | Bottleneck, measured alternative, correctness and cost decisions in APP9-AS6 |

### Required summative assessment details

- **APP9-AS1** (required problem charter, ethical research and feasible scope)
  - Outcomes: APP9-O1, APP9-O2, APP9-O3, APP9-O9, APP9-O15
  - Work: Independently choose one testable application problem, relevant actors and constraints, define an ethically appropriate stakeholder/user-task question and record a bounded acceptance/failure plan. Evaluate one consequential initial assumption using consented low-risk participant feedback when available, or clearly sourced public secondary evidence plus a labeled heuristic/synthetic task evaluation otherwise. Document a decision about requirements, risks and scope without inventing interviews, observed demand or demographic reach.
  - Criteria: The task and success/failure outcomes are concrete and feasible; actual, sourced and simulated evidence are never conflated. Real participants require voluntary informed consent, minimal records, controlled retention and no sensitive credential/data collection. At least one assumption is falsifiable and connected to a justified decision. Prioritized user journeys include important invalid/forbidden/conflict/recovery cases and acknowledge which users and claims remain unverified.
  - Evidence: Product charter and provenance, research question/method/consent or secondary-source statement, documented actual observations or cited public evidence, scope/versioned requirements, acceptance and risk matrix, ethical data-handling plan and decision rationale.

- **APP9-AS2** (required architecture, core integration plan and threat defense)
  - Outcomes: APP9-O3, APP9-O4, APP9-O6, APP9-O7, APP9-O8, APP9-O9, APP9-O14, APP9-O15
  - Work: Design a specific browser/React/TypeScript, Node/Fastify, PostgreSQL and deployed system with a meaningful protected user workflow and appropriate asynchronous/external work boundary. Draw context/component/sequence/data-flow views; publish independently inspectable HTTP/runtime/API, state, role/tenant/field, SQL/concurrency and privacy/retention contracts. Compare at least two realistic architecture alternatives with security, resource, operational and future-change implications and trace critical requirements to code and tests.
  - Criteria: The design maps accurately to the actual feasible application and places identity/access and authoritative persistence at server/DB boundaries; UI hiding, CORS, compile-time types and mocks are not security or transaction guarantees. It distinguishes DB commits from remote side effects and client pending from durable facts, includes real API/browser/SQL responsibilities and names known failure modes. The alternatives and ADRs explain proportionality, risks and why unneeded distribution or paid services are excluded; each critical requirement has assessable evidence.
  - Evidence: Architecture diagrams and request/failure sequences, API contracts, domain/relational and state models, authorization/data-retention matrix, threat/risk register, change/ADR alternatives and requirement-to-test/outcome traceability.

- **APP9-AS3** (required accessible, secure, durable full-stack product)
  - Outcomes: APP9-O3, APP9-O4, APP9-O5, APP9-O6, APP9-O7, APP9-O8, APP9-O9, APP9-O10
  - Work: Build a **substantive capstone-owned** protected user capability with accessible responsive React, actual trusted-session and runtime-validated Fastify/TypeScript and real PostgreSQL constraints. Use independent direct HTTP and SQL tests for object, action, readable/writable property and tenant authorization; coordinate real two-client writes and a lost-after-commit/duplicate replay without repeating effects. Include a justified durable local job/external fixture and observable completed/accepted/failed/recovered states with old-user responses safely discarded. Cache or file workflows are necessary only where the product uses them.
  - Criteria: The same authentic user task works in the real browser, service and committed database and has **independent** normal/forbidden/conflict/replay evidence. Forged or revoked identities cannot read or mutate restricted objects/properties/tenant rows; actual DB facts survive two-client races and duplicate/lost responses without duplicate protected effects. UI focus/keyboard/status and late-identity behavior are meaningfully observed; TypeScript types, mock sessions and hidden controls cannot establish server security. The learner explains and attributes personal, reused and AI-assisted contributions.
  - Evidence: Versioned product and local fixture source, browser/accessibility task traces, published runtime APIs and auth matrix, independent normal/negative HTTP tests, SQL schema/migrations and concurrent row checks, async state/replay simulation, observed errors/recovery and contribution attribution.

- **APP9-AS4** (required quality, security, privacy and independent corrective test)
  - Outcomes: APP9-O3, APP9-O5, APP9-O6, APP9-O7, APP9-O9, APP9-O10, APP9-O15
  - Work: Publish a risk-based plan and implement unit/domain, UI/component, independent HTTP+real-DB, consumer contract, browser end-to-end and appropriate failure tests for the actual product. Demonstrate deterministic fixtures, accessible keyboard/focus/error checks, real server-side authorization, log/secret redaction and justified data retention/deletion. Use a versioned least-privilege CI plus free local equivalent and show a deliberately seeded security, accessibility, input/state or contract defect that fails an appropriate test before a reviewed repair.
  - Criteria: The selected tests are proportional and their limitations disclosed; real PostgreSQL and independent HTTP evidence support data/security claims instead of mocks alone. A material seeded defect demonstrably fails then passes only after a meaningful fix, preserving important negative tests. Access, privacy and data lifecycle are verified to actual scope including backup retention limitations. CI gates fail closed for tested defects, use reproducible toolchain and do not expose credentials to untrusted code; unsupported security/WCAG certification is never claimed.
  - Evidence: Risk-and-layer test map, deterministic setup/teardown, CI YAML/local execution and toolchain/lockfile, real DB/API/security/browser tests, accessibility observation records, synthetic seeded defect and before/after transcript, review and residual-risk note.

- **APP9-AS5** (required operated deployment, release incident and restored state)
  - Outcomes: APP9-O9, APP9-O10, APP9-O11, APP9-O12, APP9-O15
  - Work: Operate the actual APP7-compatible product under a free local named-host HTTPS configuration with verified CA/hostname (no insecure bypass), inspectable source/image digest and protected synthetic secrets/data. Trigger and diagnose a real running-service release/proxy/dependency fault, verify affected protected user/forbidden paths and committed job/data effects, then execute a justified rollback or forward repair. Create a real populated PostgreSQL logical backup and restore into **a separate named clean target**, account for cluster-global role/privilege dependencies outside a single-database dump, inspect restored allowed/denied business tasks and measure local recovery point/time and missing file/worker effects.
  - Criteria: An independent evaluator can reproduce real local HTTPS validation, artifact identity, access isolation and an observed failed-then-repaired protected task. Safe rollback never claims to undo committed DB or external effects. The restored distinct PostgreSQL target has independently verified schema, role/tenant permissions and actual business data; an archive/checksum without restoration is insufficient. RPO/RTO observations are explicitly local and limited, not global service uptime, full file/worker restoration or WAL point-in-time recovery.
  - Evidence: Versioned deployment/proxy/config/runner, artifact digest/approvals and HTTPS verification, synthetic user/data, release/test logs and causal incident timeline, executed recovery/rollback, backup/restore commands, independent DB/HTTP tests, recovery numbers and operator runbook.

- **APP9-AS6** (required measured architecture, capacity and operational cost decision)
  - Outcomes: APP9-O1, APP9-O4, APP9-O7, APP9-O8, APP9-O12, APP9-O13, APP9-O14
  - Work: Identify one credible growth, latency, overload or reliability constraint on the running product and state a falsifiable architecture hypothesis. Execute a bounded reproducible workload with declared arrivals, tenant/task mix, seed data, client-generator capacity, sample counts, warm/cold behavior and actual success/error/timeouts. Diagnose one real bottleneck with service/DB/worker evidence; compare at least two interventions including a simpler baseline, implement a justified change or rigorously defend no change, retest security/data correctness and calculate illustrative compute/storage/egress/operations and maintenance sensitivity.
  - Criteria: Observations include meaningful tail metrics, throughput/errors and resource/DB effects, clearly explaining coordinated omission, small samples, workload mismatch and other uncertainty. Any actual change improves or preserves stated user-task/operational goals without violating authorization, data consistency, failure transparency or accessible states. Alternatives have comparable assumptions; a measured lack of reason to add complexity can pass. Financial model has units, assumptions and sensitivity but is not presented as a verified cloud quote or proof of production capacity.
  - Evidence: Workload scripts/data seeds and matched runs, tail/error/throughput resource and SQL traces, client capacity bias analysis, competing bottleneck hypotheses, source/architecture diff or no-change proof, security regression, ADR and transparent cost model.

- **APP9-AS7** (required product evaluation, revision and responsible handoff)
  - Outcomes: APP9-O1, APP9-O2, APP9-O3, APP9-O5, APP9-O9, APP9-O14, APP9-O15
  - Work: On the working product, revisit the original user-task hypothesis using genuinely consented low-risk observations where available or attributed public/secondary evidence and a **clearly synthetic** heuristic evaluation otherwise. Evaluate competing interpretations, make a meaningful requirement/UX/privacy/priority revision or defend no change/defer with evidence, and update task acceptance, relevant tests, privacy/retention, user/operator documentation, dependencies/license/AI-assistance provenance and a factual retrospective. Do not fabricate interviews, team reviews or user adoption.
  - Criteria: A real inspectable initial-to-final decision follows appropriately scoped, consented/cited/simulated evidence with limits and cannot present synthetic users as real participants. Implemented changes receive relevant accessible and tenant-policy regression; a documented justified no-change retains an honest testable consequence. Source authorship, reuse, collaboration, licensing and unresolved public-release rights are accurately disclosed; appearance and assumed demand alone do not pass.
  - Evidence: Initial/final product assumption, consented anonymized or cited secondary evidence with methodology, findings and uncertainty, updated acceptance and decision record, bounded change and regression or no-change defense, privacy/user docs, applicable source/dependency license and assistance attribution, material release-rights uncertainties and retrospective.

- **APP9-AS8** (required independent reproduction, unfamiliar change and graduation defense)
  - Outcomes: APP9-O1, APP9-O2, APP9-O3, APP9-O4, APP9-O5, APP9-O6, APP9-O7, APP9-O8, APP9-O9, APP9-O10, APP9-O11, APP9-O12, APP9-O13, APP9-O14, APP9-O15, APP9-O16
  - Work: Verify **thirteen authentic predecessor-course completion decisions**, linked to the actual assessed revisions or governed equivalent evidence, independently of APP9-AS1–AS7. Inspect **one** clean locally reproduced product, reference prior accepted AS1–AS7 rather than rebuild seven systems, and check relevant real React/API/PostgreSQL/async protected and forbidden paths, verified HTTPS/recovery and measured design choices. An assessor supplies a **previously unseen bounded** role/field, stale client, state/concurrency, replay, dependency, deployment or workload challenge from published outcomes. The learner predicts what can fail, establishes an independent before-fix oracle, implements or causally diagnoses and corrects it, runs meaningful regression and defends authorship, genuine/synthetic research, reused/AI-assisted work, alternatives and limits accessibly.
  - Criteria: All thirteen entry decisions must be independently genuine and revision linked; missing or unassessed prerequisites prevent entry/graduation. **All APP9-AS1–AS7 must already have passing decisions; AS8 cannot excuse any failed assessment or count a past course result as a new APP9 outcome.** The unfamiliar challenge must not be pre-rehearsed or secretly require an elective/paid service and must have independently reproducible failing-before/passing-after observations preserving protected data, accessible user behavior, compatible API and durable state. The learner can explain personally owned implementation and disclose AI/reused material and licenses. Written, recorded, synchronous or equivalent accessible defenses follow the **same published criteria**.
  - Evidence: Revision-linked authentic thirteen-course entry decisions, a **separate references-first APP9-AS1–AS7 acceptance/evidence index**, one attributed versioned source and clean local fixture, independent browser/HTTP/PostgreSQL and operational recovery observations, assessor's unseen prompt and before/after source/test evidence, measured/synthetic scope limitations and accessible technical defense.

### Graduation decision, evaluation revision and handoff

**APP9 is the core Application Engineering graduation
project.** Admission and graduation first require authentic
assessed completion decisions for all thirteen direct core
prerequisites (or governed outcome-equivalent assessments).
Award APP9 completion only after an evaluator
records an acceptable decision for each
`APP9-AS1` through `APP9-AS8`, observes
the stated integrated deliverables, verifies
that `APP9-O1` through `APP9-O16`
are substantively demonstrated, and
evaluates the learner's independently
defensible technical work. An attractive
presentation cannot compensate for
a substantive authorization/privacy
failure, inaccessible user task, invalid
database state, unverified deployment
recovery, untraceable research evidence,
missing clean-state reproduction or an
inadequate technical defense.

Evidence records identify specification
and source/course revision, assessment/
outcome IDs, artifact location, actual
observations, relevant environment,
protected information, evaluator
decision and stated limitations under
[OEE Evidence Rules](../../spec/evidence-rules.md).

APP9 remains the core OEE `v0.2.0` **draft**
`project`, preserving its name, classification,
full list of thirteen prior core course links
and eight independent summative judgments.
The earlier legacy checkpoint migration and
optional APP10–APP16 curricula are already
reflected in the published catalog. This source
review does not promote APP9 to `tested` or
`verified`, reassess earlier completions, impose
new electives or automatically update OEE Workspace,
content or 0xNAND source/evidence pins.

The source course remains `draft`
after green structural CI. Learner
`tested`, `verified` and educational
conformance claims require actual
independent evidence and the formal
status governance; a software pass
alone does not establish those claims.

### Public optional reference material

- [OEE Course Format](../../spec/course-format.md)
  and [OEE Evidence Rules](../../spec/evidence-rules.md)
  define public project and evidence requirements.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
  and [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/)
  inform accessibility checks, not unearned compliance claims.
- [OWASP API Security](https://owasp.org/projects/api-security-project)
  and [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
  inform synthetic negative threat verification.
- [OpenAPI](https://spec.openapis.org/oas/latest.html)
  and [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html)
  inform service contracts and HTTP semantics.
- [PostgreSQL documentation](https://www.postgresql.org/docs/current/)
  supports transaction, concurrency and actual restore exercises.
- [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
  informs evidence-limited reliability and operational decisions.
