# S15 — Reliability, Incident Response & SRE

**Track:** Systems · **Prerequisite:** S9, S11, S14 · **Core** · **Time:** 4 weeks, 60 hours · **Project:** P4 SLO/incident drill
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Reliability is an engineering property you design, measure, and practice — not a promise. You will define service-level objectives, instrument a service, respond to a simulated incident, write a blameless postmortem, and prove that a rollback and restore actually work.

## Outcomes

You can:

- translate a user journey into SLIs and SLOs;
- calculate an error budget and use it to make a release decision;
- design alerts that are actionable, symptom-based, and low-noise;
- distinguish metrics, logs, traces, and profiles and correlate them;
- explain queueing, retries, timeouts, circuit breaking, and load shedding;
- run an incident with roles, a timeline, and clear communication;
- contain, mitigate, and recover without destroying evidence;
- write a blameless postmortem with contributing factors and owned actions;
- design and test backups, restores, and a disaster-recovery plan;
- state residual risk and what the drill did not prove.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [Google SRE Book](https://sre.google/sre-book/table-of-contents/) | Ch. **1–6, 10–11, 14–15, 22–23** | SLOs, monitoring, release engineering, postmortems |
| [Google SRE Workbook](https://sre.google/workbook/table-of-contents/) | Ch. **2–5, 9–10** | Implementing SLOs, alerting, incident response, incident metrics |
| B5 *The Linux Programming Interface* | Ch. **35–36** (revisit) | Process priorities, scheduling, and resource behaviour |
| B4 *OSTEP* | Ch. **36–45** (selected) | I/O and storage failure behaviour |
| [Prometheus docs](https://prometheus.io/docs/) | Instrumentation, alerting rules, histograms | Measurement |
| [OpenTelemetry docs](https://opentelemetry.io/docs/) | Traces, metrics, logs, context propagation | Observability |
| [Kubernetes production docs](https://kubernetes.io/docs/) | Probes, disruption budgets, autoscaling | Operational controls |
| Provider status/incident reports | Two public postmortems | Learn from real failure chains |

## Modules

### 1. Service level objectives

- user journey and critical path;
- SLI: availability, latency, correctness, freshness, durability;
- specification: good events / valid events, window, threshold;
- SLO, SLA, and internal targets;
- error budgets and burn rates;
- percentile pitfalls and aggregation;
- choosing a target that users can feel;
- when not to have an SLO.

### 2. Observability that answers questions

- metrics: counters, gauges, histograms, exemplars;
- labels and cardinality cost;
- logs: structured, sampled, correlated, privacy-scrubbed;
- traces: spans, context propagation, sampling;
- profiling: CPU, heap, off-CPU;
- dashboards for diagnosis, not decoration;
- alert symptoms: latency, error rate, saturation, availability;
- alert fatigue, inhibition, grouping, and runbook links;
- synthetic checks and real-user monitoring.

### 3. Designing for failure

- timeouts and deadlines (end-to-end);
- retries with jitter, budgets, and idempotency;
- circuit breakers and bulkheads;
- load shedding and admission control;
- backpressure and bounded queues;
- graceful degradation and fallback;
- replication and failover;
- capacity and headroom;
- single points of failure;
- blast radius and cell-based architecture;
- dependency failure and retry storms;
- corruption and partial failure.

### 4. Incident command

- roles: incident commander, operations lead, communications lead, scribe;
- severity and escalation;
- first 15 minutes: assess, stabilize, communicate;
- containment versus root-cause work;
- status updates and stakeholder communication;
- evidence preservation;
- handoff and fatigue;
- declaring resolution and monitoring recurrence;
- security incidents: preserve scope and legal/notification boundaries.

### 5. Postmortems and learning

- blameless language and accountability;
- timeline from telemetry, not memory;
- contributing factors, not a single "human error";
- detection, response, and recovery gaps;
- action items with owner, due date, and verification;
- incident metrics and trend review;
- publishing sanitized learnings.

### 6. Backup, restore, and continuity

- RTO, RPO, and maximum tolerable downtime;
- backup types and retention;
- restore testing and integrity checks;
- key/secret recovery;
- region or provider failure;
- runbook drills and game days;
- dependencies outside your control.

## Labs

### Lab 1 — SLI/SLO specification

Pick P4 `workbenchd` (or another service you built). Define two user journeys, three SLIs, and one SLO per journey. Write the exact PromQL/query, the valid-event denominator, the window, and the error-budget policy.

### Lab 2 — Instrument and dashboard

Add request count, error count, duration histogram, queue depth, in-flight requests, and dependency latency. Build one dashboard that answers: "Is the service healthy?", "Where is the latency?", and "What changed?" Add a runbook link to every alert.

### Lab 3 — Load, saturation, and failure

Run a stepped load test. Find the knee. Then inject:

- dependency latency;
- dependency errors;
- a slow consumer;
- a pod restart;
- a full queue.

Verify timeouts, retries, load shedding, and recovery. Record p50/p95/p99 and error rate at each step.

### Lab 4 — Incident drill

Have someone else (or a script) inject one of the failures without telling you the cause. Respond in real time:

- declare severity and take the IC role;
- write a timestamped timeline;
- communicate at fixed intervals;
- mitigate, then verify;
- preserve logs and traces;
- close only after recovery is stable.

Record the drill, but do not fabricate realism you did not have.

### Lab 5 — Postmortem and restore

Write a blameless postmortem from the timeline. Include contributing factors, what went well, what made detection slow, and three owned actions with tests. Test one backup restore end-to-end and measure actual RTO/RPO.

## Exercises

1. Turn "the API should be fast" into a testable SLO.
2. Compute a 30-day error budget for 99.9% availability.
3. Explain why averaging latency hides user pain.
4. Design a retry policy that does not create a retry storm.
5. Explain the difference between a timeout and a deadline.
6. Design an alert for a dependency whose latency doubled.
7. Write an incident communication template.
8. Distinguish root cause from contributing factors.
9. Explain what a backup does not prove.
10. Name three things a game day cannot reproduce.

## Project increment — P4 SLO/incident drill

Add to P4:

- SLI/SLO definitions and a dashboard;
- actionable alerts with runbooks;
- a load/failure test report;
- an incident timeline and postmortem;
- tested rollback and restore;
- an error-budget policy for future releases.

**Brief:** [P4 — workbenchd](../projects/project-ladder.md#p4--workbenchd)

## Exit check

- [ ] define an SLI/SLO and compute its error budget;
- [ ] demonstrate a dashboard and an alert that fired for a real injected failure;
- [ ] find the load knee and show bounded behaviour under overload;
- [ ] run an incident with a timeline and communication;
- [ ] mitigate and verify recovery;
- [ ] write a blameless postmortem with owned, verifiable actions;
- [ ] restore from backup and report measured RTO/RPO;
- [ ] state residual risk and drill limitations.

## Common failure modes

- Choosing an SLO that measures only server uptime, not user success.
- Alerting on every cause instead of user-visible symptoms.
- Retrying without a budget, jitter, or idempotency.
- Declaring an incident resolved before verifying stable recovery.
- Writing "human error" as the root cause.
- Action items with no owner or no verification.
- Assuming a snapshot is a restore.
- Running a game day without a stop condition or rollback.

## Evidence to commit

- `labs/systems/S15/` with SLO spec, dashboard queries, load test, incident timeline, postmortem, restore report
- P4 alerts/runbooks and error-budget policy
- `notes/systems/S15/summary.md`

## Optional depth

- *Site Reliability Engineering* and *The SRE Workbook* in full.
- *The Field Guide to Understanding 'Human Error'* (Dekker).
- *Chaos Engineering* (Rosenthal & Jones).
- *Database Reliability Engineering* (Campbell & Majors).
- Incident Commander training material from PagerDuty or Google.
