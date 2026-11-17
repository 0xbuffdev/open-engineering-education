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

### Module 1 — Release Engineering, Environment Model and Operational Responsibility

#### Outcomes

- APP7-O1
- APP7-O11
- APP7-O14

#### Lessons

1. **Deployment history and operational purpose** — Trace manual server releases to verified artifacts, staged rollouts and declarative infrastructure without confusing DevOps with one product.

2. **APP5 and APP6 capability handoff** — Reuse the authenticated product, tests, telemetry and SLIs while identifying new release and recovery obligations.

3. **User journey as operating criterion** — Define which protected business transaction must succeed before and after a deployment.

4. **Architecture context and resource map** — Draw React assets, Fastify service, PostgreSQL, ingress, private files, worker and clients with actual boundaries.

5. **Threat and shared-responsibility inventory** — Assign accountability for OS, network, TLS, identity, data, secrets and incident decisions.

6. **Availability, safety and recoverability** — Define observable operational acceptance without claiming cloud uptime or verified SLO attainment.

7. **Deployment strategy selection** — Choose a small modular-monolith environment over premature clusters and microservices.

8. **Evidence and revision provenance** — Record platform/tool versions, synthetic tenants, resource ownership, tested boundaries and missing observations.

9. **Cold-start review** — Identify missing startup dependencies, stale state and unverified service assumptions before a first release.

*Optional practice — release-readiness audit:* Show why passing unit tests alone does not prove safe ingress, restoration or rollback.

### Module 2 — Linux Processes, Service Supervision and State

#### Outcomes

- APP7-O2
- APP7-O3
- APP7-O5
- APP7-O12

#### Lessons

1. **Process and user boundaries** — Inspect UID/GID, working directory, process environment, file ownership and open sockets.

2. **Supervision and Graceful Process Termination** — Use systemd, a controlled service runner or suitable process manager and verify restart/stop policy; trace SIGTERM and bounded shutdown through HTTP requests, database connections and worker loops.

3. **Startup, liveness and readiness** — Distinguish existence, listening, dependency readiness and end-to-end user-workflow success.

4. **Filesystem and volume semantics** — Separate ephemeral app data, temporary files, persisted database and recoverable private uploads.

5. **Least privilege at runtime** — Run without unnecessary root capabilities and test a denied write or sensitive path read.

6. **Resource and connection budgets** — Apply feasible memory/CPU/connection limits and observe service behavior under safe constraints.

7. **Crash-loop controls** — Diagnose invalid environment, failed migrations and restart storms with useful error reporting.

8. **Controlled failure cleanup** — Inspect open connections, timers, volumes and network handles after both successful and failed stop.

*Optional practice — process incident:* Repair an instance that reports healthy while it cannot commit data or exit cleanly.

### Module 3 — Container Images, Runtime Isolation and Artifact Provenance

#### Outcomes

- APP7-O2
- APP7-O3
- APP7-O7
- APP7-O12

#### Lessons

1. **Image versus running container** — Distinguish immutable filesystem layers, runtime mounts, process identity and persisted data.

2. **Multi-stage build design** — Separate TypeScript compilation/development tools from a minimal production-runtime stage.

3. **Context control and .dockerignore** — Exclude credentials, build caches, test-only inputs and private files before building.

4. **Base image and dependency provenance** — Pin reviewed versions/digests and identify actual versus assumed supply-chain properties.

5. **Tags versus immutable digests** — Record the tested image digest and why mutable latest tags are unsafe promotion references.

6. **Non-root image execution** — Configure an explicit user, service-owned writable path and no unjustified privileged capabilities.

7. **Secrets and build layers** — Test synthetic secret leakage and use safe runtime injection rather than image ARG/ENV secrets.

8. **Runtime health, stdout and shutdown** — Verify process exit, signal forwarding and structured logs under the selected engine.

9. **Image replacement and volumes** — Replace the app image and independently verify intended PostgreSQL and file persistence.

*Optional practice — image review:* Reduce oversized build contents and repair root-required writes without breaking the user task.

### Module 4 — Composed Application Services and Network Exposure

#### Outcomes

- APP7-O1
- APP7-O3
- APP7-O4
- APP7-O12

#### Lessons

1. **Local composed topology** — Run real proxy, app, database and optional worker as isolated free processes or Compose services.

2. **Ports and bind addresses** — Inspect loopback versus public binds, service DNS and published host ports.

3. **Private database boundaries** — Deny unneeded inbound DB access and prove clients only reach the intended ingress.

4. **Persistent volumes and environment names** — Give staging and release-like instances distinct paths, service identities and database resources.

5. **Process/service readiness order** — Wait on meaningful readiness rather than brittle sleeps or mere successful process creation.

6. **Network failure taxonomy** — Trace DNS, TCP, proxy, TLS and upstream timeout failures to the owning layer.

7. **Worker and job lifetimes** — Demonstrate safe worker restart with durable intent or honest pending outcomes.

8. **Service and data cleanup** — Remove only named disposable resources, preserving a separate backup/restore target.

*Optional practice — isolation defect:* Fix a shared staging database or leaked unpublished backend port and verify the corrected topology.

### Module 5 — TLS, Reverse Proxies, DNS and Forwarded Trust

#### Outcomes

- APP7-O4
- APP7-O5
- APP7-O11
- APP7-O12

#### Lessons

1. **Network-to-origin trace** — Reuse APP1 HTTP/DNS concepts to map client hostname through TLS proxy to local Fastify.

2. **Certificate chain and hostname verification** — Inspect leaf issuer, SAN and scoped trust root without turning off TLS checks.

3. **Local CA versus public ACME** — Explain trusted public DNS validation and why a local internal CA is only trusted where installed.

4. **Caddy or equivalent verified HTTPS** — Operate local HTTPS with an explicitly scoped CA and document cleanup of trust changes.

5. **Host routing and HTTPS redirection** — Verify host/SNI match, intended route redirects and response behavior.

6. **Upstream budgets and errors** — Bound proxy request body, timeout and unavailable-backend response semantics.

7. **Forwarded header authenticity** — Reject attacker-chosen X-Forwarded-Proto/Host/For unless supplied through a trusted ingress.

8. **Cookies, origins and CSRF** — Exercise Secure/HttpOnly/SameSite policies consistent with authenticated local HTTPS.

9. **Certificate expiry and renewal planning** — Distinguish public and local issuance, expiration checks and safe planned rotation.

*Optional practice — HTTPS defect:* Detect an invalid certificate or spoofed forwarded identity and repair the trust boundary.

### Module 6 — Stage/Production-like Environments, Secrets and Access

#### Outcomes

- APP7-O5
- APP7-O7
- APP7-O12

#### Lessons

1. **Environment purposes and isolation** — Define test/staging/release-like intent and differences that can affect production behavior.

2. **Build-time and runtime configuration** — Prevent private credentials and service secrets being compiled into React bundles or images.

3. **Configuration schema and fail-closed startup** — Reject missing, contradictory or unsafe environment parameters before receiving traffic.

4. **Separate tenant and database identity** — Ensure each local stage has independent roles, data/volume paths and keys.

5. **Scoped secret injection** — Supply synthetic tokens or passwords through controlled runtime interfaces without plaintext commits.

6. **Credential rotation** — Rotate a test DB/session identity with overlap/revocation and verify service access continuity.

7. **Operator authorization** — Assign release, secrets and restoration privileges to separate roles with reviewable actions.

8. **Audit and sensitive output checks** — Inspect logs, IaC plans and artifacts for leaked secrets and unnecessary personal data.

*Optional practice — environment leak:* Repair an implicit development-secret fallback during release-like startup.

### Module 7 — Infrastructure as Code, State Protection and Drift

#### Outcomes

- APP7-O1
- APP7-O5
- APP7-O6
- APP7-O12

#### Lessons

1. **Desired and actual resource state** — Explain declarative resource graphs, remote ownership and the limits of configuration as truth.

2. **OpenTofu or equivalent applied local provider** — Select a free local provider or controller that genuinely creates and inspects real resources.

3. **Plan review and controlled apply** — Read resource-add/change/destroy consequences before applying to explicitly approved test targets.

4. **Two isolated environment instances** — Parameterize state, ports and resource names and prove independent creation.

5. **Idempotent repeated reconciliation** — Show no unintended changes on an unchanged re-plan and re-apply.

6. **Deliberate drift and refresh** — Mutate a local resource, detect drift and choose a justified correction.

7. **State sensitivity and locking** — Protect file permissions, secrets, shared state concurrency and disposal of review artifacts.

8. **Guard destructive replacement** — Reject unsafe planned deletion of a persistent volume or restoring into the wrong target.

9. **Local infrastructure teardown** — Destroy only the selected disposable resources and verify backup and other environment remain intact.

*Optional practice — drift decision:* Review a stale plan and explain why it must be regenerated after resource or state changes.

### Module 8 — Trusted CI-to-CD Artifact Promotion and Release Audit

#### Outcomes

- APP7-O2
- APP7-O5
- APP7-O7
- APP7-O8
- APP7-O12

#### Lessons

1. **CI versus CD ownership** — Reuse APP6 validation while separating environment targeting, approval and release credential authority.

2. **Build once and promote** — Use exactly the reviewed digest/hash across stage and release environments.

3. **Release pipeline graph** — Sequence quality gates, artifact verification, stage smoke, approvals and release checks.

4. **Untrusted contribution isolation** — Verify an untrusted PR cannot access deployment keys or privileged workflow events.

5. **Approval and concurrency policies** — Enforce release ownership and prevent overlapping destructive environment changes.

6. **Protected secrets and OIDC boundaries** — Explain hosted ephemeral identities honestly and exercise only locally verifiable controls.

7. **Smoke tests and denial cases** — Run actual authorized and forbidden requests before and after promotion.

8. **Manifest and release identity** — Record source SHA, artifact digest, config, migration state, decision actor and outcome.

9. **Rollback approval and artifact availability** — Verify access to a previously known-good immutable artifact and compatible data.

*Optional practice — wrong-artifact incident:* Reject a floating tag, changed digest or skipped approval with documented failing evidence.

### Module 9 — Traffic Shifts, Health Signals and Bad-Release Recovery

#### Outcomes

- APP7-O7
- APP7-O8
- APP7-O9
- APP7-O11
- APP7-O13

#### Lessons

1. **Deployment versus feature release** — Separate installed candidate, enabled feature and actual traffic shift decisions.

2. **Rolling, blue-green and canary tradeoffs** — Compare spare capacity, state compatibility, failure blast radius and local testability.

3. **Running old and new versions** — Keep two local versions and a controlled proxy/route selection.

4. **Readiness and draining** — Stop sending new requests to unready instances and handle bounded in-flight work.

5. **User-centered smoke checks** — Verify login/authorized mutation/denial rather than trusting only /health.

6. **Release-correlated SLI observations** — Compare errors, latency and job state by release version using APP6 telemetry.

7. **Guarded traffic-shift criteria** — Declare success thresholds, responder and rollback/forward-repair triggers in advance.

8. **Defective candidate drill** — Inject a route, config or incompatible response regression and observe real client symptoms.

9. **Observed rollback or forward repair** — Execute a safe previous-version switch or compatible fix and verify business state.

*Optional practice — unready-canary defect:* Repair a traffic switch that routes users to an instance with no database access.

### Module 10 — Stateful Releases and Database Schema Compatibility

#### Outcomes

- APP7-O8
- APP7-O9
- APP7-O10
- APP7-O13

#### Lessons

1. **Old/new app/DB compatibility table** — Test previous and current clients/services against actual schema revisions.

2. **Expand-before-contract principle** — Add compatible columns/fields and phase deprecation without losing readers/writers.

3. **Backfill planning** — Bound transaction size, idempotence, lock/IO effects and restartable partial progress.

4. **Mixed-version writes** — Demonstrate old and new services safely writing during an intended rollout window.

5. **Contract and client compatibility tests** — Verify prior API consumers before dropping a field or changing required semantics.

6. **Rollback and irreversible effects** — Trace committed writes, queue actions, private files and delivered notifications that code rollback cannot undo.

7. **Forward repair and pause strategy** — Choose safe migration repair or traffic stop when old code cannot read revised data.

8. **Migration audit and drift** — Record schema revision, backfill counts, affected constraints and data integrity without private records.

*Optional practice — incompatible deployment:* Seed a schema change that breaks an old writer, detect it and correct staging.

### Module 11 — Real PostgreSQL Backup, Restore and Recovery Objectives

#### Outcomes

- APP7-O3
- APP7-O5
- APP7-O10
- APP7-O11
- APP7-O13

#### Lessons

1. **Choose recovery point and time goals** — Define measured local RPO/RTO objectives for a synthetic protected user workflow.

2. **Logical dump versus physical backup** — Explain pg_dump, base backup and WAL archiving differences using PostgreSQL's supported methods.

3. **Consistent actual backup** — Take a real dump from an active disposable PostgreSQL dataset and retain version/manifest information.

4. **Backup scope and security** — Preserve backup independently from the primary, restrict access, record checksum and describe encryption/retention.

5. **Simulated data loss only in test targets** — Verify isolated database and destructive command scope before any drop/corruption experiment.

6. **Restore into a named separate instance** — Restore with supported PostgreSQL tooling and verify actual completion/status.

7. **Data, authorization and job/file validation** — Inspect relational constraints, tenant isolation, task completion and missing non-DB resources after restore.

8. **Measure actual restoration** — Compute latest recoverable commit and observed outage, distinguishing goals from achieved local numbers.

9. **Point-in-time recovery limits** — Explain that a logical dump cannot prove WAL-based PITR, and what archival/continuity evidence is needed.

10. **Operational runbook and rehearsal** — Write backup/restore/check/cleanup steps, wrong-target safeguards and a future re-test cadence.

### Module 12 — Operational Monitoring, Incident Response and Handoff

#### Outcomes

- APP7-O8
- APP7-O10
- APP7-O11
- APP7-O13

#### Lessons

1. **Monitoring as a release decision input** — Translate APP6 user-focused SLIs into pre/post deployment operational gates.

2. **Release metadata correlation** — Connect source/digest, API config, DB migration, request and job errors without privacy leaks.

3. **Misleading green health** — Reproduce /health success when protected business work fails and design a more meaningful readiness signal.

4. **Incident severity and responder roles** — Assign decision, diagnosis, communication and documentation ownership for a local exercise.

5. **Containment and change freeze** — Decide safe traffic stop, secret rotation, configuration switch or restore to protect users/data.

6. **Actual controlled incident** — Break the deployed TLS/proxy/secret/release path and record observed user impact.

7. **Recovery verification** — Check authenticated and forbidden requests, durable records, background jobs and old/new compatibility afterward.

8. **Blameless timeline and handoff** — Publish evidence, causal hypotheses, completed recovery and runbook changes, not invented production history.

*Optional practice — bad signal diagnosis:* Identify alert noise versus a real rollout regression and justify mitigation steps.

### Module 13 — Hosting Choices, Shared Responsibility, Capacity and Cost

#### Outcomes

- APP7-O1
- APP7-O11
- APP7-O14
- APP7-O15

#### Lessons

1. **Self-managed VM, containers and managed compute** — Compare portability, control, patch responsibility and scaling boundaries.

2. **Managed PostgreSQL and object storage** — Evaluate backups, access, recovery guarantees and provider versus application duties.

3. **Networking and edge services** — Compare DNS, load balancing, TLS, CDN, private networks and per-byte egress risks.

4. **Realistic workload assumptions** — Specify concurrency, monthly requests, data growth, retention, backup and service uptime goals.

5. **Total Resource Costs, Egress and Logging** — Calculate instance-hours, allocated disk, backup bytes and requests from disclosed rates; include network transfer, storage operations, metrics retention and data restore costs.

6. **Scale strategy and failure modes** — Discuss vertical/horizontal changes, cold starts and dependency bottlenecks without APP8 deep modeling.

7. **Responsibility and vendor lock-in** — Allocate IAM, OS patching, certificates, recovery, secret management and exit costs.

8. **Sensitivity and cost guardrails** — Change traffic/storage/egress assumptions and compare alternatives and budget alert triggers.

*Optional practice — economical deployment decision:* Reject an unjustified complex stack and defend a simpler reliable design.

### Module 14 — Integrated Deployed Product and Independent Operational Defense

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

1. **Choose a bounded APP5 product** — Reuse authenticated React/Fastify/PostgreSQL source and APP6's trusted quality tests and signals.

2. **Publish deployment/secret/backup contract** — State topology, trust, environment names, resource IDs, recovery objectives and rollback decision policy.

3. **Build artifact and private local services** — Package source-provenance image/process, run least privilege and preserve only intended durable data.

4. **Configure verified TLS ingress** — Connect a scoped local CA reverse proxy, verify hostname and deny untrusted forwarded identity.

5. **Apply IaC to two isolated environments** — Reproduce stage/release-like real local resources with reviewed plans and drift evidence.

6. **Promote approved immutable artifact** — Use one digest with separate gate/approval and meaningful protected user task smoke test.

7. **Stage compatible stateful change** — Validate old/new services, schema/data change and in-flight/job consistency.

8. **Seed, detect and recover a bad release** — Trigger actual release failure and execute safe rollback or forward repair.

9. **Back up and restore PostgreSQL** — Induce only disposable loss, restore independently and measure RPO/RTO and object/job coverage gaps.

10. **Compare provider and cost alternatives** — Make workload-based budget, responsibility/security and sensitivity choices.

11. **Independent unfamiliar operational change** — Repair an unseen TLS, credential, release or restoration defect and defend evidence and limitations.

## Completion requirements

All **sixteen APP7 outcomes** must be demonstrated through
the **seven required summative assessments**. The same evolving
deployed APP5 product may satisfy multiple requirements when the
claimed user actions, release transitions, restored records and
operational evidence can be examined independently. Formative
lesson investigations and optional paid provider exercises are
not additional graduation gates.

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
  - Work: Package a reproducible APP5/APP6 app using a multi-stage container image or equivalently inspectable managed process. Verify source/artifact digest, non-root runtime, bounded mutable paths, private network and durable PostgreSQL state during replacement; inject a failed boot, denied file access and graceful shutdown with active work.
  - Criteria: The tested artifact is reproducible from recorded local inputs; no synthetic secrets or unnecessary build-only tools are shipped. Safe start/exit/readiness, least privilege, resource cleanup and intended persistent data survival are independently observed, while container-engine limitations are disclosed.
  - Evidence: Versioned manifest/container or process configuration, digest, source/toolchain record, startup/shutdown/network/permission test logs, persistent data observations and clean-checkout recipe.

- **APP7-AS2** (required https ingress, environment and credential safety)
  - Outcomes: APP7-O3, APP7-O4, APP7-O5, APP7-O11, APP7-O12
  - Work: Configure stage and release-like isolated deployments behind a controlled reverse proxy with real locally verified HTTPS. Test hostname and trust root, untrusted forwarded headers, direct-backend exposure, cookie/credential assumptions, missing synthetic secrets and safe rotation; demonstrate appropriate CA trust cleanup.
  - Criteria: An actual client validates TLS without insecure bypass; local CA is not misrepresented as public trust. Spoofed identity, unintended backend/DB exposure and cross-environment access are rejected; secrets do not appear in source, image layers, static assets, IaC state or public logs.
  - Evidence: Local TLS/proxy/environment configuration, positive/negative HTTPS and header traces, network and session tests, rotation record, scoped CA/trust cleanup and residual-risk explanation.

- **APP7-AS3** (required declarative infrastructure, drift and protected state)
  - Outcomes: APP7-O1, APP7-O5, APP7-O6, APP7-O7, APP7-O12
  - Work: Apply open-source IaC with an actual local provider or equivalent declarative resource controller, creating two isolated and named local deployment environments. Capture plan/apply/replan, introduce a controlled manual resource drift, reconcile it, reject a potentially destructive persistent-state change and clean only the disposable target.
  - Criteria: Real named resources are created, observed and recreated; a diagram or non-applied plan is insufficient. Repeated unchanged configuration is effectively idempotent, drift is observed, resource/state access is protected, and destructive actions require real review and target confirmation.
  - Evidence: Versioned IaC and local dependency instructions, plan/apply and inventory, repeat/no-op/drift logs, protected state/approval rationale and teardown evidence.

- **APP7-AS4** (required approved artifact promotion, release rollout and stateful compatibility)
  - Outcomes: APP7-O2, APP7-O5, APP7-O7, APP7-O8, APP7-O9, APP7-O11, APP7-O12
  - Work: Extend APP6 CI with locally runnable promotion, approval, immutable artifact verification and smoke gates. Deploy two versioned services behind controlled traffic selection, implement a staged PostgreSQL expand/backfill/contract-compatible change, seed a defective candidate and actually execute a rollback or verified forward repair.
  - Criteria: Untrusted contributions, incorrect digest, failed gates or missing approval cannot promote; the same tested artifact is used in both environments. Old/new readers/writers and authenticated/denied users remain safe as documented, release readiness is measured, and rollback does not falsely undo committed database/file/job effects.
  - Evidence: Versioned CI-to-CD workflow and release manifest, digest and permission model, old/new compatibility matrix and SQL migration, smoke/negative tests, traffic-shift timeline, failure, rollback/repair and data checks.

- **APP7-AS5** (required consistent backup, independent restore and measured recovery)
  - Outcomes: APP7-O3, APP7-O5, APP7-O9, APP7-O10, APP7-O11, APP7-O13
  - Work: Define numerical local recovery goals, take and protect a real consistent PostgreSQL backup from live synthetic records, induce data loss only in a verified disposable environment, restore into a separately named database and re-connect a compatible application. Verify constraints, tenant ownership, private file/job consistency and the actual protected user task; report measured recovery time and latest recoverable commit.
  - Criteria: Backup passes a real independent restore and authorized/denied checks, not just a creation command. Restore targets cannot affect shared data; RPO/RTO goals and observed local values are distinguished, and a logical dump is not falsely represented as WAL/PITR or a complete object-store backup.
  - Evidence: Backup artifact/checksum, scope and retention notes, disposable loss/restore transcript, DB and user-journey tests, timings, non-DB gaps and recovery runbook.

- **APP7-AS6** (required deployment incident, shared responsibility and cost review)
  - Outcomes: APP7-O1, APP7-O4, APP7-O8, APP7-O11, APP7-O12, APP7-O13, APP7-O14, APP7-O15
  - Work: Cause a controlled TLS, proxy, secret or release defect in a running local deployment and use version-correlated APP6 telemetry to detect affected user tasks. Contain, repair or roll back, verify security/business state and document a responder timeline. Compare two feasible hosting models and build an illustrative monthly cost with compute, DB, backup, storage, egress, logging and varied workload assumptions.
  - Criteria: The incident genuinely impacts the local running service and recovery is demonstrated and recorded, with no fabricated real-user history. After recovery TLS, proxy, authorization and durable business outcomes are tested. Provider responsibilities and cost estimates use declared units, formulas and sensitivity rather than invented real-time quotes.
  - Evidence: Observed incident/telemetry/recovery trace, updated runbook and security/DB checks, hosting option diagram, shared responsibility and budget/sensitivity worksheet.

- **APP7-AS7** (required integrated deployed product and independent operational defense)
  - Outcomes: APP7-O1, APP7-O2, APP7-O3, APP7-O4, APP7-O5, APP7-O6, APP7-O7, APP7-O8, APP7-O9, APP7-O10, APP7-O11, APP7-O12, APP7-O13, APP7-O14, APP7-O15, APP7-O16
  - Work: Deliver and reproduce one operational APP5 product using APP6 trusted quality checks, verified locally scoped HTTPS, least-privilege deployable artifacts, isolated staging and release-like environments, applied declarative resources, approved digest promotion, stateful compatible releases, observability, a real bad-release recovery and an independently tested PostgreSQL restoration. Explain a provider/cost decision and respond to an unfamiliar bounded deployment or recovery defect.
  - Criteria: A reviewer using documented free, locally provisioned tools reproduces actual normal, denied, TLS, stateful release, drift, failure, restored-data and security checks, without a paid account or public domain. Promotion trust, data integrity and operations remain valid under the unfamiliar change; unsupported cloud/production reliability claims are identified honestly.
  - Evidence: Versioned deployment/release/IaC/TLS/backup source, signed-off review decisions and digests, clean local setup, synthetic users/DB, negative and normal tests, bad-release and restore timelines with recovery metrics, cost models and accessible independent technical defense.

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

APP7 retains its code and title but replaces the legacy
nine-week checkpoint/lab contract and APP3 + APP6
prerequisites with an outcome-driven OEE `v0.2.0`
**draft** requiring APP5 + APP6 directly. APP3
remains required transitively. Historical learner
records remain pinned to their actual prior course
revision; they cannot be silently interpreted as
passing these new outcomes. APP8/APP9 and APP10–APP16
remain separately reviewed migrations. OEE Workspace,
content/book mappings and 0xNAND consumer pins must
be reconciled deliberately rather than auto-upgraded.

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
