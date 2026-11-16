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

**Complete required core:** The explicit prerequisites cover APP1–APP8 and APP17–APP21. They encompass first-principles web/Internet and HTML/CSS; JavaScript, TypeScript and the Node runtime; framework-neutral browser and React; data/SQL and typed backend service engineering; integrated application, quality/CI, actual deployment/recovery and measured production architecture. Every capability must find meaningful use in the *same product*. Simply citing completed course IDs does not establish APP9 mastery. Optional APP10–APP16 electives, SYS/Rust and proprietary or paid services are **not** required.

**Acceptable product problem spaces:** An accessible education tool, multi-user business workflow, developer platform/tool, document/resource system or other bounded authenticated application with real user tasks, persistent state, authorization boundaries and a justified asynchronous or simulated external side effect. The product must include frontend, typed service, PostgreSQL, quality and a real locally operated deployment. A modular monolith is sufficient when evidence does not justify distribution. Avoid mandatory AI features, public hosting, microservice fleets or a commercial identity provider.

**Ownership and reuse:** Learners may build on earlier APP5–APP8 work or suitable starter templates, libraries and AI assistance, with clear attribution and independent explanation. There must be a **substantive capstone-owned change**—a new or materially revised user workflow, product requirement, security boundary, operating capability or architecture decision—and the learner must implement and defend it. Unmodified old coursework or a generated project that the learner cannot explain is insufficient. Solo projects are valid; collaboration must not be fabricated.

**Research integrity and equitable access:** If actual stakeholders or participants are available, use voluntary informed consent, appropriate minimization and ethical low-risk task observation. If not, cite relevant public evidence or perform explicitly labeled heuristic/synthetic task analysis. Neither synthetic personas nor fictitious interviews prove real demand. The required capability is thoughtful, reviewable research, bounded interpretation and a reasoned product decision, not access to personal networks or paid research panels.

**Integrated engineering:** The UI must demonstrate semantic, responsive, accessible React and sound browser state. A real TypeScript/Node/Fastify service must validate runtime inputs and enforce session/resource/tenant/action/property authorization independently of hidden UI controls. Actual PostgreSQL data must implement credible relational constraints and transactional concurrency. An asynchronous or external interaction must have honest accepted/completed/uncertain states, bounded retries and a defensible idempotency policy. Security and privacy also apply to cached resources, files, background jobs and logs according to features used.

**Engineering quality and operation:** Design real multi-layer tests and reproducible local CI, including normal/invalid/forbidden/concurrent failure cases. Deploy using free local APP7-compatible processes/containers and isolated synthetic data with genuinely verified local HTTPS, controlled release identity, secrets isolation and actual real-database restore. Investigate one injected running-service failure, then perform a reproducible workload or reliability/architecture decision comparing sensible options using measured results, financial assumptions and limitations. One laboratory run cannot certify public uptime, cloud security, global scalability or market demand.

**Independent evaluation:** A reviewer must be able to reproduce actual behavior from a clean environment with documented free provisioned dependencies, ask a bounded unfamiliar requirement or fault within published outcomes, inspect the learner's corrective evidence and challenge design alternatives. Technical defense may be live, written, recorded or equivalently accessible. The reviewer must not impose private criteria, unpublished technologies or paid systems.

**Duration and completion:** 12–16 weeks at 10–15 focused hours/week is provisional, not an evidence-backed workload guarantee. This course uses **eight cumulative summative assessments** with one evolving project. All ordinary lessons and planning milestones are formative unless explicitly used as evidence for a required assessment; no hidden attendance or checkmark gates apply.

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

### Module 1 — Project Charter, Ownership and Evidence

#### Outcomes

- APP9-O1
- APP9-O3
- APP9-O4
- APP9-O15
- APP9-O16

#### Lessons

1. **Capstone versus previous laboratories** — Explain why independent product ownership is different from submitting earlier APP5–APP8 coursework.

2. **Full-core capability inventory** — Map HTML/CSS, JS/TS/Node, React, HTTP, Fastify, SQL, quality, deployment and production architecture to integrated work.

3. **Choosing a bounded product** — Compare an educational, workflow, developer, document or business application by actual user tasks and completion risk.

4. **Constraints and scope** — Limit the product to an inspectable protected user journey and measurable outcomes in 12–16 weeks.

5. **Authorship and reused components** — Attribute former course code, templates, third-party dependencies, AI help and real collaborators; identify new learner-owned work.

6. **Public evidence and provenance** — Map claims to independently inspectable source, HTTP, database, browser, research and operating artifacts.

7. **Free local toolchain** — Identify compatible versions, synthetic fixtures, runtime permissions and provisioned dependencies without requiring commercial accounts.

8. **Milestone risk plan** — Allocate time to risk-first implementation, product evaluation, security, recovery and defense.

9. **Formative charter critique** — Challenge an unjustified product-success claim or mandatory distributed dependency.

### Module 2 — Ethical Product Discovery and Validation

#### Outcomes

- APP9-O1
- APP9-O2
- APP9-O3
- APP9-O9
- APP9-O15

#### Lessons

1. **User tasks and affected stakeholders** — Differentiate imagined personas from observed users and actual existing alternatives.

2. **Falsifiable product questions** — State what evidence would favor or reject a consequential product assumption.

3. **Research ethics and consent** — If people participate, define voluntary informed consent, privacy, minimal retention and withdrawal.

4. **Secondary and synthetic alternatives** — Use cited public documents, structured scenario tasks or heuristic audits when participants are unavailable, clearly identifying unobserved behavior.

5. **Sampling and bias** — Identify convenience samples, researcher expectation and limitations of synthetic feedback.

6. **Task success and observation protocol** — Specify task, accessibility accommodations, outcome and minimally necessary evidence.

7. **Consent-conscious research records** — Avoid names, secrets, personal screenshots and identifiable transcripts when anonymous outcomes suffice.

8. **Interpretation and decision** — Map evidence to scope or acceptance changes without inventing demand or success metrics.

9. **Formative provenance audit** — Rewrite false claims that role-play or simulated users prove real-world usability.

### Module 3 — Requirements, Acceptance and Domain Planning

#### Outcomes

- APP9-O1
- APP9-O3
- APP9-O4
- APP9-O9
- APP9-O15

#### Lessons

1. **Actors and capability boundaries** — Define authenticated roles, tenants, resources and user intent for the proposed product.

2. **Observable acceptance tests** — State setup/action/result for normal, invalid, denied, conflict, slow, unavailable and recovered flows.

3. **Domain model and invariants** — Identify entities, keys, states, ownership and prohibited transitions.

4. **Traceability matrix** — Link requirement to interface, API, SQL, independent tests, risk and assessment evidence.

5. **Prioritization and exclusions** — Classify essential protected behavior and explicitly defer nonessential realtime, microservices or commercial features.

6. **Nonfunctional measurement targets** — Define representative accessibility, security, latency, reliability, privacy and cost objectives with units and uncertainty.

7. **Risk-first implementation plan** — Order authentication/data, working vertical slice, adverse tests and independent deployment early enough for repair.

8. **Requirement change control** — Track changed user assumptions and acceptance rules before and after product evaluation.

9. **Formative requirement challenge** — Strengthen an underspecified update flow with role denial, concurrent revision and expired session behavior.

### Module 4 — Application Architecture, Alternatives and Threat Models

#### Outcomes

- APP9-O3
- APP9-O4
- APP9-O6
- APP9-O7
- APP9-O8
- APP9-O9
- APP9-O14

#### Lessons

1. **Context and component diagrams** — Show actual browser, service, DB, worker, local dependencies and ingress instead of unrelated architecture illustrations.

2. **Programming and service boundaries** — Explain semantic HTML/CSS, JS behavior, TS boundaries, Node lifetime and Fastify request/serialization responsibilities.

3. **Domain/application/repository seams** — Choose cohesive modularity and explain dependency direction without speculative abstractions.

4. **Identity and data-flow trust** — Track client claims through server authentication, resource authorization, SQL constraints and output filtering.

5. **State and transaction scope** — Separate UI drafts, cache, committed DB facts, job intent and external side effects.

6. **Request and failure sequences** — Map protected HTTP requests, latency, error classification, retry and partial commit uncertainty.

7. **Alternative architecture options** — Compare simple monolith, worker separation, caching or extraction by measured need and risks.

8. **ADRs and falsifiable decisions** — Publish meaningful alternatives, security, maintainability, cost and change triggers.

9. **Formative alternative defense** — Reject premature microservices where a bounded simpler approach meets product requirements.

### Module 5 — Accessible Browser and React User Journey

#### Outcomes

- APP9-O3
- APP9-O5
- APP9-O6
- APP9-O9
- APP9-O10

#### Lessons

1. **Semantic interface and responsive CSS** — Build task-oriented HTML structure with keyboard access and usable narrow/zoomed layouts.

2. **React ownership and identity** — Distinguish component state, server data, drafts and cached resources and prevent cross-account disclosure.

3. **Typed and runtime-validated Fetch** — Handle real response shapes and network/status/error semantics independent of static TypeScript assurance.

4. **Forms, validation and navigation** — Design accessible field feedback and preserve input under failed submissions.

5. **Authentication and expiry UX** — Handle actual session expiry, revocation and logout while verifying server-side permission independently.

6. **Optimistic and uncertain states** — Distinguish pending, conflict, committed and lost-response results without false success.

7. **Error focus and announcements** — Inspect keyboard/focus, status messages, accessible notifications and correct empty/forbidden states.

8. **Usability across environments** — Check reduced motion, small display/reflow and selected assistive-technology behavior with honest limits.

9. **Formative client race** — Repair stale tenant data after a late Fetch or a failed mutation that erases user input.

### Module 6 — Typed API, Identity and Relational Integrity

#### Outcomes

- APP9-O4
- APP9-O6
- APP9-O7
- APP9-O8
- APP9-O9
- APP9-O10

#### Lessons

1. **Typed service contracts** — Design independently consumable Fastify/TS routes, runtime JSON schemas and safe status/error responses.

2. **Server-side input authority** — Validate URL, body and query and exclude unapproved mass-assignment/output properties.

3. **Synthetic authentication lifecycle** — Demonstrate actual session creation, expiry, revocation, logout and correct credential handling.

4. **Action, object, property and tenant checks** — Test direct wrong-role and guessed-resource HTTP access and inspect durable state.

5. **Schema normalization and constraints** — Model meaningful keys, foreign keys, unique/check constraints, indexes and data ownership.

6. **Actual concurrent transactions** — Use independent PostgreSQL sessions to test races, revisions, conflicts and committed invariants.

7. **Versioned migration compatibility** — Add a real schema/contract evolution while keeping defined older consumers safe.

8. **Domain and persistence ownership** — Separate domain decisions from SQL access without mocking away transactional claims.

9. **Formative integrity failure** — Find a partial transaction or authorization bypass that still returns a misleading successful response.

### Module 7 — Asynchronous Work and Data Stewardship

#### Outcomes

- APP9-O5
- APP9-O7
- APP9-O8
- APP9-O9
- APP9-O12

#### Lessons

1. **Justified delayed work** — Choose a real bounded background or local external operation with clear user value and progress semantics.

2. **Durable intent and transactional outbox** — Record important work with committed state and explain why remote effects are not DB-atomic.

3. **Idempotent replay** — Repeat a request after a lost response and show no duplicated protected business effect.

4. **Tenant-owned job visibility** — Authorize progress reads and stop polling or streams on logout and route teardown.

5. **External partial failure** — Distinguish accepted, queued, completed, uncertain, retryable and permanently failed work.

6. **Private files and caching when relevant** — Use safe ownership, capacity and cleanup controls if the product needs resource/file or cache features.

7. **Retention/deletion with backups** — Define personal/synthetic data, logs, jobs, file deletion and surviving backup constraints honestly.

8. **Failure recovery and UI reconciliation** — Refetch authoritative work state after missed events or dependency restoration.

9. **Formative delayed-work race** — Repair a progress notification that falsely overrides a committed database status.

### Module 8 — Software Quality, CI, Security and Accessibility

#### Outcomes

- APP9-O5
- APP9-O6
- APP9-O7
- APP9-O8
- APP9-O9
- APP9-O10
- APP9-O15

#### Lessons

1. **Risk-based verification** — Select component, domain, API, real-DB, consumer, browser, security and failure tests proportional to risk.

2. **Independent negative oracles** — Check actual forbidden DB effects, not only status codes or self-validating mocks.

3. **Deterministic fixtures** — Use controlled clocks, concurrency, separate DBs, synthetic identities and reliable teardown.

4. **Accessibility and privacy review** — Test focus/keyboard/zoom, status announcements, data visibility, secret-safe logs and retention.

5. **Fail-closed quality gates** — Author a versioned CI policy with free local runner equivalent, typecheck, lint and meaningful tests.

6. **Build and dependency provenance** — Record lockfiles/toolchain, source/artifact hashes and reviewed supply-chain limitations.

7. **Meaningful code review** — Explain changed behavior, risk and corrections, attributing collaborators only if they actually contributed.

8. **User/operator documentation** — Keep install, usage, config, security and troubleshooting aligned to observed source.

9. **Formative seeded defect** — Demonstrate a material security/contract regression fails independently before a tested correction.

### Module 9 — Local Deployment, Release and Verified Recovery

#### Outcomes

- APP9-O9
- APP9-O10
- APP9-O11
- APP9-O12
- APP9-O15

#### Lessons

1. **Running deployment contract** — Operate the integrated service with protected app/data separation and a genuine user-facing HTTPS path.

2. **Artifact identity and promotion** — Apply recorded digest, quality/approval controls and a reproducible local release equivalent.

3. **Scoped TLS and secret security** — Verify local hostname/cert trust without insecure bypass and keep secrets outside static assets/image layers.

4. **Safe stateful release** — Demonstrate compatible service/API/schema updates and a justified rollback or forward-repair policy.

5. **User-centered operational signals** — Connect logs, request IDs, failure rate/latency and actual protected task to release identity.

6. **Controlled release or dependency failure** — Inject a bounded local fault and record user impact, diagnosis and mitigation.

7. **Actual PostgreSQL backup and restore** — Restore separately into a disposable target and verify a protected task and authorization.

8. **Recovery point and time evidence** — Report observed restore time, recoverable commit and non-DB state gaps, not production guarantees.

9. **Formative restore audit** — Identify a backup that exists but cannot support the user task or permission model after restoration.

### Module 10 — Measured Performance and Architecture Economics

#### Outcomes

- APP9-O4
- APP9-O12
- APP9-O13
- APP9-O14

#### Lessons

1. **Choose a real architecture question** — Target a bottleneck, saturation or fault affecting an actual user task rather than benchmark tourism.

2. **Representative workload** — State arrival patterns, data size, tenant mix, warm-up, client saturation, errors and execution environment.

3. **Tail and failure measurement** — Capture supported percentiles, timeouts, throughput, DB/pool/event-loop and other relevant resource symptoms.

4. **Bottleneck alternatives** — Consider index/query fix, batching, bounded queue, cache and capacity before a service split.

5. **Experiment and compare** — Implement or justify rejecting an intervention using matched repeated workload plus security regressions.

6. **Fault containment at scale** — Bound retry, queue and timeout under synthetic dependency loss without leaking user data.

7. **Costs and maintenance effort** — Estimate compute, DB, backups, egress, logs and developer/operational work with stated units/sensitivity.

8. **Architecture decision and revisit trigger** — Explain why simplicity or added complexity best meets the evidence and future conditions for re-evaluation.

9. **Formative invalid speedup** — Find warm-cache or underpowered load generator bias in a claimed production improvement.

### Module 11 — Product Feedback, Revision and Handoff

#### Outcomes

- APP9-O1
- APP9-O2
- APP9-O3
- APP9-O5
- APP9-O9
- APP9-O14
- APP9-O15

#### Lessons

1. **Revisit original product assumption** — Select a task hypothesis that can be evaluated against the delivered feature.

2. **Consent or evidence-based alternative** — Conduct a limited participant task with consent or a labeled secondary/heuristic audit without fabricated observations.

3. **Actual versus expected task result** — Record objective evidence, sampling bias and unresolved uncertainty.

4. **Scope and acceptance decision** — Change a meaningful requirement or document defensible no-change after checking the original criterion.

5. **Implement bounded improvement** — Demonstrate a tested UX or functional adjustment when new requirements call for it.

6. **Retest accessibility and privacy** — Check changed focus, status, data retention and authorization under relevant conditions.

7. **Evidence and participant data stewardship** — Minimize participant artifacts, cite public sources and honor retention choices.

8. **User/operator handoff** — Update known limitations, help, runbooks and meaningful future work.

9. **Formative product impact challenge** — Explain why one anecdote or synthetic success does not establish product-market fit.

### Module 12 — Independent Reproduction and Engineering Defense

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

1. **Evidence map and frozen release** — Link every requirement/outcome/assessment to commits, architecture, tests, product evaluation and operational records.

2. **Fresh-checkout reproduction** — Have an independent reviewer or clean environment provision from public free instructions without hidden private files.

3. **Complete protected journey** — Demonstrate accessible React to authenticated Fastify, real DB, async work and coherent normal/error outcomes.

4. **Independent security challenge** — Exercise unauthorized tenant, expired session, malformed input and data retention without actual sensitive information.

5. **Live local recovery** — Trace a controlled failed release or dependency and independently verified restored DB state.

6. **Capacity and product decision defense** — Explain measured bottleneck/cost choices and honestly sourced user research.

7. **Unseen bounded requirement or fault** — Implement or diagnose an unfamiliar public-class case in authorization, stale state, a failing dependency, deployment or performance.

8. **Preserve invariants and show evidence** — Capture failing-before/passing-after results, source diff and tested normal/negative regression behavior.

9. **Authorship and attribution discussion** — Explain personal changes, dependency/template/AI use and genuine contribution of collaborators.

10. **Critical design and limitation defense** — Answer architecture, correctness, safety, economic and future-scale questions with concrete evidence.

11. **Reflect and hand off** — Record risks, unresolved constraints and tasks for a future maintainer.

## Completion requirements

### One coherent graduation product and required deliverables

The following describe **supporting project deliverables** for
the eight publicly defined assessments below; they are not
eight more independent summative gates or a demand for
a separate app for every previous course.

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

The eight milestones below are **planning and feedback
checkpoints**, not additional mandatory evaluations.
Artifacts may contribute to a named required assessment
if they satisfy its published criteria. Iteration and
overlap are expected; alternative ordering is acceptable
if required outcomes and dependency safety are retained.

| Milestone | Suggested sequence | Reviewable progress | Related summative |
| --- | --- | --- | --- |
| M1 — Charter and inquiry | Early | Bounded user task, problem evidence, ethics and initial assumptions | APP9-AS1 |
| M2 — Architecture and trace | Early–middle | System/data/identity design, alternatives, runtime contracts and test plan | APP9-AS2 |
| M3 — Protected vertical slice | Middle | Accessible React, typed API, genuine session/SQL and async state | APP9-AS3 |
| M4 — Quality correction | Middle | Independent negative tests, deterministic CI, seeded fault and fix | APP9-AS4 |
| M5 — Operated release and restore | Middle–late | Verified TLS, release failure, recovery and separate database restore | APP9-AS5 |
| M6 — Capacity and alternatives | Later | Measured representative workload, bottleneck and economic decision | APP9-AS6 |
| M7 — Product revision and handoff | Later | Feedback/provenance, justified scope/UX change and maintained documentation | APP9-AS7 |
| M8 — Independent defense | Final | Clean reproduction and unfamiliar scoped change or diagnosis | APP9-AS8 |

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
not an extra independent assessment or a
substitute for observing new APP9 outcomes.

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
  - Evidence: Initial/final product assumption, consented anonymized or cited secondary evidence with methodology, findings and uncertainty, updated acceptance and decision record, bounded change and regression or no-change defense, privacy/user docs and retrospective.

- **APP9-AS8** (required independent reproduction, unfamiliar change and graduation defense)
  - Outcomes: APP9-O1, APP9-O2, APP9-O3, APP9-O4, APP9-O5, APP9-O6, APP9-O7, APP9-O8, APP9-O9, APP9-O10, APP9-O11, APP9-O12, APP9-O13, APP9-O14, APP9-O15, APP9-O16
  - Work: Present a single independently reproducible final product and reference all qualifying APP9-AS1–AS7 artifacts. An assessor or independently documented clean-state procedure must install and run free local dependencies, exercise protected browser/API/SQL/async behavior, verify security negative tests, a faulty deployed release and actual restored database, and inspect reasoned product and architecture choices. Then introduce an **unfamiliar bounded** new authorized field/role, API contract variant, stale-state bug, deployment failure, workload constraint or dependency fault within published outcomes. Implement or correctly diagnose it, show an appropriate failing-before/passing-after test or equivalent causal evidence, and defend authorship, source reuse, design choices, uncertainties and remaining risks in an accessible format.
  - Criteria: The software, deployment and evidence can be independently examined without hidden environment state, undocumented manual intervention or required paid services. All eight required assessment decisions and every actual APP9 outcome have credible observable evidence; an evaluator does not grant credit merely because a course was previously passed or an outcome ID is listed. The unfamiliar scenario preserves protected data, meaningful user experience, old/new contract and rollback safety, and the learner can explain personally contributed code/decisions and attribution. The challenge stays within public outcome classes, feasible local tools and equivalent accessible written/recorded/live defense criteria.
  - Evidence: Single versioned source/product and complete outcome/evidence index, clean-run/fixture transcript, independent browser/API/PostgreSQL/security and deployed recovery traces, assessor's bounded scenario and source/test changes, product/architecture/cost decisions, evidence-limited reflections and accessible recorded/written/live defense.

### Graduation decision, evaluation revision and handoff

**APP9 is the core Application Engineering graduation
project.** Award completion only after an evaluator
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
remain optional and still require
their own migrations. OEE Workspace,
content/resource mappings and 0xNAND
course-consumer evidence pins require
separate reviewed alignment.

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
