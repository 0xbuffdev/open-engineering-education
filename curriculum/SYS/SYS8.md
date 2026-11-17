# SYS8 — Systems Design & Production Engineering

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** [SYS6](SYS6.md), [SYS7](SYS7.md)
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional)

> [Systems Engineering](README.md) · [Course format](../../spec/course-format.md) · [Design guide](../DESIGN-GUIDE.md)

## Overview

**SYS8 converts already tested systems mechanisms into defensible operational architecture and a reviewable release decision.** [SYS6](SYS6.md) establishes replicated-state failure models, durability, quorum and consistency; [SYS7](SYS7.md) establishes workload characterization, measurement accuracy, capacity/queue analysis and privacy-safe telemetry. SYS8 does **not** teach a second consensus algorithm, reimplement profiler tools, duplicate APP product/web deployment, or assume paid Kubernetes/cloud certification. It teaches a distinct engineering obligation: making explicit choices about **service guarantees and SLOs, component/failure domains, overload and recovery budgets, secure configuration, reproducible lifecycle and compatibility, actionable alerting, tested incident/rollback procedures and independent go/no-go review**.

**Required cumulative work:** Select a previously assessed SYS4-style network service, SYS6-style replicated service or a publicly supplied functionally equivalent nonprivileged synthetic artifact. Publish a bounded service and operator scenario, compare two credible architectures, design SLI/SLO/error-budget policies and measured resource headroom, then provide a repeatable package with typed config, safe startup, health/readiness, clean shutdown, rollback constraints, a small monitoring/incident runbook and independent fault/recovery evidence. **Reuse the same service** for the architecture, capacity, lifecycle, readiness and unfamiliar-constraint assessments rather than create multiple unrelated products. Actual execution is required for locally testable startup, overload, fault, backup/restore or rollback paths; infrastructure beyond the learner's control can be modeled transparently.

**Precision in claims:** A service-level indicator must state **eligible observations, numerator, denominator, time window, missing data and user-visible success criteria**. A written objective is not a contractual SLA or evidence that a real service achieves it; an error budget is an explicit decision policy under a given sampling frame. SLOs, RTO/RPO, failure-domain independence, rollback and recovery are distinct claims. A three-replica local simulation has **one shared host/power/network fault domain**; synthetic partitions and a successful restart cannot establish geographic availability, physical disk persistence or a promised disaster-recovery window. An engineer may correctly **block a release** or document limited local readiness when required guarantees cannot be defended.

**Safe reference environment:** Stable Rust/Cargo, a nonprivileged Linux user, learner-owned temporary fixtures, loopback-only services and deterministic load/fault scripts, finite resource limits, synthetic secrets and a basic local process supervisor/script are sufficient. Optional container/VM and other open tooling may aid teaching, but no root, public Internet listener, commercial observability platform, organization-specific production access, real credential, paid cloud or mandated 24/7 on-call rotation is required. Source provenance and secure development are assessed as **bounded design and operating practices**, not a claim of compliance certification. Include accessible text equivalents to architecture diagrams and meaningful alternatives to external dashboards.

**Time and assessment integrity:** The **12–16-week** duration at **10–15 focused hours/week** (about 120–240 focused hours) remains provisional for study, design alternatives, bounded experiments, corrective changes, handoff and technical defense. These are estimates, not attendance or completion gates. All twelve existing SYS8 outcomes and five existing summative IDs are preserved. Revisions of work/criteria/evidence apply prospectively to this source; historical completed learner decisions retain their original curriculum/spec revision.

## Learning outcomes

- **SYS8-O1:** Translate a systems brief into measurable functional requirements, workload assumptions and reliability/capacity targets.
- **SYS8-O2:** Select component boundaries, communication, persistence and consistency trade-offs from declared failure and resource constraints.
- **SYS8-O3:** Design explicit failure domains, redundancy, retries, circuit breaking and graceful degradation without inventing availability guarantees.
- **SYS8-O4:** Define service-level indicators, objectives and error-budget or risk policies appropriate to a bounded operating context.
- **SYS8-O5:** Estimate CPU, memory, disk, network and queue capacity from measured demand and include justified safety margins.
- **SYS8-O6:** Design secure nonprivileged configuration, secrets handling, limits and change-control policies for a systems component.
- **SYS8-O7:** Specify reproducible packaging, startup, readiness, health, deploy, rollback and version-compatibility behavior.
- **SYS8-O8:** Design actionable monitoring, incident detection, escalation and operator procedures using diagnosable service signals.
- **SYS8-O9:** Conduct risk-driven load, soak, fault and recovery exercises with independent safety and acceptance oracles.
- **SYS8-O10:** Compare architecture alternatives by total operational complexity, cost, performance and failure consequences.
- **SYS8-O11:** Perform an independent production-readiness review, documenting unresolved risks and legitimate release blockers.
- **SYS8-O12:** Defend a revised systems architecture after an unfamiliar failure, capacity or operational constraint.

## Modules

### Module 1 — Systems Requirements, Workloads and Service-Level Contracts

#### Outcomes

- SYS8-O1
- SYS8-O4
- SYS8-O10
- SYS8-O11

#### Lessons

1. **From SYS6/SYS7 evidence to operating decisions** — Start with SYS6's distributed consistency and crash-recovery boundaries and SYS7's independent latency, load and profiler evidence. Turn those outputs into a system-design decision without reteaching consensus internals, queueing theory or a benchmark tutorial.
2. **Actors, operations and user-visible outcomes** — Specify a bounded service's users/operators, correct requests, explicit rejection, timeouts, state change and accepted degraded behavior. Separate user-visible availability from a process merely listening on a TCP port.
3. **Workload envelope and seasonal demand** — Define request mix, payloads, concurrency, offered arrivals, burst/steady distribution, state size and expected growth using recorded synthetic fixtures; name which assumptions are measured versus hypothetical.
4. **SLI numerator, denominator and population** — Choose a request-based or time-based SLI with exact eligible events, successes, exclusions, measurement windows and treatment of synthetic requests, missing telemetry and unknown completion. Show a counterexample where excluding failed requests fabricates perfect reliability.
5. **Latency, correctness, freshness and durability targets** — Define a small set of meaningful user-focused SLOs with thresholds and units, including when a fast incorrect response does not count as healthy. Distinguish latency distribution, replication freshness and persistence guarantees instead of conflating them with raw uptime.
6. **SLO arithmetic and error budgets** — For a declared window and SLI, compute target compliant events, allowed bad events and remaining budget after failures; discuss policy under low request volume, no data and nonstationary load instead of assuming every service needs a popular 99.9% target.
7. **SLAs, objectives and capability claims** — Separate internally chosen objectives from contractual SLAs, and a local modeled recovery goal from an empirically established production guarantee. Do not pretend a synthetic traffic fixture creates customer obligations.
8. **Privacy, staffing and infrastructure constraints** — Record team size, maintenance capacity, data retention, access, available hosts, security restrictions, budget and legal/organizational obligations as explicit scenario assumptions, not an invisible mandatory enterprise environment.
9. **Acceptance and traceability matrix** — For each important functional, error-handling, SLO, overload, recovery and maintenance requirement, publish the observable evaluation, source artifact and legitimate failure condition; distinguish blocker from negotiable non-goal before selecting an architecture.

*Optional formative feedback:* Calculate the failure budget for a fixed synthetic request population; revise the numerator/denominator after discovering timeouts omitted from monitoring.

### Module 2 — Architecture Ownership, Consistency and Failure-Domain Decisions

#### Outcomes

- SYS8-O2
- SYS8-O3
- SYS8-O10

#### Lessons

1. **Monolith, local processes and service split** — Compare one deployable service, two communicating processes and a fixed three-member replica set for the same demand and staffing model; account for new protocols, ownership boundaries and operations instead of assuming microservices are inherently resilient.
2. **Data ownership and state transitions** — Map authoritative data, caches, queues, durable state and request identity to components and identify which transitions must be atomic, ordered or explicitly ambiguous after a failed call.
3. **Consistency versus degraded access** — Reuse SYS6's documented quorum, stale-read and dedup guarantees to decide which requests can be served in minority partition, which must fail closed and when a stale answer must be plainly labeled.
4. **Failure-domain inventory** — Distinguish process, host, filesystem, disk, power, network, rack or geographic failure domains and identify common causes. Three learner-owned processes on one laptop are not evidence of independent-host redundancy.
5. **Dependency graphs and critical paths** — Trace one client operation through front end, handler, persistence and any optional peer/dependency; label synchronous waits, retry edges, timeouts, queue bounds and first component to fail when one dependency stalls.
6. **Single points of failure and redundancy cost** — For two architecture alternatives, reason about lost quorum, leader identity, shared storage and deployment/control-plane dependencies; state which failures are tolerable only under independently realized infrastructure.
7. **Stateful versus stateless replacement** — Explain what can restart safely from configuration alone and what requires durable replay, backup restoration or replication; prevent a restart policy from making duplicate non-idempotent effects.
8. **Architecture options and rejection rationale** — Evaluate at least two credible alternatives against operation guarantees, workload limits, failure domains, maintenance expertise, cost and security exposure, with explicit criteria that could change the chosen answer.
9. **Evidence-based architecture diagrams** — Produce a component, authority/data-lifecycle and failure-domain diagram or equivalent text table linked to public behavior and test fixtures; drawings without invariants are not substitutes for engineering reasoning.

### Module 3 — Capacity, Backpressure, Resilience and Recovery Objectives

#### Outcomes

- SYS8-O3
- SYS8-O4
- SYS8-O5
- SYS8-O9

#### Lessons

1. **Demand and capacity ledger** — Translate SYS7's measured service time, offered load and working-set data into requests/s, CPU budget, memory bytes, disk bytes, descriptor count, queue slots and network throughput under explicit instance assumptions.
2. **Headroom under variable demand** — Compute required capacity under one average and one burst scenario, choosing a stated safety margin and explaining why a measured high-load point is not guaranteed sustainable production capacity.
3. **Bounded queues and rejection semantics** — Select max connections, outstanding work, per-client and aggregate buffers, queue length and deadlines; calculate worst-case resource demand before tuning and show when fast refusal is safer than unbounded waiting.
4. **Timeout, retry and deadline composition** — Budget an end-to-end deadline across upstream/worker/dependency stages; model retry fan-out, max attempts, backoff with jitter and dedup/idempotency obligations to prevent cascaded overload or duplicate effects.
5. **Circuit breakers, bulkheads and degraded modes** — Specify state and trigger thresholds for circuit opening, half-open probes, resource isolation and recovery; compare against simpler immediate refusal and prevent breaker logic from silently inventing a strongly consistent answer.
6. **Saturation and autoscaling limits** — Analyze load-driven scale-up/down using only a small numerical model or free local executor; distinguish scaling stateless workers from safe scaling of quorum-bearing state, startup latency and shared-bottleneck limits.
7. **Memory, disk and retention growth** — Budget caches, WAL/snapshots, compaction temporary space, error logs and stale file retention over time. Identify a write-amplification or full-disk scenario where a service must stop acknowledging durability rather than keep accepting writes.
8. **RTO, RPO and measured recovery** — Define recovery time objective, allowable data-loss point and exact event/clock boundaries, then distinguish objective, modeled restart experiment, and unsupported site-disaster guarantee.
9. **Backup, restore and reconciliation contracts** — Specify a consistent backup point, restore compatibility/checksum, access controls and verification against an independent data oracle; a copied directory or green startup is not automatically a valid restore.
10. **Failure-budget-informed capacity choice** — Connect capacity, timeouts, rejected work and SLO bad-event policy, disclosing that intentional rejection may preserve safety while still consuming user-facing availability or latency budget.

### Module 4 — Secure Service Configuration, Trust and Supply-Chain Provenance

#### Outcomes

- SYS8-O6
- SYS8-O7
- SYS8-O10

#### Lessons

1. **Threat modeling against bounded deployment** — Name untrusted clients, local filesystem writers, operators, build inputs and network peers; identify what the chosen reference service can and cannot protect in a one-host unprivileged fixture.
2. **Typed configuration and startup validation** — Specify schema, defaults, valid ranges and precedence for config file/environment/CLI settings; reject missing required credentials, impossible capacities, wildcard exposure and incompatible storage format before serving traffic.
3. **Least privilege and local isolation** — Run as a normal user on ephemeral loopback ports with restricted fixture paths and file permissions. Compare what OS permissions, Linux namespaces and a guest VM do without requiring privileged container configuration.
4. **Secret generation, storage and rotation boundaries** — Use only disposable synthetic tokens/credentials; never commit or log them. Demonstrate safe injection, redaction, replacement and revocation behavior, with honest limitations of environment variables, logs and host permissions.
5. **Input and resource abuse defenses** — Verify length/schema rejection, no arbitrary file/process action and bounded concurrent/queued work from earlier courses; apply explicit security acceptance rules instead of presuming safe Rust or a reverse proxy secures a service.
6. **Dependency and build provenance** — Record exact source revision, Rust toolchain, manifest/lockfile, dependency versions and build artifacts with reproducible commands; explain why a digest or SBOM inventory aids traceability but is not itself a supply-chain security audit.
7. **Safe release and change authorization** — Define who can approve release/config changes, what review and test evidence is required, how sensitive values stay separate from code and how a change may be canceled/reverted under an incident.
8. **Security claims and unresolved exposure** — Distinguish integrity checksums from authentication/encryption, localhost-only training behavior from exposed Internet service and a locally repeatable package from a NIST-compliant or security-certified product.

*Optional formative feedback:* Review a release config with an unsafe wildcard listener, a secret-bearing log field and an unbounded queue; select justified startup blockers and a safe revision.

### Module 5 — Reproducible Packaging, Rollout, Health and Rollback

#### Outcomes

- SYS8-O6
- SYS8-O7
- SYS8-O9
- SYS8-O10

#### Lessons

1. **Release artifact and environment contract** — Build from a clean checkout with pinned toolchain, known Cargo lockfile and local target assumptions; identify binary, config, logs, persistent data, fixture version and executable startup contract.
2. **Deployable layout and directory lifecycle** — Specify nonprivileged paths for state, temporary artifacts, logs and backups; validate ownership and minimum permissions and ensure an isolated install cannot overwrite unrelated files.
3. **Startup readiness versus liveness** — Define liveness as 'can the process make local progress?' and readiness as 'can it legitimately serve supported traffic?', including dependency/quorum checks where claimed. A TCP accept or unconditional 200 response alone does not prove usable state.
4. **Startup sequencing and durable recovery** — Order config validation, storage inspection/replay, listener exposure, optional peer coordination and readiness advertisement; fail closed if incompatible or unrecoverable durable state would make promised responses unsafe.
5. **Graceful stop, handoff and in-flight ambiguity** — Define stop-admission, bounded drain, cancellation, checkpoint or flush when applicable and hard-stop fallback. Distinguish client-visible acknowledgment from in-flight outcomes without pretending SIGTERM guarantees remote delivery.
6. **Rolling, blue-green and local replacement choices** — Compare recreate, staged local replacement and blue/green-style routing in terms of state ownership, readiness, spare capacity and client retry semantics; a cloud orchestrator is not necessary to reason about release order.
7. **Storage/protocol compatibility matrix** — Publish old/new binary, RPC and on-disk schema compatibility and a rollback-safe cut line; show why a forward-only schema/data migration can make reverting the program binary unsafe.
8. **Rollback drill and state preservation** — Run one bounded release change followed by a deliberately failed verification and corrective rollback or documented safe refusal; verify accepted data, configuration and error contract against independent fixtures.
9. **Release gates and artifact records** — Define minimum tests, dependency/source provenance, operator approval, synthetic fault pass, restore/rollback result and monitored post-release acceptance before a decision to promote or stop a build.

### Module 6 — Operational Signals, Actionable Alerts and Incident Procedures

#### Outcomes

- SYS8-O4
- SYS8-O8
- SYS8-O9
- SYS8-O11

#### Lessons

1. **SLO-focused monitoring rather than metric volume** — Reuse SYS7's privacy-safe counters, queues, traces and histograms to monitor user-facing valid responses, latency and unknown outcomes; map each to an operator action rather than demand a new commercial telemetry stack.
2. **Synthetic black-box versus internal signals** — Distinguish end-to-end client probe of a documented operation from internal CPU, memory, storage and quorum state; show a healthy process metric with an unhealthy user-visible result.
3. **Error-budget burn and alert thresholds** — Compute bad-event rate and burn relative to the budget over a declared window, with numerator/denominator and minimum-sample/low-traffic handling. Design a fast/page and slower/ticket policy without claiming one threshold fits all products.
4. **False positives, missing data and alert fatigue** — Classify intermittent telemetry gaps, deploy spikes, maintenance and natural workload variability; define silence/escalation rules and ensure 'no metrics' is not silently treated as perfect reliability.
5. **Monitoring cardinality and privacy budget** — Bound per-label combinations, retained traces and diagnostic IDs, sanitizing payloads, secret values and user metadata. Explain how increased observability cost can itself saturate the service.
6. **Incident detection, roles and escalation** — Specify a small-team on-call scenario with incident severity, discoverer, decision owner, communications, first responder and optional escalation; document what can be supported with a solo maintainer rather than requiring a 24/7 enterprise rotation.
7. **First-minute stabilization and rollback decisions** — Distinguish user impact, suspected root cause and confirmed event; choose safe mitigation such as rejection, pausing rollout or isolating background work before invasive fixes.
8. **Status communication and factual timelines** — Draft an incident update with affected operations, time bounds, confidence level, mitigation and next checkpoint, while protecting identifying data and distinguishing measured events from inferences.
9. **Post-incident learning and prevention** — Build a blameless causal timeline, contributing conditions, detection gap, regression test, responsible follow-up and risk acceptance; do not attribute an outage solely to a worker when systemic causes remain.

### Module 7 — Controlled Load, Fault and Restore Readiness Exercises

#### Outcomes

- SYS8-O3
- SYS8-O5
- SYS8-O7
- SYS8-O8
- SYS8-O9

#### Lessons

1. **A finite and safe exercise plan** — Use the same SYS4 or SYS6 service fixture with declared CPU, memory, disk, port, process, runtime and request limits; define normal/negative acceptance oracles before faults are injected.
2. **Steady, burst and overload probes** — Replay two bounded traffic envelopes, showing offered/admitted/completed/failed work, queue depth and CPU or memory headroom without silently dropping slow requests from the denominator.
3. **Dependency stall and retry storm** — Inject a delayed peer or handler and compare bounded timeout/retry/backoff/queue policy against a naïve unbounded retry history, keeping the load finite and independent of external hosts.
4. **Disk full and storage recovery** — In a disposable constrained directory or simulated adapter, inject full disk or failed sync, then verify correct refusal, preserved acknowledged state and documented restart/replay or supported restore.
5. **Readiness and liveness conflict** — Inject a missing quorum, corrupted local state or unavailable dependency while the process remains running. Confirm that readiness and monitoring communicate the contractual inability to serve strong operations.
6. **Failed rollout and rollback preconditions** — Exercise a newly built artifact/config, deliberately failed health or compatibility check, and safe rollback/hold decision; verify that no irreversible schema migration was silently undone.
7. **Backup restoration and integrity checks** — Recover a known fixture snapshot/backup into a clean isolated directory, compare independently derived key/state and refusal outcomes, and record which broader disaster-recovery properties were not tested.
8. **Soak, resource leakage and cleanup** — Run a bounded short-duration repetitive workload with finite data to inspect descriptor, queue, log and heap growth, then prove cleanup and disclose why such a test is not a months-long reliability demonstration.

### Module 8 — Architecture Decision Records, Cost and Independent Readiness Review

#### Outcomes

- SYS8-O1
- SYS8-O2
- SYS8-O4
- SYS8-O8
- SYS8-O10
- SYS8-O11

#### Lessons

1. **Decision record tied to a concrete choice** — State context, considered options, controlling constraints, evidence and consequences of one architecture/reliability decision. Avoid writing an ADR merely to satisfy a document template.
2. **Operational ownership and toil** — Estimate who can operate, troubleshoot, upgrade and restore the proposed system; include human-response time, unknown dependencies and repeated manual work as costs of an elaborate architecture.
3. **Cost, capacity and failure comparison** — Evaluate realistic relative CPU, memory, disk, storage redundancy, transfer, instrumentation and staff burden of alternatives with common units and admitted uncertainty, avoiding invented commercial pricing.
4. **Release criteria versus educational completion** — Define release/no-go criteria for a bounded teaching service. Distinguish 'course outcome demonstrated' from 'ready for real customer data or production Internet exposure' with independent risk ownership.
5. **Material blockers and accepted risk** — Classify integrity loss, unverified recovery, exposed secrets, public listener or unbounded resource use as blockers when violating the published contract; distinguish lower-priority limitations with accountable mitigation.
6. **Evidence matrix and contradiction resolution** — Map SLO, failover, deployment, config security, runtime, recovery and operator handoff claims to actual artifact, test and observed result. Resolve cases where a promising diagram contradicts a negative exercise trace.
7. **Independent operator reproducibility** — Have another reviewer follow a cold-start, load, failure or rollback procedure against a fresh disposable environment, or use a clearly independent scripted variant with reviewer inspection; report confusing or unsafe steps rather than rewriting history.
8. **Go/no-go board and conditional decision** — Reach a defendable approve, block or limited local-release decision with named conditions, unresolved risks, time/owner for corrective action and a statement of what controlled tests cannot establish.

### Module 9 — Integrated Systems Design, Operational Handoff and Unseen Defense

#### Outcomes

- SYS8-O1
- SYS8-O2
- SYS8-O3
- SYS8-O4
- SYS8-O5
- SYS8-O6
- SYS8-O7
- SYS8-O8
- SYS8-O9
- SYS8-O10
- SYS8-O11
- SYS8-O12

#### Lessons

1. **Choose one existing service and operating scenario** — Select a prior SYS4 or SYS6 implementation or free equivalent synthetic service, along with finite demand, access, failure and staffing assumptions; no unrelated project, paid provider or new Raft implementation required.
2. **Publish a user-visible service contract** — Combine valid operation semantics, SLI denominator/success rule, SLO targets, retry/admission constraints, RTO/RPO objectives and an honest list of unsupported production claims into a testable public brief.
3. **Produce alternatives and one target architecture** — Compare at least two component/data-authority arrangements under measured demand, actual resource/failure constraints, ownership and operational complexity, retaining a decision rationale that can change with new evidence.
4. **Deliver a safe reproducible operating package** — Supply build source/lockfile, configuration schema, nonprivileged startup, readiness/liveness checks, bounded service data paths, secure synthetic secret policy, clean stop/restart and rollback conditions.
5. **Quantify capacity and resilience predictions** — Present measured client work, CPU/memory/disk/network/queue estimates, headroom and failure behavior with assumption-sensitive arithmetic before running finite local traffic and outage fixtures.
6. **Demonstrate monitoring, recovery and rollback** — Use synthetic privacy-safe signals, alert tests, an incident runbook, one controlled fault or resource saturation and one independently checked restoration or rollback/hold decision.
7. **Obtain an independent operator review** — Reproduce essential startup/health/change/failure/restore paths from a fresh fixture and document contradictions, limitations, release blockers and actionable reviewer feedback.
8. **Defend an unfamiliar operational change** — Accept a reviewer-supplied new traffic spike, failed dependency, leaked config, unrecoverable disk or unsafe rollback scenario; form two competing hypotheses/architectural options before investigating and revise the decision with new evidence.
9. **Issue the responsible release recommendation** — Present the minimum evidence packet, measured and modeled guarantees, rejected design, remaining risks and a justified go/limited-go/no-go judgment, including why a student local rehearsal is not a production certification.

*Optional formative feedback:* Take a fresh reviewer constraint that invalidates the preferred rollout path and show how the choice, runbook and release gate must change without falsifying earlier evidence.

## Completion requirements

**Five required summative evaluations establish SYS8-O1–SYS8-O12.** Study exercises, optional cloud exercises, drawing architecture diagrams and attending incident simulations do not earn automatic credit. AS1 publishes and defends a service architecture; AS2 sizes its resource/recovery envelope; AS3 packages it safely; AS4 independently reviews and executes essential operations; AS5 challenges the design with a genuinely new constraint. A **single bounded service and its evidence** can satisfy all five assessments when the distinct competency claims are independently evaluated. No unsupported production deployment, paid service or formal compliance certification is required.

- **SYS8-AS1** — Measurable Service Contract and Architecture Decision
  - **Outcomes:** SYS8-O1, SYS8-O2, SYS8-O3, SYS8-O4, SYS8-O10.
  - **Work:** Define a concrete system and operating scenario with functional/user-visible success and refusal rules, workload envelope, SLI numerator/denominator, explicitly scoped SLO/error-budget policy and consistency/durability constraints. Compare **at least two viable component architectures** under the same failure domains, staffing, data ownership and resources; map each dependency, retry, quorum and degraded-operation boundary. Independently solve a small SLO/error-budget calculation including bad and missing requests.
  - **Criteria:** Success, error, timeout, unavailable/unknown and measurement-window semantics are unambiguous, and an SLI never hides rejected or timed-out eligible requests to fabricate reliability. Both alternatives preserve required correctness or explicitly reject requests rather than pretending stale state is strong; named shared-failure domains prevent unsupported independent-host/high-availability claims. The chosen architecture follows reasoned workload/cost/staffing/security trade-offs and documents what would change the decision. Calculations, limitations and excluded capabilities remain consistent with SYS6 safety guarantees and SYS7 offered-load evidence. An arbitrary SLO value or diagram without inspectable operations is insufficient.
  - **Evidence:** Public requirements and SLI/SLO grammar, synthetic operation/workload fixture, error-budget arithmetic, component/data/authority/failure-domain and dependency graphs or accessible equivalents, two-option decision matrix, rejected alternative, safety/availability assumption ledger and trace-to-outcome register.

- **SYS8-AS2** — Capacity, Overload, Dependency and Recovery Model
  - **Outcomes:** SYS8-O3, SYS8-O4, SYS8-O5, SYS8-O9.
  - **Work:** Calculate and publish CPU, memory, disk/temporary storage, file descriptor, network and work-queue budgets for a **measured baseline** and a changed peak-demand or failure scenario, using SYS7-style raw workload evidence. Include a numeric retry/deadline/queue policy, safety headroom and a defined RTO/RPO/restore-objective scenario. Execute **at least two bounded local experiments**, one involving overload, backpressure or dependency stall and one involving process restart, persistence error or controlled restore, with separately derived accepted/refused/recovered-state oracles.
  - **Criteria:** Units, service capacity, admitted versus offered demand, peak versus steady state and finite resource caps are mathematically consistent; headroom is justified by observations and assumptions, not declared a universal percentage. Timeout/retry/breaker/degradation rules do not accidentally cause unbounded fan-out, stale strong reads or duplicate non-idempotent effects. Tests show correct visible responses, bounded memory/queue/disk behavior and independently predicted recovery within the declared test fixture; missing independent hosts or real power failures do not become a guaranteed production SLA, physical RPO or RTO. SLO/error-budget impact counts refused and failed eligible operations according to AS1's contract.
  - **Evidence:** Capacity and resource ledger with two worked numeric regimes, benchmark configuration/raw results and confounders, failure-domain/retry-state policy, bounded load and controlled fault scripts/seeds, observed client work/queue/resource traces, recovery-state oracle and measured-versus-target RTO/RPO statement.

- **SYS8-AS3** — Secure Package, Startup, Health and Safe Change Lifecycle
  - **Outcomes:** SYS8-O6, SYS8-O7, SYS8-O8.
  - **Work:** Produce a clean-checkout build and **nonprivileged local operating package** for the same service: source/toolchain/dependency pinning, typed configuration and safe defaults, synthetic-secret injection/redaction, bounded data paths, startup/replay/readiness/liveness, clean stop and restart, release gates, and a **real scripted rollback or rigorously demonstrated incompatibility-aware refusal**. Publish a short operator runbook with one actionable alert/incident decision and a before/after release protocol/storage compatibility table.
  - **Criteria:** An independent tester reproduces baseline startup from synthetic data, valid/invalid config outcomes, permission and secret-handling tests, accurate readiness failure when a required dependency/quorum/storage state is unavailable, and bounded shutdown/recovery. No tested path exposes secrets in logs or publishes a wildcard listener accidentally. Rollback may proceed only when persisted schema, binary/protocol version and data state permit it, with an observed invariant-preserving correction or an explicit no-rollback blocker. Build digests/lockfiles support provenance but are not misrepresented as a security audit, and neither a Docker image nor a paid orchestrator is a mandatory output.
  - **Evidence:** Versioned source/build/run scripts and lockfile, declarative schema/example config with synthetic credentials, redacted logs/permissions checks, readiness/liveness transition tests, clean start/stop and release/rollback fixtures, compatibility matrix, operator playbook and unresolved risk statement.

- **SYS8-AS4** — Independent Operational Readiness and Incident Review
  - **Outcomes:** SYS8-O1, SYS8-O4, SYS8-O7, SYS8-O8, SYS8-O9, SYS8-O10, SYS8-O11.
  - **Work:** Prepare an independently reproducible readiness packet and have a **separate reviewer or explicitly independent scripted test plus reviewer inspection** follow a fresh start, service check, bounded failure/alert, restart/restore or rollback, and decision procedure. Demonstrate an actionable synthetic incident with a timeline, impact classification, symptom alert, mitigation, communication and risk register. Apply written go/limited-go/no-go acceptance criteria from before the review.
  - **Criteria:** The reviewer can distinguish proven source/test behavior from paper-only capacity/redundancy/production claims and verify at least one controlled incident and recovery or honest refusal without hidden organizational tools. Measurable SLI definitions and client-level failures inform the alert, including unknown/missing telemetry and minimum sample constraints. Material release blockers (unsafe data loss, corrupted/unrestorable state, exposed real secret, unauthorized listener, inaccurate health or unbounded overload) are neither hidden by a green build nor automatically waived because the service is educational. Reviewer discrepancies prompt a documented correction and rerun or a legitimate hold/no-go decision; privacy-safe artifacts and remaining risk ownership are preserved.
  - **Evidence:** Readiness checklist traced to outcome/acceptance claims, independent fresh-run logs/scripts, test results and negative cases, SLO/burn-rate or symptom-alert calculation, incident role/mitigation/status update, annotated fact-versus-hypothesis timeline, residual-risk and conditional release decision.

- **SYS8-AS5** — Unfamiliar Operational Constraint and Architecture Defense
  - **Outcomes:** SYS8-O2, SYS8-O3, SYS8-O5, SYS8-O6, SYS8-O9, SYS8-O10, SYS8-O11, SYS8-O12.
  - **Work:** Respond to a **previously unseen** small reviewer-supplied or transparently generated scenario, such as a shared-disk failure invalidating advertised redundancy, a workload spike saturating a retry queue, a compromised synthetic secret, unsafe backward schema migration, missing telemetry or partial restore. **Before** investigating, state two competing causal explanations or architecture options and an expected discriminating observation. Revise service design/config, resource and recovery assumptions, runbook or release decision, then verify independent negative/previously correct cases in a finite local exercise or source-grounded model.
  - **Criteria:** The learner identifies exactly which previous assumption or acceptance invariant changed, computes at least one material consequence for capacity, consistency, readiness, security or recoverability and rejects an unsafe mitigation rather than silently weakening a promised guarantee. Evidence either supports a corrected bounded local behavior or justifies a defensible release blocker/hold decision; revised alternatives, staffing/cost/complexity and residual risk are explicitly stated. The analysis separates one-host fixture evidence from independent infrastructure properties and preserves regression behavior and source provenance. A rehearsed checklist without a new discriminating decision or causal explanation cannot satisfy SYS8-O12.
  - **Evidence:** New scenario/seed, pre-measurement hypotheses or options, amended architecture/SLI/resource/compatibility ledger, discriminating trace and independently computed expected results, targeted change or release-refusal record, regression checks, accountable risk decision and a written/recorded/live technical defense.

### Curriculum ownership, accessibility and scope

SYS6 already assesses replicated logs, quorums, deduplication, durability and consistency safety; SYS7 already assesses profiling, queueing and telemetry measurement science; SYS4 already assesses the basic multi-client listener and overload correctness. SYS8 **consumes their evidence** for service-level targets, failure-domain architecture, resource headroom, nonprivileged secure operation, versioned release, actionable incident response and responsible go/no-go judgment. It does not add a mandatory cloud account, IaC platform, Linux root operation, commercial telemetry backend, new consensus engine, container orchestrator, real company secret or production traffic. [SYS9](SYS9.md) later integrates the chosen systems mechanism and operational-readiness evidence into a learner's independently defended capstone; SYS8 is still a `course`, not the capstone or credential authorization.

The reference is an unprivileged synthetic test service with finite traffic, resource and disk limits. Text operation tables, ASCII architecture/failure-domain diagrams and accessible reviewer notes can replace visual dashboard or whiteboard drawings without reducing causal assessment. Any incident and security exercise uses synthetic credentials and local fixtures, never unauthorized scans, live credential exfiltration, destructive recovery on user files or unsupported high-availability deployment claims. A systems design review may properly finish as **no-go** when important guarantees cannot be demonstrated: that can satisfy the educational reasoning outcomes without implying the actual product is release-ready.

### Historical evidence, reproducibility and readiness

Stable outcome IDs **SYS8-O1–SYS8-O12** and assessment IDs **SYS8-AS1–SYS8-AS5** are preserved, while the more explicit release, SLO arithmetic, resource and incident criteria apply to **this course revision**. Prior authentic learner artifacts remain tied to their historical course/specification revisions, not automatically regraded or declared complete by new editorial wording. Each assessment decision records the course/source revision, reviewer, mapped outcome/assessment IDs, independent expected and actually observed fixture results, decision, limits and any unresolved blockers. Repository lint or a completed code review does **not** promote educational status from `draft`; real learner trials and independent qualified review are necessary.

## Optional disciplinary references

These freely available sources support study and source accuracy. They are not hidden paid requirements or evidence of accreditation:

- [Google SRE Workbook — Implementing SLOs](https://sre.google/workbook/implementing-slos/) and [Error Budget Policy](https://sre.google/workbook/error-budget-policy/) — user-centered indicators, objectives and operational release trade-offs.
- [Google SRE — Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) — symptom-based, actionable monitoring and operational evidence.
- [AWS Builders' Library — Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) and [Avoiding insurmountable queue backlogs](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/) — bounded resilience and dependency-overload reasoning.
- [NIST SP 800-218 — Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) — risk-aware release provenance and security practices; this course does not claim NIST certification.
- [OpenTelemetry Metrics](https://opentelemetry.io/docs/specs/otel/metrics/) — portable concepts for counters, histograms and bounded telemetry attributes.
