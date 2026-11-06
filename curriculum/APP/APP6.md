# APP6 — Software Quality & Engineering Operations

**Program:** APP — Application Engineering
**Type:** `course`
**Prerequisites:** [APP3](APP3.md), [APP5](APP5.md)
**Duration:** 7 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Develop a practical quality strategy for production applications. You will work across unit, integration, and end-to-end testing, CI, static analysis, dependency management, observability, configuration, and production debugging.

## Learning outcomes

By the end of this course, the learner will be able to:

- Choose appropriate test levels for different application behaviors.
- Build CI workflows that continuously verify software quality.
- Use logging, metrics, and traces to investigate application failures.
- Manage configuration, secrets, dependencies, and reproducible builds safely.
- Turn discovered production failures into durable tests and engineering improvements.
- Apply reproducible CI security controls to dependency, credential and artifact supply-chain risks.
- Define and evaluate service-level objectives using user-centered error and latency signals.
- Diagnose a load-related regression using repeatable benchmarks, resource telemetry and evidence-based remediation.
- Convert incidents and discovered defects into durable automated tests and measurable operational improvements.

## Modules

### Module 1 — Testing Strategy

#### Outcomes

- Explain **Unit, integration, and end-to-end tests** in the context of the course.
- Apply **Choosing the right test boundary** in a problem, implementation, experiment, or design decision.

- Choose tests that reveal real system risks with reliable, maintainable feedback.

#### Lessons

1. **Course introduction: Software Quality & Engineering Operations** — `lesson`

   Develop a practical quality strategy for production applications. You will work across unit, integration, and end-to-end testing, CI, static analysis, dependency management, observability, configuration, and production debugging.
2. **Unit, integration, and end-to-end tests** — `lesson`
3. **Choosing the right test boundary** — `lesson`
4. **Test doubles, fakes and contract-test realism** — `lesson`
5. **Property-based testing and invariants** — `lesson`
6. **Deterministic fixtures and test isolation** — `lesson`
7. **test strategy** — `test`
8. **Move one over-mocked test to the most useful level** — `lab`

### Module 2 — Automation & Delivery Quality

#### Outcomes

- Explain **CI, static analysis, and dependency management** in the context of the course.
- Apply **Reproducible checks before merge** in a problem, implementation, experiment, or design decision.

- Implement CI quality gates that detect changes in behavior, dependency risk, and reproducibility.

#### Lessons

1. **CI, static analysis, and dependency management** — `lesson`
2. **Reproducible checks before merge** — `lesson`
3. **Quality gates, test sharding, and caching safely** — `lesson`
4. **Software supply chain and dependency review** — `lesson`
5. **Reproducible build inputs and artifacts** — `lesson`
6. **engineering automation** — `test`
7. **Build a CI workflow that fails on tests or quality violations** — `lab`

### Module 3 — Observability

#### Outcomes

- Explain **Structured logging and metrics** in the context of the course.
- Apply **Tracing concepts and cross-component diagnosis** in a problem, implementation, experiment, or design decision.

- Correlate logs, metrics and traces without exposing sensitive information or exploding label cardinality.

#### Lessons

1. **Structured logging and metrics** — `lesson`
2. **Tracing concepts and cross-component diagnosis** — `lesson`
3. **Telemetry cardinality and data sensitivity** — `lesson`
4. **Structured trace context propagation** — `lesson`
5. **Useful latency and error-rate signals** — `lesson`
6. **observability** — `test`
7. **Trace one failed request through multiple components** — `lab`

### Module 4 — Incident Debugging

#### Outcomes

- Explain **Incident symptoms, evidence, and hypotheses** in the context of the course.
- Apply **Configuration, secrets, and recovery practices** in a problem, implementation, experiment, or design decision.

- Use a repeatable incident method to identify causes and verify an effective repair.

#### Lessons

1. **Incident symptoms, evidence, and hypotheses** — `lesson`
2. **Configuration, secrets, and recovery practices** — `lesson`
3. **Incident severity, triage, and safe response** — `lesson`
4. **Hypothesis testing and rollback decisions** — `lesson`
5. **Blameless postmortems and regression prevention** — `lesson`
6. **incident reasoning** — `test`
7. **Diagnose a controlled production-style failure from logs and configuration** — `lab`

### Module 5 — Security & Supply-Chain Quality

#### Outcomes

- Prioritize exploitable risks over raw scanner counts.
- Validate dependency, artifact and credential controls before release.

#### Lessons

1. **Threat models and misuse cases in CI** — `lesson`
2. **Static and dynamic analysis boundaries** — `lesson`
3. **Dependency vulnerabilities, SBOMs, and provenance** — `lesson`
4. **Secret detection and controlled disclosure** — `lesson`
5. **Security gate and false-positive analysis** — `test`
6. **Harden a compromised build pipeline** — `lab`

### Module 6 — Reliability Targets & Service Levels

#### Outcomes

- Define meaningful service-level indicators linked to user workflows.
- Evaluate alert quality and incident impact using measured error/latency signals.

#### Lessons

1. **Service level indicators, objectives and error budgets** — `lesson`
2. **User-centered availability and latency monitoring** — `lesson`
3. **Burn rates and actionable alerting** — `lesson`
4. **Recovery objectives and incident rehearsal** — `lesson`
5. **SLO selection and alert evaluation** — `test`
6. **Rehearse an SLO-driven incident response** — `lab`

### Module 7 — Performance & Regression Engineering

#### Outcomes

- Separate valid performance evidence from noisy or unrepresentative benchmarks.
- Establish a repeatable regression test tied to operational limits.

#### Lessons

1. **Benchmark design and workload realism** — `lesson`
2. **Concurrency and saturation measurements** — `lesson`
3. **Regression budgets and noisy measurements** — `lesson`
4. **Capacity risk and performance failure triage** — `lesson`
5. **Interpreting performance regressions** — `test`
6. **Investigate a load-induced production fault** — `lab`

### Module 8 — Reliability Upgrade

#### Outcomes

- Complete and explain the Reliability Upgrade lab, demonstrating the applicable course outcomes and retaining required evidence.

#### Lessons

1. **Apply the Reliability Upgrade to the APP5 product** — `lab`

## Completion requirements

- Complete the required practical exercises, knowledge checkpoints, and evaluated labs described in the modules.
- Complete the final integrated `lab` in the last module and satisfy its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, failures investigated, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required practical exercises:**

- turn a bug into a regression test
- build a CI pipeline
- trace one failed request across components
- remove a flaky test
**Final integration lab — required work:**

Required artifact: **Reliability Upgrade**.

Take the APP5 product and add a meaningful test strategy, CI pipeline, observability, deployment-safe configuration and a documented incident/debugging workflow.

**Expanded module assessments and practical work:**

- **Module 1 checkpoint and micro-lab:** Show that representative unit, integration and browser tests each detect a distinct intentionally seeded defect.
- **Module 2 checkpoint and micro-lab:** Demonstrate a failed gate on a seeded defect and a clean build with repeatable tool versions and inputs.
- **Module 3 checkpoint and micro-lab:** Trace a failed request across components and validate required correlation IDs and redacted fields.
- **Module 4 checkpoint and micro-lab:** Present an incident timeline, reproducible cause, remediation and regression test instead of only a symptom patch.

- **Module 5 — Security & Supply-Chain Quality (Harden a compromised build pipeline):**
  - Prerequisites: Explain the module outcomes and complete the instructional lessons.
  - Environment: A controlled reproducible implementation or simulation with documented configuration and test data.
  - Required work: Introduce safe seeded examples of a leaked credential and outdated library into a test branch, configure detection and document remediation.
  - Verification: Build fails on the policy violation; secret is removed and rotated in a simulation, and the remediation produces an audit artifact.
  - Evidence: Scanner configuration, sanitized logs, SBOM/lockfile, policy rationale.
  - Failure analysis: Discuss untrusted CI inputs, secret masking limitations and dependency false positives.
- **Module 6 — Reliability Targets & Service Levels (Rehearse an SLO-driven incident response):**
  - Prerequisites: Explain the module outcomes and complete the instructional lessons.
  - Environment: A controlled reproducible implementation or simulation with documented configuration and test data.
  - Required work: Instrument a small API, create a controlled elevated error rate and apply an alert threshold; assess the signal against actual user impact.
  - Verification: Show the objective, error budget, telemetry window and decision made when the threshold is exceeded.
  - Evidence: Dashboard/query definitions, fault injection, incident timeline and retrospective.
  - Failure analysis: Explain alert fatigue, misleading aggregate metrics and monitoring without user impact.
- **Module 7 — Performance & Regression Engineering (Investigate a load-induced production fault):**
  - Prerequisites: Explain the module outcomes and complete the instructional lessons.
  - Environment: A controlled reproducible implementation or simulation with documented configuration and test data.
  - Required work: Run staged load against a controlled service, identify throughput and latency limits, and improve the dominant bottleneck.
  - Verification: Record percentile latency, error rate, throughput and resource use before and after under matched conditions.
  - Evidence: Load generator, telemetry, test scripts and measured trade-offs.
  - Failure analysis: Distinguish coordinated omission, cache warmup effects and client-side test bottlenecks.

**Exit assessment expectation:**

Demonstrate the relevant course outcomes on an unfamiliar scenario, including failure behavior and independently reproducible evidence. Checkpoint responses must explain mechanisms; every final lab or project must integrate and verify the expanded material.

**Exit demonstration:**

The learner can choose appropriate test levels, diagnose a failing production workflow from evidence, and explain why a test belongs where it does.

---
