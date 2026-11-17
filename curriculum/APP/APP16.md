# APP16 — Platform Engineering

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `elective`
**Prerequisites:** [APP6](APP6.md) — Software Quality & Engineering Operations, [APP7](APP7.md) — Deployment, Cloud & DevOps
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (provisional; validate with learners)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

**Design, implement, evaluate and defend a small internal developer platform that makes an application team's recurring work safely self-service.** Start from observed developer tasks rather than a portal or orchestration product. Publish a versioned platform contract; enable discoverable ownership, a reproducible service golden path, bounded self-service provisioning and release operations, policy-enforced authorization, operational recovery, and an evidence-based decision about adoption, maintenance cost and future investment.

**Distinct from prerequisites:** [APP6](APP6.md) already owns automated verification, trusted CI, provenance, observability, service SLOs and incident analysis. [APP7](APP7.md) already owns single-application deployment, HTTPS, declarative infrastructure, immutable promotion, stateful recovery and cost-aware operations. APP16 applies those proven skills to **a reusable service offered to other developers**: developer-facing product discovery, request-to-state reconciliation, safe delegation of privileged actions, multi-consumer contract evolution, support responsibility and empirically justified abstraction. No foundational testing, Docker, cloud, CI/CD or SLO course is repeated.

**Reference task and independence:** Use a locally reproducible platform slice that supports at least **two separately identified synthetic developer consumers** and **two distinct small application/service instances**. One consumer must be unable to affect the other's resources. A version-controlled template and metadata catalog feed a documented CLI, local API or other usable self-service interface; an orchestrator handles scoped create/inspect/update/retire requests with durable state, an auditable policy decision and reliable compensation/reconciliation after failure. Exercise an approved artifact promotion and a controlled incident using local/simulated environments. A small web portal is optional; a usable CLI/API plus accessible textual documentation is sufficient. Real human participants are useful but **not mandatory**: clearly label scripted role-based tasks or peer trials as simulations rather than invented user research.

**Safety, costs and alternatives:** The work must run with free and locally controllable tools, synthetic data, scoped credentials and disposable resources. No paid cloud, enterprise identity provider, public cluster, Kubernetes, Backstage, production deployment, privileged host access or large team is mandatory. Kubernetes/Backstage/GitOps are valid designs to **compare**, not badges required for completion. A local identity/role fixture may test authorization if its trust limitations are explained; a text-only policy diagram is not enough to prove enforcement. Avoid real secret handling where a scoped test token and redacted trace suffice. Preserve a clear manual or directly automated alternative to test whether a shared platform actually adds value.

**Outcome contract:** Seventeen observable outcomes across eleven conceptually distinct modules lead to seven linked, cumulative required assessments. Activities and optional practices prepare for assessed evidence; passing lesson counts, checkboxes or repeated module quizzes is not the completion rule. APP16 remains an **elective**, not a prerequisite for APP9 or APP graduation, and remains `draft` until independently validated with learner evidence.

## Learning outcomes

- **APP16-O1:** Define an internal platform's product boundary, consumers, responsibilities and alternatives using a demonstrable workflow problem rather than tool popularity.
- **APP16-O2:** Measure a repeatable developer task baseline, identify friction and specify useful developer-facing success measures with credible limitations.
- **APP16-O3:** Publish versioned platform service contracts and a clear platform/consumer shared-responsibility boundary, including documented exceptions and portability limits.
- **APP16-O4:** Build and evolve reproducible, parameter-validated service templates and golden paths that work for more than one consumer without hidden setup.
- **APP16-O5:** Maintain an inspectable service catalog that exposes actual ownership, lifecycle, dependencies, access routes and usable runbooks, including stale-entry handling.
- **APP16-O6:** Implement a bounded self-service interface and durable request/state model with explicit operations, identity, deduplication and intelligible failure states.
- **APP16-O7:** Reconcile interrupted, replayed and partially completed platform actions without unauthorized effects, duplicate resources or permanently hidden orphan state.
- **APP16-O8:** Provision, inspect, repair and retire isolated reproducible environments using controlled parameters, drift detection and verified cleanup.
- **APP16-O9:** Enforce scoped authentication and authorization for self-service actions across two consumers, preventing confused-deputy access, privilege escalation and leaked secrets.
- **APP16-O10:** Enforce independently testable platform policy and auditable approval boundaries for privileged operations and artifact trust, including negative paths.
- **APP16-O11:** Offer a safe, documented promotion/release service that consumes tested immutable artifacts and preserves application-team ownership of application behavior.
- **APP16-O12:** Make platform discovery, setup, errors, documentation, support and justified escape hatches usable and accessible to a developer without private operator knowledge.
- **APP16-O13:** Define developer-workflow SLIs/SLOs, observe platform failures, perform recovery, and distinguish platform impact from application incidents.
- **APP16-O14:** Evaluate task outcomes, adoption, support toil, latency, reliability and operating cost with appropriately bounded measurements, rather than vanity metrics.
- **APP16-O15:** Manage platform contract/template change, deprecation, migration, rollback and retirement with consumer communication and ownership continuity.
- **APP16-O16:** Defend whether a platform service, simpler automation or existing tool is justified under security, portability, maintenance, developer experience and cost constraints.
- **APP16-O17:** Reproduce and defend an integrated self-service platform slice, independently diagnose an unfamiliar bounded change or failure, and explain residual risks.

## Modules

### Module 1 — Platform Engineering as a Product and a Discipline

#### Outcomes

- APP16-O1
- APP16-O2
- APP16-O3
- APP16-O16

#### Lessons

1. **Course introduction, origin and applications** — Trace the evolution from manually operated team environments through DevOps and internal self-service interfaces. Distinguish platform engineering from cloud administration, IT service management, a web portal and application deployment; explain where shared workflows help or harm real teams.

2. **Consumer, operator and application boundaries** — Draw the people, trust boundaries, source repositories, application services and shared platform responsibilities. Identify who owns business correctness and incidents versus who owns the platform control surface.

3. **Paved roads versus autonomy** — Explain golden paths, optional escape hatches and the difference between useful standardization and coercive uniformity; identify a workflow that should remain outside the platform.

4. **Choose the recurring task** — Select a repeatable onboarding, service instantiation, environment request or guarded release task and reject platform scope that does not shorten or de-risk it.

5. **Document a simpler non-platform alternative** — Create a reproducible manual or direct-automation path as a fair comparator, including its operational risks and required privileges.

6. **Define value and failure hypotheses** — Record user-facing completion, correctness, risk, time, friction, support and cost hypotheses before building the platform; define what would cause the proposal to be rejected.

7. **Responsibility and adoption risks** — Explore lock-in, hidden operators, shared-fate outages, unavailable support and improper claims of team-level gains from one learner's exercise.

*Optional practice — Write a one-page rejection case for a proposed developer portal that cannot improve any supported task.*

### Module 2 — Developer Journeys, Discovery and Public Service Contracts

#### Outcomes

- APP16-O2
- APP16-O3
- APP16-O12
- APP16-O16

#### Lessons

1. **Task decomposition and baseline protocol** — Define start/end conditions, persona, environment, success, error states and repeatable trials for manual onboarding or release; collect a baseline without hiding retries.

2. **Two consumer journeys** — Define two consumers with different service requirements or permissions; identify common work, justified variations and risks of accidental cross-consumer access.

3. **Service contract surface** — Specify supported commands or endpoints, parameters, preconditions, outputs, errors, state transitions, idempotency scope and observable authorization failures.

4. **Workflow abstraction and escape routes** — Separate reusable platform capabilities from application-specific choices; document a safe manual alternative when a golden path does not fit.

5. **Human-readable interface usability** — Design help, confirmation, progress, explicit failures, timestamps, owner/support contact and accessible non-color-only status reporting.

6. **Boundary and ownership diagrams** — Trace which component builds, approves, provisions, observes, supports and owns each resource. Identify actions that must remain privileged.

7. **Measure useful experience rather than interface clicks** — Distinguish task success and time-to-working-service from portal visits, raw template downloads or unverified self-reported satisfaction.

8. **Document the minimum viable service offering** — Publish a service agreement with supported environments, service limits, failure states, scope exclusions and an operator escalation path.

*Optional practice — Conduct a scripted task walkthrough with a deliberate invalid parameter and revise the interface based on observable confusion.*

### Module 3 — Service Catalogs, Templates and Consumer Ownership

#### Outcomes

- APP16-O3
- APP16-O4
- APP16-O5
- APP16-O12
- APP16-O15

#### Lessons

1. **Authoritative service identity and ownership** — Model stable service ID, actual accountable owner, code source, lifecycle, exposed interfaces, dependencies, environment references and runbook links; explain what metadata is merely descriptive.

2. **Catalog data and validation** — Choose a small version-controlled JSON/YAML schema; reject duplicates, broken references, missing owners and invalid lifecycle transitions before publication.

3. **Catalog synchronization and stale records** — Distinguish registration from source-of-truth updates, stale cache, archived repositories and owner departure; build an inspectable reconciliation or validation path.

4. **Versioned golden-path template** — Define generated source structure, pinned dependencies, required configuration, secure defaults, tests and documented bootstrap commands. Do not hardcode hidden privileged credentials.

5. **Constrained parameters and safe rendering** — Validate service names, paths, ports and environment selections; reject traversal, untrusted expansion and template injection before creating files.

6. **Clean consumption without operator help** — Generate two independent service instances from a clean checkout; check runnable behavior and explain which configuration intentionally differs.

7. **Template evolution and consumer-owned code** — Separate one-time scaffolding from managed updates. Avoid overwriting application changes and publish a compatibility and migration decision.

8. **Documentation as part of the product** — Give discoverable prerequisites, version support, accessible examples, expected output, errors, safe cleanup and support channel.

9. **Classify a portal requirement** — Compare a static or CLI catalog with a Backstage-style portal; show when additional integration, hosting and permissions are justified.

*Optional practice — Deliberately remove an owner or break a runbook link, then verify the catalog surfaces the defect without creating a second unsupported metadata source.*

### Module 4 — Self-Service Control Plane and Durable Request State

#### Outcomes

- APP16-O3
- APP16-O6
- APP16-O7
- APP16-O9

#### Lessons

1. **Control plane versus managed resources** — Distinguish the developer request interface, authoritative desired-state store, operation runner, observed resources and application data plane.

2. **Request lifecycle and states** — Design accepted, rejected, queued, running, succeeded, failed, reconciling and retired states with stable request/resource IDs and clear caller-visible transitions.

3. **Durable store and resource attribution** — Persist request intent, authenticated principal, consumer scope, idempotency key, operation events and resource ownership before executing effects.

4. **Validation and bounded execution** — Reject unsupported parameters, excessive request size, resource quotas, timeouts and unsafe shell/path arguments at a defined boundary.

5. **Idempotency and duplicate delivery** — Show why duplicated submissions, retries and process restarts must not create duplicate platform resources; distinguish at-most-once processing claims from idempotent effects.

6. **Concurrent change and conflict handling** — Prevent two conflicting updates or retire/create races from silently corrupting the same resource; use serializable state changes or an explicit equivalent.

7. **Read-only status, audit and error semantics** — Return precise state, correlation ID, retryability and next action without leaking secrets or pretending an unobserved action succeeded.

8. **Worker restart and uncertain outcome** — Simulate a crash after an external effect but before the response; reconcile from recorded desired and observed state rather than blindly repeating a non-idempotent action.

*Optional practice — Write a small transition table and reproduce one invalid state transition with a focused test.*

### Module 5 — Reproducible Provisioning, Drift and Environment Lifecycle

#### Outcomes

- APP16-O4
- APP16-O6
- APP16-O7
- APP16-O8

#### Lessons

1. **Service provisioning contract** — Connect a validated template to a constrained local runtime/environment with declared resource limits, dependencies and cleanup responsibilities.

2. **Apply versus plan versus observe** — Use declarative IaC or an equivalently inspectable local provisioner to compare intended resources, current state and proposed changes; avoid assuming a plan has executed.

3. **Consumer isolation and resource names** — Enforce per-consumer namespaces/paths/ports or equally strong isolation; test that one consumer cannot impersonate another through identifiers.

4. **Creation and readiness checks** — Provision two services independently; report health readiness, expected run command and partial dependencies rather than only a successful process exit.

5. **Drift and repair semantics** — Mutate an environment out of band, detect the difference and choose repair, flag or intentional exception with recorded ownership.

6. **Bounded resource usage** — Apply quotas, expiration or explicit lifecycle rules to prevent leaked preview environments and uncontrolled disk/process growth.

7. **Retirement and finalizers** — Remove only scoped resources, handle incomplete cleanup and verify the absence of orphans without deleting shared data.

8. **Failure injection and resume** — Interrupt provisioning between dependent steps; show durable action history, safe reconciliation and a stable recovery outcome after restart.

*Optional practice — Contrast a one-off APP7 deployment script with a self-service environment request that offers a reusable lifecycle contract.*

### Module 6 — Platform Identity, Delegated Authority and Policy Enforcement

#### Outcomes

- APP16-O3
- APP16-O6
- APP16-O9
- APP16-O10
- APP16-O11

#### Lessons

1. **Caller, operator and workload identity** — Identify developer principals, platform service identity, execution actor and their separate authorities; explain the risk of a privileged confused deputy.

2. **Trust model for the local fixture** — Implement explicit synthetic identity/roles and binding to owned resources; document the missing security guarantees of local fixtures versus production identity systems.

3. **Least privilege and scope** — Authorize create, inspect, approve, promote and retire independently; deny wrong tenant, wrong role, expired/forged identity and uncontrolled privilege escalation.

4. **Parameter and supply-chain trust** — Distinguish untrusted user input, template repository source, pipeline changes and signed/trusted artifact policy; never infer trust from a friendly UI label.

5. **Policy as an executable contract** — Write deny-by-default decisions or a policy engine equivalent with testable inputs, explicit rules and deterministic allow/deny outcomes.

6. **Sensitive approval gates** — Keep deployment authorization separate from creator privileges and demonstrate that an unauthorized self-approval or altered approval record cannot pass.

7. **Credential boundary and short-lived scope** — Use inert/synthetic tokens and separated local secrets; design real rotations, expiry and no log exposure without requiring production credential issuance.

8. **Audit integrity and privacy** — Record who requested, who decided, which policy/version approved, what changed and the artifact digest; ensure redacted logs preserve sufficient investigation context.

9. **Negative-path threat investigation** — Inject forged owner, changed resource ID, malicious template parameter and privilege-crossing request; demonstrate rejected effects and unchanged authoritative state.

*Optional practice — Compare policy-as-code with a directly implemented authorization check; defend what each verifies and what remains outside the exercise.*

### Module 7 — Shared Release Service and Artifact Promotion Interfaces

#### Outcomes

- APP16-O3
- APP16-O9
- APP16-O10
- APP16-O11

#### Lessons

1. **Reuse APP7's delivery primitives** — Bring a previously tested immutable artifact, release metadata and environment contract; identify exactly what changes when another team self-serves it.

2. **Release API and approval states** — Publish a request to promote an existing digest, with consumer, target environment, accepted policy, approval evidence and progress/error surface.

3. **No rebuild on promotion** — Verify that the promoted digest matches the previously tested digest; a mutable tag alone is not trusted release identity.

4. **Policy boundary on target selection** — Reject a consumer deploying to an unauthorized environment or using an artifact with missing/invalid declared trust evidence.

5. **Team versus platform failure** — Separate application health failure and stateful compatibility decisions owned by the service team from platform orchestration faults.

6. **Failure and rollback as a service contract** — Expose a recoverable failure state and approved rollback/forward repair path, with clear cases where rollback is unsafe due to application data changes.

7. **Audit and end-user confirmation** — Provide a developer-inspectable release decision record: request, digest, actor, policy version, environment transition, result and any follow-up.

*Optional practice — Stage a denied cross-consumer promotion and verify no deploy action occurs.*

### Module 8 — Platform Reliability, Reconciliation and Incident Ownership

#### Outcomes

- APP16-O6
- APP16-O7
- APP16-O8
- APP16-O13

#### Lessons

1. **User-centered platform service indicators** — Define successful task completion, provision readiness, request failure, queue wait and recovery latency as developer-facing SLIs; distinguish them from application uptime.

2. **SLO and error budget reasoning** — Set a plausible provisional platform SLO with a defined population, observation window and exclusion policy; report limitations of a small local simulation.

3. **Telemetry across request boundaries** — Correlate authenticated request, approval, worker attempt, provisioned resources and resulting status without logging credentials or unnecessary tenant data.

4. **Platform versus app incident attribution** — Trace symptoms through CLI/API, queue, policy, environment provisioner and app health; avoid treating every failing application as a platform outage.

5. **Partial failure and compensation** — Inject interruption after resource creation, denied policy, lost status response and failed cleanup; test reconciliation with no orphan or double side effect.

6. **Operator recovery and support** — Document a runbook using inspect, retry, reconcile, pause, quarantine and safe retire operations with an explicit on-call/escalation responsibility.

7. **Platform degradation and fairness** — Enforce bounded queue/admission and per-consumer capacity; demonstrate one excessive consumer cannot silently starve the other.

8. **Incident learning and corrective verification** — Trace a user-visible failure through root cause, code/config correction and independent regression check; estimate rather than fabricate real service reliability.

*Optional practice — Write a fault-injection transcript showing how the same request appears to both the caller and operator.*

### Module 9 — Developer Experience, Adoption and Platform Economics

#### Outcomes

- APP16-O1
- APP16-O2
- APP16-O12
- APP16-O14
- APP16-O16

#### Lessons

1. **Comparable before/after trials** — Use the same task definition, environment cleanliness, correctness criteria, representative role and recorded retries for direct automation versus platform.

2. **Onboarding and task success** — Measure time-to-usable-service, failed attempts, ambiguous steps and operator interventions; distinguish task completion from a successful scaffold command.

3. **Adoption with denominators** — Define eligible consumers, active use, successful repeat use, bypass, exceptions and sampling limits; one synthetic trial is not proof of organization-wide adoption.

4. **Usability and accessibility review** — Test CLI help and errors, readable non-color indicators, transcript accessibility, documentation navigation and recovery without private chat support.

5. **Support toil and operational ownership** — Estimate maintenance, upgrade, incidents, policy requests, template upkeep and on-call burden; count what manual automation would cost too.

6. **Cost and capacity assumptions** — Build a bounded local resource/operator cost model with clear assumptions, price sensitivity, fixed versus marginal costs and no invented cloud bill.

7. **Failure costs and externalities** — Evaluate shared-fate outage, developer waiting, slow change approvals and hidden risk introduced by centralization.

8. **Decision memo and counterfactual** — Defend invest, narrow, automate directly or retire, conditioned on measured results and data limitations rather than enthusiasm for a portal.

*Optional practice — Report a case where the platform loses to a documented script and specify a valid decision to stop building it.*

### Module 10 — Platform Contract Evolution, Governance and Exit Paths

#### Outcomes

- APP16-O3
- APP16-O4
- APP16-O5
- APP16-O12
- APP16-O15
- APP16-O16

#### Lessons

1. **Semantic contract and template versions** — Differentiate command/API contract evolution, one-off generated application code and managed template updates; specify compatibility expectations.

2. **Consumer compatibility matrix** — Demonstrate older/newer CLI or request representations against the current controller; reject incompatible versions with actionable migration instructions.

3. **Deprecation and support windows** — Publish notice, owner, support period, replacement paths, and rollback criteria that match a credible local maintenance budget.

4. **Data and metadata portability** — Export catalog and request records in a documented format; identify what cannot be migrated automatically and who remains accountable.

5. **Exception governance** — Allow justified independent tool choices and a non-platform workflow without bypassing required security constraints; analyze lock-in from overprescribed toolchains.

6. **Retirement and cleanup** — Simulate service deprecation and removal with preserved ownership history, bounded consumer communication, secure revocation and verified resource cleanup.

7. **Decision and revision record** — Defend a future platform roadmap that prioritizes observed developer outcomes, security, capacity and lifecycle costs rather than a feature checklist.

*Optional practice — Review a proposed breaking template migration and explain why a generated repository cannot simply be overwritten.*

### Module 11 — Integrated Self-Service Platform and Independent Technical Defense

#### Outcomes

- APP16-O1
- APP16-O2
- APP16-O3
- APP16-O4
- APP16-O5
- APP16-O6
- APP16-O7
- APP16-O8
- APP16-O9
- APP16-O10
- APP16-O11
- APP16-O12
- APP16-O13
- APP16-O14
- APP16-O15
- APP16-O16
- APP16-O17

#### Lessons

1. **Public task brief and baseline** — Choose a concrete self-service application team problem, a reproducible non-platform comparator, minimum functionality, synthetic consumer roles and safety limits.

2. **Contract and ownership design** — Publish interface/state/API decisions, catalog schema, template versions, approval model, platform/operator responsibilities and user-visible failure states.

3. **Two independently reproducible consumers** — From separate clean workspaces create two service instances; confirm intentionally different allowed configuration and isolated ownership, without an unrecorded operator action.

4. **Working catalog and documentation** — Find a service owner, bootstrap method, support/runbook and lifecycle status through user-facing tools; reject broken metadata and accessible-help defects.

5. **Durable self-service operation** — Execute create/inspect/update/retire with bounded inputs, idempotency, asynchronous status, safe concurrency and reconciliation after an injected crash.

6. **Denied operation and artifact trust** — Demonstrate cross-consumer denial, unapproved release refusal, suspicious input rejection, trusted immutable digest checks and legible audit decisions.

7. **Guarded release and recoverable fault** — Promote an approved digest into local simulated stages, inject a platform-level failure, prove authoritative state and repair the platform pathway.

8. **Workflow SLO, experience and economics** — Record reproducible before/after task trials, synthetic adoption limitations, support burden and cost comparison; make a falsifiable continuation decision.

9. **Version and retirement exercise** — Upgrade an API/template or deprecate a capability with old/new consumer tests, clear communication, rollback or safe forward-only repair and cleanup.

10. **Independent unfamiliar technical change** — Respond to a reviewer-provided bounded new role, stale ownership, interrupted provision, schema compatibility, resource-leak or policy escalation defect without relying on a rehearsed answer.

11. **Authorship, reproducibility and defense** — Recreate the system from a clean state, show required negative outcomes and failure/recovery, defend platform-versus-script choice, disclose limitations and identify unresolved production risks.

*Optional practice — Before the summative defense, rehearse with a new developer using only public docs; record uncertainty and revise the path rather than labeling the rehearsal as user research.*

## Completion requirements

**Required:** Demonstrate all **APP16-O1–APP16-O17** through seven required outcome-mapped summative assessments, using one evolving local platform slice where practical. The work must be inspectable and reproducible; claims about developer adoption, reliability, trust or economics must be explicitly bounded by evidence. The final defense includes an unfamiliar bounded change or fault and does not merely replay the learner's prepared demonstration.

**Not required:** A specific portal, Backstage, Kubernetes, paid CI/cloud, public deployment, production credentials, real multi-team user study or every optional module practice. Module lessons, formative walkthroughs, template examples and self-checks are not separate course completion gates. No APP16 assessment is a condition of APP9 graduation.

### Shared environment, security and evidence boundaries

- **Reference fixture:** Document free tools, supported OS/runtime versions, exact application/template source revisions, lockfiles, local service runner, state store and clean-checkout commands. Use at least two differently scoped synthetic consumers and two independently instantiated services; a small SQLite/JSON state store, local HTTP/CLI interface and simulated release targets are acceptable when the behavior is truly implemented and testable.
- **Isolation and adversarial cases:** Require actual denial and unchanged state for an unauthorized cross-consumer request. Test duplicate requests, worker interruption after resource creation, concurrent conflict, invalid input, drift and cleanup. Never run an assessment against unconsenting systems, production credentials or public services. Record what the local identity fixture **does not** prove about production authentication.
- **Reproducible decisions:** Retain assessment ID, relevant source revision, criteria, actual commands and observations, success/failure records and independently verifiable artifacts. Record synthetic measurements as synthetic. A diagram, green CI badge, screenshot or claimed percentage improvement alone cannot establish the relevant outcome.
- **Scope and reuse:** APP6/APP7 work may serve as input, but APP16 must independently demonstrate developer-facing reusable interfaces, multi-consumer authorization and lifecycle contracts. Do not require an entire cloud platform when a carefully bounded slice covers the published outcomes.

### Required summative assessments

- **APP16-AS1** — Developer Workflow Baseline, Product Boundary and Platform Decision
  - **Outcomes:** APP16-O1, APP16-O2, APP16-O3, APP16-O16.
  - **Work:** Choose one recurring service/onboarding or release workflow; document two consumer roles, a reproducible direct-automation baseline, task and failure definitions, constraints, responsibilities, a proposed service contract and a viable do-not-build alternative.
  - **Criteria:** Baseline trial includes observable task success, retries and setup assumptions; the candidate platform owns only reusable work; the comparative task can be repeated by another reviewer; scope and non-platform alternative are falsifiable, not tool endorsements.
  - **Evidence:** Baseline scripts/commands or walkthrough fixture, task protocol and observations, workflow/ownership map, success thresholds, scope decision and explicit limitations of synthetic user evidence.

- **APP16-AS2** — Service Golden Path, Ownership Catalog and Developer Discovery
  - **Outcomes:** APP16-O3, APP16-O4, APP16-O5, APP16-O12, APP16-O15.
  - **Work:** Provide a versioned service template and validated catalog; instantiate two distinct consumer-owned services from clean workspaces; publish discoverable setup, ownership, support and retirement instructions; demonstrate a controlled template/catalog evolution.
  - **Criteria:** Both generated services boot and pass a declared basic check without undocumented privileges; unsafe parameters, duplicate IDs, missing owners and broken references fail visibly; consumers can locate usable help and runbooks; changes do not silently overwrite consumer code.
  - **Evidence:** Template source/version, catalog schema and fixtures, two clean-run transcripts, negative metadata/parameter tests, accessible help text, old/new contract evidence and consumer-facing migration notes.

- **APP16-AS3** — Durable Self-Service Provisioning and Safe Resource Lifecycle
  - **Outcomes:** APP16-O4, APP16-O6, APP16-O7, APP16-O8, APP16-O9.
  - **Work:** Implement a real local self-service request interface and persisted operation state; create/inspect/repair/retire scoped environments; replay a request, collide concurrent changes and interrupt the worker after a partial effect.
  - **Criteria:** Every accepted request has inspectable identity/scope/status; unauthorized or invalid requests change no resource; replay does not duplicate resources; interrupted or drifted operations reconcile or surface an actionable bounded failure; cleanup leaves no unowned resource.
  - **Evidence:** Source and state schema, request/response traces, adversarial fixtures, resource inventory before/after, crash/repair observations, test commands, quota/cleanup proof and explicit consistency limitations.

- **APP16-AS4** — Delegated Authority, Policy Gates and Trusted Promotion
  - **Outcomes:** APP16-O3, APP16-O9, APP16-O10, APP16-O11.
  - **Work:** Add enforceable developer/operator role policy and an artifact-digest-based release action; demonstrate approval separation, cross-consumer authorization and negative artifact/parameter paths through the actual interface.
  - **Criteria:** Different principals receive different permitted actions; cross-consumer and forged approvals are denied with unchanged target state; approved release uses the same previously tested artifact digest without rebuilding; sensitive values are not recorded in logs and rollback/forward-repair limits are honestly documented.
  - **Evidence:** Permission matrix and policy source/version, positive and denied execution transcripts, synthetic credential boundary, tested artifact manifest/digest, approval/audit decision events, invalid release tests and safe recovery note.

- **APP16-AS5** — Platform Reliability, Fault Recovery and Developer-Facing SLO
  - **Outcomes:** APP16-O6, APP16-O7, APP16-O8, APP16-O13.
  - **Work:** Instrument the platform request journey; define a developer-facing SLI/SLO with observation window; inject a platform fault during provisioning/promotion and another during cleanup or retry; diagnose, restore and prevent recurrence.
  - **Criteria:** Status and diagnostic signals distinguish platform faults from application failures; request-to-resource traces are correlated without leaking consumer secrets; recovery is independently repeatable, bounded and preserves authorization/resource ownership; numerical reliability claims state sample and environment limitations.
  - **Evidence:** SLI definition and observed small-sample data, injected faults and request traces, reconciliation/state proofs, incident analysis, corrective regression test and operator-facing recovery runbook.

- **APP16-AS6** — Platform User Value, Economics, Change and Exit Review
  - **Outcomes:** APP16-O1, APP16-O2, APP16-O12, APP16-O14, APP16-O15, APP16-O16.
  - **Work:** Compare fair baseline and platform workflows using repeated local trials; inspect developer experience, accessibility, support and cost; propose an adoption and service-health measurement plan; implement a controlled contract/template change and a retirement/export path.
  - **Criteria:** Correctness and task boundary remain comparable; results report time, failure/retry, operator intervention and actual limitations rather than invented adoption or savings; maintenance/security costs are included; older consumer behavior and safe retirement are verified; decision to continue, narrow or retire follows the evidence.
  - **Evidence:** Task scripts and measured samples, result tables/raw data, accessibility/usability findings, cost assumptions and sensitivity, compatibility tests, deprecation/export transcript and a defensible decision memo.

- **APP16-AS7** — Integrated Self-Service Platform and Unfamiliar Technical Defense
  - **Outcomes:** APP16-O3, APP16-O4, APP16-O5, APP16-O6, APP16-O7, APP16-O8, APP16-O9, APP16-O10, APP16-O11, APP16-O12, APP16-O13, APP16-O14, APP16-O15, APP16-O16, APP16-O17.
  - **Work:** Independently recreate one working platform slice from clean source; onboard two isolated consumers, discover ownership, provision and release, inspect authorization and request state, inject and repair a failure, demonstrate version/retirement behavior and resolve a reviewer-selected unfamiliar bounded defect or change.
  - **Criteria:** An independent reviewer can execute the public commands; denied requests have no forbidden side effect; state and resources converge or fail visibly; platform-versus-application responsibility is explicit; evidence substantiates reliability/value claims; the learner explains a new situation and justifies a correction without concealed operator steps.
  - **Evidence:** Full pinned source and fixtures, replay instructions, platform contract and catalog, two consumer journeys, authorization/release/failure traces, SLI and cost results, migration evidence, unfamiliar-change patch/test, technical defense and residual-risk statement.

### Completion decision and revision protection

Evaluators decide each assessment against its criteria and supporting evidence, then confirm every required outcome has actually been demonstrated. Partial coverage is not course completion; prior APP6 or APP7 results alone cannot satisfy APP16's platform-specific outcomes. A learner may reuse the same verified source revision across assessments rather than producing seven independent systems. A technical defense may be recorded, written, live or otherwise reviewable, provided authorship, design, negative-path behavior, unfamiliar reasoning and limitations can be evaluated.

APP16 is a newly migrated **v0.2.0 draft**, not `tested`, `verified`, formally conformance-certified or a validated 14–18-week claim. Preserve historical legacy-revision evidence under its original contract; do not silently reclassify previous module checkpoints as evidence for APP16-O1–O17. The course revision, required outcome/assessment IDs and any future material change must remain identifiable for consumers such as OEE Workspace, resource mappings and 0xNAND. Actual learner trials, independent academic review and status governance follow the OEE [Status Labels](../../spec/status-labels.md), [Evidence Rules](../../spec/evidence-rules.md) and [Conformance](../../spec/conformance.md).

### Public non-mandatory study references

These are research and background references, not paid prerequisites, additional completion rules or mandatory implementation choices.

- [CNCF: Platform engineering maturity from toolchain to self-service](https://www.cncf.io/blog/2026/09/01/platform-engineering-maturity-from-toolchain-to-self-service/) — distinguish interface, adoption, operations and measurement maturity.
- [DORA: State of AI-assisted Software Development 2025](https://dora.dev/research/2025/dora-report/) — investigate platform quality, developer outcomes and the limitations of organizational correlations.
- [Backstage Software Catalog](https://backstage.io/docs/features/software-catalog/) — reference patterns for software ownership metadata and discoverability, without requiring Backstage.
- [OWASP CI/CD Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html) — analyze delegated permissions, credential and pipeline trust boundaries.
- [SLSA v1.1 provenance](https://slsa.dev/spec/v1.1/provenance) — identify what artifact provenance supports and why verification policy matters.
- [Google SRE Workbook: Error Budget Policy](https://sre.google/workbook/error-budget-policy/) — examine SLO-driven change and reliability decisions; adapt to a developer platform rather than copying an enterprise policy.
