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

**Reference task and independence:** Build one locally reproducible platform slice for **two differently authenticated/scoped synthetic developer consumers** and **two independently running small service instances**. An A→B create/inspect/promote/retire attempt must be denied at the **execution authority**, with unchanged actual resources. A catalog and versioned template feed an accessible CLI/local API; a real persisted control-plane request includes verified actor/owner, immutable parameter fingerprint, desired generation and a distinct observed status. The controller **actually** creates, updates, detects drift and retires named disposable resources with reconciliation after process death. Approval binds a separate approver to exact target/digest/policy and must be revalidated at execution; release only an already tested immutable artifact. A portal and Kubernetes are optional. Scripted developer trials are *synthetic*, not organizational adoption research, and an independently executed direct script is a legitimate value comparator.

**Safety, costs and alternatives:** The work must run with free and locally controllable tools, synthetic data, scoped credentials and disposable resources. No paid cloud, enterprise identity provider, public cluster, Kubernetes, Backstage, production deployment, privileged host access or large team is mandatory. Kubernetes/Backstage/GitOps are valid designs to **compare**, not badges required for completion. A local identity/role fixture may test authorization if its trust limitations are explained; a text-only policy diagram is not enough to prove enforcement. Avoid real secret handling where a scoped test token and redacted trace suffice. Preserve a clear manual or directly automated alternative to test whether a shared platform actually adds value.

**Instructional sufficiency and completion:** Seventeen outcomes span eleven distinct platform-service mechanisms and seven **independently decidable** assessments on one actual running two-consumer slice. Preserve a *conceptual model → worked request/desired-versus-observed trace → real normal/failure exercise → corrective feedback → independently checkable judgment* for every new mechanism. A successful `202 Accepted`, plan-only infrastructure file, green controller health endpoint, portal screenshot, generated scaffold or self-reported adoption number **does not** prove a service was safely created and authorized. The reference must actually store accepted intent and apply/reconcile **real locally owned resources**, with a current policy recheck before side effects, independently verified approval and safe cleanup. A **platform is a product**, not a compulsory Kubernetes/Backstage portal: a fair direct-script alternative and two synthetic developer consumers are enough to test usefulness, not to claim measured company-wide adoption. Formative lessons are not hidden completion gates. APP16 remains an **elective** outside APP9/core graduation and `draft` pending real learner/reviewer assessment.

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

1. **From deployment scripts to a developer-facing platform product** — Trace why teams evolved from manual infrastructure and siloed DevOps to self-service interfaces; compare what is actually new beyond APP6 CI/APP7 deployment and why a portal is neither necessary nor sufficient.

2. **Developers, platform operator and application responsibility** — Map two synthetic consumers, service/data ownership, platform privileged actor and application team's independently authorized domain decisions, using one failed handoff to reveal shared-responsibility boundaries.

3. **Select a repeated task with an independent baseline** — Choose one safe service instantiation/environment or guarded artifact promotion task with two differing consumers and observable start/finish, refused access, retries and support needs.

4. **Build the simpler approved alternative first** — Run one documented direct script/manual workflow under comparable resource and permission constraints; explain golden-path opt-in and when a separate service should **not** be built.

5. **Falsifiable cost, safety and completion hypothesis** — Define task time-to-working-service, no-unauthorized-effects, recovery, two-consumer fairness, operator support and maintenance limits before writing controller code; record how a failed hypothesis changes scope.

*Optional practice — Write a one-page rejection case for a proposed developer portal that cannot improve any supported task.*

### Module 2 — Developer Journeys, Discovery and Public Service Contracts

#### Outcomes

- APP16-O2
- APP16-O3
- APP16-O12
- APP16-O16

#### Lessons

1. **Measure developer work from a true ready state** — Record identical task input, clean environment, role, exact authorization/terminal resource or user-task state, failed attempts and assistance under script versus platform.

2. **Two distinct owned consumers and different needs** — Define consumer A and B, their allowed separate service/resource namespaces and justified variant, and identify a negative A→B action that a catalog description alone cannot block.

3. **Versioned public API with durable request semantics** — Publish actual CLI/API create/inspect/update/retire and promote contracts, stable idempotency key scope, parameter/error/async status states, version negotiation and retry expectations.

4. **Product boundary and permitted escape hatch** — Separate application-authored code and business data from platform-owned repeatable operation, offering a tested non-platform path that does not bypass required security/approval.

5. **Readable human-facing progress and denial** — Demonstrate an actual screen-reader-friendly text/CLI output with pending/unknown/denied/status, no color-only indicators, support owner and a safe next action after partial failure.

6. **Task success with legitimate and forbidden denominator** — Measure independently verified live service readiness, retries and operator intervention for both consumers; a successful API 202, generated files or portal click is not completed useful work.

7. **Service contract, limits and support obligation** — Document supported target/runtime, resource quotas, SLO measurement assumptions, current owner, escalation, cancellation and failure/retirement semantics with one verifiable invalid request example.

*Optional practice — Conduct a scripted task walkthrough with a deliberate invalid parameter and revise the interface based on observable confusion.*

### Module 3 — Service Catalogs, Templates and Consumer Ownership

#### Outcomes

- APP16-O3
- APP16-O4
- APP16-O5
- APP16-O12
- APP16-O15

#### Lessons

1. **Source-of-truth service identity versus discovery metadata** — Capture stable service ID, accountable owner, repo, environment/version, exposed interfaces, dependencies and runbook; do not treat arbitrary catalog owner string as trusted access-control identity.

2. **Schema constraints and dangerous stale owner** — Validate duplicate keys, invalid lifecycle values and references, then change the real service owner and prove stale catalog metadata does not grant or revoke privilege by itself.

3. **Catalog ingestion, staleness and orphan resolution** — Inspect actual repo/source revision versus indexed metadata under rename, archived repo or departed owner; expose stale/orphan status and controlled ownership repair rather than silently delete.

4. **Golden path as a versioned starting point** — Publish safe template, pinned dependencies, executable bootstrap/tests, approved environment properties and optional variations without committing privileged tokens.

5. **Render only validated names, ports and file paths** — Inject path traversal, shell metacharacters, duplicate service ID and misleading tenant/namespace labels, then prove no files or resources escape the scoped output.

6. **Two truly independent clean template consumers** — Generate, run and test two distinguishable services in separate directories/users with no local operator setup; compare documented variant, source/ID and observed readiness.

7. **Consumer-owned edits and managed upgrade distinctions** — Update a generator and an already scaffolded app, comparing manual migration versus centrally managed feature and demonstrating application-owned files cannot be silently overwritten.

8. **Discoverable docs, incident owner and useful fallback** — Follow actual catalog→template→build→request→support links from a clean consumer, detect one broken reference and provide an accessible repair and non-platform path.

*Optional practice — Deliberately remove an owner or break a runbook link, then verify the catalog surfaces the defect without creating a second unsupported metadata source.*

### Module 4 — Self-Service Control Plane and Durable Request State

#### Outcomes

- APP16-O3
- APP16-O6
- APP16-O7
- APP16-O9

#### Lessons

1. **Control plane writes intent; resource plane performs effect** — Draw CLI/API, authenticated caller, persisted desired spec/generation, work queue, provisioner and independently observed actual resources; do not confuse accepted command with created service.

2. **Finite operation state and observable transitions** — Define accepted, queued, applying, ready, degraded, reconciling, failed, retiring, retired/attention with exact legitimate transitions, actual timestamp provenance and explicit unknown outcome.

3. **Durable accepted intent, owner and stable fingerprint** — Before effect, atomically store request ID, verified actor and consumer/resource scope, operation kind, input fingerprint, desired generation, idempotency key and operator-visible state in a real local transactional store.

4. **Pre-execution and re-execution parameter limits** — Validate path/namespace/quantity, deadline/quota and current principal at submission **and before effect**, avoiding a queued approval/owner action that outlives revocation.

5. **Duplicate ID and changed-payload collision** — Replay a completed or in-flight request and a same-key different-body/owner attempt; prevent duplicate actual resource, reject ambiguous payload and avoid claiming exactly-once worker execution.

6. **Concurrent owner updates, revisions and retirement race** — Run two controller attempts against one resource while another consumer tries retire/create, using expected version/compare-and-swap or transaction guard to prevent stale deletion.

7. **Read-only request status versus observed truth** — Expose desired generation, observed version/readiness, attempt/failure and correlation ID without secrets; a marked succeeded request must be checked against actual resource, not only a queue ACK.

8. **Worker dies after real effect before status commit** — Actually interrupt a separately restartable local worker between creating a named service and writing status, inspect real resource, reconcile safely after restart without second service or hidden orphan.

*Optional practice — Write a small transition table and reproduce one invalid state transition with a focused test.*

### Module 5 — Reproducible Provisioning, Drift and Environment Lifecycle

#### Outcomes

- APP16-O4
- APP16-O6
- APP16-O7
- APP16-O8

#### Lessons

1. **Turn a validated spec into bounded real resources** — Apply a constrained self-service template to a real disposable local process/container/service instance, tracking resource identity, cost/quotas and explicit owner rather than a no-op mock.

2. **Actual plan versus apply versus resource inventory** — Run a relevant OpenTofu provider/resource or equivalent controlled local provisioner and inspect real creation/alteration; a plan, empty folder or arbitrary unrelated file is not evidence a service was provisioned.

3. **Consumer namespace, rights and shared-state protection** — Provision two independently runnable services, then attempt cross-consumer inspect/update/retire with forged owner/path; verify actual denied filesystem/process/resource and unchanged state.

4. **Ready user task, not provisioner process exit** — Read an actual service response/health plus declared expected application behavior and match observed endpoint/resource ID to accepted platform request.

5. **Out-of-band drift and authoritative repair decision** — Mutate an owned resource outside controller, detect mismatch with desired generation and choose safe repair, documented exception or paused incident; verify current owner rights before destructive action.

6. **Quotas, expiration and legitimate cancellation** — Bound local CPU/memory/disk/process/time and queue per consumer; test timeout/expiry with a partially created service that cannot be silently abandoned.

7. **Finalizers protect scoped deletion and audit history** — Retire exactly the identified resource and dependencies while preserving authorization, shared assets, owner record and a durable finalizer/attention state if cleanup fails.

8. **Crash during actual create and partial retire** — Kill worker after first step and again during owned resource cleanup, compare recorded and actual effects, then reconcile from observed state without deleting a neighbor's service.

*Optional practice — Contrast a one-off APP7 deployment script with a self-service environment request that offers a reusable lifecycle contract.*

### Module 6 — Platform Identity, Delegated Authority and Policy Enforcement

#### Outcomes

- APP16-O3
- APP16-O6
- APP16-O9
- APP16-O10
- APP16-O11

#### Lessons

1. **Three distinct identities and privileged confused deputy** — Trace developer, platform control actor and worker/deployer identity through request/policy/target, showing why service credentials do not authorize the caller's chosen tenant.

2. **Signed fixture claims versus production auth limits** — Implement locally trustworthy server-side principals/roles bound to two resource scopes, distinguish an attacker-supplied JSON owner from verified identity and disclose no external IDP claims.

3. **Current action/object/target policy at effect time** — Allow A create/update its own service and separately operator approve/promote; revoke A or change owner while pending and verify worker rejects the now-forbidden attempt.

4. **Template provenance, resource input and artifact trust** — Differentiate untrusted template source/user parameter, pinned approved template revision, actual tested release digest and verified build source evidence; an unchecked SHA string alone does not authenticate its producer.

5. **Deny-by-default executable policy and independent tests** — Use an inspectable direct authorization module or optional OPA/Rego with versioned rules and a seeded allow→deny regression; never require hosting a paid policy engine.

6. **Two-principal approval with stale-change protection** — Require genuinely different requester and approver principal/policy revision/target/digest, deny self-approval, forged approval and approval used after scope/target/artifact change.

7. **Short-lived local secret fixture and revocation** — Use dummy tokens/roles, deny expired or forged values and prevent raw credentials in rendered template, logs and queued jobs; don't claim a local stub proves production identity/rotation.

8. **Audit links policy version to observed effect** — Record request actor, actual approver, policy revision, target resource, immutable artifact digest and observed result/attempt as redacted auditable state, not a mutable yes/no checkbox.

9. **Forge, revoke and swap while action is queued** — Inject a changed template, forged owner, cross-tenant identifier, altered release digest or expired approval **between accept and execute**, verify no forbidden actual effect even if submission was earlier allowed.

*Optional practice — Compare policy-as-code with a directly implemented authorization check; defend what each verifies and what remains outside the exercise.*

### Module 7 — Shared Release Service and Artifact Promotion Interfaces

#### Outcomes

- APP16-O3
- APP16-O9
- APP16-O10
- APP16-O11

#### Lessons

1. **Existing APP7 artifact versus platform service** — Reuse actually verified immutable APP7 test artifact and its application-level compatibility boundaries; platform adds a *separately consumed request-to-deploy service*, not a second APP7 deployment tutorial.

2. **Promotion request and verifiable approval binding** — Publish an operation with consumer, immutable digest, desired target, identity, policy version and approval record, with accepted/denied/running/unknown/committed visibility.

3. **Verified tested digest and provenance limits** — Ensure exactly the tested digest is the deployed candidate and verify any available trusted provenance subject/builder before applying policy; copying a hash from caller input does not prove prior testing or signer identity.

4. **Recheck deployment target after approval** — Attempt promote A's artifact to B's stage using a legitimate old approval after target/policy has changed, rejecting mismatch before an actual service update.

5. **Platform controller fault versus app defect** — Use independent healthy/wrong-origin application and queued platform states to attribute an incident; the platform may pause/rollback deployment but does not own app business-data migration truth.

6. **Explicit safe rollback or forward repair ownership** — Stop a rejected/partially applied promotion, check real artifact and DB state, choose reversible platform routing/config versus application-owner forward data repair, never pretend a digest rollback undoes writes.

7. **Audit, notification and approved result retrieval** — Show separate requester and approver plus actual running digest/target, time/state, policy revision, denied case and operator-facing repair without leaking test credentials.

*Optional practice — Stage a denied cross-consumer promotion and verify no deploy action occurs.*

### Module 8 — Platform Reliability, Reconciliation and Incident Ownership

#### Outcomes

- APP16-O6
- APP16-O7
- APP16-O8
- APP16-O13

#### Lessons

1. **Developer journey SLI from accepted to usable service** — Define authorized requests with matching real ready resources, queue wait, completion, denied/failed and recovered outcomes; raw controller availability is not a user-facing platform SLI.

2. **Provisional SLO denominator and meaningful window** — Compute a small example with eligible/denied and stalled requests and defined observation window, disclosing synthetic small-sample limits and no production availability claim.

3. **Privacy-safe intent→attempt→observed effect trace** — Correlate real request ID, desired generation, queued attempt, local resource, release and status while avoiding token/tenant path in high-cardinality metrics labels.

4. **Locate platform queue/policy fault versus app defect** — Inject app failure and independent platform controller failure, compare user-visible symptom, actual deployed artifact/service health and responsible operator escalation.

5. **Real partial create and failed finalizer recovery** — Kill after resource creation before status, then fail a scoped retire; inspect actual orphan/finalizer and recover while preserving other consumer’s resources.

6. **Operator runbook with verified least-privilege path** — Exercise pause, inspect, reconcile, retry/quarantine and safe retire via real controls and alternate authorized admin, with no private undocumented host console steps.

7. **Two consumers under burst and finite fairness** — Submit bounded task burst by A while B requests a service, measure queue age/concurrency, ensure A cannot exhaust B's quota or gain another consumer's status.

8. **New incident hypothesis and independent correction** — Introduce a different unknown worker/policy/observed-version issue, retain before-fix status/resource evidence and measure repair with regression; no fabricated uptime improvements.

*Optional practice — Write a fault-injection transcript showing how the same request appears to both the caller and operator.*

### Module 9 — Developer Experience, Adoption and Platform Economics

#### Outcomes

- APP16-O1
- APP16-O2
- APP16-O12
- APP16-O14
- APP16-O16

#### Lessons

1. **Fair script versus platform trials with true completion** — Run equivalent tasks with clean local state, comparable permissions, accepted and failed requests, real resource readiness, attempts and operator interventions—not a faster but less secure path.

2. **Time-to-working-service and cognitive friction evidence** — Measure interactive steps, actual task success, accessible instruction/help issues and recovery, comparing multiple bounded synthetic runs instead of claiming human satisfaction.

3. **Adoption denominators and no fake teams** — Design eligible consumer, repeated successful use and bypass metrics for a real organization, but label two local actors as synthetic and never report inferred percent organization adoption.

4. **Accessible interface and documentation repair test** — Have an independently scripted fresh consumer use CLI/help/status/failure paths, check keyboard/text-only/no-color output and correct one observed confusion or missing step.

5. **Operator toil, exceptions and long-term cost** — Count reviewed approvals, policy/template maintenance, incidents/cleanup, support escalations and lock-in against a direct script, including expenses the platform centralizes or hides.

6. **Reproducible resource and labor unit assumptions** — Model measured CPU/runtime/disk/queue and stated operator-hour rates with total/fixed/marginal costs, unknown cloud fees and sensitivity to adoption or platform downtime.

7. **Shared-fate failure and security externality** — Inject a central platform outage versus two independent scripts and quantify bounded missed tasks, bottleneck or denied access while distinguishing model from measured company loss.

8. **Evidence-based continue, narrow or retire decision** — Produce a reviewer-usable product decision with expected developer need, measured task/correctness trade-offs, non-platform alternative, unknown user validity and a revisit trigger.

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

1. **API versions versus generated-code ownership** — Differentiate platform control protocol evolution, managed platform contract and one-off generated app source with explicit old/new compatibility promises.

2. **Real old/current consumer compatibility matrix** — Exercise two versioned request/CLI clients and unsupported fields/status, showing a concrete accepted version and rejected incompatible contract, not merely labeling semver.

3. **Graceful notice, migration window and owner response** — Publish a locally plausible deprecation calendar relative to support capacity, contract owner, still-running consumers and an honest rollback/forward repair policy.

4. **Export desired state, resource facts and accountable owner** — Serialize original source versions/ownership/catalog and durable request/status history with redacted secrets, explaining what cannot be recreated or entrusted to another platform.

5. **Escape hatches without approval bypass** — Run a legitimate alternate script for an out-of-template service with the same nonnegotiable permission/artifact policy; avoid proprietary vendor lock-in.

6. **Retire only authorized resources and preserve evidence** — Demonstrate app/capability deprecation with advance consumer notice, revocation of old token, actual finalizer cleanup of scoped services and unchanged other-team resources.

7. **Version decision tied to support and developer evidence** — Record old/new contract results, real migration/blockers, bounded maintenance and a stop/continue trigger rather than a roadmap of aspirational portal features.

*Optional practice — Review a proposed breaking template migration and explain why a generated repository cannot simply be overwritten.*

### Module 11 — One Independently Operable Platform and Unfamiliar Defense

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

1. **One real platform slice and accepted prior results** — Reuse one actual two-consumer control-plane/catalog/template/provision/release system, **reference individually accepted APP16-AS1–AS6** source and observed evidence rather than rebuild six separate platforms.

2. **Clean setup, ownership and independently observed effects** — Recreate two running owned services with safe CLI/API, catalog, request store and actual resource inventory, verifying one authorized and one denied operation including deployed immutable digest.

3. **Recheck actual crash, approval and migration regressions** — Select representative accepted unknown-outcome worker interruption, finalizer cleanup, revoked queued approval, two-consumer fairness and old/new CLI contract tests with real state and clear platform/app responsibility.

4. **Reviewer supplies unforeseen bounded platform failure** — Receive previously unseen stale owner/policy version, idempotency fingerprint collision, lost status, cross-consumer path, mismatched tested digest, orphaned environment or contract change and predict actual request/resource danger.

5. **Repair from independent state and confirm no privilege leak** — Observe failing-before persisted request, current policy and actual resources, implement narrowly causal fix or safe reconciliation and rerun targeted AS1–AS6 security, user-task and resource regressions.

6. **Defend source, product value and reproducibility** — Explain personally authored/borrowed source, manual-script counterfactual, setup/operating cost, support/exit ownership and honest synthetic-evidence limits in accessible written/recorded/live review.

## Completion requirements

**Required:** Demonstrate all **APP16-O1–APP16-O17** through seven **separately pass/fail** outcome-mapped assessments on **one** evolving locally running developer platform. APP16-AS1 owns the fair task baseline/product decision; AS2 verified consumer templates/catalog; AS3 **real** self-service resource reconcile; AS4 independent current authorization, two-person approval and trusted immutable promotion; AS5 a *distinct* actual platform incident and SLO; AS6 valid value/change/exit economics; AS7 one **new unfamiliar bounded failure** with independent before/after persisted request, real resource, authorization and user-task evidence. Previously passed AS1–AS6 artifacts may be linked, not duplicated as seven applications. Neither an all-green CI job nor AS7 itself waives any earlier decision. Synthetic adoption/latency claims remain explicitly qualified.

**Not required:** A specific portal, Backstage, Kubernetes, paid CI/cloud, public deployment, production credentials, real multi-team user study or every optional module practice. Module lessons, formative walkthroughs, template examples and self-checks are not separate course completion gates. No APP16 assessment is a condition of APP9 graduation.

### Shared environment, security and evidence boundaries

- **Reference fixture:** Pin free OS/runtime/template/provider versions, lockfiles and clean-run instructions; use two genuinely differently scoped principals and **two independently instantiated real local services**. Persist control-plane intent/status in **transactional SQLite or an equivalently atomic durable store**, using owner-bound resources, versioned spec and actual inspectable observed state. JSON files qualify **only if** equivalent atomicity, crash recovery, unique operation identity and concurrency correctness are **independently demonstrated**, not presumed from writing JSON. A local CLI/API and controlled real release targets are sufficient; cloud/cluster subscriptions and a portal are unnecessary.
- **Isolation and adversarial cases:** Prove *actual* A→B denied state and unchanged file/process/service/release target for cross-consumer actions. Attempt same-key/different-payload idempotency and concurrent updates; **kill an actual separate local worker after resource effect but before status**, detect out-of-band drift, refuse stale/forged approvals, and exercise partial destructive retirement. An accepted request does not count as completed provision until a real service is observed usable. Never touch unconsenting systems or real credentials; local synthetic role checks do not prove hosted IDP identity.
- **Reproducible decisions:** Retain assessment ID, relevant source revision, criteria, actual commands and observations, success/failure records and independently verifiable artifacts. Record synthetic measurements as synthetic. A diagram, green CI badge, screenshot or claimed percentage improvement alone cannot establish the relevant outcome.
- **Scope and reuse:** APP6/APP7 work may serve as input, but APP16 must independently demonstrate developer-facing reusable interfaces, multi-consumer authorization and lifecycle contracts. Do not require an entire cloud platform when a carefully bounded slice covers the published outcomes.

### Required summative assessments

- **APP16-AS1** — Developer Workflow Baseline, Product Boundary and Platform Decision
  - **Outcomes:** APP16-O1, APP16-O2, APP16-O3, APP16-O16.
  - **Work:** Using actual APP6/APP7 competencies, define a repeated developer task with a reproducible **non-platform direct script** and measurable authorized **two-consumer** start-to-real-ready-service conditions, negative role/resource case, retry/partial-failure population, operator help and cost/maintainability. Draft a versioned self-service API/CLI contract, shared responsibility and scope exclusions, with a clearly valid decision **not** to build an IDP.
  - **Criteria:** An independent reviewer runs the same task/permissions/data and observes actual successful/denied and retry states, time-to-usable-service, provider/runtime assumptions and whether platform abstraction is supported by real friction rather than portal popularity. A generated file or API 202 is not successful provision. No invented developer team interviews, organization adoption or hidden extra course/tool burden.
  - **Evidence:** Versioned task and non-platform script fixture, two consumer identities/service descriptions, clean-state start/finish/error observations, contract/owner/limits, baseline sample counts, falsifiable adoption and complexity decision.

- **APP16-AS2** — Service Golden Path, Ownership Catalog and Developer Discovery
  - **Outcomes:** APP16-O3, APP16-O4, APP16-O5, APP16-O12, APP16-O15.
  - **Work:** Author an actually runnable versioned service golden path plus catalog schema/source with accountable identity, repository, lifecycle, dependency, support link and source revision. From **two clean separate consumer workspaces**, instantiate **two distinct running small services** with safe parameter variants and available help. Deliberately invalidate duplicate IDs/owner/runbook reference, inject name/path traversal and stale catalog owner and demonstrate visible validation plus current authority not derived from catalog labels. Evolve a template with consumer-owned modifications without overwriting app code.
  - **Criteria:** Both services actually run and a fresh caller can locate docs, source and owner; generated source and accessible CLI/help are independently executable. Path/template abuse and stale/broken catalog source are rejected/surfaced, and catalog metadata **does not by itself authorize** platform actions. At least one actual old/current template/consumer migration preserves owned changes; no secret or unobserved operator action is required.
  - **Evidence:** Pinned free template/catalog schema, two clean workspace build/service responses, dependency/owner/metadata negative fixtures, stale registry inspection, parameter escape test and documented old/current consumer migration.

- **APP16-AS3** — Durable Self-Service Provisioning and Safe Resource Lifecycle
  - **Outcomes:** APP16-O4, APP16-O6, APP16-O7, APP16-O8, APP16-O9.
  - **Work:** Implement a real authenticated local CLI/API with **transactionally durable** accepted requests bound to owner, resource ID, action, payload fingerprint, desired version and status; have a **separately restartable local worker** perform an actual create/inspect/update/retire of two consumer-scoped running resources, **not merely plan**. Replay same request, send same-key-different-payload and different-owner attempts, race update-versus-retire, mutate a resource out of band, kill worker **after resource creation but before recording success**, and interrupt owned cleanup. Show observed/desired reconciliation, real readiness, no orphan and bounded quota/finalizer repair.
  - **Criteria:** Separate client, durable request and actual independently inspected file/process/service inventories show the two real services were created, modified/repaired and safely retired; 202/plan/status flags alone cannot pass. Duplicate IDs cannot duplicate resources or reinterpret a changed payload, stale version conflicts fail, unauthorized A→B attempts have **unchanged actual B resources**, and crash/restart catches an existing effect without blind duplicate. Partial destructive cleanup stays visible/repairable; no shared asset is deleted, no unbounded request quota or secret log.
  - **Evidence:** Controller/worker, transactional state schema, genuine two-service resource inventory/health, before/after same-ID collision, concurrent and stopped-process traces, desired-versus-observed drift, finalizer/cleanup and denial regression.

- **APP16-AS4** — Delegated Authority, Policy Gates and Trusted Promotion
  - **Outcomes:** APP16-O3, APP16-O9, APP16-O10, APP16-O11.
  - **Work:** At the **actual execution boundary**, evaluate a deny-by-default owner/action/object/environment policy for two independent synthetic developer identities and a **separate approver** using a real locally recorded approved artifact digest and applicable tested build/manifest evidence. Bind approval to requester, approver, exact target, artifact digest, policy revision and time/expiry, and test denial of self-approval, forged principal, wrong tenant/target, changed payload/artifact and role/owner revocation **between queue acceptance and worker execution**. Perform a permitted local release operation that actually runs the **same previously tested immutable artifact**, without rebuilding or trusting a caller-provided digest string as provenance.
  - **Criteria:** Distinct real actors authorize create versus approve/promote/retire; changed roles/policy/target/digest after acceptance are rechecked and cannot cause a delayed privileged action. Denied, forged, expired, swapped and cross-consumer requests show **unchanged actual artifact and B's resources**, not only an HTTP status. Approved promotion is independently inspected at running target with exactly the tested digest and an auditable policy revision, distinguishing checksum bytes from trusted builder identity. No real production secrets, paid OPA/IDP or fabricated SLSA certification required.
  - **Evidence:** Verified synthetic principal and action/object matrix, explicit current-execution policy source/version, separate request/approval states, before/after forbidden target inventory, tested source-to-digest manifest, running release proof, redacted scope/actor/policy audit and rollback/forward-repair limits.

- **APP16-AS5** — Platform Reliability, Fault Recovery and Developer-Facing SLO
  - **Outcomes:** APP16-O6, APP16-O7, APP16-O8, APP16-O13.
  - **Work:** Define a developer-task SLI/SLO over **eligible truly usable service requests**, with timestamps, incomplete/denied/error populations, low-sample synthetic caveat and queue age. Inject a **real distinct** platform controller/worker interruption mid-provision **and a failed scoped finalizer/cleanup** while another synthetic consumer can still attempt work; independently inspect durable intent/status and actual resource effects, diagnose, repair via controlled owner-authorized reconciliation and repeat an unrelated app-health failure for correct platform-vs-app incident attribution. Apply a new regression test and exercise an operator runbook.
  - **Criteria:** A reviewer can trace request→actual effect→status and observe an unsuccessful platform user task even when gateway/controller /health is green. Crash or failed cleanup cannot silently abandon or duplicate resources, mutate another consumer or hide unknown result. SLO math names time window/sample and never claims measured organization/production uptime; real fault repair has causal before/after evidence and support escalation remains accessible without secret host commands.
  - **Evidence:** Specific eligible work/SLI denominator and synthetic traces, actual killed worker/cleanup inventory, app-vs-platform fault differentiation, redacted correlation and failure analysis, replay/resolution regression and operator runbook.

- **APP16-AS6** — Platform User Value, Economics, Change and Exit Review
  - **Outcomes:** APP16-O1, APP16-O2, APP16-O12, APP16-O14, APP16-O15, APP16-O16.
  - **Work:** Perform repeated **matched actual two-consumer** direct-script versus platform provision/release/cleanup tasks with same allowed permissions, resource readiness, retry and error counting. Review CLI/help accessibility, support toil, shared-fate outages and fixed/marginal compute/operator costs. Define **future** real adoption/satisfaction measurement rather than invent reports from synthetic actors. Implement an **actual old/new client/platform contract test**, a template migration with consumer-owned code intact and a practical catalog/request-state **export and capability retirement** with owner notification/cleanup. Recommend continue, narrow to a script, replace or retire based on bounded data.
  - **Criteria:** The comparison counts actual usable completed and failed/denied work, sample size and intervention—not portal sessions or a faster unsecure method. The synthetic dataset is not presented as organization adoption, survey or human UX study. The platform's operational, policy, repair, maintenance and lock-in burden has explicit unit and sensitivity assumptions; breaking version is really rejected or migrated, export preserves who owns resources, and only correct owned resources are retired while the other consumer remains unaffected.
  - **Evidence:** Repeatable matched trial scripts/raw observations and timing/error denominator, accessible help/fix, cost/maintenance assumptions, old/current contract/consumer source tests, exported service ownership/desired-state record, actual retirement inventory and evidence-based platform-versus-automation memo.

- **APP16-AS7** — Integrated Self-Service Platform and Unfamiliar Technical Defense
  - **Outcomes:** APP16-O3, APP16-O4, APP16-O5, APP16-O6, APP16-O7, APP16-O8, APP16-O9, APP16-O10, APP16-O11, APP16-O12, APP16-O13, APP16-O14, APP16-O15, APP16-O16, APP16-O17.
  - **Work:** Present **one actually running small developer platform** with **two independently scoped real services**, and **reference previously accepted individual APP16-AS1–AS6 decisions** rather than rebuild or resubmit separate projects. In a clean pinned local environment, demonstrate a public CLI/API+template+catalog, durable request store, safe current worker authority, actual resource creation/ready state, approved immutable promotion, denial of A→B and a real after-effect crash/cleanup reconciliation. A reviewer supplies a **previously unseen** changed owner/approval, reused idempotency key, stale observed generation, leaked namespace, orphaned resource, bad trusted digest, migration/retirement or queue fairness case. Predict and independently reproduce incorrect resource/request/policy behavior, correct or safely reconcile, recheck affected prior security/workflow/compatibility criteria and defend measured platform value against direct script.
  - **Criteria:** All APP16-AS1–AS6 have **separate passing decisions**; AS7 cannot waive them or add APP16 to APP9 graduation. A previously unrehearsed bounded failure has observed **before-and-after persisted request, current policy, running resources and correct user task** evidence, not just green tests, diagrams or 202. No caller can change another consumer's resource, a stale approval cannot execute, already executed effects cannot be undone by clearing request status, and shared platform reliability/adoption claims stay appropriately synthetic. Independent reproducer plus accessible technical defense establishes personal source ownership, realistic maintenance cost and unsupported production limits.
  - **Evidence:** One pinned actual CLI/API, two running service instances, transactional store/provisioner/template/catalog fixtures, **references-first accepted APP16-AS1–AS6 outcome index**, immutable release/policy/worker/cleanup tests, separate assessor unfamiliar case and failing-before/passing-after actual resource/policy/request transcript, direct-script economic counterfactual and accessible written/recorded/live source defense.

### Completion decision and revision protection

Evaluators decide each assessment against its criteria and supporting evidence, then confirm every required outcome has actually been demonstrated. Partial coverage is not course completion; prior APP6 or APP7 results alone cannot satisfy APP16's platform-specific outcomes. A learner may reuse the same verified source revision across assessments rather than producing seven independent systems. A technical defense may be recorded, written, live or otherwise reviewable, provided authorship, design, negative-path behavior, unfamiliar reasoning and limitations can be evaluated.

APP16 remains the already published **v0.2.0 draft**, not learner-`tested`, independently `verified`, formally accredited or empirically validated for 14–18 weeks. The earlier checkpoint migration is historical, not a newly introduced prerequisite or completion change. Preserve genuine prior learner evidence under the exact originally evaluated revision; never reinterpret module checkmarks as satisfying APP16-O1–O17. The course revision, required outcome/assessment IDs and any future material change must remain identifiable for consumers such as OEE Workspace, resource mappings and 0xNAND. Actual learner trials, independent academic review and status governance follow the OEE [Status Labels](../../spec/status-labels.md), [Evidence Rules](../../spec/evidence-rules.md) and [Conformance](../../spec/conformance.md).

### Public non-mandatory study references

These are research and background references, not paid prerequisites, additional completion rules or mandatory implementation choices.

- [CNCF: Platform engineering maturity from toolchain to self-service](https://www.cncf.io/blog/2026/09/01/platform-engineering-maturity-from-toolchain-to-self-service/) — distinguish interface, adoption, operations and measurement maturity.
- [DORA: State of AI-assisted Software Development 2025](https://dora.dev/research/2025/dora-report/) — investigate platform quality, developer outcomes and the limitations of organizational correlations.
- [Backstage Software Catalog](https://backstage.io/docs/features/software-catalog/) — reference patterns for software ownership metadata and discoverability, without requiring Backstage.
- [OWASP CI/CD Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html) — analyze delegated permissions, credential and pipeline trust boundaries.
- [SLSA v1.2 provenance](https://slsa.dev/spec/v1.2/provenance) — identify what artifact provenance supports and why verification policy matters.
- [Google SRE Workbook: Error Budget Policy](https://sre.google/workbook/error-budget-policy/) — examine SLO-driven change and reliability decisions; adapt to a developer platform rather than copying an enterprise policy.
