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

The modules below are **cumulative project work stages**, not a second sequence of lectures that reteaches APP1–APP8 or APP17–APP21. Review the named learning outcomes and corresponding `APP9-AS1`–`APP9-AS8` requirements as the product evolves. Small checks and critique are formative unless explicitly cited as required assessment evidence. Retain useful work across stages rather than rebuilding the same product.

### Module 1 — Charter, Ethical Inquiry and Feasible Scope

#### Outcomes

- APP9-O1
- APP9-O2
- APP9-O3
- APP9-O9
- APP9-O15

#### Lessons

1. **Prior learning, admission evidence and authorship** — Verify all thirteen prerequisite course-completion decisions with authentic revisions and assessed evidence (or approved equivalence), stopping if a prerequisite remains unverified. Then distinguish prior artifacts worth reusing from the new product change the learner must independently design, implement and defend.

2. **Real problem and affected people** — Describe a specific user task, stakeholder constraints and credible provenance; distinguish a supplied brief from observed demand and state whose interests and data are at risk.

3. **Responsible product inquiry** — Choose a falsifiable product assumption and a consented, secondary or explicitly synthetic evaluation method; define risks, sampling limits and what evidence cannot support.

4. **Interpreting imperfect evidence** — Analyze findings or a public/synthetic case without claiming real user trials; identify alternatives and record a defensible scope or interaction decision.

5. **Acceptance and failure contracts** — Express prioritized end-to-end user outcomes, authorization/tenant invariants, accessibility and privacy obligations, recovery behavior and measurable acceptance tests.

6. **Constraints, exclusions and milestones** — Bound the smallest coherent product, plan its dependency-aware development, and record unimplemented features and assumptions rather than concealing them.

7. **Critique and revise the charter** — Expose the charter to a counterexample or independent review, revise a weak assumption, and preserve the reasoned decision; this is formative unless the published assessment evaluates the result.

### Module 2 — Architecture, Trust and Reproducible Design

#### Outcomes

- APP9-O3
- APP9-O4
- APP9-O6
- APP9-O7
- APP9-O8
- APP9-O9
- APP9-O14
- APP9-O15

#### Lessons

1. **One product and its boundaries** — Draw context and component views for browser, typed React client, Node/Fastify service, PostgreSQL and any genuinely required worker or external fixture; justify a modular monolith where sufficient.

2. **User, system and failure sequences** — Trace a protected task from client intent through API and authoritative data changes to UI confirmation, denied access, timeout and recovery; distinguish local feedback from a committed result.

3. **Identity, authorization and privacy** — Specify roles, object/field/tenant authority, session trust, retention/deletion and sensitive-data flow at each cross-process or cache boundary.

4. **Data model and concurrency contract** — Define entities, keys, relational constraints, transactions, query assumptions and schema compatibility, including two conflicting writers and durable outcomes.

5. **Contract and asynchronous boundaries** — Specify runtime validation, HTTP status/error semantics, replay safety, background intent, status visibility and client reconciliation without promising exactly-once side effects.

6. **Architecture alternatives, review and evidence** — Compare at least two credible designs against correctness, accessibility, risk, operations and cost; map requirements to independent tests, then review a supplied counterexample or trust flaw and correct the choice before implementing.

### Module 3 — Implement the Protected Application Journey

#### Outcomes

- APP9-O4
- APP9-O5
- APP9-O6
- APP9-O7
- APP9-O8
- APP9-O9

#### Lessons

1. **Semantic and accessible client skeleton** — Implement responsive HTML/CSS, meaningful navigation, forms, focus and named controls for the selected task; verify keyboard and failure-state access rather than repeating basic HTML instruction.

2. **React state and network lifecycle** — Integrate typed components, navigation, session continuity, validated Fetch responses and explicit pending, empty, invalid, expired, forbidden, conflict and failed states.

3. **Typed backend and authoritative authorization** — Build real Fastify routes, runtime schema checks and protected sessions; show direct HTTP requests cannot bypass role, tenant, object or field policy.

4. **Relational schema and durable integrity** — Implement a PostgreSQL schema and versioned migrations with keys and constraints for the product's actual user task; inspect invalid-input rejection and authoritative persisted state using an independent SQL oracle.

5. **Transactional concurrency and replay** — Implement bounded transaction and revision controls; exercise two conflicting writers, duplicate submissions and an uncertain response while checking committed state and invariant preservation.

6. **Durable asynchronous or external effect** — Implement a justified bounded worker or controlled external fixture with persisted intent, replay limits and truthful status; make lost-response recovery and identity scope observable.

7. **Privacy-safe auxiliary resources** — Use caching or file workflows only when necessary for the product; demonstrate appropriate authorization, retention and invalidation without making unrelated features graduation requirements.

8. **Integrative failure walkthrough** — Trace the same user action through successful, denied, stale, racing and partially failed conditions; repair incorrect UI claims and preserve state invariants.

### Module 4 — Independent Quality, Security and Corrective Evidence

#### Outcomes

- APP9-O5
- APP9-O6
- APP9-O7
- APP9-O8
- APP9-O9
- APP9-O10
- APP9-O15

#### Lessons

1. **Risk-led verification plan** — Translate the actual product risks into domain, browser, API, database, contract, accessibility and deployment checks; avoid a test-count quota and independent-oracle circularity.

2. **Authorization and data-integrity attacks** — Attempt invalid, cross-tenant, cross-role, replayed and concurrent actions through direct client and HTTP paths; inspect both response and authoritative database state.

3. **Browser, accessibility and privacy inspection** — Test keyboard, focus, feedback and reduced-motion/zoom scenarios appropriate to the user task; audit sensitive DOM, logging, storage and data exposure.

4. **Deterministic execution and fault controls** — Use declared fixtures, seeds, controlled time, process and network faults, isolated databases and teardown to make failure claims reproducible.

5. **Secure build and CI decisions** — Publish reproducible build steps, dependency review, scoped CI privileges and meaningful fail-closed tests; document where the free local equivalent differs from a hosted provider.

6. **Seeded defect, correction and review** — Introduce a material regression, reproduce it using an independent failing check or causal trace, implement a correction, verify that security and integrity checks still hold, and produce an attributed, maintainer-reviewable change explanation with remaining limitations.

### Module 5 — Release, Observe and Recover the Same Product

#### Outcomes

- APP9-O9
- APP9-O10
- APP9-O11
- APP9-O12
- APP9-O15

#### Lessons

1. **Reproducible operational package** — Start the same full-stack system from versioned source and isolated synthetic data; identify immutable artifact versions, startup/shutdown health and service boundaries.

2. **Verified HTTPS and secret isolation** — Demonstrate local certificate/hostname verification, trusted proxy headers, runtime configuration isolation and denied unauthorized environmental access.

3. **Compatible application and database release** — Stage old/new client, service and schema combinations; justify rollback versus forward repair for a persistent change and retain the tested artifact identity.

4. **Signals for user-visible service health** — Collect privacy-safe request, data and release observations that distinguish green process health from a broken protected user journey.

5. **Controlled incident and restored service** — Inject a bounded failed release or dependency, diagnose impact, contain it and verify user-task recovery using before/after facts.

6. **Actual PostgreSQL recovery** — Back up real test data, restore into a separate clean instance and check relations, authorization, outstanding work and defensible recovery point/time; a backup command without restoration is insufficient.

7. **Operational handoff and limitations** — Publish clear setup, monitoring, release/recovery and shutdown instructions, unsafe assumptions and what the local exercise does not establish about public-cloud production.

### Module 6 — Measured Evolution, Product Revision and Economics

#### Outcomes

- APP9-O1
- APP9-O2
- APP9-O3
- APP9-O4
- APP9-O12
- APP9-O13
- APP9-O14
- APP9-O15

#### Lessons

1. **Return to the original product hypothesis** — Compare the promised user task with ethical observations, credible secondary evidence or a labeled synthetic evaluation; state uncertainty before deciding to change the interface.

2. **Capacity and correctness hypothesis** — Choose a measured latency, resource, saturation, or failure claim tied to a real task, protected data and an operational constraint rather than benchmark theater.

3. **Representative workload and bias** — Record task/tenant mix, data scale, warm-up, request arrival, environment, trials and generator limits; distinguish throughput, tail latency, failures and unmeasured effects.

4. **Locate the causal bottleneck** — Correlate browser/API/Node/SQL and dependency observations; challenge simplistic averages, coincidental correlations and unvalidated optimization claims.

5. **Compare at least two credible decisions** — Evaluate remove-work/no-change, caching/queue/concurrency or appropriate architectural alternatives against correctness, privacy, availability, cost and maintenance burden.

6. **Implement or defensibly reject a change** — Apply one bounded improvement when supported, otherwise preserve the simpler design with evidence; rerun a matched negative and protected-journey check.

7. **Revise, document and hand off** — Revisit acceptance, user guidance, costs, energy/operational implications and original assumptions; identify bias, limitations, unsatisfied requests and next safe iteration.

### Module 7 — Independent Reproduction, Unfamiliar Change and Defense

#### Outcomes

- APP9-O1
- APP9-O2
- APP9-O3
- APP9-O4
- APP9-O5
- APP9-O6
- APP9-O7
- APP9-O8
- APP9-O9
- APP9-O10
- APP9-O11
- APP9-O12
- APP9-O13
- APP9-O14
- APP9-O15
- APP9-O16

#### Lessons

1. **Freeze and index reviewable evidence** — Link every required assessment to the actual versioned artifact, evaluated outcomes, source authorship, relevant tests and decisions; do not duplicate submissions without new evidence.

2. **Clean-state product reproduction** — Recreate the entire protected service and synthetic database from a clean checkout with publicly understandable commands and inspectable failure responses.

3. **One authentic end-to-end demonstration** — Exercise accessible client navigation, validated API, server-held permissions, concurrent persistence, async uncertainty and data lifecycle for the same user task.

4. **Independent safety and correctness challenge** — Respond to a direct HTTP, race, replay, identity-switch or privacy scenario and verify the authoritative state using evidence independent of the implementation.

5. **Operational fault and real restoration** — Reproduce an injected release/dependency incident and independently confirm recovery of actual PostgreSQL data and the protected user journey.

6. **Performance and product decisions** — Defend the measured workload, comparative architecture and product evaluation findings without claiming measured effects or stakeholder experience that never occurred.

7. **Unfamiliar bounded change** — Accept a previously unseen requirement or failure within the published core scope; implement or correctly diagnose it, demonstrate the change and protect critical invariants.

8. **Attribution, limits and future obligations** — Explain personal work, reused material, assistance, consent, licensing, unresolved defects, accessibility accommodations and why the release is or is not fit for its defined purpose.

9. **Accessible technical defense** — Provide an inspectable live, recorded, written or equivalent defense of actual reasoning, causal observations, alternatives and limits; satisfy each public assessment criterion, not a presentation-style quota.

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

**All sixteen APP9 outcomes** must be independently
demonstrated across **APP9-AS1–APP9-AS8**.
A reference in this table identifies evaluation
responsibility; actual criteria and inspected
evidence, not an ID or checkbox, determine mastery.

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
  - Work: Implement a substantive independently contributed product slice linking semantic responsive React through runtime-validated authenticated Fastify/TypeScript services into real PostgreSQL state and an appropriately scoped asynchronous/local simulated external operation. Demonstrate functional roles, tenant/resource/field-level denial, actual valid/invalid client handling, competing write conflict, one transactional invariant, session expiry, duplicate/lost-response replay and meaningful loading/pending/failed/recovered user feedback. An independent client and SQL query must verify security/state claims.
  - Criteria: The meaningful user task works through actual accessible UI, typed service and committed DB, while direct forbidden HTTP calls cannot read or mutate another user's/tenant's objects or fields. Concurrent requests do not violate modeled invariants, duplicate retry does not repeat a protected side effect and external/async uncertainty is not mislabeled success. Browser focus, keyboard and status/error behavior are tested as actually supported; TypeScript does not substitute for runtime parsing. Clearly documented new learner-owned contributions and attributed reuse are necessary.
  - Evidence: Versioned product and local fixture source, browser/accessibility task traces, published runtime APIs and auth matrix, independent normal/negative HTTP tests, SQL schema/migrations and concurrent row checks, async state/replay simulation, observed errors/recovery and contribution attribution.

- **APP9-AS4** (required quality, security, privacy and independent corrective test)
  - Outcomes: APP9-O3, APP9-O5, APP9-O6, APP9-O7, APP9-O9, APP9-O10, APP9-O15
  - Work: Publish a risk-based plan and implement unit/domain, UI/component, independent HTTP+real-DB, consumer contract, browser end-to-end and appropriate failure tests for the actual product. Demonstrate deterministic fixtures, accessible keyboard/focus/error checks, real server-side authorization, log/secret redaction and justified data retention/deletion. Use a versioned least-privilege CI plus free local equivalent and show a deliberately seeded security, accessibility, input/state or contract defect that fails an appropriate test before a reviewed repair.
  - Criteria: The selected tests are proportional and their limitations disclosed; real PostgreSQL and independent HTTP evidence support data/security claims instead of mocks alone. A material seeded defect demonstrably fails then passes only after a meaningful fix, preserving important negative tests. Access, privacy and data lifecycle are verified to actual scope including backup retention limitations. CI gates fail closed for tested defects, use reproducible toolchain and do not expose credentials to untrusted code; unsupported security/WCAG certification is never claimed.
  - Evidence: Risk-and-layer test map, deterministic setup/teardown, CI YAML/local execution and toolchain/lockfile, real DB/API/security/browser tests, accessibility observation records, synthetic seeded defect and before/after transcript, review and residual-risk note.

- **APP9-AS5** (required operated deployment, release incident and restored state)
  - Outcomes: APP9-O9, APP9-O10, APP9-O11, APP9-O12, APP9-O15
  - Work: Deploy the product using free pre-provisionable local APP7-compatible tooling with an inspectable artifact identity, isolated config/DB, verified locally trusted HTTPS, appropriately scoped secrets and quality-to-release approval. Trigger a real controlled bad release or local dependency failure, observe a protected user task and sanitized operating signals, then carry out an actual rollback or safe forward repair with verified DB/job state. Create a real consistent PostgreSQL backup and restore into a separately named disposable database, testing authorization and a complete user task, recording observed recovery point/time and non-DB gaps.
  - Criteria: A reviewer can reproduce the running deployment and TLS name/CA verification without an insecure bypass or paid account. Artifacts, secrets, release role and DB targets are protected and inspectable. The seeded failure is observable in a running system and mitigation actually restores appropriate user behavior without assuming code rollback reverses committed data. The backup is truly restorable into an isolated target with business invariants intact; measured local RPO/RTO is distinguished from hypothetical production assurance and missing private file/worker state is identified.
  - Evidence: Versioned deployment/proxy/config/runner, artifact digest/approvals and HTTPS verification, synthetic user/data, release/test logs and causal incident timeline, executed recovery/rollback, backup/restore commands, independent DB/HTTP tests, recovery numbers and operator runbook.

- **APP9-AS6** (required measured architecture, capacity and operational cost decision)
  - Outcomes: APP9-O1, APP9-O4, APP9-O7, APP9-O8, APP9-O12, APP9-O13, APP9-O14
  - Work: Identify one credible growth, latency, overload or reliability constraint on the running product and state a falsifiable architecture hypothesis. Execute a bounded reproducible workload with declared arrivals, tenant/task mix, seed data, client-generator capacity, sample counts, warm/cold behavior and actual success/error/timeouts. Diagnose one real bottleneck with service/DB/worker evidence; compare at least two interventions including a simpler baseline, implement a justified change or rigorously defend no change, retest security/data correctness and calculate illustrative compute/storage/egress/operations and maintenance sensitivity.
  - Criteria: Observations include meaningful tail metrics, throughput/errors and resource/DB effects, clearly explaining coordinated omission, small samples, workload mismatch and other uncertainty. Any actual change improves or preserves stated user-task/operational goals without violating authorization, data consistency, failure transparency or accessible states. Alternatives have comparable assumptions; a measured lack of reason to add complexity can pass. Financial model has units, assumptions and sensitivity but is not presented as a verified cloud quote or proof of production capacity.
  - Evidence: Workload scripts/data seeds and matched runs, tail/error/throughput resource and SQL traces, client capacity bias analysis, competing bottleneck hypotheses, source/architecture diff or no-change proof, security regression, ADR and transparent cost model.

- **APP9-AS7** (required product evaluation, revision and responsible handoff)
  - Outcomes: APP9-O1, APP9-O2, APP9-O3, APP9-O5, APP9-O9, APP9-O14, APP9-O15
  - Work: Revisit a consequential product assumption on the now functional application through consented low-risk user/stakeholder task review where possible or attributable public/secondary evidence and an honestly labeled structured heuristic evaluation otherwise. Describe actual results and selection bias, update a substantive product requirement/UX behavior/privacy policy or justify explicitly retaining scope, test any change and revise clear user/operator documentation, retained-data rules, known limitations and a factual engineering retrospective.
  - Criteria: A traceable initial assumption, suitable method and real source observations support a responsible decision; fabricated interviews, unconsented participant data and synthetic feedback presented as real are unacceptable. At least one meaningful acceptance/priority/design decision is reviewed and either implemented/tested or transparently deferred with justification. Relevant accessibility, role/privacy and regression checks are preserved. Collaboration, authorship and project handoff reflect what actually happened, not simulated teamwork.
  - Evidence: Initial/final product assumption, consented anonymized or cited secondary evidence with methodology, findings and uncertainty, updated acceptance and decision record, bounded change and regression or no-change defense, privacy/user docs, applicable source/dependency license and assistance attribution, material release-rights uncertainties and retrospective.

- **APP9-AS8** (required independent reproduction, unfamiliar change and graduation defense)
  - Outcomes: APP9-O1, APP9-O2, APP9-O3, APP9-O4, APP9-O5, APP9-O6, APP9-O7, APP9-O8, APP9-O9, APP9-O10, APP9-O11, APP9-O12, APP9-O13, APP9-O14, APP9-O15, APP9-O16
  - Work: Confirm the pre-entry register of thirteen authentic predecessor-course completion decisions or governed equivalence evidence, without re-assessing those courses. Present a single independently reproducible final product and reference all qualifying APP9-AS1–AS7 artifacts. An assessor or independently documented clean-state procedure must install and run free local dependencies, exercise protected browser/API/SQL/async behavior, verify security negative tests, a faulty deployed release and actual restored database, and inspect reasoned product and architecture choices. Then introduce an **unfamiliar bounded** new authorized field/role, API contract variant, stale-state bug, deployment failure, workload constraint or dependency fault within published outcomes. Implement or correctly diagnose it, show an appropriate failing-before/passing-after test or equivalent causal evidence, and defend authorship, source reuse, design choices, uncertainties and remaining risks in an accessible format.
  - Criteria: All thirteen predecessor-course completion decisions are revision-linked and authentic; missing or unassessed prerequisite evidence blocks APP9 entry/graduation rather than receiving automatic capstone credit. The software, deployment and evidence can be independently examined without hidden environment state, undocumented manual intervention or required paid services. All eight required APP9 assessment decisions and every actual APP9 outcome have credible observable evidence; an evaluator does not grant credit merely because a course was previously passed or an outcome ID is listed. The unfamiliar scenario preserves protected data, meaningful user experience, old/new contract and rollback safety, and the learner can explain personally contributed code/decisions and attribution. The challenge stays within public outcome classes, feasible local tools and equivalent accessible written/recorded/live defense criteria.
  - Evidence: Revision-linked thirteen-course pre-entry completion index with safe references to actual assessed decisions, a separate APP9 outcome/evidence index, single versioned source/product, clean-run/fixture transcript, independent browser/API/PostgreSQL/security and deployed recovery traces, assessor's bounded scenario and source/test changes, product/architecture/cost decisions, evidence-limited reflections and accessible recorded/written/live defense.

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

APP9 preserves its course code, title,
`project` type, core classification
and full 13-preceding-core direct
prerequisite list. It replaces
the legacy completion checkpoint and
final integration lab with an outcome-
driven OEE `v0.2.0` **draft** project.
Historical learners and evidence remain
pinned to their prior assessed course
revision; no newly authored outcome
may silently mark earlier learners
complete or incomplete. APP10–APP16
remain optional and now publish their
own outcome-driven `v0.2.0` drafts.
OEE Workspace, content/resource mappings
and 0xNAND course-consumer evidence pins
still require separate reviewed alignment.

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
