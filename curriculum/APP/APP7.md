# APP7 — Deployment, Cloud & DevOps

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `core`
**Prerequisites:** [APP5](APP5.md) — Full-Stack Application Architecture, [APP6](APP6.md) — Software Quality & Engineering Operations
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (provisional; calibrate with learner evidence)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Take an authenticated, tested full-stack application into an **actually
running, observable, secure and recoverable deployed environment**.
Build inspectable immutable application artifacts, supervise processes,
isolate services and persistent data, expose verified local HTTPS,
apply declarative infrastructure, promote an approved artifact through
delivery controls, manage stateful rolling releases, restore a real
database from an independently verified backup, respond to deployment
incidents and make responsible cost/security trade-offs.

**Direct prerequisites:** [APP5](APP5.md) and [APP6](APP6.md).
APP5 already owns React/Fastify/PostgreSQL business behavior, identity,
private resources and asynchronous jobs; APP6 owns test strategy, trusted
CI checks, build inputs, quality gates, user-centered SLO methodology,
telemetry and incident diagnosis. APP7 turns these prior competencies
into **service and release operations**. It does not introduce
JavaScript, Linux command-line fundamentals, TypeScript, SQL,
beginner testing or generic observability a second time.

**Reference environment:** A reproducible, locally owned Linux/VM or
equivalent host with free Docker/Podman-compatible containers or an
equally inspectable supervised process environment, a local
multi-service runner, synthetic PostgreSQL, an HTTPS reverse proxy
such as Caddy and a scoped local CA, source-pinned releases and an
open-source declarative IaC tool such as OpenTofu with a *real* local
provider/resource model. The toolchain may be pre-provisioned.
After provisioning, assessments must run using free local artifacts;
no paid cloud, public domain, shared production database, commercial
secrets/telemetry system, Kubernetes cluster or real account is
required. Proving **actual deployment** is still required: a static
mockup, plan-only IaC file or unexecuted rollback script does not
satisfy real service, resource or restoration outcomes.

**TLS trust is explicit.** A local CA certificate can verify a
local hostname if that certificate's test trust root was intentionally
installed or configured in the specific client. It does not confer
publicly trusted HTTPS. Never disable certificate checking or
permanently trust an unreviewed root merely to pass a demo.
Distinguish true client-to-proxy trust, proxy upstream policy,
forwarded header authenticity, cookie rules and direct backend
reachability. Public DNS/ACME operation is taught conceptually
and compared honestly against local evidence.

**CI is not CD.** APP6's test gates establish what passed;
APP7 establishes which *immutable artifact* may be released,
by whom, under which configuration and with which approval,
predeployment and rollback safeguards. Untrusted PR code cannot
borrow protected deployment credentials. Moving image tags,
cache reuse, sensitive IaC state and installed secrets require
specific controls and review.

**Database state outlives any release.** A code revert cannot
reverse a committed write, irreversible schema contraction,
file publication or external job delivery. Plan compatible
schema updates and mixed-version readers/writers, release
health checks and forward repair when rollback is unsafe.
An SQL dump and subsequent real restore establishes only
the demonstrated recovery scope, not WAL-based point-in-time
recovery or complete object/worker recovery. Measure RPO and
RTO honestly using a separate disposable restoration target.

APP7 owns **deployment**: packaging, runtime permission and
persistence, HTTPS ingress, environment isolation, secrets,
infrastructure creation/drift, CI-to-CD promotion, rolling
release, stateful compatibility, backup/restore, operational
watching, a controlled incident and cloud economics.
APP8 owns deep production-scale architectural evolution,
resilience/capacity decisions and distributed data trade-offs.
APP9 owns a complete independent product defense.
Production cloud deployment and vendor-specific platform skills
may be explored additionally but are not hidden completion gates.

Work uses only synthetic users and learner-controlled loopback
networks. No external load, unconsented security scanning or
shared-data destruction is appropriate. Status remains
`draft`: a local deployed product cannot prove global
uptime, public CA validity, provider backup guarantees
or operational readiness under genuine production traffic.
The provisional duration is not validated workload evidence.

## Learning outcomes

- **APP7-O1:** Translate an application release need into a documented deployment topology, trust model, user-facing release/availability criteria and proportionate operational responsibilities, explicitly separating tested conditions from assumed production behavior.
- **APP7-O2:** Build and verify a source-traceable deployable artifact with reviewed immutable identity, minimal runtime contents, least-privilege execution, declared runtime inputs and reproducible start/stop behavior.
- **APP7-O3:** Configure, diagnose and supervise application processes and container lifecycles, including port ownership, writable/persistent paths, health/readiness, signals, resource boundaries and graceful shutdown.
- **APP7-O4:** Establish and independently verify a local HTTPS reverse-proxy path, certificate/hostname trust, ingress restriction and trusted-forwarded-header behavior, explaining local CA versus public DNS/ACME operation.
- **APP7-O5:** Isolate development, staging and production-like configurations, resource identities, credentials and data; verify least-privilege secret injection/rotation without disclosing secrets in image layers, browser bundles, logs or infrastructure state.
- **APP7-O6:** Provision and recreate a real bounded local deployment declaratively, inspect concrete plans, demonstrate safe idempotence and drift detection, and protect state and destructive changes.
- **APP7-O7:** Connect pre-existing APP6 quality checks to a separately controlled CD promotion process with immutable artifacts, environmental approval, deployment credential isolation, smoke gates and a reviewable release record.
- **APP7-O8:** Perform a controlled staged/blue-green/rolling-like release and measured rollback or forward repair of a defective version, using readiness, user-impact evidence and verified in-flight/state behavior.
- **APP7-O9:** Plan, apply and validate an old/new compatible database/API release through expand/backfill/contract stages, explaining irreversible writes, side effects and situations in which a code revert is unsafe.
- **APP7-O10:** Create, protect and verify an actual consistent PostgreSQL backup; restore it in a separate disposable environment and demonstrate data/tenant integrity, relevant non-DB gaps and measured recovery point/time assumptions.
- **APP7-O11:** Operate release-specific health, readiness, observability, alert response and documented operator procedures, applying APP6 signals to deployed user-journey impact rather than merely a successful /health response.
- **APP7-O12:** Test deployment-specific security boundaries including network ingress/egress, service permissions, trusted proxies, runtime secrets, artifact provenance, data separation and privileged delivery events using controlled negative cases.
- **APP7-O13:** Execute a controlled incident in a real locally running deployment, communicate impact, contain failure, restore or forward-repair, verify persistent/user state and document an operational review.
- **APP7-O14:** Compare deployment models and cloud service responsibility boundaries using documented needs for resilience, portability, capacity, security, backup and operational effort rather than technology preference.
- **APP7-O15:** Prepare a transparent illustrative deployment budget and sensitivity analysis for compute, storage, backups, data egress, observability and availability, with explicit units, assumptions and cost controls.
- **APP7-O16:** Reproduce, evolve and independently defend an operationally coherent full-stack deployment, verified HTTPS, artifact promotion, two isolated environments, actual bad-release recovery and independent real-data restore under an unfamiliar bounded change.

## Modules

### Module 1 — Release Need, User Evidence and Operational Responsibility

#### Outcomes

- APP7-O1
- APP7-O11
- APP7-O14

#### Lessons

1. **Historical Release Problems and Accountable Operations** — Trace the change from manual server replacement to versioned artifacts, supervised runtimes, declarative resources and staged changes through one real deployment failure; DevOps is a responsibility model, not a product checklist.

2. **Carry Forward a Protected APP5 Journey and APP6 Gates** — Reuse the already functioning React/Fastify/PostgreSQL app, verified tenant permissions, private files/jobs, quality checks and task-centered signals; identify the *new* release/restore/ingress obligations.

3. **Running Topology, Trust Owners and Named Resources** — Map actual proxy, app, database, optional worker, files, ports and administrative access, naming which layer controls credentials, TLS, network, persistence and operator actions.

4. **Release Acceptance, Recovery Scope and Wrong-Target Risks** — Publish measurable authorized/denied task, availability, in-flight, preservation and isolation criteria, mark which goals are locally testable and identify irreversible state and operator error risks.

5. **Bounded Deployment Choice and Evidence Map** — Choose a free locally reproducible modular-monolith topology over premature clusters, and trace each operational acceptance to a distinct exercise, trusted artifact, observation or acknowledged gap.

*Optional practice — release-readiness audit:* Show why passing unit tests alone does not prove safe ingress, restoration or rollback.

### Module 2 — Supervised Runtime, Composed Networking and Persistent State

#### Outcomes

- APP7-O1
- APP7-O2
- APP7-O3
- APP7-O5
- APP7-O12

#### Lessons

1. **Process Identity, Ports and Filesystem Authority** — Inspect actual UID/GID, working directory, listening ports, environment and file/volume ownership; demonstrate a denied protected-path access rather than relying on a YAML setting.

2. **Supervision, Process Restart and Signal Semantics** — Operate a controlled service runner or supported container supervisor, inspect real restart policy and SIGTERM/portable stop, and trace HTTP, DB connection and worker cleanup under a bounded drain.

3. **App, Proxy, Database and Worker Composition** — Bring up the real local multi-service topology with named networks, mounts and process roles; distinguish application process, image/container and persisted database/file data.

4. **Loopback Exposure, Service DNS and Direct-Access Denial** — Verify externally reachable/loopback bindings and that private database, backend or worker endpoints are inaccessible from unintended client networks; test paths, not just network diagrams.

5. **Started Is Not Ready—Conditional Dependency Health** — Demonstrate why Compose short-form depends_on only orders starts; use a *real* meaningful service_healthy or equivalent readiness gate, and detect a DB-listening but business-unready state.

6. **State Persistence Across Replacement and Worker Restart** — Replace/stop app and worker instances, verify actual SQL data, private objects and durable job intent survive, and reject orphan or cross-environment volumes.

7. **Bounded Runtime Resources and Crash-Loop Diagnosis** — Apply reasonable CPU/memory/connection/restart budgets, inject bad config or unavailable DB, collect safe diagnostics and prevent a service from being reported ready while unable to transact.

8. **Partial Startup, Teardown and Wrong-Target Protection** — Rehearse failed setup/stop and inspect owned ports, DB sockets, file resources and volumes. Destroy only explicitly named disposable resources, preserving separate restored datasets.

*Optional practice — process incident:* Repair an instance that reports healthy while it cannot commit data or exit cleanly.

### Module 3 — Minimal Deployable Artifacts and Verified Runtime Identity

#### Outcomes

- APP7-O2
- APP7-O3
- APP7-O7
- APP7-O12

#### Lessons

1. **Image Layers, Runtime Process and Mutable Volumes** — Distinguish image/root filesystem, container process and persistent mounts and show a concrete result from replacing only the immutable app image.

2. **Source/Build Inputs and Minimal Multistage Output** — Reuse APP6's lockfile, source revision and reviewed dependencies to produce a small runtime image or equivalently inspectable process bundle without unnecessary compilation tools.

3. **Build Context, Base Digests and Secret Exclusion** — Exclude synthetic credentials and private data from source context and layers, identify reviewed base digest and relevant execution scripts, and inspect actual artifact contents.

4. **Published Digest versus Moving Release Tag** — Record and compare the tested immutable content digest/hash rather than a floating latest tag; verify actual stage/release artifact identity before a handoff.

5. **Nonroot Process, File Ownership and Exit Signals** — Run with least privilege and service-owned writable destinations, prove denied read/write to protected paths and observe startup, log output, bounded shutdown and meaningful health.

6. **Actual Replacement and Persistent Business Check** — Replace the built runtime under the declared manager and independently confirm tenant data, relevant file/job states, safe logs and a protected user transaction remain valid.

*Optional practice — image review:* Reduce oversized build contents and repair root-required writes without breaking the user task.

### Module 4 — Locally Verified HTTPS and Proxy Trust Boundaries

#### Outcomes

- APP7-O4
- APP7-O5
- APP7-O11
- APP7-O12

#### Lessons

1. **Hostname, SAN, Issuer and Chain Verification** — Explain and *test* how a named host, certificate SAN, issuer, trust root and expiry determine TLS acceptance for a chosen client, not by bypassing verification.

2. **Scoped Local CA versus Public ACME/DNS** — Use an intentionally configured test trust store or temporary local CA; demonstrate wrong-CA/hostname failure and explain why this does not establish public DNS or public CA trust.

3. **Actual Reverse Proxy to Protected Fastify** — Run Caddy or an equivalent maintained proxy for the same app, verify client→TLS ingress→upstream handling and inspect the actual origin/response boundary.

4. **Forwarded Header and Original Client Spoof Counterexample** — Inject attacker-chosen Forwarded and X-Forwarded-* values through client and direct-backend attempts, demonstrate what the proxy overwrites/ignores and configure only truly trusted hops for application decisions.

5. **Cookies, Origin, CSRF and Direct Backend Restrictions** — Verify secure session transport, appropriate SameSite/HttpOnly/origin assumptions and API authorization through the proxy and denied bypass, without mistaking CORS for a firewall.

6. **Proxy Body/Timeout and Unready Upstream Failure** — Test bounded request body, unavailable backend and carefully chosen upstream timeout with honest status and no trusted identity from an unverified hop.

7. **Expiry, Trust Cleanup and Authenticity Limits** — Show expiry or intentional certificate replacement behavior, remove temporary client/system test trust and document which local verifications do not establish public PKI readiness.

*Optional practice — HTTPS defect:* Detect an invalid certificate or spoofed forwarded identity and repair the trust boundary.

### Module 5 — Isolated Environments, Runtime Secrets and Operator Privileges

#### Outcomes

- APP7-O5
- APP7-O7
- APP7-O12

#### Lessons

1. **Test, Staging and Release-Like Ownership** — Name two independently created free local environments, with distinct data/volumes, service users, ports and configuration scopes rather than mere filename prefixes.

2. **Build-Time versus Runtime Secrets and Client Artifacts** — Demonstrate that private DB/session/release credentials do not enter frontend JavaScript bundles, image build layers, checked-in source or client-facing responses.

3. **Fail-Closed Configuration and Effective Role** — Reject missing/unsafe configuration before traffic; independently verify configured runtime identity, actual DB privilege and tenant/role isolation rather than trust an env var string.

4. **Scoped Injection and Safe Rotation** — Inject only fabricated credentials through a suitable local runtime secret mechanism, rotate a session/DB credential with documented cutover and revocation and verify service continuity or explicit fail-closed behavior.

5. **Release Approval, Restore Authority and State Exposure** — Distinguish ordinary code/tests, deploy operator, secret custodian and restore permissions; inspect logs/IaC plan/state and artifacts for synthetic secrets and unjustified administrative power.

6. **Two-Environment Negative Verification** — Attempt cross-env DB/file/credential access and unintended direct backend entry, inspect denied access and safely test environment cleanup without deleting the other instance.

*Optional practice — environment leak:* Repair an implicit development-secret fallback during release-like startup.

### Module 6 — Applied Infrastructure as Code, Drift and Destructive-State Protection

#### Outcomes

- APP7-O1
- APP7-O5
- APP7-O6
- APP7-O12

#### Lessons

1. **Actual Resources, Desired Configuration and State** — Explain provider/controller ownership and actual service-relevant resource identities; a stand-alone example local_file unrelated to the deployed topology is **not** sufficient deployment IaC.

2. **Versioned OpenTofu/Equivalent with Pinned Provider** — Use a compatible free local resource controller/provider that actually creates, configures or replaces a named deployed resource; pin binary/provider versions and distinguish a plan from an applied effect.

3. **Two Independently Isolated Namespaces and Named Plans** — Parameterize state path, service, port, data and resources for both environments, inspect an approved add/change/destroy plan and execute actual resource creation.

4. **Idempotence and Observable Drift** — Run unchanged plan/re-apply to verify effective no-op, deliberately modify an owned real resource and demonstrate refresh/drift detection and a justified reconciliation.

5. **Protect State, Locks, Secrets and Destructive Targets** — Control local/remote state file permissions and locking, avoid leaking secret values in saved plans/state, and deny mistaken replacement of another environment, database volume or retained backup.

6. **Change Approval, Replacement and Actual Inventory** — Review a real release-affecting resource update, check actual postapply network/port/config state and prove failed/unsafe plan leaves protected resources unchanged.

7. **Selective Teardown and Reprovisioning** — Destroy and recreate only the designated disposable environment, verify absence/presence of actual resources and ensure the other environment/restore target remains intact.

*Optional practice — drift decision:* Review a stale plan and explain why it must be regenerated after resource or state changes.

### Module 7 — Quality-to-Delivery Promotion and Immutable Release Decisions

#### Outcomes

- APP7-O2
- APP7-O5
- APP7-O7
- APP7-O8
- APP7-O12

#### Lessons

1. **Trusted Quality Gate versus Protected Release Authority** — Reuse APP6 check results as evidence but give separate control to artifact selection, destination credentials, approval, environment lock and rollback.

2. **Build Once, Inspect and Promote by Exact Digest** — Record source revision, tested image/hash, approved dependencies and schema state; promote the identical verified artifact stage→release-like without rebuilding a moving tag.

3. **Pipeline Ordering, Approval and Concurrency** — Design gate→artifact→staging smoke→human/defined approval→locked release→smoke and fail closed on skipped/failed/missing approval or simultaneous incompatible changes.

4. **Untrusted PR/Actions/Caches versus Deployment Privilege** — Test a local fake untrusted contribution/wrong digest/poisoned artifact case and review provider-specific OIDC, privileged event and environment controls honestly—local simulation is **not** hosted enforcement.

5. **Real Protected User and Forbidden-Action Smoke** — Issue local HTTPS/independent HTTP normal and denied requests before/after promotion, checking actual DB/job state and release-correlated readiness rather than only /health.

6. **Release Manifest, Recovery Candidate and Version Trace** — Record actor, approval, immutable source/digest, config, DB migration, observed traffic selection and a known-good recovery artifact whose compatibility has actually been checked.

*Optional practice — wrong-artifact incident:* Reject a floating tag, changed digest or skipped approval with documented failing evidence.

### Module 8 — Traffic Switching, Stateful Compatibility and Safe Release Repair

#### Outcomes

- APP7-O7
- APP7-O8
- APP7-O9
- APP7-O11
- APP7-O13

#### Lessons

1. **Deployment Versus User Feature Exposure** — Separate installed candidate, enablement, approved routing and actual user requests; choose a workable staged, blue/green or small rolling-like pattern for the local topology.

2. **Actual Old and New Versions behind a Controlled Selector** — Operate two different app versions concurrently and inspect which handles each request, without requiring a Kubernetes cluster or public internet traffic.

3. **Health, Business Readiness and In-Flight Drain** — Reject new traffic to unready instances, let bounded in-flight work complete or fail transparently, and verify actual prior/new backend availability.

4. **Expand Schema without Breaking Existing Writers** — Apply a compatible DB/API schema addition before requiring it and test old/new read/write clients against actual PostgreSQL rows, not a hypothetical migration description.

5. **Restartable, Bounded Backfill with Integrity Check** — Demonstrate real partial and resumed progress with transaction/resource limits and independent row counts, including a deliberately interrupted operation.

6. **Mixed-Version Writes, Contracts and Retained Fields** — Exercise both running service versions under a real old/new transaction/client matrix, prove no dropped field or inconsistent job/file ownership, and delay contraction until all older readers/writers are gone.

7. **Release-Specific Signals and Traffic-Shift Decision** — Compare authorized user journey, denied action, errors, in-flight jobs and latency by immutable release identity, with an explicit stop/rollback criterion.

8. **Defective Candidate and Real Controlled Traffic Exposure** — Inject a bad response/permission/config/DB compatibility defect, route bounded test traffic, observe actual failure and stop promotion rather than claim a green health probe means safe rollout.

9. **Safe Rollback versus Forward Repair after State Change** — Execute a switch to a known-good *compatible* artifact or a verified forward fix; demonstrate that a code rollback does not undo committed writes, published files or sent jobs.

10. **Post-Release Audit and State Reconciliation** — Inspect persisted row invariants, pending jobs/private objects, old/new consumers, release manifest and actual live route after the decision, recording unresolved effects.

11. **Security and Availability under Partial Shift** — Recheck tenant/role denial, proxy and secret boundaries during old/new overlap, and report measured local downtime/availability as an experiment, not production SLO evidence.

*Optional practice — unready-canary defect:* Repair a traffic switch that routes users to an instance with no database access.

### Module 9 — PostgreSQL Backup, Separate Restore and Honest Recovery Scope

#### Outcomes

- APP7-O3
- APP7-O5
- APP7-O9
- APP7-O10
- APP7-O11
- APP7-O13

#### Lessons

1. **Recovery Goals, Real Snapshot Point and Scope** — Define test RPO/RTO targets before work, identify actual backup snapshot/recoverable state and prove retention target names; a guessed last commit time is not a measured recovery point.

2. **Logical Consistency, Tool Versions and Global Roles** — Use supported pg_dump/pg_restore and a truly consistent synthetic snapshot; document that pg_dump does not include cluster-global roles/tablespaces/configuration, which need separate approved reconstruction or pg_dumpall --globals-only.

3. **Create, Protect and Independently Verify a Real Backup** — Back up an active disposable source, record exit/warnings, scope, hash, tool/server versions, storage isolation and permissions; a checksum alone does not prove restorable data or confidentiality.

4. **Loss Only in a Named Disposable Target** — Prove database identity, data-owner role and resource names before a simulated loss; never destroy the live source, other staging environment or retained backup.

5. **Restore into a Distinct Clean PostgreSQL Instance** — Rebuild globals/roles/permissions explicitly as appropriate, restore to a **separate** named empty target, detect failed/ignored errors and independently check actual schema, constraints and tenant rows.

6. **Restore Authenticated Task and Non-DB Gaps** — Run real authenticated allowed/denied client actions after restoration and inspect absent/mismatched private files, durable worker intent, external notifications and role/config dependencies.

7. **Observed RPO/RTO and PITR Limitations** — Time the complete restore plus validation and compare recovered source markers/commits with defined goals; distinguish local logical-dump recovery from WAL archiving, physical backup or true point-in-time restoration.

8. **Recovery Runbook, Repeatable Cleanup and Audit** — Publish explicit capture/restore/check/cleanup steps, source/target/backup safeguards, missing-data report and test cadence, without claiming automatic production continuity.

### Module 10 — Operational Incident, Release Telemetry and Verified Recovery

#### Outcomes

- APP7-O8
- APP7-O10
- APP7-O11
- APP7-O13

#### Lessons

1. **Release/User Outcome Correlation and Incident Roles** — Reuse APP6 signals, but bind real deployed version, TLS/proxy, request/job and DB observations to one affected authenticated user task and named responder/communication roles.

2. **A Distinct Actual Deployment Fault** — Seed a *new* local TLS expiry/trust, proxy configuration, credential rotation, ingress or readiness defect not identical to AS4's bad app release; observe actual impact before mitigation.

3. **Evidence, Competing Causes and Safe Containment** — Collect redacted version/route/request/DB/credential timeline, distinguish cause from symptom and decide a bounded route stop, config repair, credential revocation or compatible rollback.

4. **Recovered User, Tenant, Worker and File State** — After repair, exercise permitted and forbidden HTTPS/API actions, actual committed database data, pending worker and private file/tenant isolation; green health alone is insufficient.

5. **Actual Recovery Timings and Misleading Monitors** — Record elapsed detection, containment and verified restoration intervals with environment and telemetry gaps, no fictitious production user history or universally achieved availability.

6. **Reviewed Runbook and Handoff to Architecture** — Update an actionable operational procedure and release/monitoring safeguards based on the observed failure; distinguish APP8's capacity/distribution design from APP7 running-service operations.

*Optional practice — bad signal diagnosis:* Identify alert noise versus a real rollout regression and justify mitigation steps.

### Module 11 — Hosting Models, Responsibility and Cost Sensitivity

#### Outcomes

- APP7-O1
- APP7-O11
- APP7-O14
- APP7-O15

#### Lessons

1. **Choose Two Feasible Models for the Same Workflow** — Compare self-managed VM/container and one managed compute/database/storage option on patching, recovery, TLS/identity, vendor risk and operational ownership.

2. **Units, Evidence and Service Responsibility Matrix** — State sample monthly requests, concurrency, allocated compute-hours, DB/storage size, backups, transfer, logging retention and realistic performance/availability assumptions with sourced or explicitly hypothetical rates.

3. **Monthly Compute, Persistent Data and Egress Formula** — Calculate instance-hour, storage/backup, operations, network egress and telemetry costs for both models, including where charges differ with idle capacity or data restoration.

4. **Sensitivity, Failure Exposure and Budget Guards** — Vary traffic/data/egress and backup-retention assumptions, identify dominant cost/risk changes and justify a proportional alert/limit strategy.

5. **Decide Operability and Future APP8 Questions** — Defend a lower-complexity reference deployment under the declared constraints and identify what higher scale, queueing, replicas or distributed reliability APP8 would need to assess.

*Optional practice — economical deployment decision:* Reject an unjustified complex stack and defend a simpler reliable design.

### Module 12 — One Deployed Product and Independent Operational Defense

#### Outcomes

- APP7-O1
- APP7-O2
- APP7-O3
- APP7-O4
- APP7-O5
- APP7-O6
- APP7-O7
- APP7-O8
- APP7-O9
- APP7-O10
- APP7-O11
- APP7-O12
- APP7-O13
- APP7-O14
- APP7-O15
- APP7-O16

#### Lessons

1. **One Product, Release Contract and Accepted Evidence Index** — Reuse the same APP5 deployed source evaluated in APP7-AS1–AS6; map architecture, environment, role, TLS, release, restore and cost decisions to prior independently accepted evidence.

2. **Integrated Real Run, Trust and Immutable Promotion** — Confirm actual stage/release-like running services, least-privilege process, verified local HTTPS, applied IaC and protected digest promotion, linking earlier accepted observations rather than redoing unrelated reports.

3. **Failed Release, Backup and User Recovery Recheck** — Verify real mixed-version change, bad-release repair and separate PostgreSQL restore plus denied/user data/file/job outcomes under explicit evidence scope and prior accepted AS4–AS6 traces.

4. **New Unfamiliar Bounded Operational Fault and Regression** — Diagnose and repair assessor-supplied wrong digest, TLS trust, approval, drift, migration, credential or restore fault and recheck earlier permissions, data integrity and active service behavior.

5. **Fresh Local Reproduction and Technical Defense** — Recreate setup/start/test/stop using pinned free provisioned local artifacts, one evidence index and accessible explanation of actual versus assumed hosted/cloud capabilities and APP8 boundaries.

## Completion requirements

All **sixteen APP7 outcomes** require **seven independently
decidable summative assessments** on **one evolving deployed APP5
product**, with separate artifact/process (AS1), verified HTTPS
and environment security (AS2), actually applied IaC (AS3),
immutable promotion/stateful traffic recovery (AS4), real separate
database restore (AS5), a *distinct* deployment incident and
cost/responsibility analysis (AS6), and an unfamiliar independent
operational defense (AS7). Previously **accepted evidence may be
referenced**, not resubmitted as seven independent deployments.
Formative lesson work and optional hosted/provider study do not
create additional completion gates.

| Required assessment | Required outcome coverage | Principal evidence |
| --- | --- | --- |
| `APP7-AS1` — Deployment Artifact, Service Lifecycle and Isolation | APP7-O1, APP7-O2, APP7-O3, APP7-O5, APP7-O6, APP7-O12 | Versioned manifest/container or process configuration, digest, source/toolchain record, startup/shutdown/network/permission test logs, persistent data observations and clean-checkout recipe |
| `APP7-AS2` — HTTPS Ingress, Environment and Credential Safety | APP7-O3, APP7-O4, APP7-O5, APP7-O11, APP7-O12 | Local TLS/proxy/environment configuration, positive/negative HTTPS and header traces, network and session tests, rotation record, scoped CA/trust cleanup and residual-risk explanation |
| `APP7-AS3` — Declarative Infrastructure, Drift and Protected State | APP7-O1, APP7-O5, APP7-O6, APP7-O7, APP7-O12 | Versioned IaC and local dependency instructions, plan/apply and inventory, repeat/no-op/drift logs, protected state/approval rationale and teardown evidence |
| `APP7-AS4` — Approved Artifact Promotion, Release Rollout and Stateful Compatibility | APP7-O2, APP7-O5, APP7-O7, APP7-O8, APP7-O9, APP7-O11, APP7-O12 | Versioned CI-to-CD workflow and release manifest, digest and permission model, old/new compatibility matrix and SQL migration, smoke/negative tests, traffic-shift timeline, failure, rollback/repair and data checks |
| `APP7-AS5` — Consistent Backup, Independent Restore and Measured Recovery | APP7-O3, APP7-O5, APP7-O9, APP7-O10, APP7-O11, APP7-O13 | Backup artifact/checksum, scope and retention notes, disposable loss/restore transcript, DB and user-journey tests, timings, non-DB gaps and recovery runbook |
| `APP7-AS6` — Deployment Incident, Shared Responsibility and Cost Review | APP7-O1, APP7-O4, APP7-O8, APP7-O11, APP7-O12, APP7-O13, APP7-O14, APP7-O15 | Observed incident/telemetry/recovery trace, updated runbook and security/DB checks, hosting option diagram, shared responsibility and budget/sensitivity worksheet |
| `APP7-AS7` — Integrated Deployed Product and Independent Operational Defense | APP7-O1, APP7-O2, APP7-O3, APP7-O4, APP7-O5, APP7-O6, APP7-O7, APP7-O8, APP7-O9, APP7-O10, APP7-O11, APP7-O12, APP7-O13, APP7-O14, APP7-O15, APP7-O16 | Versioned deployment/release/IaC/TLS/backup source, signed-off review decisions and digests, clean local setup, synthetic users/DB, negative and normal tests, bad-release and restore timelines with recovery metrics, cost models and accessible independent technical defense |

### Shared execution, privacy, recovery and safety boundaries

- Provide a pinned and mutually compatible reference baseline
  for React/Fastify, Node/TypeScript, PostgreSQL, the container or
  process runner, reverse proxy, local CA and IaC dependencies.
  Record source, build inputs, resource requirements, OS/runtime,
  test-only hostnames and environment identities. Initial free
  dependency installation may need network access; required
  demonstrations are reproducible thereafter using provisioned
  local artifacts and synthetic identities.
- **Actual local runtime evidence is required**: a launched
  service, correctly verified HTTPS, a genuinely applied
  declarative local resource change, protected artifact
  promotion, a failed release with recovery and an actual
  PostgreSQL restore. Simulated hosted-cloud behavior can
  inform architecture comparison but cannot replace the
  on-host demonstration or be labeled live provider proof.
- Use a minimal app/runtime artifact, least-privilege user,
  appropriate CPU/memory/connection limits and isolated
  database/worker networks. Verify shutdown, restart,
  persistent state, staging/release data separation and
  no unauthorized direct backend or database exposure.
- A locally issued certificate is **not globally trusted**.
  Validate name, chain and trust root deliberately using
  a client scoped for the exercise; never use an insecure
  TLS bypass as security evidence or leave unwanted
  system-wide trust changes after cleanup. Review
  forwarded client identity only when supplied by a
  named trusted proxy hop.
- Treat CI artifacts, caches, release approval, untrusted
  PR triggers and deployment identities as separate
  privilege domains. Promote by reviewed digest/hash
  rather than floating tag, fail closed on wrong
  artifact or unavailable approval, and redact all
  synthetic secrets from frontend bundles, source,
  image layers, IaC plans/state, logs and review artifacts.
- Stateful release evidence must show old/new reader
  and writer compatibility, safe expand/backfill/contract
  sequence and a verified rollback or forward-repair
  decision. Never assume a redeployment undoes
  committed database transactions or external effects.
- Use a **separately identified disposable restoration
  database** for real backup verification. Record dump
  scope, SHA-256 or equivalent checksum, access controls,
  ownership, tool versions and user-visible data
  checks. State which private files, metadata and
  job intent lie outside the chosen backup; do not
  call a logical dump a WAL-based PITR rehearsal.
- Identify RPO and RTO goals *before* recovery, then
  report observed local recoverable point and restoration
  time including setup/application validation. An
  illustrative test does not certify future service-level
  commitments or fully recover a production topology.
- Bound failures, restarts, requests and load to
  learner-controlled loopback or an authorized
  isolated free VM. Do not test third-party networks
  or delete shared resources, and validate targets
  before destructive commands. Use synthetic
  credentials and data only.
- Run one operational incident against a real local
  running release; report affected user tasks,
  version, sanitized logs/metrics, declared decision,
  actual mitigation, data integrity and permission
  checks after recovery. Do not invent production
  users, downtime or cloud telemetry.
- Cloud comparisons require clear resource/workload
  assumptions, numerical units, price provenance
  as available and sensitivity, not a required
  credit card, live price quote or vendor-specific
  certification. If a quote cannot be verified,
  label its figures as illustrative.
- Independent evaluation may introduce an unfamiliar
  bounded TLS, failed promotion, secret isolation,
  drift, rollback or restore scenario. Provide
  accessible written/recorded/live technical defense
  using the same public criteria without demanding
  Kubernetes, public DNS or paid deployment tools.

### Required summative assessments

- **APP7-AS1** (required deployment artifact, service lifecycle and isolation)
  - Outcomes: APP7-O1, APP7-O2, APP7-O3, APP7-O5, APP7-O6, APP7-O12
  - Work: Start **one real locally running APP5/APP6 deployment** from a pinned source/build: use a multi-stage image or equally inspectable managed process, verified immutable digest, nonroot runtime, scoped writable paths and a composed proxy/app/PostgreSQL/worker reference. Observe actual ports, container/process identity, private backend/DB denial, durable state across app replacement, and meaningful `service_healthy`/equivalent readiness (not just Compose startup ordering). Inject failed config/start, wrong file permission and a bounded shutdown with an active request/job; inspect cleanup.
  - Criteria: A reviewer actually launches and inspects the named services, confirms the tested artifact digest and toolchain/source inputs, nonroot privileges and **real denied path and network access**, and verifies durable records survive app replacement. Readiness is checked with a real business dependency and fails for a listening-but-unready backend; conditional health behavior follows the selected Compose/runner version. Failed/partial startup, active-request drain and targeted cleanup are observed, not asserted from a Dockerfile.
  - Evidence: Versioned manifest/container or process configuration, digest, source/toolchain record, startup/shutdown/network/permission test logs, persistent data observations and clean-checkout recipe.

- **APP7-AS2** (required https ingress, environment and credential safety)
  - Outcomes: APP7-O3, APP7-O4, APP7-O5, APP7-O11, APP7-O12
  - Work: On the **same locally running system**, establish two independently isolated stage/release-like environments with a real client-verified local CA HTTPS proxy. Probe correct SAN/hostname/chain, wrong hostname/untrusted CA and trusted proxy versus attacker-controlled `Forwarded`/`X-Forwarded-*`, direct backend/DB access, authenticated cookies/CSRF as relevant and protected resource/tenant denial. Rotate a synthetic session/DB secret, show missing-secret fail-closed behavior and inspect frontend bundle, image/plan/state and logs for leakage; remove any temporary trust changes.
  - Criteria: A real client accepts the intended local hostname **without insecure TLS bypass**, rejects wrong name/root, and protected API/auth state is not spoofed by caller headers or bypass routes. Both environments use distinct data/roles/volumes/secrets with independently observed denial; local CA never counts as public trust. Secrets are absent from exposed artifacts and test logs; if a declarative state or plan would contain synthetic secrets, the course requires secured/redacted handling or explicit redesign rather than assuming a `sensitive` annotation removes storage.
  - Evidence: Local TLS/proxy/environment configuration, positive/negative HTTPS and header traces, network and session tests, rotation record, scoped CA/trust cleanup and residual-risk explanation.

- **APP7-AS3** (required declarative infrastructure, drift and protected state)
  - Outcomes: APP7-O1, APP7-O5, APP7-O6, APP7-O7, APP7-O12
  - Work: Use a versioned free OpenTofu/local provider or equivalent declarative controller to **actually create or configure deployment-relevant resources** for two isolated environments—service/process, ports, network, files/volumes or equivalent runtime-owned targets—rather than merely create an unrelated sample `local_file`. Record plan/apply and inspect the actual affected running resource, show repeated no-op reconciliation, then cause a real bounded drift and re-plan/reconcile. Review and deny a wrong-environment/durable-volume deletion, check state locking/permissions, and destroy/reprovision only a disposable target.
  - Criteria: Named real running-service resources are created and changed by an **actual apply**, not a plan or diagram, while the other environment's application/data and restore target remain untouched. A genuine manually changed resource is detected against state and safely reconciled; unchanged configuration is effectively idempotent under pinned tools/provider. Privileged state/plans are protected, approval and destructive target guards are inspectable, and the teardown proves selected scope without assuming a provider simulates cloud behavior it has not implemented.
  - Evidence: Versioned IaC and local dependency instructions, plan/apply and inventory, repeat/no-op/drift logs, protected state/approval rationale and teardown evidence.

- **APP7-AS4** (required approved artifact promotion, release rollout and stateful compatibility)
  - Outcomes: APP7-O2, APP7-O5, APP7-O7, APP7-O8, APP7-O9, APP7-O11, APP7-O12
  - Work: Extend existing APP6 checks into an independently approved **local CD promotion** of the same content-addressed tested artifact stage→release, with wrong-digest, skipped-gate, untrusted-contributor and missing-approval denial. Run two actual app versions under a controlled traffic selector and an **applied PostgreSQL expand/backfill/contract-compatible** migration. Interrupt/restart a bounded backfill and verify old/new read/write clients and real rows while both versions run. Inject a defective version, shift limited traffic, observe protected user/denied requests, in-flight work and release-specific signals, then execute a **real safe switch back or verified forward repair** that accounts for committed data/files/jobs.
  - Criteria: Both environments run the **same reviewed digest** when promoted, and source/gate/approval record and operator privileges correspond to actual locally enforced decisions; hosted-only OIDC/environment permissions are explicitly labeled untested if not exercised. The mixed-version client/data matrix and interrupted resumed backfill show independent database truth, and contraction does not break a still-running old writer. Bad-release traffic actually fails, is stopped/redirected and recovered without leaking identities, dropping committed data or claiming a code revert reverses external effects. Health checks alone do not prove safe user work.
  - Evidence: Versioned CI-to-CD workflow and release manifest, digest and permission model, old/new compatibility matrix and SQL migration, smoke/negative tests, traffic-shift timeline, failure, rollback/repair and data checks.

- **APP7-AS5** (required consistent backup, independent restore and measured recovery)
  - Outcomes: APP7-O3, APP7-O5, APP7-O9, APP7-O10, APP7-O11, APP7-O13
  - Work: Define **beforehand** a numerical synthetic recovery point and time objective for the already running APP7 product. Create a real consistent `pg_dump`/supported archive from populated PostgreSQL, capture version/warnings, SHA-256 and access/snapshot scope, then restore into a **separately named clean disposable database instance**, never onto the original source or an unrelated environment. Deliberately verify the presence/absence of cluster-global **roles, tablespaces and parameter privileges** (`pg_dump` alone excludes them), reconstruct needed globals safely, and independently check constraints, two-tenant authorization and an authenticated user workflow. Inspect private files, job state and external effects outside dump scope; measure **observed** complete restore/validation time and last recoverable data marker and distinguish logical snapshot from WAL/PITR.
  - Criteria: The restore runs successfully in an independently verified target with correct version, role/privilege/extension dependencies, row constraints and authorized/denied HTTP behavior; a dump command/checksum alone is insufficient. Accidental source or other-environment destruction is prevented and separate retained backup remains protected. RPO/RTO observations cite real recoverable records, timings and scope, not guessed final commits or hypothetical production availability. Object/worker/global-setting exclusions and difference between a consistent logical dump, physical backup and true point-in-time recovery are documented.
  - Evidence: Backup artifact/checksum, scope and retention notes, disposable loss/restore transcript, DB and user-journey tests, timings, non-DB gaps and recovery runbook.

- **APP7-AS6** (required deployment incident, shared responsibility and cost review)
  - Outcomes: APP7-O1, APP7-O4, APP7-O8, APP7-O11, APP7-O12, APP7-O13, APP7-O14, APP7-O15
  - Work: Cause a **new** actual deployment-specific TLS/proxy trust, secret rotation, ingress, readiness or environment failure distinct from AS4's bad application release and AS5's restore exercise. Observe a real protected user-task impact in the running local release, correlate version/TLS/network/DB/job data using APP6 privacy-safe signals, compare at least two possible causes, contain and correct the defect, then verify local HTTPS, authorized/forbidden actions and persistent state with measured response/recovery intervals. Separately compare **two feasible** hosting/provider responsibility models and compute a transparent illustrative monthly budget for compute, DB, storage/backup, ingress/egress, logging and sensitivity with disclosed units/rates/assumptions.
  - Criteria: The independent incident is reproducibly observed before repair and the remedy demonstrably restores the deployed protected task and denies forbidden traffic, rather than recycling AS4/AS5 logs or presenting a narrative-only drill. Redacted timeline distinguishes measured impact/recovery from inference/missing telemetry and updates an operational runbook. Provider obligations and cost alternatives follow actual assumed units, volume/rate arithmetic and sensitivity; unverifiable prices are explicitly illustrative, not fabricated live quotations.
  - Evidence: Observed incident/telemetry/recovery trace, updated runbook and security/DB checks, hosting option diagram, shared responsibility and budget/sensitivity worksheet.

- **APP7-AS7** (required integrated deployed product and independent operational defense)
  - Outcomes: APP7-O1, APP7-O2, APP7-O3, APP7-O4, APP7-O5, APP7-O6, APP7-O7, APP7-O8, APP7-O9, APP7-O10, APP7-O11, APP7-O12, APP7-O13, APP7-O14, APP7-O15, APP7-O16
  - Work: Deliver **one cumulative deployed APP5 application** with APP6 quality gates, content-addressed least-privilege runtime, correctly verified local HTTPS, two isolated environments, real applied service-relevant IaC, explicit digest approval/promotion, two-version compatible stateful rollout, an observed bad-release recovery, a **separate actual PostgreSQL backup/restore** and a distinct incident and provider/cost defense. **Reference independently accepted APP7-AS1–AS6 observations** rather than rebuilding seven demonstrations or pasting duplicate reports. Independently investigate and repair an unfamiliar bounded TLS, wrong artifact, drift, approval, migration, permission or restoration fault, then run targeted regression from a clean pinned free local setup.
  - Criteria: An assessor can reproduce actual named running resources, verified TLS and denial, artifact/environment isolation, chosen promotion decision, real old/new writes, recovered data and user task with only the documented free local dependencies. **AS7 cannot excuse missing/failing AS1–AS6 competence.** The new fault has observed before/after correction and preserves earlier data, auth, release, restore and operational invariants. Public CA, hosted pipeline privileges, production-scale availability and PITR assurances remain honestly unclaimed unless separately actually demonstrated.
  - Evidence: One versioned deployable source, pinned local toolchain/provider and reproducible start/stop instructions; an **outcome-to-previously-accepted-AS1–AS6 evidence index**, digests and targeted independent TLS/IaC/release/restore observations, unfamiliar-fault regression, actual protected user/DB/file/job verification, cost assumptions and reviewable accessible operational defense.

### Completion decision and historical revision protection

Completion requires acceptable inspectable decisions for
`APP7-AS1` through `APP7-AS7` covering
`APP7-O1` through `APP7-O16`. A green CI pipeline
or running server alone cannot establish network
trust, safe stateful deployment, recovery or independent
operational competency. Untrusted TLS, unnecessary
privilege, cross-environment data leakage, invalid
artifact promotion, failed restoration or unsupported
rollback claims must be corrected before passing.

Preserve course and OEE revision, tested source/artifact
digests, environments and fixture identities, assessed
IDs, observed failures and recovery, measured restore
scope/RPO/RTO, verification transcripts, technical
defense and reviewer decision under
[OEE Evidence Rules](../../spec/evidence-rules.md).

APP7 remains an OEE `v0.2.0` **draft** with
the **already published** APP5 + APP6 direct prerequisites;
APP3 remains in their transitive closure. The old
nine-week checkpoint format and APP3 + APP6 direct
prerequisites are historical, not changes pending in
this reassessment. APP8/APP9 and electives already
have published draft curricula. This editorial review
does **not** establish learner-`tested`, independently
`verified` or accredited status, rewrite another
course's graduation requirements, or automatically
reclassify historical learner evidence or change
OEE Workspace/content/0xNAND revision pins.

### Public non-mandatory study references

These public resources support review of technology
and standards without introducing hidden requirements.

- [Docker multi-stage builds](https://docs.docker.com/build/building/multi-stage/)
  and [Docker Compose](https://docs.docker.com/compose/)
  for minimal artifacts and locally reproducible services.
- [Caddy automatic HTTPS](https://caddyserver.com/docs/automatic-https)
  for local/internal CA and public ACME distinctions.
- [OpenTofu core workflow](https://opentofu.org/docs/intro/core-workflow/)
  for reviewed plan, apply, state and drift.
- [PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup.html)
  for logical dump, physical backup and WAL-PITR boundaries.
- [OWASP CI/CD security guidance](https://owasp.org/www-project-top-10-ci-cd-security-risks/)
  for artifact, privilege and delivery trust controls.
- [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
  for incident/release and recovery reasoning.
- [HTTP Semantics RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html)
  for proxy and method contracts.
