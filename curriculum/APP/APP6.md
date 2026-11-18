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
Progression moves from risk and layered evidence to
deterministic tests, safe CI/build trust, measured signals,
incident/performance repair and independent defense.
The seven public assessments remain the **only
summative completion decisions**; optional module
practice does not create hidden gates. Fewer editorial
lessons do not establish less learner work or tested status.

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

### Module 1 — Quality Risk, Historical Context and Evidence Priorities

#### Outcomes

- APP6-O1
- APP6-O2
- APP6-O14
- APP6-O16

#### Lessons

1. **Quality as Observable User and System Behavior** — Situate modern test automation and quality assurance historically through a concrete APP5 user journey; compare correctness, maintainability, confidentiality, accessibility, throughput and trustworthy change evidence rather than green-check counts.

2. **Inspect the Existing APP5 Risk Surface** — Select a bounded prior React/Fastify/PostgreSQL service, identify sensitive tenant/data/cache/job conditions, actual user consequences and uncertainties; do not rebuild its feature implementation.

3. **Prioritize Failure Modes and Trade-Offs** — Compare an observed privacy exposure, integrity loss, slow interaction and maintenance hazard by severity, detectability and incomplete frequency evidence; justify why the next engineering effort matters.

4. **Acceptance, Oracles and Verification Limits** — Define normal, forbidden, conflict, expired, duplicate, failed and recovery cases with independently checkable expected facts at the relevant UI/HTTP/DB/job boundary.

5. **Risk-to-Test-to-Decision Map** — Assign high-value risks to specific test/telemetry/quality gates with expected failures, evidence limits and review ownership; avoid a fixed count/coverage percentage as a quality objective.

*Optional practice — risk audit:* Compare two proposed quality investments, defend priority using a known failure scenario and identify which tests would remain weak.

### Module 2 — Layered Tests and Independent System Oracles

#### Outcomes

- APP6-O1
- APP6-O2
- APP6-O3
- APP6-O14

#### Lessons

1. **Test Level by Failure Detection Cost** — Compare pure-domain, React component, Fastify contract, real Postgres, browser and external-failure tests by defect detected, feedback speed and what each cannot establish, without a universal pyramid quota.

2. **Pure Domain and Component Behavior** — Test genuine invariants and user-visible React state transitions under abnormal values without coupling to implementation-specific render counts or brittle snapshots.

3. **Actual Fastify and PostgreSQL Integration** — Use actual HTTP serialization/auth hooks plus disposable PostgreSQL constraints, rollback and two-tenant data as needed; explain exactly why a mock repository cannot demonstrate a DB invariant.

4. **Independent API Consumer and Real Browser Journey** — Compare a separately authored old/new client with the published API contract and verify browser navigation, focus, session expiry and background status via the real local host.

5. **Negative Cases, Boundary Fixtures and Coverage Blind Spots** — Select representative denied, conflict, malformed and duplicate cases; interpret scenario matrices and code/branch coverage as limited diagnostics, never a substitute for inspected behavior.

6. **Choose the Smallest Credible Test Portfolio** — Demonstrate one defect caught cheaply at a lower layer and one that only real system integration reveals; retain enough browser/DB testing for independent truth without duplicating every scenario across layers.

*Optional practice — misplaced-test exercise:* Move a flaky browser test to a stable lower level while retaining one real journey that verifies the integration boundary.

### Module 3 — Properties, Generated Counterexamples and Mutation Adequacy

#### Outcomes

- APP6-O2
- APP6-O3
- APP6-O4
- APP6-O15

#### Lessons

1. **Representative Examples and Equivalence Partitions** — Derive normal, missing, malformed, boundary and unauthorized cases from an actual service invariant instead of arbitrary random data.

2. **Pure/Stateful Invariants and Trusted Oracles** — Express tenant isolation, no duplicate business mutation and bounded resources as falsifiable properties; identify which oracle needs real persisted state.

3. **Seeded Generation, Shrinking and Reproduction** — Use a free deterministic property generator or a small controlled harness, record seed and minimal counterexample, and confirm an actual failure at the chosen test layer.

4. **Metamorphic and Old/New Differential Checks** — When a trusted expected output is incomplete, choose valid transformations or independent prior/new behavior, investigating differences instead of assuming either version is correct.

5. **Mutation Testing with Material Surviving Mutants** — Introduce a safe code mutation affecting auth/replay/domain logic, observe a surviving mutant, strengthen assertions and show the mutant is killed; reject arbitrary mutation-score targets.

6. **Bounded Negative and Fault Injection** — Inject a duplicate job, bad dependency result, invalid tenant or DB failure using disposable fixtures and inspect actual outcomes while distinguishing one counterexample from general system reliability.

*Optional practice — mutant repair:* Demonstrate a surviving authorization or retry mutant, add a meaningful failing test and record limitations of the mutation runner.

### Module 4 — Deterministic Scheduling, Isolation and Flake Root Cause

#### Outcomes

- APP6-O2
- APP6-O3
- APP6-O4
- APP6-O13

#### Lessons

1. **Owned Test Resources and Clean Teardown** — Create isolated DB rows/schemas, files, synthetic identities, ports and processes, then demonstrate cleanup after partial initialization as well as successful runs.

2. **Seed, Clock and Scheduler Control** — Replace nondeterministic expiry/retry sleeps with reproducible fake clocks, controlled barriers and recorded random seeds where supported; retain one real host lifecycle integration test.

3. **Real Concurrency Barriers and State Assertions** — Reproduce an actual two-request/DB-session ordering defect with deliberate barriers, independent final-row oracle and no lucky-sleep timing requirement.

4. **Classify a Flake with Competing Hypotheses** — Distinguish race, shared global state, test order, external fixture, time, OS and invalid assertion by observed evidence; record a failing trace or bounded recreated schedule.

5. **Causal Fix, Repeated Trials and No Blind Retries** — Remove the true timing/ownership problem, run controlled repeated tests and check resource leaks; quarantine with owner/expiry only when necessary and never report absence of all future flakes.

*Optional practice — intermittent test repair:* Capture a failing seed/timing schedule, fix the root cause and compare repeated controlled runs without claiming zero future flakes.

### Module 5 — Least-Privilege CI, Untrusted Contributions and Secret Boundaries

#### Outcomes

- APP6-O1
- APP6-O5
- APP6-O6
- APP6-O9
- APP6-O15

#### Lessons

1. **Versioned Workflow and Local Quality Gate** — Define dependency-ordered format/type/unit/integration/security/contract/browser checks and a locally executable equivalent, distinguishing source/test CI from APP7 deployment.

2. **Untrusted Pull Request versus Protected Code** — Threat-model branch/fork events, contributor-supplied commands, third-party actions and privileged source/check-out, especially dangerous pull_request_target or workflow_run designs.

3. **Minimal Permissions, Pinning and Artifact Publication** — Set narrow job token permissions, review third-party action identity and immutable pinning where supported, and separate build/read checks from protected write/release publication.

4. **Secret Types, Local Fake Fixtures and Credential Hygiene** — Distinguish environment settings from genuine credentials, use disposable synthetic secret fixtures and enforce no protected value in untrusted code execution, environment, process arguments, logs or artifacts.

5. **Cache Restoration and Dependency Execution Trust** — Test untrusted cache/artifact poisoning, mutable install scripts and job dependency elevation; privilege cannot be inferred from a cache key or job display name.

6. **Hosted Enforcement versus Local Simulation** — Prove a local failing/passing seeded malicious workflow case and explicitly identify which GitHub/hosted event, OIDC, token and environment-approval constraints remain untested without a real trusted platform.

7. **Rotation, Revocation and Failure Handling** — Simulate discovery/removal/rotation of a fake credential, inspect residual build logs/artifacts/history references and demonstrate that masking alone is not prevention or guaranteed deletion.

8. **Reviewable Gate Results and Source-to-Release Handoff** — Fail on an actual seeded test/security/config violation, preserve actionable nonsecret diagnostics and hand pinned approved outputs to APP7 without claiming a release was deployed.

*Optional practice — attack on the pipeline:* Inspect an untrusted change that tries to publish an artifact or read a secret and document why the revised job policy prevents it.

### Module 6 — Reproducible Inputs, Dependency Assurance and Artifact Provenance

#### Outcomes

- APP6-O5
- APP6-O6
- APP6-O7
- APP6-O8
- APP6-O9
- APP6-O15

#### Lessons

1. **Dependency Graph, Lockfile and Toolchain Scope** — Inspect direct/transitive dependencies, manifest/lockfile, compiler/runtime/platform and resolved bytes; explain that a semver range or a lockfile alone does not prove authentic artifacts.

2. **Clean Build and Controlled Environment** — Run a free local build from pre-provisioned inputs and synthetic fixtures with documented OS, clocks/locale, flags, network policy and environment choices; report unavailable offline resources rather than silently fetch.

3. **Byte-Level Reproducibility Counterexample** — Compare artifacts across two controlled builds, identify timestamp/order/locale/compiler drift and qualify exactly which inputs produce matching hashes—not a universal hermeticity claim.

4. **Artifact Digest, Manifest and Threat Limit** — Record source commit, builder command and SHA-256 artifact identity, demonstrate altered bytes being detected, and distinguish untrusted self-reported hashes from independently verified authenticity.

5. **SBOM with Transitive Scope and Vulnerability Triage** — Generate CycloneDX/SPDX inventory using free tooling, identify missing packages, and assess a specific advisory by affected version, reachable code, exploit conditions, remediation and justified exception.

6. **SLSA v1.2 Source versus Build Provenance** — Compare recorded source history, build attestation, builder identity and actual verified controls using SLSA v1.2's distinct source/build tracks, without claiming any achieved level from a local inventory or hash.

7. **Untrusted Build Step and Dependency Origin** — Inspect package lifecycle scripts, mutable tags, repository/release provenance and one synthetic tampering/substitution fault under contained privileges; fix a policy/control rather than just suppress scanner findings.

8. **Build and Supply-Chain Change Decision** — Review a concrete package upgrade or artifact mismatch with independent test/security results, document a bounded fix/rollback plan and hand verified build inputs—not an unearned signed release—to APP7.

*Optional practice — build drift:* Reproduce a build mismatch after an unpinned transitive dependency or environment change and verify the repaired documented inputs.

### Module 7 — Privacy-Safe Logs, Metrics and Trace Correlation

#### Outcomes

- APP6-O1
- APP6-O10
- APP6-O12
- APP6-O15

#### Lessons

1. **Questions, Events and Correlation Contracts** — Start from a real user-visible failed APP5 task and define what browser/API/DB/worker events must reveal, with bounded IDs and no raw authentication credentials.

2. **Structured Logs and Cross-Layer Trace Ownership** — Correlate sanitized request/job events and trace IDs while distinguishing trusted host-generated context from untrusted incoming baggage, including actual missing spans and clock differences.

3. **Metric Types, Dimensions and Cardinality Attack** — Choose counters/histograms/gauges/rates appropriate to errors, latency, queue and resource pressure; reproduce a raw-user/path/request-ID label explosion and repair with bounded meaningful attributes.

4. **Sampling, Retention and Secret Redaction** — Document dropped/sampled telemetry, access/retention and exception path leaks; test that tokens, PII, body contents and risky baggage do not enter output.

5. **Traffic, Errors, Latency and Saturation in Context** — Measure a bounded set of relevant golden signals for one user task rather than a maximal dashboard; distinguish successful transport from completed business work.

6. **Observable Defect and Diagnostic Blind Spot** — Seed a missing/false-success event or misleading trace, detect and repair it, and state what the resulting signals still cannot prove without a deployed monitor.

*Optional practice — telemetry audit:* Repair a request-ID-as-metric-label or raw-token logging defect and show the resulting bounded metric series.

### Module 8 — User Outcome SLIs, SLO Windows and Error-Budget Decisions

#### Outcomes

- APP6-O1
- APP6-O10
- APP6-O11
- APP6-O12

#### Lessons

1. **Define an Eligible User Operation and Denominator** — Distinguish accepted HTTP/202 from completed authorized user work, choosing an explicit population, numerator, denominator and observed/unknown status policy.

2. **SLO Threshold, Observation Window and Empty/Low Traffic** — Define a numerical reliability or latency target and time/event window, handle no-eligible-event periods and small samples rather than treating zero requests as 100% success.

3. **Correct Error-Budget Calculation and Synthetic Data** — Calculate allowable failures, actual consumption and uncertainty for a disclosed synthetic/local event series; no mathematical budget by itself establishes production service availability.

4. **Percentiles, Cohorts and Hidden User Harm** — Compute/interpret useful tail latency groups and task outcomes, identifying when an aggregate mean or unrepresentative cohort hides failure.

5. **Burn Rates, Multiwindow Evidence and Actionability** — Compare short/long windows, noisy spikes and sustained budget burn, deriving a justified alert with clear responder action and limits rather than a mandatory paging template.

6. **Engineering Choice and APP7 Operations Boundary** — Use actual locally calculated evidence to justify a test/gate/performance fix or advisory and state what future deployed measurements/rollout controls APP7 must implement.

*Optional practice — SLO failure analysis:* Revise an objective based on aggregate HTTP 200 that ignores denied or permanently pending user tasks.

### Module 9 — Controlled Incident Causality and Resilience Repair

#### Outcomes

- APP6-O1
- APP6-O3
- APP6-O10
- APP6-O11
- APP6-O12
- APP6-O14
- APP6-O15

#### Lessons

1. **Select User Impact and Two Plausible Failure Causes** — Prioritize privacy/integrity/availability effects from a synthetic dependency outage, retry loop, corrupt configuration, cache/permission or duplicate job, with explicitly competing hypotheses.

2. **Bounded Fault Injection and Failure-State Ownership** — Inject a controlled timeout, denied request, duplicate worker or unavailable DB/upstream under local fixtures; prove known cleanup and avoid third-party or destructive live chaos.

3. **Causal Cross-Layer Timeline and Missing Data** — Reconstruct sanitized browser/API/DB/job events, clock limitations, failed operation boundaries and absent signals; distinguish a proximal exception from a supported system-level cause.

4. **Retry Budget, Side Effect and Authorization under Outage** — Reproduce a compounded UI/API/worker retry or unsafe fallback, verify committed state and ensure denied users cannot access protected cached data while service is degraded.

5. **Containment, Degradation and Recovery Policy** — Select bounded backoff, circuit/stop, queue/reconcile or truthful failure responses, preserving a safe user path rather than claiming completed work or undoing external effects.

6. **One Verifiable Corrective Change and Adverse Regression** — Repair the actual mechanism, verify failing-before/passing-after at the relevant HTTP/DB/worker/browser boundaries and check unrelated tenant/privacy/normal cases.

7. **Blameless Review, Human Factors and Operational Limits** — Write an observed-facts versus hypotheses timeline with action owners, follow-up checks and concrete prevention; do not call a local simulation an actual workplace incident or production drill.

8. **CI/SLI/Runbook Feedback and Repeated Recheck** — Feed the discovered failure into a proportionate test, quality gate, alert or troubleshooting guide, rerun after repair and explicitly hand actual deployment/restore/rollout to APP7.

*Optional practice — incident drill:* Distinguish a cache-scope leak from a session-expiry symptom using evidence from the same cross-layer request.

### Module 10 — Performance Load, Measurement Bias and Corrective Experiment

#### Outcomes

- APP6-O3
- APP6-O4
- APP6-O10
- APP6-O13
- APP6-O15

#### Lessons

1. **User Workload, Arrival Model and Local Safety Budget** — Choose realistic operation mix, request/body sizes, tenants, bounded concurrency/arrival and failure classes, with a locally owned loopback load ceiling.

2. **Warm-up, Cache, Hardware and Comparison Controls** — Pin device/software, data snapshot, warm/cold caches, compiler/JIT warm-up and background work; compare only meaningful matched trial conditions.

3. **Latency Distributions, Errors and Throughput** — Record p50/p95/p99 only with sufficient samples and interpretation, and include failed operations, resource pressure, counts and variance rather than one deceptively favorable average.

4. **Generator Saturation, Open/Closed Loop and Coordinated Omission** — Demonstrate or diagnose a slowed client generator and distinguish scheduled arrival timestamps from observed completion so extreme user delays are not hidden by coordinated omission.

5. **Correlate CPU, Memory, Event Loop and Database Contention** — Use real process/pool/queue/host observations to test two plausible bottleneck hypotheses, explicitly qualifying missing spans and timing noise.

6. **One Bounded Improvement and Matched Regression** — Fix a query, blocking code path or queue policy, compare repeated baseline/post-change distributions including error/failure/authorization outcomes, and defend uncertainty.

7. **Statistical Gate, False Positives and Scope** — Choose a proportionate regression threshold informed by measured run-to-run variance; disclose local-only capacity limits and avoid unapproved public-service load or denial-of-service tests.

*Optional practice — load defect:* Find a hidden saturated client generator or cache-warmth mismatch and correct the measurement before claiming the service improved.

### Module 11 — Maintainability, Review and Tested Change Economics

#### Outcomes

- APP6-O1
- APP6-O2
- APP6-O7
- APP6-O12
- APP6-O14

#### Lessons

1. **Change Friction, Dependency Ownership and Real Risk** — Identify repeated defects, coupling, brittle fixtures, upgrade pressure and confusing API boundaries in an existing component; do not use code length alone as a metric.

2. **Characterization Tests before Refactoring** — Record externally observable client/API/DB behavior and negative tests, then make a small defensible structure change rather than speculative plugin frameworks.

3. **Static Findings, Reviewer Judgment and Accepted Exceptions** — Compare lint/type/security clues with actual reachable behavior, document a justified false positive or fix and explain its risk/expiry.

4. **Reviewable Diff, Alternatives and Traceability** — Publish changed contract, risk, causal defect, alternatives and test evidence in a compact PR-quality review while protecting sensitive logs/data.

5. **Behavior, Performance and Reliability after Change** — Verify stable API, tenant permissions, fixtures, user workflow and measured incident/regression indicators after the refactor, without inventing long-run developer productivity trends.

6. **Runbook, Ownership and Future Work Handoff** — Update clean local test/debug/cleanup instructions and bounded quality evidence, reserving deployed operations, backup/restore and release management for APP7.

*Optional practice — maintainability review:* Defend a small simplification over an unproven broad rewrite with risk and passing negative-path evidence.

### Module 12 — One Quality Upgrade and Independent Engineering Defense

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

1. **One APP5 Product, Risk Register and Prior Decisions** — Improve the same existing React/Fastify/PostgreSQL codebase assessed by APP6-AS1–AS6, mapping each independently accepted gate to the real risk it addresses.

2. **Reusable Tests, CI and Trusted Build Inputs** — Integrate seeded negative/property/flake regressions with actual local CI gates, dependency/SBOM/hash provenance and secret-safe untrusted contribution boundaries, citing accepted evidence instead of copying reports.

3. **Telemetry, SLO, Fault and Load Recheck** — Demonstrate one real sampled task/metric and error budget calculation, a controlled load/incident repair and rechecked data/privacy/accessibility behavior with local limits.

4. **Unfamiliar Test, Incident or Supply-Chain Failure** — Respond to a new bounded flake, unsafe PR secret/artifact path, false telemetry, regression or unexpected dependency failure, reproduce and correct the responsible layer and verify accepted earlier work remains valid.

5. **Fresh Local Reproduction and Technical Defense** — Build/run/test and stop from pinned free pre-provisioned inputs, present an outcomes-to-accepted-AS1–AS6 evidence index and defend methods, uncertainty, change economics and APP7 deployment boundaries.

## Completion requirements

All **sixteen APP6 outcomes** require **seven
independently decidable required assessments**.
Use **one evolving APP5 application** as the source
of failure cases and improvements: AS1 risk/test
selection, AS2 flake correction, AS3 CI/build trust,
AS4 privacy-safe observability and SLO decisions,
AS5 controlled load/resilience, AS6 a *distinct*
incident/maintainability repair, and AS7 a new bounded
fault plus independent defense. Accepted prior source,
traces and test judgments may be referenced instead of
duplicated across seven products. Module exercises and
optional tools are not additional completion gates.

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
  - Work: Using **the same existing APP5 product** for this course, define an actual risk-to-user-task test strategy with independent expected states and layer responsibilities. Select bounded pure domain, React, real Fastify/SQL, independently authored API consumer and actual browser tests, each tied to a distinct risk. Inject one material incorrect authorization/replay/transition or property/mutation counterexample that ordinary happy-path assertions miss; produce real failing-before/passing-after behavior. Explain where mocks stop proving a live browser/DB property and why a coverage percentage alone is insufficient.
  - Criteria: Each priority risk has appropriate distinct public-behavior evidence and a credible oracle; critical SQL, tenant, serialization and browser claims have real relevant integration observations. The seeded failure is reproducibly detected and corrected, and property/mutation examples have a meaningful counterexample rather than an arbitrary score. Tests are isolated and proportionate, not repeated across all layers merely to satisfy a count.
  - Evidence: Risk-to-test and negative-case matrix, versioned source and fixture commands, normal and seeded defect runs, property/mutation counterexample or justified equivalent, verified database/browser behavior and reviewer-oriented rationale.

- **APP6-AS2** (required deterministic verification and flaky-test root cause)
  - Outcomes: APP6-O2, APP6-O3, APP6-O4, APP6-O13, APP6-O14
  - Work: Reproduce one intermittent APP5 test caused by shared state, clock/randomness, concurrent clients or leaked resources, record its seed/barrier/environment and at least two causal hypotheses. Replace sleeps/blanket retries with owned fixtures, fake clock where appropriate, controlled synchronization and correct setup/teardown; retain a real host/DB concurrency test where simulated scheduling cannot establish behavior. Recheck repeated controlled failures/successes and identify any untested OS/time behavior.
  - Criteria: A genuinely observed or controlled reproduced failure has a testable root cause and a passing-after fix rather than blind retries, disabled cases or unsupported claims of perfect future determinism. Fixture isolation and cleanup after both success and partial failure are inspectable, negative-path coverage remains meaningful and no actual integration claim relies solely on a fake.
  - Evidence: Before/after test source, failing input/seed or schedule, diagnostic timeline, deterministic repair, repeated-run summary and environment, leak/isolation verification and limitations statement.

- **APP6-AS3** (required ci, build reproducibility and software-supply-chain security)
  - Outcomes: APP6-O5, APP6-O6, APP6-O7, APP6-O8, APP6-O9, APP6-O15
  - Work: Add **one version-controlled CI workflow and equivalent locally runnable gates** to the evolving APP5 source: useful format/type, selected real tests, contract/security checks, reviewed dependencies and source/build artifacts. Record a maintained toolchain/lockfile, build environment, actual output hash and transitive SBOM, then identify artifact/source-builder provenance and the selected **SLSA v1.2** Source versus Build track controls without claiming an achieved level. Seed a fake credential, untrusted-PR privileged action or poisoned dependency/cache and demonstrate safe failing-before/passing-after policy. Review event-specific GitHub permissions, pull_request_target/workflow_run misuse, actions pinning, secrets, OIDC and artifact publication; **explicitly distinguish hosted controls only inspected from mechanisms actually executed locally**.
  - Criteria: The local and declared hosted workflows have traceable substantive gates; an actual test/security policy defect fails and a correction passes without publishing secrets. Token permissions and untrusted-code boundaries are reviewed against the declared provider/event semantics, not presented as experimentally enforced merely because a local YAML check passed. Build hashes, SBOM and provenance identify the **actual** source/inputs and independent trust assumptions; a lockfile, self-reported digest or SBOM is neither guaranteed reproducibility nor signed attestation/SLSA certification. Only synthetic credentials are used and logs/artifacts are checked for leaks.
  - Evidence: Versioned CI YAML and local entry scripts, pinned toolchain/lockfile, build commands and checksums, sanitized failure/passing logs, SBOM/dependency and provenance report, permissions/trust diagram, malicious-fixture before/after and security limitations.

- **APP6-AS4** (required observability, slo and actionable alert investigation)
  - Outcomes: APP6-O1, APP6-O9, APP6-O10, APP6-O11, APP6-O12, APP6-O15
  - Work: Instrument **the same full-stack user journey** with sanitized bounded correlation through browser/API/worker and appropriate counters/histograms/trace context. Seed a high-cardinality metric label, sensitive baggage/log value or false-success event and repair it. Define an SLI with explicit eligible/success events, unknown/timeout handling, denominator, target and window, including **zero-traffic or low-sample interpretation**. Compute a reproducible synthetic/local error-budget series and short/long-window burn or alert rule; distinguish HTTP 202 accepted from completed user work and account for actual sampling/missing traces.
  - Criteria: Observed logs/metric series and trace IDs reflect controlled events, have privacy-safe bounded attributes and do not trust unvalidated upstream baggage as authorization. SLI arithmetic uses one coherent denominator/window, explicitly handles zero eligible traffic and sample limitations, and alerts correspond to an actionable user risk rather than raw HTTP 200 counts. Distinguish measured local data from synthetic examples, sampling gaps and unproven production uptime; a green dashboard or histogram alone does not pass.
  - Evidence: Instrumentation and metric/trace source, sanitized request correlation and local histogram/counter samples, synthetic/observed dataset provenance, numerical SLI/SLO/error-budget computations, revised alert rule, injected telemetry defect repair and measurement limits.

- **APP6-AS5** (required load regression and controlled resilience experiment)
  - Outcomes: APP6-O3, APP6-O4, APP6-O10, APP6-O11, APP6-O13, APP6-O15
  - Work: Use a bounded localhost authenticated APP5 operation and explicit arrival/client-capacity/resource budget for a reproducible load experiment. Report repeated baseline/error/throughput/tail latency with actual environment, warm-up, cache state, sample counts and client-generator saturation/coordinated-omission risks. Inject one measurable query/CPU/pool/queue bottleneck **and** a separate bounded partial dependency outage, identify competing causes, repair the actual mechanism, and compare matched post-change distributions plus tested privacy, authorization, idempotency, failure/recovery and error budgets.
  - Criteria: A causal performance repair is supported by comparable traces, sample/variance and client/server resource data rather than one run, profiler screenshot or unexplained throughput claim. Open/closed generator interpretation, omitted arrivals, error response mix and local-only capacity constraints are disclosed. A simulated outage does not bypass tenant permissions, allow unbounded compounded retries or falsely report committed work as completed; normal and adverse relevant regressions pass.
  - Evidence: Reproducible local load script and seed, documented runtime/hardware and conditions, repeated distribution/error/throughput/telemetry tables, bottleneck hypothesis and repair diff, fault-injection tests, and qualified conclusion.

- **APP6-AS6** (required incident causality, maintainability and regression prevention)
  - Outcomes: APP6-O1, APP6-O2, APP6-O7, APP6-O10, APP6-O11, APP6-O12, APP6-O14, APP6-O15
  - Work: Independently investigate a **new controlled incident not identical to the AS5 performance/outage scenario**, such as a cache-scope privacy error, misleading completed-job signal, wrong source CI rule or dependency/artifact integrity failure in the same APP5 service. Collect redacted user-impact, HTTP/DB/job/metric/log evidence, propose at least two causal explanations and discriminate them with a focused experiment. Repair a genuine maintenance/design/configuration boundary, update an actionable test/CI/SLI/runbook policy and document a fact-based blameless retrospective with unknowns and a new regression.
  - Criteria: The newly introduced failure has a failing-before/passing-after record and independently checked affected behavior, not merely replayed AS5 logs. The root-cause explanation differentiates observed fact from hypothesis, includes actual change/review cost and residual risks, and prevents recurrence through a suitable nonduplicated test or policy. No retry-only camouflage, invented organization incident or false production certification is accepted; privacy, authorization, configuration and consumer contracts remain preserved.
  - Evidence: Redacted incident and user-impact timeline, competing hypotheses and observation sources, failing-before/passing-after test output, patch and review notes, updated CI/runbook/SLI evidence, maintenance impact statement and remaining uncertainties.

- **APP6-AS7** (required integrated quality and reliability upgrade with independent defense)
  - Outcomes: APP6-O1, APP6-O2, APP6-O3, APP6-O4, APP6-O5, APP6-O6, APP6-O7, APP6-O8, APP6-O9, APP6-O10, APP6-O11, APP6-O12, APP6-O13, APP6-O14, APP6-O15, APP6-O16
  - Work: Deliver **one incremental quality/reliability upgrade to the existing APP5 product**, with a concise reference map to previously accepted APP6-AS1–AS6 evidence rather than seven independent projects or resubmitted reports. Demonstrate risk-led test choices and deterministic counterexamples, an actually fail-closed local CI analogue and reviewed hosted-policy limitations, pinned build/SBOM/provenance, secret-safe telemetry and correctly calculated SLO, a controlled load/incident correction and proportionate maintainability review. Reproduce a new bounded unfamiliar test failure, unsafe CI trust boundary, misleading metric or incident, repair it and recheck impacted earlier contracts from a clean provisioned local checkout.
  - Criteria: A reviewer can independently run free local source/build/test checks and reproduce a real user/API/DB abnormal path, protected-secret policy, bounded telemetry, SLI calculation and causal remediation. **Previously missing or failed AS1–AS6 evidence cannot be excused by AS7 integration.** Each material security/data/reliability claim has actual supporting evidence and the learner distinguishes local simulation from hosted privilege enforcement, achieved SLSA assurance, real production uptime and APP7 deployed operations. New changes retain tenant privacy, input correctness, CI policy, browser accessibility and known user behavior.
  - Evidence: One versioned APP5 source and local fixture/test plan, an **outcome-to-accepted-AS1–AS6 evidence index** rather than duplicated logs, actual CI/pipeline/source/dependency/SBOM/digest artefacts, bounded metric/SLO/load/incident and regression findings, new unfamiliar change, verified local setup and an accessible technical defense.

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

APP6 remains an OEE `v0.2.0` **draft** with its
already published **sole direct prerequisite APP5**.
The legacy seven-week lab and old APP3 + APP5
requirements are historical migration decisions,
not changes pending in this review. APP7–APP9
and APP electives are already published; this
source reassessment does not silently revise
their criteria or earlier APP6 learner results.
Passing source validation does **not** establish
learner-`tested`, independent-`verified` or
accredited readiness. Historical evidence and any
OEE Workspace/content/0xNAND consumer pins require
explicit assessed revision review, not auto-upgrade.

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
