# APP6 — Software Quality & Engineering Operations

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `core`
**Prerequisites:** [APP5](APP5.md) — Full-Stack Application Architecture
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (provisional; validate with learner/reviewer evidence)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Improve the quality, security, maintainability and
operational trustworthiness of an existing, integrated
full-stack application through **risk-based evidence**
rather than tool checklists. Start from the cross-layer
React/Fastify/PostgreSQL product and authenticated,
cache/job/file workflows in [APP5](APP5.md). Design
proportionate verification, deterministic failure
investigations, least-privilege continuous integration,
reproducible dependency/build inputs, practical
software supply-chain review, privacy-aware
observability, user-centered service-level indicators,
incident analysis, performance experiments and
documented reliability improvements.

**APP5 is the sole direct prerequisite.** Its transitive
closure already contains APP20, APP3, TypeScript,
Node, browser and database engineering. APP6 is not
a learner's first testing course: APP18 and each
subsequent implementation course already introduce
real tests and debugging. Here learners **choose the
right evidence**, establish systematic change gates,
investigate subtle failure and monitor meaningful
quality/reliability outcomes across a whole system.

The reference application remains a cohesive, free,
locally reproducible APP5 vertical slice with synthetic
tenants, client/service, disposable PostgreSQL,
optional bounded job worker and local simulated
external dependencies. Use a versioned pipeline
definition (for example GitHub Actions) **plus a
locally runnable equivalent**, open-source testing,
analysis, metrics and reporting tools, and pinned
local environment/dependency artifacts. No paid
CI account, cloud, production deployment, public
load target, proprietary observability vendor,
production credential or real personal data is
required. Hosted workflow permissions, OIDC and
release protections are studied explicitly but
must not be claimed as experimentally verified
when only a local simulation was performed.

**System-level quality strategy is APP6's subject.**
APP5 already verifies its individual end-to-end
features; APP6 teaches how to select and sustain
efficient test layers, challenge false confidence,
prevent and reproduce flakes, keep dependencies
and build artifacts trustworthy, triage security
findings and turn incidents into measurable
engineering changes. High coverage, a green
scanner, an SBOM or an output hash is not in
itself a security certification or supply-chain
assurance level. If investigating SLSA source
or build tracks, use the actually selected version
and distinguish collected local evidence from
an attested verified level.

**SLOs and performance experiments require a
precise measurement contract.** Define eligible
events, success/failure conditions, observation
windows and reference environment. An illustrative
error-budget calculation or synthetic request trace
does not establish real service uptime. Unbounded
metrics labels, trace baggage, request bodies
and credentials can create resource and privacy
risks; inspect what telemetry actually records,
and state what is missing or sampled.
Performance comparisons must account for
request distributions, generator saturation,
warm-up, caching, concurrency, samples and
timing noise. A small local load test cannot
prove global production capacity.

**APP7 remains distinct:** APP6 prepares versioned
checks, safe build inputs, observable service
behavior, incident diagnosis, reliability targets
and a justified engineering improvement. APP7
teaches deployed environment provisioning,
containers, CI/CD deployment, secrets for
real infrastructure, release/rollback, backups,
restore drills and live operational practice.
APP8 then tests production-scale architecture,
capacity, cost and failure containment. APP6
must not require public deployment, a live SLO
or a production-on-call shift.

Security/failure investigations must use local
synthetic data and bounded conditions. Build
untrusted contributor scenarios and fake
credential leaks in disposable branches only,
never with a real token. Test denial of access,
cache isolation, user error visibility and
authenticated work under controlled faults;
record the actual traces and limitations.
A blameless retrospective is an analysis of
causal system conditions and corrective actions,
not proof that a real organization experienced
the synthetic incident.

The proposed duration and workload are planning
estimates, not empirically established readiness.
Progression moves from risk and layered testing
to quality automation, signals, reliability
investigation and independent defense. Formative
lessons are preparation; **only the seven explicitly
required assessments** below form the summative
completion contract.

## Learning outcomes

- **APP6-O1:** Evaluate the risks of an existing full-stack application and define proportionate, user-centered software quality, security, reliability and maintainability acceptance criteria with a traceable evidence strategy.
- **APP6-O2:** Design and justify an efficient layered verification strategy across pure units, components, contracts, HTTP/database integration, browser journeys and failure/security boundaries, explicitly identifying what each test cannot prove.
- **APP6-O3:** Apply examples, boundaries, invariants, property-based or generative cases, mutation-based test assessment and controlled fault injection to reveal defects missed by happy-path assertions.
- **APP6-O4:** Build independently repeatable, isolated tests and fixtures, diagnose flaky behavior due to time, concurrency, randomness, external dependencies or shared state, and verify a durable correction without hiding failures with retries.
- **APP6-O5:** Design and verify a least-privilege continuous-integration quality pipeline with meaningful change gates, dependency ordering, untrusted contribution boundaries and clear failure reports using a publicly inspectable runner definition.
- **APP6-O6:** Produce and compare pinned dependency and toolchain inputs, executable build/test recipes and reviewable artifacts, explaining caching, environment drift, reproducible-build limitations and integrity checks.
- **APP6-O7:** Integrate and evaluate static analysis, formatting, type checking, dependency/security scans and appropriate dynamic checks; prioritize material findings by exploitability and impact rather than treating scanner output as conformance.
- **APP6-O8:** Create a reviewable dependency inventory/SBOM and source/build/artifact provenance record, verify relevant hashes and trust boundaries, and distinguish local provenance evidence from unearned supply-chain assurance levels.
- **APP6-O9:** Establish safe configuration and credential handling across development and CI, proving that untrusted changes cannot obtain privileged secrets or alter privileged releases and that logs/artifacts avoid sensitive data.
- **APP6-O10:** Instrument an existing application with bounded, privacy-aware structured logs, metrics and trace correlation; select useful stable attributes and distinguish actual observations, sampling and missing telemetry.
- **APP6-O11:** Define user-centered service-level indicators, objectives, windows and error budgets; reason quantitatively about observed compliance, actionable alert thresholds and burn-rate limitations without claiming production availability from fixtures.
- **APP6-O12:** Perform a reproducible incident investigation from symptoms to competing hypotheses, causal evidence, containment, verified repair, recovery decisions and a blameless learning record.
- **APP6-O13:** Design and interpret controlled performance and load experiments using credible workloads, percentile latency/error/throughput/resource data, warm-up and client-side constraints, identifying a verified bottleneck and regression.
- **APP6-O14:** Evaluate and improve a maintainability problem through deliberate API/design refactoring, code review, dependency boundaries, documented trade-offs and regression coverage without adding unjustified architectural complexity.
- **APP6-O15:** Plan and test quality/reliability/security failure scenarios involving corrupted configuration, denied access, resource limits, dependency outage, job replay, supply-chain compromise and unsafe monitoring, documenting verified controls and remaining risk.
- **APP6-O16:** Reproduce, improve and independently defend an integrated full-stack reliability/quality upgrade with CI, verifiable tests, safe dependency/configuration inputs, useful telemetry, an SLO/performance investigation and an unfamiliar bounded regression or incident.

## Modules

### Module 1 — Quality Engineering Scope, Risk and Decision Evidence

#### Outcomes

- APP6-O1
- APP6-O2
- APP6-O14
- APP6-O16

#### Lessons

1. **Quality is a verified property of behavior** — Distinguish functional correctness, robustness, security, accessibility, maintainability and operability from merely having green tests.

2. **The historical role of engineering quality** — Explain how increasingly integrated programs shifted from manual checks to automated regression and evidence-based change control; avoid depicting automation as a substitute for review.

3. **Carry forward APP5's integrated user journey** — Inspect a typed React, Fastify and PostgreSQL workflow with real tenant boundaries, cache, job and partial-failure policies rather than rebuild the stack.

4. **Quality attributes and trade-off conflicts** — Identify tension between response latency, confidentiality, developer change cost and measured reliability for a bounded user outcome.

5. **Risk Inventory and Verifiable Acceptance Criteria** — Identify likely failure, likelihood uncertainty, impacted users/data and detectability; prioritize observed risks over arbitrary fashionable tooling; derive normal, denied, conflict, failed, recovered, accessibility and maintenance outcomes with measurable thresholds appropriate to a local environment.

6. **Verification traceability map** — Map each critical risk to an appropriate test layer, observable artifact, reviewer and limitation.

7. **Review evidence versus conformance** — Separate evidence that one run passed from a claim of systematic quality, security certification or production availability.

*Optional practice — risk audit:* Compare two proposed quality investments, defend priority using a known failure scenario and identify which tests would remain weak.

### Module 2 — Test Architecture, Realism and Contract Verification

#### Outcomes

- APP6-O1
- APP6-O2
- APP6-O3
- APP6-O14

#### Lessons

1. **Feedback speed versus behavioral coverage** — Explain trade-offs of unit, component, API, database, contract and browser E2E tests without asserting a mandatory universal pyramid shape.

2. **Pure domain and invariants** — Test APP3/APP5 business rules independent of transport and examine unhandled boundary values.

3. **React component interaction tests** — Verify accessible user-visible transitions rather than private render implementation details or brittle snapshots alone.

4. **Framework HTTP integration tests** — Exercise Fastify schema, auth hooks, status/errors and response contracts with a real application factory.

5. **PostgreSQL and transaction fixtures** — Verify constraints, tenant isolation, concurrency and rollback with actual disposable database connections where mocks cannot establish behavior.

6. **API consumers and contract versioning** — Run current and supported previous consumer fixtures against the same service; identify drift in fields, status and error semantics.

7. **Real browser end-to-end journeys** — Test navigation, session expiry, keyboard/focus, pending/job states and partial failures with a browser and local components.

8. **Test Realism and Coverage Limits** — Select fakes for controlled failure/race injection but disclose when a mock cannot prove driver, OS or database behavior; interpret statement/branch coverage and scenario matrices without equating coverage percentages to correctness.

*Optional practice — misplaced-test exercise:* Move a flaky browser test to a stable lower level while retaining one real journey that verifies the integration boundary.

### Module 3 — Invariants, Generative Tests and Mutation Analysis

#### Outcomes

- APP6-O2
- APP6-O3
- APP6-O4
- APP6-O15

#### Lessons

1. **Examples and equivalence partitions** — Choose representative normal, invalid, boundary and authorization cases tied to a real failure hypothesis.

2. **Stateful property and invariant reasoning** — Specify invariants such as no cross-tenant reads, no duplicate committed mutation and bounded resource use without presuming random inputs alone prove them.

3. **Property-based input generation** — Use a free deterministic generator or small reproducible harness with recorded seeds and valid/invalid input strategies.

4. **Shrinking and counterexamples** — Preserve the smallest failing counterexample and explain which input shape or state transition violated the property.

5. **Metamorphic and differential checking** — Compare old/new behavior or property-preserving transformations when a trusted oracle is incomplete.

6. **Mutation testing as test assessment** — Introduce safe local code mutations, inspect survived mutants and improve assertions rather than chase a universal score.

7. **Fault injection and test scope** — Inject an external timeout, job duplicate or failed DB operation under disposable fixtures and distinguish test coverage from proof of general reliability.

8. **Security and negative assertions** — Test denied access, hidden fields and data cleanup; inspect unauthorized DB state rather than only a 403 status.

*Optional practice — mutant repair:* Demonstrate a surviving authorization or retry mutant, add a meaningful failing test and record limitations of the mutation runner.

### Module 4 — Determinism, Test Isolation and Flake Investigation

#### Outcomes

- APP6-O2
- APP6-O3
- APP6-O4
- APP6-O13

#### Lessons

1. **Fixture lifetimes and ownership** — Allocate and clean local database schemas, users, files, ports and processes per test or per isolated suite.

2. **Controlling Time and Randomness** — Replace real waits with controlled clocks for expiry, retries and deadlines where the behavior permits, while retaining one real lifecycle test; record generator seeds and distribution assumptions so a failure can be rerun as the same case.

3. **Concurrency barriers and ordering** — Use controlled scheduling points and independent sessions to reproduce a race rather than rely on sleeps or a lucky interleaving.

4. **Unstable external services** — Simulate third-party failures locally, keep one independent integration boundary and disclose which assumptions are unverified.

5. **Flake diagnosis and evidence** — Classify nondeterministic failures by observable timings, shared state, environment, dependency or invalid assertion before changing code.

6. **Why retries do not fix flakiness** — Explain how retry-on-fail can hide a defect; document temporary quarantine, triage ownership and deadline where necessary.

7. **Isolation and teardown tests** — Detect leaked listeners, handles, workers, stale DB rows and unexpected file artifacts, including partial setup failures.

*Optional practice — intermittent test repair:* Capture a failing seed/timing schedule, fix the root cause and compare repeated controlled runs without claiming zero future flakes.

### Module 5 — Continuous Integration, Change Gates and Trust Boundaries

#### Outcomes

- APP6-O1
- APP6-O5
- APP6-O6
- APP6-O9
- APP6-O15

#### Lessons

1. **CI as automated evidence production** — Distinguish source review, test execution, recorded results, trusted artifact creation and eventual APP7 release deployment.

2. **Stages and DAG of verification jobs** — Order formatting, type checks, unit/integration, security/contract and browser tests with relevant dependencies and transparent failure status.

3. **Versioned pipeline as source** — Write a maintained CI configuration and a local executable equivalent; explain when the hosted syntax cannot be exercised without an account.

4. **Pull request event and trust model** — Separate untrusted external contribution code from protected branches, privileged credentials and artifact publication.

5. **Least privilege for CI tokens** — Declare minimal job permissions, no unnecessary write access, no secret exposure to untrusted forks and review event-specific privilege behavior.

6. **Third-party actions and execution risks** — Pin reviewed actions by immutable commit digest where the platform supports it, examine mutable tags/install scripts and isolate dangerous workflow triggers.

7. **Cache safety and artifact policy** — Design scoped cache keys and restore rules, prohibit privileged reuse of untrusted cache content and validate artifact provenance.

8. **Fail-closed gates with useful diagnoses** — Verify checks fail on seeded test, type, security or contract defects and report actionable causes without leaking environment data.

9. **Local pipeline and hosted differences** — Demonstrate equivalent shell/container execution, record which permissions and event semantics require a real GitHub Actions security review.

*Optional practice — attack on the pipeline:* Inspect an untrusted change that tries to publish an artifact or read a secret and document why the revised job policy prevents it.

### Module 6 — Reproducible Builds, Dependencies and Artifact Integrity

#### Outcomes

- APP6-O5
- APP6-O6
- APP6-O7
- APP6-O8

#### Lessons

1. **Lockfiles and dependency graphs** — Document direct/transitive packages, toolchain versions and integrity resolution; distinguish version constraints from byte-identical installed contents.

2. **Build inputs and environment** — Record OS/runtime, locale/timezone, compiler flags, dependency cache, nonsecret environment values and generated file order.

3. **Clean-checkout and offline reproduction** — Rebuild from a fresh local checkout using pre-provisioned dependencies and synthetic fixtures, documenting genuine missing resources.

4. **Artifact hashes and manifests** — Produce and verify SHA-256 digests plus source revision/input metadata and state which tampering risks they can and cannot detect.

5. **Caches versus reproducibility** — Explain when caches speed execution and when they undermine fresh verification or trust boundaries.

6. **Hermeticity and nondeterministic timestamps** — Investigate an input that changes build bytes and repair it when reasonable; avoid claiming globally reproducible outputs without measured bit-for-bit equivalence.

7. **Dependency updates as change** — Compare locked updates, API breakage, license/advisory implications and rollback/forward remediation in a controlled branch.

8. **Artifacts and deployment ownership** — Prepare versioned trusted inputs and reviewable outputs but defer actual public deployment, cluster rollout and release promotion to APP7.

*Optional practice — build drift:* Reproduce a build mismatch after an unpinned transitive dependency or environment change and verify the repaired documented inputs.

### Module 7 — Static Analysis, Supply-Chain Security and Provenance

#### Outcomes

- APP6-O7
- APP6-O8
- APP6-O9
- APP6-O15

#### Lessons

1. **Static, type and dynamic check boundaries** — Select formatter, linter, type checker, unit/integration, SAST-like and dynamic tests with explicit blind spots.

2. **False positives and exploitable context** — Triage findings by reachability, severity, constraints and actual code path rather than raw vulnerability count.

3. **Dependency advisories and exceptions** — Record affected version, exploit preconditions, maintained fix, owner, expiry and compensating controls for a temporary exception.

4. **SBOM meaning and generation** — Produce a minimal machine-readable CycloneDX or SPDX inventory using a free tool or simple documented exporter; verify included direct and transitive packages.

5. **Source, build and artifact provenance** — Distinguish source revision identity, builder claim, manifest/hash, signed attestation and independently verified provenance.

6. **SLSA tracks and assurance limits** — Review SLSA 1.2 source/build tracks as a reference and explicitly avoid claiming an achieved SLSA level without its full controls and attestations.

7. **Untrusted scripts and dependency execution** — Inspect postinstall scripts, arbitrary CI commands and dependency substitution risk under minimal privileges.

8. **Policy gates and human review** — Fail locally on a seeded material credential/vulnerability finding while documenting accepted false positives and a steward override procedure.

*Optional practice — supply-chain scenario:* Detect a fake package-origin mismatch or unsafe build step, correct inputs and record what the check actually proves.

### Module 8 — Configuration, Secrets and Operational Safety Controls

#### Outcomes

- APP6-O5
- APP6-O6
- APP6-O9
- APP6-O15

#### Lessons

1. **Configuration and secret classification** — Distinguish nonsecret environment choices, session/DB credentials, deploy keys, access tokens and signing identities.

2. **Validation and failing safely** — Reject missing, contradictory or unsafe configuration before starting the local APP5 app or verification job.

3. **Local secret fixture design** — Use fake credentials, test-only scopes and disposable accounts while explaining why test literals are not production secrets.

4. **Credential injection and masking limits** — Demonstrate protected values are not passed to untrusted jobs, process arguments or logs and explain why masking is not a general security boundary.

5. **Ephemeral identity and OIDC** — Compare short-lived identity federation with long-lived cloud secrets conceptually; do not require a real cloud provider or falsely claim simulated OIDC verification.

6. **Token and artifact permission review** — Apply minimal privileges to pipeline actions, test denied write/publish operations and prevent unsafe privilege escalation through workflow configuration.

7. **Rotation and response to exposure** — Simulate detection, revocation, replacement, log cleanup and historical artifact review without using any real secret or promising deletion from all history.

*Optional practice — credential leak:* Seed a fake token in a disposable branch, ensure the gate fails, remove/rotate the fixture and verify artifact/log outputs contain no value.

### Module 9 — Logging, Metrics, Traces and Privacy-Aware Signals

#### Outcomes

- APP6-O1
- APP6-O10
- APP6-O12
- APP6-O15

#### Lessons

1. **Observability questions before tools** — Ask what the user experienced, which part failed, what committed and which evidence can answer the question.

2. **Structured event logging** — Record time, event category, status and bounded request/job correlation without raw cookies, bodies, names or user secrets.

3. **Metrics kinds and aggregation** — Choose counters, histograms, gauges and rates appropriate to error, latency, queue depth and resource observations.

4. **Cardinality and dimensions** — Explain why raw user ID, arbitrary path or request ID labels make metrics explode; keep identifiers in controlled logs/traces instead.

5. **Trace and span context** — Propagate compatible synthetic trace context through browser/API/worker and recognize trusted versus untrusted upstream trace fields.

6. **Sampling and missing data** — Differentiate absent signal from proof of success, and document sampling, clock differences and partial span coverage.

7. **Golden signals in context** — Examine traffic, errors, latency and saturation for the actual task, not a dashboard of irrelevant raw measurements.

8. **Sensitive telemetry and retention** — Bound logs/metric labels, decide retention and access, and test that redaction succeeds during error and exception paths.

*Optional practice — telemetry audit:* Repair a request-ID-as-metric-label or raw-token logging defect and show the resulting bounded metric series.

### Module 10 — User-Centered SLIs, SLOs and Error-Budget Reasoning

#### Outcomes

- APP6-O1
- APP6-O10
- APP6-O11
- APP6-O12

#### Lessons

1. **Service promise versus observed outcome** — Distinguish user-visible successful tasks, HTTP transport success and completed asynchronous work when defining an indicator.

2. **Choose event-based and time-based SLIs** — Define numerator/denominator, eligible events, timeout boundaries and sample bias for a chosen workflow.

3. **Objectives, windows and excluded events** — Specify numerical targets, monitoring periods, maintenance assumptions and precisely what counts as success/failure.

4. **Compute budget consumption** — Calculate allowed failures from total eligible events and an example target, and interpret a synthetic series without treating it as actual uptime.

5. **Latency distribution and percentiles** — Choose meaningful percentile/service window goals and explain how averages and aggregate groups can hide user harm.

6. **Error-budget burn rates and alert windows** — Interpret short and long window evidence, distinguish fast/slow consumption and explain multi-window alert trade-offs.

7. **Avoid noisy and misleading alerts** — Compare actionability, severity, ownership and cost of paging against a benign spike or an unobserved dependency failure.

8. **Quality gates and release decisions** — Use local SLO/error-budget evidence to inform an engineering decision; APP7 owns actual production rollouts and operational policy.

*Optional practice — SLO failure analysis:* Revise an objective based on aggregate HTTP 200 that ignores denied or permanently pending user tasks.

### Module 11 — Incident Triage, Diagnosis and Learning Loop

#### Outcomes

- APP6-O10
- APP6-O11
- APP6-O12
- APP6-O14
- APP6-O15

#### Lessons

1. **Incident definition and user impact** — Classify a controlled production-style incident by affected users, integrity, privacy and task consequences.

2. **Evidence collection and timeline** — Construct a time-sequenced, redacted log/metric/trace/job/DB record with explicit clock and missing-data limitations.

3. **Hypotheses, experiments and controls** — List at least two plausible causes, identify discriminating measurements and reproduce a controlled failure safely.

4. **Containment and recovery trade-offs** — Choose stop-the-bleeding measures for local fixtures, protect committed state and explain when a rollback is unsafe.

5. **Root cause versus proximate trigger** — Avoid confusing an error message or last failing frame with the full causal chain; include system/process contributors.

6. **Verified corrective action** — Implement a targeted change and verify behavior with failing-before/passing-after normal and adverse tests.

7. **Blameless and accountable retrospective** — Write a factual incident report with impact, timeline, contributing conditions, action owner, test and measurable follow-up; do not invent real incidents.

8. **Feedback into quality policy** — Update a CI gate, test plan, SLI or review checklist based on what the investigation actually exposed.

*Optional practice — incident drill:* Distinguish a cache-scope leak from a session-expiry symptom using evidence from the same cross-layer request.

### Module 12 — Performance Experiments, Saturation and Regression Gates

#### Outcomes

- APP6-O3
- APP6-O4
- APP6-O10
- APP6-O13
- APP6-O15

#### Lessons

1. **Workload model and user impact** — Choose an access pattern, concurrency/arrival rate, request payload, state mix and representative normal/denied/failure path.

2. **Warmup, caches and comparable baselines** — Control JIT warmup, dependency caches, seed data, local background load, run duration and device/software versions.

3. **Percentile, throughput and error reporting** — Record p50/p95/p99 or suitable distributions with sample counts and intervals, successful/failed throughput and observed saturation; avoid spurious precision.

4. **Open versus closed loop generators** — Explain client concurrency constraints, request scheduling and why coordinated omission can make the slowest user experience disappear from statistics.

5. **Resource diagnostics** — Observe CPU, memory, event-loop delay, DB pool waits and queue depth with clearly stated causal uncertainty.

6. **Bottleneck hypotheses and controlled intervention** — Change one justified query/queue/blocking path, measure again and compare distributions and error rates under matched conditions.

7. **Regression budgets and noisy thresholds** — Choose a reviewable threshold supported by variance and risk, balancing false positives with real performance regressions.

8. **Safe local-only load scope** — Bound concurrency and duration to learner-owned loopback systems; avoid public-service testing or dangerous denial-of-service conditions.

*Optional practice — load defect:* Find a hidden saturated client generator or cache-warmth mismatch and correct the measurement before claiming the service improved.

### Module 13 — Reliability Failure Injection and Resilience Trade-offs

#### Outcomes

- APP6-O1
- APP6-O3
- APP6-O11
- APP6-O12
- APP6-O15

#### Lessons

1. **Failure-mode analysis** — Prioritize dependency outage, malformed config, disk/resource pressure, duplicate work and authorization failure by user and data harm.

2. **Small controlled chaos at application scope** — Inject local response delays and failures with reproducible switches, bounded scope and planned cleanup; no production chaos platform required.

3. **Deadline and cancellation truth** — Show timeouts do not reverse committed SQL or external side effects, and that cancellation depends on actual API support.

4. **Queue, retry and load amplification** — Trace duplicate job/retry patterns and prove bounded attempt/backoff behavior without equating an outbox with exactly-once external execution.

5. **Fault containment and graceful degradation** — Document which user tasks remain available, which must fail and which can be truthfully queued while dependencies are unavailable.

6. **Recovery readiness evidence** — Re-enable the local dependency, reconcile authoritative state and show no cross-tenant data or orphaned worker remains.

7. **Reliability versus deployment responsibility** — Treat APP6 as diagnosis and engineering mitigation; APP7 owns deployed rollouts, backups, restore rehearsals and infrastructure controls.

8. **Security regression from outage** — Test that fail-open authorization, private cache fallback or leaked error details do not appear during failure.

*Optional practice — dependency outage:* Repair a retry storm or falsely successful UI fallback and provide a local failure/normal test pair.

### Module 14 — Maintainability, Code Review and Evidence-Based Evolution

#### Outcomes

- APP6-O1
- APP6-O2
- APP6-O7
- APP6-O12
- APP6-O14

#### Lessons

1. **Readable code and contract ownership** — Review component names, domain boundaries, API schema ownership and documentation rather than assuming all complexity is a code-length issue.

2. **Change friction and technical debt** — Identify repeated corrections, risky coupling, unstable test fixtures, large diffs and upgrade pressure as measurable maintenance signals.

3. **Dependency and abstraction design** — Choose narrow interfaces and independent tests for a justified refactor; avoid introducing speculative plugin architecture.

4. **Static findings and reviewer context** — Use linter/type output as clues, not sole proof of maintainability; resolve a meaningful code path or document a justified exception.

5. **Reviewer-friendly change history** — Structure a PR with risk, alternatives, seeded failure, backward compatibility and tests, and explain changed behavior clearly.

6. **Refactor without behavioral drift** — Apply characterization tests, perform a targeted restructuring and verify API/client/DB contracts and performance remain intact.

7. **Documentation and runbooks** — Update local operation/test instructions and a reproducible incident/debug note with safe configuration and cleanup steps.

8. **Quantifying engineering improvement** — Track measured flake frequency, changed test reliability, incident recurrence or developer feedback without inventing long-run data.

*Optional practice — maintainability review:* Defend a small simplification over an unproven broad rewrite with risk and passing negative-path evidence.

### Module 15 — Integrated Reliability Upgrade and Independent Defense

#### Outcomes

- APP6-O1
- APP6-O2
- APP6-O3
- APP6-O4
- APP6-O5
- APP6-O6
- APP6-O7
- APP6-O8
- APP6-O9
- APP6-O10
- APP6-O11
- APP6-O12
- APP6-O13
- APP6-O14
- APP6-O15
- APP6-O16

#### Lessons

1. **Select the bounded APP5 product risk** — Choose an authenticated React/Fastify/PostgreSQL workflow with known cache/job/privacy and failure expectations and publish its quality threat model.

2. **Build a risk-to-verification plan** — Map user-visible success, security, data invariants, contracts and changed requirements to unit/component/API/DB/browser/fault tests.

3. **Improve deterministic test fixtures** — Replace one brittle time/race dependency, add invariant or property examples and demonstrate a mutant/seeded defect that tests now detect.

4. **Implement least-privilege CI gates** — Create a versioned pipeline plus locally runnable equivalent, fail it on deliberate changes and document untrusted contributor/secret boundaries.

5. **Capture build and dependency evidence** — Pin local toolchain/dependencies, export inspectable artifact hashes and inventory/SBOM, and state source/build provenance limits.

6. **Instrument real user-journey signals** — Record sanitized request/trace and bounded error/latency metrics through UI/API/job under versioned local load and failure tests.

7. **Define an SLI and evaluate a local objective** — Publish numerator/denominator and window, compute error-budget examples, and decide what local alert would actually trigger.

8. **Investigate a performance and dependency defect** — Inject a controlled partial failure plus one load bottleneck, capture matched telemetry, implement fixes and verify access/privacy safeguards.

9. **Refactor and review a maintenance hazard** — Improve one risky boundary with characterization/contract tests and a clear code-review explanation of change and limitations.

10. **Fresh-run, unfamiliar incident and technical defense** — Recreate setup from provided free local artifacts, respond to an unseen bounded regression or incident and defend evidence, limitations and APP7 handoff.

## Completion requirements

**All sixteen required APP6 outcomes** are assessed
through the **seven required summative assessments**
below. Learners can improve the **same existing APP5
application** throughout, with separately inspectable
evidence rather than seven unrelated software
products. Lesson experiments, debugging exercises
and optional tools do not impose additional hidden
completion gates.

| Required assessment | Required outcome coverage | Principal evidence |
| --- | --- | --- |
| `APP6-AS1` — Risk-Based Quality Strategy and Multi-Layer Test Selection | APP6-O1, APP6-O2, APP6-O3, APP6-O4, APP6-O14 | Risk-to-test and negative-case matrix, versioned source and fixture commands, normal and seeded defect runs, property/mutation counterexample or justified equivalent, verified database/browser behavior and reviewer-oriented rationale |
| `APP6-AS2` — Deterministic Verification and Flaky-Test Root Cause | APP6-O2, APP6-O3, APP6-O4, APP6-O13, APP6-O14 | Before/after test source, failing input/seed or schedule, diagnostic timeline, deterministic repair, repeated-run summary and environment, leak/isolation verification and limitations statement |
| `APP6-AS3` — CI, Build Reproducibility and Software-Supply-Chain Security | APP6-O5, APP6-O6, APP6-O7, APP6-O8, APP6-O9, APP6-O15 | Versioned CI YAML and local entry scripts, pinned toolchain/lockfile, build commands and checksums, sanitized failure/passing logs, SBOM/dependency and provenance report, permissions/trust diagram, malicious-fixture before/after and security limitations |
| `APP6-AS4` — Observability, SLO and Actionable Alert Investigation | APP6-O1, APP6-O9, APP6-O10, APP6-O11, APP6-O12, APP6-O15 | Instrumentation and metric/trace source, sanitized request correlation and local histogram/counter samples, synthetic/observed dataset provenance, numerical SLI/SLO/error-budget computations, revised alert rule, injected telemetry defect repair and measurement limits |
| `APP6-AS5` — Load Regression and Controlled Resilience Experiment | APP6-O3, APP6-O4, APP6-O10, APP6-O11, APP6-O13, APP6-O15 | Reproducible local load script and seed, documented runtime/hardware and conditions, repeated distribution/error/throughput/telemetry tables, bottleneck hypothesis and repair diff, fault-injection tests, and qualified conclusion |
| `APP6-AS6` — Incident Causality, Maintainability and Regression Prevention | APP6-O1, APP6-O2, APP6-O7, APP6-O10, APP6-O11, APP6-O12, APP6-O14, APP6-O15 | Redacted incident and user-impact timeline, competing hypotheses and observation sources, failing-before/passing-after test output, patch and review notes, updated CI/runbook/SLI evidence, maintenance impact statement and remaining uncertainties |
| `APP6-AS7` — Integrated Quality and Reliability Upgrade with Independent Defense | APP6-O1, APP6-O2, APP6-O3, APP6-O4, APP6-O5, APP6-O6, APP6-O7, APP6-O8, APP6-O9, APP6-O10, APP6-O11, APP6-O12, APP6-O13, APP6-O14, APP6-O15, APP6-O16 | Versioned repository and local fixture commands, risk/coverage and test architecture, stable test/seed logs, CI policy/permissions and failure evidence, build input/lockfile/SBOM/hash provenance, privacy-safe telemetry and SLO worksheet, bounded load/fault/incident reports, maintenance diff and review history, fresh-reproduction and accessible written/recorded/live engineering defense |

### Shared reproducibility, security and evidence boundaries

- Use a maintained, recorded React/TypeScript,
  Node/Fastify and PostgreSQL baseline with pinned
  versions and locally reproducible synthetic
  fixtures, an unprivileged account and
  documented cleanup. Any toolchain download
  may occur during initial free provisioning;
  required test, build, log and load exercises
  must work from provided local artifacts
  without relying on a paid service.
- A version-controlled CI configuration must have
  a locally runnable equivalent with matching
  substantive checks. An assessor must **not**
  demand a hosted GitHub Actions account or
  external runner merely to show automation.
  Clearly distinguish actual local test results
  from unverified hosted token/event controls.
- Treat proposed code from an untrusted contributor
  as executable attacker-controlled material.
  Do not give it privileged release credentials,
  protected secrets or unwarranted write
  permissions. Review source of third-party
  actions, immutable pinning and cache scopes
  for the declared provider and workflow event.
  Do not execute seeded attacks against a real
  organization or publish any real token.
- Keep package manifests/lockfiles, toolchains,
  accepted advisories, dependency inventory
  and build artifact hashes inspectable.
  Document accepted nondeterminism. SBOMs,
  static scans and local integrity records
  do not alone establish a SLSA level,
  signed provenance or actual dependency safety.
- Use real, disposable integration tests where
  the claim concerns SQL invariants, credentials,
  tenant boundaries, HTTP serialization or
  browser behavior. Mocks and local synthetic
  incidents provide useful controlled evidence
  but are not production penetration testing
  or a service availability guarantee.
- Diagnose intermittent tests by seed, clock,
  concurrency and resource state; do not pass
  them through blind retries or delete adverse
  cases solely to achieve green CI. Demonstrate
  cleanup after both passing and failing setup.
- Build telemetry from sanitized request/job IDs,
  bounded categories and meaningful labels.
  Do not log cookies, tokens, PII, full bodies
  or private database/file content. Document
  trace sampling/absence and avoid placing
  user IDs, raw routes or per-request IDs
  in high-cardinality metric attributes.
- State SLI numerator, denominator, sampling/
  exclusions, observation window and target
  before calculating an error budget or an
  alert. Distinguish **illustrative local**
  figures from real production objectives.
  Explain alert-actionability, severity
  and false-positive/false-negative trade-offs.
- Performance and failure experiments are
  bounded to learner-controlled loopback
  services, local synthetic identities,
  fixtures and approved concurrency/duration
  limits. Compare like-for-like workloads,
  client-generator capacity, sample counts,
  warm-up, cache state and relevant tail
  latency plus error rates. Avoid any
  third-party load or denial-of-service test.
- Every incident claim must identify observed
  inputs, causal timeline, competing hypotheses,
  missing measurements, a tested correction
  and a blameless retrospective. Do not
  invent production traces, damage estimates,
  participant observations or success metrics.
- A reviewer may introduce a bounded unfamiliar
  regression, quality gate failure, telemetry
  anomaly or synthetic incident related to
  these public outcomes. They may accept an
  accessible written, recorded, live or
  equivalently inspectable defense without
  imposing hidden paid software, deployed
  infrastructure or APP7-specific certification.

### Required summative assessments

- **APP6-AS1** (required risk-based quality strategy and multi-layer test selection)
  - Outcomes: APP6-O1, APP6-O2, APP6-O3, APP6-O4, APP6-O14
  - Work: Audit a bounded APP5 full-stack workflow and publish a risk register, user-centered acceptance matrix and independent verification plan. Implement or repair representative domain, API/database, React/browser, contract and adverse/security tests so each demonstrates a different failure mode. Introduce a controlled mutant, property counterexample or invalid authorized/unauthorized transition and show that an appropriate test fails before a justified repair. Document where mocks cannot prove a behavior and which real integration tests are necessary.
  - Criteria: The plan maps important user/business/privacy risks to tests, thresholds, evidence and residual limitations without arbitrary test-count targets. A seeded defect is actually detected with failing-before/passing-after logs; correct API/database/client outcomes are distinguishable. Tests have explicit fixtures, isolation, teardown and no real external targets. Maintained tests remain readable and focused on public behavior rather than brittle implementation internals.
  - Evidence: Risk-to-test and negative-case matrix, versioned source and fixture commands, normal and seeded defect runs, property/mutation counterexample or justified equivalent, verified database/browser behavior and reviewer-oriented rationale.

- **APP6-AS2** (required deterministic verification and flaky-test root cause)
  - Outcomes: APP6-O2, APP6-O3, APP6-O4, APP6-O13, APP6-O14
  - Work: Start with a deliberately intermittent concurrency, timeout, random-fixture or shared-state test of the same application. Capture failing seed/schedule or competing resource ownership, form two competing hypotheses and reproduce a controlled failure. Replace time sleeps or shared fixtures with an injected clock, deterministic synchronization, scoped database/file resources or other justified mechanism, keeping a real boundary test where required. Re-run a documented sample of controlled executions, inspect cleanup and explain what remains timing- or OS-sensitive.
  - Criteria: The original flake is observed or recreated with a credible controlled schedule, and the fix addresses causality rather than adding blind retries or disabling the test. Clean fixture setup/teardown and resource ownership are demonstrated, representative normal and negative cases still pass, and meaningful performance/concurrency observations are not lost by over-mocking. Claims about the absence of all future flakes are explicitly avoided.
  - Evidence: Before/after test source, failing input/seed or schedule, diagnostic timeline, deterministic repair, repeated-run summary and environment, leak/isolation verification and limitations statement.

- **APP6-AS3** (required ci, build reproducibility and software-supply-chain security)
  - Outcomes: APP6-O5, APP6-O6, APP6-O7, APP6-O8, APP6-O9, APP6-O15
  - Work: Author a version-controlled CI workflow for the APP5 product and locally runnable equivalent with formatting, TypeScript checks, multi-layer tests, a material dependency/credential policy check, pinned dependency inputs and reviewable artifacts. Publish a dependency inventory/SBOM, source revision and artifact checksums or a suitable local provenance record. Seed a test-only policy violation, unsafe untrusted-PR privilege or fake credential; demonstrate failure and correction, and explain cache isolation, least privilege, token exposure, trusted publication and any hosted-only behavior not exercised.
  - Criteria: Gates fail on observed seeded regressions and finish green only after correction; versions, inputs, environmental assumptions and artifact digests are inspectable. A proposed untrusted contribution cannot access claimed protected secrets or write a privileged artifact under the documented platform/event permissions. The review explicitly acknowledges if actual hosted-token enforcement was not exercised locally, and distinguishes SBOM/provenance artifacts from achieved SLSA attestation/level. CI logs, artifacts and final source contain no real secrets or private user data.
  - Evidence: Versioned CI YAML and local entry scripts, pinned toolchain/lockfile, build commands and checksums, sanitized failure/passing logs, SBOM/dependency and provenance report, permissions/trust diagram, malicious-fixture before/after and security limitations.

- **APP6-AS4** (required observability, slo and actionable alert investigation)
  - Outcomes: APP6-O1, APP6-O9, APP6-O10, APP6-O11, APP6-O12, APP6-O15
  - Work: Instrument a synthetic user-facing APP5 journey with sanitized structured logs, bounded metrics and cross-component correlation through browser/API/worker. Define a precise success/latency SLI with numerator/denominator, eligibility, chosen SLO and time window, then collect or replay a disclosed local dataset with controlled timeouts/errors and compute eligible events, budget consumption and a reasonable alert/burn-policy decision. Seed high-cardinality or secret-bearing telemetry and repair it; compare what logs, traces and metric aggregates reveal or cannot reveal.
  - Criteria: Logs, metrics and trace identifiers correspond to the actual controlled request and remain privacy-safe; high-cardinality labels are bounded and sensitive values not published. The SLI reflects the declared user task rather than arbitrary 200 counts, calculations use a consistent denominator and window, and alert decisions explain false-positive/false-negative trade-offs. Synthetic numbers and local measurements are not reported as production reliability. The learner correctly handles absent telemetry and incomplete traces.
  - Evidence: Instrumentation and metric/trace source, sanitized request correlation and local histogram/counter samples, synthetic/observed dataset provenance, numerical SLI/SLO/error-budget computations, revised alert rule, injected telemetry defect repair and measurement limits.

- **APP6-AS5** (required load regression and controlled resilience experiment)
  - Outcomes: APP6-O3, APP6-O4, APP6-O10, APP6-O11, APP6-O13, APP6-O15
  - Work: Build a bounded localhost workload for one representative authenticated APP5 operation, including controlled concurrency/arrival pattern, payload/tenant mix, warm-up, cache conditions, error/status classification and reproducible fixture size. Profile repeated baseline p50/p95/p99 (or appropriately justified percentiles), error rate, throughput, memory/CPU/event-loop or DB waits and client generator health. Seed a query/pool/blocking bottleneck and a local partial dependency failure; identify cause, apply a verified bounded change, and rerun matched normal/adverse and privacy/authorization tests.
  - Criteria: The observed bottleneck is backed by comparable client/server measurements with sample count and uncertainty, not a single score or a fabricated capacity estimate. The test prevents or discusses coordinated omission, constrained client generator, small samples and warm-cache bias. Changed code has matched before/after traces plus behavioral regressions; rate/timeouts/retries remain bounded, and simulated outage does not create unsafe cross-tenant access or misrepresent persisted state. No load is directed at a public/external system.
  - Evidence: Reproducible local load script and seed, documented runtime/hardware and conditions, repeated distribution/error/throughput/telemetry tables, bottleneck hypothesis and repair diff, fault-injection tests, and qualified conclusion.

- **APP6-AS6** (required incident causality, maintainability and regression prevention)
  - Outcomes: APP6-O1, APP6-O2, APP6-O7, APP6-O10, APP6-O11, APP6-O12, APP6-O14, APP6-O15
  - Work: Investigate a controlled production-style incident in the evolving full-stack application involving one real local failure such as unauthorized cached data, hidden database retry, wrong feature flag, queue duplication or failing dependency. Build a correlated sanitized timeline, distinguish user impact, trigger, root-cause evidence and missing information, then repair at least one meaningful maintainability or configuration boundary. Add layered regression tests, revise the appropriate CI/SLI or runbook control and document an engineering review and blameless retrospective.
  - Criteria: A reproducible test or controlled setup demonstrates the incident before repair, and the new behavior passes independently at the right test layer. The explanation distinguishes evidence from hypothesis and does not infer deployed production facts from a simulation. The fix does not merely suppress alerts or retry errors indefinitely, preserves contract/privacy constraints and reduces or justifies change risk. The retrospective has meaningful preventive action, verification method, ownership and unverified remaining risk.
  - Evidence: Redacted incident and user-impact timeline, competing hypotheses and observation sources, failing-before/passing-after test output, patch and review notes, updated CI/runbook/SLI evidence, maintenance impact statement and remaining uncertainties.

- **APP6-AS7** (required integrated quality and reliability upgrade with independent defense)
  - Outcomes: APP6-O1, APP6-O2, APP6-O3, APP6-O4, APP6-O5, APP6-O6, APP6-O7, APP6-O8, APP6-O9, APP6-O10, APP6-O11, APP6-O12, APP6-O13, APP6-O14, APP6-O15, APP6-O16
  - Work: Deliver one fully reviewable quality/reliability upgrade to an existing local APP5 React/Fastify/PostgreSQL product, reusing qualifying prior APP6 assessments rather than building seven unrelated apps. Produce risk-based layered tests and deterministic fixtures, a least-privilege CI pipeline with a local equivalent, pinned dependency/build and supply-chain evidence, sanitized metrics/logs/traces, a stated SLI/SLO and representative budget calculation, a reproducible performance or resilience investigation, an incident-to-regression repair and a justified maintainability improvement. Demonstrate a clean-checkout/locally provisioned reproduction, then independently resolve an unfamiliar bounded defect or CI/security/observability incident while preserving the previous normal and negative paths.
  - Criteria: An assessor can execute disclosed free local setup, normal and seeded-failure gates, inspect artifact hashes/dependency inventory, trace one user task and verify its safe/failed/denied outcomes without a cloud, paid CI, real secrets or production exposure. The verifier can identify precisely which quality claims are supported and which are merely local simulations; secret/cache/tenant integrity remains intact, performance results are controlled, and the unfamiliar change produces a meaningful tested repair. The learner explains quality trade-offs, CI trust, observability/SLO interpretation and why deployment/backup/restore and production infrastructure decisions remain APP7's responsibilities.
  - Evidence: Versioned repository and local fixture commands, risk/coverage and test architecture, stable test/seed logs, CI policy/permissions and failure evidence, build input/lockfile/SBOM/hash provenance, privacy-safe telemetry and SLO worksheet, bounded load/fault/incident reports, maintenance diff and review history, fresh-reproduction and accessible written/recorded/live engineering defense.

### Completion decision and revision protection

To complete APP6, the evaluator must accept
`APP6-AS1` through `APP6-AS7` with
evidence jointly satisfying `APP6-O1`
through `APP6-O16`. A successful test
command, high code-coverage percentage,
green security scanner, SBOM, local
histogram or simulated incident is
**not** sufficient by itself. The reviewer
must inspect the claimed failure, corrective
change, independent quality gate, actual
user-facing effect and limitations.

Material failures in reproducibility,
least-privilege CI, secret/privacy handling,
tenant authorization, regression coverage
or evidence integrity must be repaired
before passing. Record assessment/outcome
IDs, source/OEE revision, local environment,
observations, protected artifacts, failures,
retests, explanations and review decisions
according to [OEE Evidence Rules](../../spec/evidence-rules.md).

APP6 retains its course ID while replacing
the legacy seven-week test/lab contract
and APP3 + APP5 direct prerequisites
with a new OEE `v0.2.0` **draft** requiring
APP5 directly. Earlier APP6 learning
evidence stays attached to its prior
source revision, not auto-promoted into
completion of these new assessment IDs.
A passing repository validator does not
mean the curriculum has become
`tested` or `verified`.
APP7–APP9 and APP10–APP16 now publish separately migrated
`v0.2.0` drafts; independent academic review and learner
readiness are separate from source conversion. OEE Workspace,
content/resource mappings
and 0xNAND pinned consumers must account
for actual revised course identity.

### Public non-mandatory study references

These open reference materials inform
mechanism and version inspection; they
do not introduce undisclosed completion
criteria beyond the course above.

- [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
  and [Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/)
  for SLI/SLO/error-budget and incident reasoning.
- [GitHub Actions security guidance](https://docs.github.com/en/actions/security-for-github-actions/security-guides)
  for event-specific permissions, untrusted
  pull requests, credential isolation and
  reviewed pinned actions.
- [SLSA v1.2 specification](https://slsa.dev/spec/v1.2/)
  for actual source/build tracks, provenance
  terminology and limits of assurance claims.
- [OpenSSF Scorecard](https://scorecard.dev/)
  for supply-chain indicators and
  context-aware audit discussion.
- [SPDX specification](https://spdx.dev/use/specifications/)
  and [CycloneDX](https://cyclonedx.org/)
  for dependency inventory formats.
- [OpenTelemetry signals](https://opentelemetry.io/docs/concepts/signals/)
  and [OpenTelemetry metrics](https://opentelemetry.io/docs/concepts/signals/metrics/)
  for logging/metrics/traces, labels and
  cardinality considerations.
- [OWASP CI/CD security guidance](https://owasp.org/www-project-top-10-ci-cd-security-risks/)
  and [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)
  for risk-based pipeline and dependency
  review without unsupported guarantees.
