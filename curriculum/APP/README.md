# Program 2 — APP: Application Engineering

> [OEE curriculum](../README.md) · [Specification](../../spec/README.md) · [OEE Workspace](https://github.com/0xbuffdev/oee-workspace)

## Overview

Application Engineering follows Software Engineering Foundations. Learners trace how the Web works, author accessible documents, and develop JavaScript, TypeScript, browser, Node and database skills. They then integrate frontend and backend services, test their behavior, deploy a real application, investigate failures and defend engineering decisions. Work from one course may become the starting point for another, provided each course's own outcomes are assessed.

## Prerequisites

**SEF — Software Engineering Foundations.** Course-level prerequisites are listed below. Equivalent prior competence may be demonstrated through an appropriate diagnostic assessment.

## Learning outcomes

By the end of the core program, the learner will be able to:

- Author accessible semantic documents and robust responsive styles, then design and build maintainable frontend, backend and full-stack applications.
- Design HTTP APIs with validation, authentication, authorization and explicit failure handling.
- Model relational data and reason about queries, indexes, transactions and schema migrations.
- Integrate asynchronous work, caching and external services while preserving state, identity, authority and failure boundaries.
- Build testing, CI, observability and production-debugging workflows.
- Deploy and operate an application with secure configuration, HTTPS, health checks, monitoring and rollback.
- Measure performance and capacity, investigate bottlenecks and make evidence-based architectural changes.
- Deliver and defend a complete product through implementation, deployment and operation.

## Program completion standard

**Graduation requires two distinct decisions:** (1) authentic, assessed completion evidence for the thirteen core courses preceding APP9 (APP1–APP8 and APP17–APP21), or governed outcome-equivalent decisions tied to the applicable course/spec revisions; and (2) successful, independently inspectable completion of all eight APP9 summative evaluations and all sixteen capstone outcomes through **one** reproducible, evaluated and defended application. Verify the predecessor decisions **before capstone entry**. A polished APP9 product cannot substitute for missing prior course mastery, and a prior course checkmark cannot substitute for new APP9 evidence.

APP9 assesses a meaningful integrated product, not thirteen re-created course assignments. Its [pre-entry and graduation-evidence procedure](APP9.md#verified-prerequisite-closure-and-capstone-integration) distinguishes verified prior competence from relevant new application and does not demand unrelated features simply to re-demonstrate earlier topics. The capstone includes reproducible artifacts, design choices, verification results, failure analysis, source/reuse attribution, professional release judgment and a technical retrospective.

Electives provide optional specialization and are **not** prerequisites for the capstone or graduation.

---

## Courses

The catalog follows a prerequisite-valid study order. Core courses are required for graduation; electives are optional. Each status cell combines a course's classification with its educational readiness label. Durations are planning estimates that need calibration through learner work.

| Course | Title | Duration | Prerequisites | Kind | Status |
| --- | --- | --- | --- | --- | --- |
| [APP1](APP1.md) | Web & Internet Foundations | 12–16 weeks | SEF10 | `course` | Core · draft |
| [APP17](APP17.md) | HTML & CSS Engineering | 10–12 weeks | APP1 | `course` | Core · draft |
| [APP18](APP18.md) | JavaScript Programming | 12–16 weeks | SEF10 | `course` | Core · draft |
| [APP19](APP19.md) | TypeScript Programming | 10–14 weeks | APP18 | `course` | Core · draft |
| [APP4](APP4.md) | Databases & Data Modeling | 12–16 weeks | SEF10 | `course` | Core · draft |
| [APP2](APP2.md) | Browser & Frontend Engineering | 12–16 weeks | APP17, APP19 | `course` | Core · draft |
| [APP21](APP21.md) | Node.js & Backend Foundations | 12–16 weeks | APP18 | `course` | Core · draft |
| [APP20](APP20.md) | React Application Engineering | 12–16 weeks | APP2 | `course` | Core · draft |
| [APP3](APP3.md) | Backend Framework Engineering | 14–18 weeks | APP19, APP21, APP4 | `course` | Core · draft |
| [APP5](APP5.md) | Full-Stack Application Architecture | 14–18 weeks | APP20, APP3 | `course` | Core · draft |
| [APP6](APP6.md) | Software Quality & Engineering Operations | 14–18 weeks | APP5 | `course` | Core · draft |
| [APP7](APP7.md) | Deployment, Cloud & DevOps | 14–18 weeks | APP5, APP6 | `course` | Core · draft |
| [APP8](APP8.md) | Production Application Architecture | 14–18 weeks | APP5, APP6, APP7 | `course` | Core · draft |
| [APP9](APP9.md) | Application Engineering Capstone | 12–16 weeks | APP1–APP8, APP17–APP21 | `project` | Core · draft |
| [APP10](APP10.md) | Advanced Frontend Performance | 12–16 weeks | APP20, APP6 | `course` | **Elective · draft** |
| [APP11](APP11.md) | Advanced Backend Architecture | 14–18 weeks | APP3, APP4, APP6 | `course` | **Elective · draft** |
| [APP12](APP12.md) | Realtime Systems | 14–18 weeks | APP3, APP5, APP6 | `course` | **Elective · draft** |
| [APP13](APP13.md) | Mobile Application Engineering | 14–18 weeks | APP19, APP3 | `course` | **Elective · draft** |
| [APP14](APP14.md) | API Gateways & Edge Delivery | 14–18 weeks | APP3, APP7 | `course` | **Elective · draft** |
| [APP15](APP15.md) | TypeScript–Rust Application Interoperability | 14–18 weeks | APP19, APP21, APP6 | `course` | **Elective · draft** |
| [APP16](APP16.md) | Platform Engineering | 14–18 weeks | APP6, APP7 | `course` | **Elective · draft** |

**Current totals:** 14 core courses (including APP9's project capstone) and 7 optional electives, all `draft`. The electives APP10–APP16 are not required for graduation.

**Current source:** All 21 APP courses publish OEE `v0.2.0` outcomes, ordered lessons and required assessments. Each remains `draft`. APP15 is an optional TypeScript–Rust specialization: it builds on APP19, APP21 and APP6 and expects Rust foundations from SYS2 or equivalent preparation, without requiring SYS enrollment. The catalog and course definitions specify current prerequisites and completion requirements.

```text
SEF10 → APP1, APP18, APP4
APP1 → APP17
APP17 + APP19 → APP2
APP18 → APP19, APP21
APP2 → APP20
APP19 + APP21 + APP4 → APP3
APP20 + APP3 → APP5
APP5 → APP6
APP5 + APP6 → APP7
APP5 + APP6 + APP7 → APP8
APP1–APP8 + APP17–APP21 → APP9
```

## How the courses fit together

The course order respects prerequisites. Independent branches may be studied concurrently. Course numbers identify courses; they do not prescribe enrollment order.

- **Independent entry paths:** After completed SEF, APP1 establishes Internet/Web/browser mechanisms, APP18 teaches JavaScript using local Node/npm tooling, and APP4 teaches relational data/SQL independently. These paths can be studied concurrently.
- **Web documents and typed code:** APP17 applies APP1 to semantic HTML, native forms, responsive CSS and accessibility. APP19 follows APP18 to teach TypeScript's static contracts and runtime-data boundaries. Neither assumes React or a backend framework.
- **Separate browser and server branches:** APP2 combines APP17 and APP19 for framework-neutral interaction, browser security, accessibility and usable state. APP20 adds React-specific rendering, Hooks and component/data lifecycles. Separately, APP21 follows APP18 for raw Node I/O, streams, HTTP and lifecycle mechanisms; APP3 joins APP19, APP21 and APP4 for secure, typed Fastify service contracts and durable PostgreSQL behavior.
- **Integration and professional quality:** APP5 joins React and backend branches around one authenticated end-to-end product. APP6 then develops system-level test strategy, CI/supply-chain safety, observability, incident investigation and maintainability, without re-teaching language or framework basics.
- **Operation and evolution:** APP7 makes the integrated system deployable and recoverable through verified HTTPS, isolated configuration, immutable promotion, actual database restores and rollback/forward repair. APP8 evaluates measured capacity, overload, fairness, data consistency, architecture evolution and operational cost; no unsupported microservice requirement is introduced.
- **Graduation:** APP9 starts only after all 13 preceding core courses have recorded assessed completion decisions or appropriately governed outcome-equivalent evidence. Seven cumulative project stages lead to **one independently reproduced, tested, operated, evaluated and defended application**, with a genuinely unfamiliar bounded change. The prerequisite register is an entry check, not a ninth project assessment; previous source revisions and actual learner evidence remain distinct from APP9's new outcomes.

## Workload and pacing

The published core durations add up to **174–228 course-weeks**. At **10–15 focused hours per week**, that corresponds to about **1740–3420 focused course-hours** if every course is taken in full. These totals are provisional estimates, not minimum attendance requirements or validated completion times. Independent branches can overlap; actual effort depends on practice, setup, debugging, assessment and revision. Electives are excluded.

Workload must be calibrated against actual study, experimentation, debugging and summative work, not by counting lessons. Reusing a verified implementation across APP5–APP9 is permitted where later outcomes are independently demonstrated; APP9 remains one independently defended graduation product, not a requirement to resubmit each earlier lab. Outcome evidence, not elapsed weeks or lesson checkboxes, determines completion. Estimates remain provisional until genuine learner evidence supports calibration.

## Optional specializations

All seven electives remain outside APP9's required prerequisites and program graduation. Each has its own entry requirements and independent evidence contract.

- **APP10 — Advanced Frontend Performance:** After APP20 + APP6, investigate browser/React traces, LCP, INP, CLS, resource delivery, long-session memory and regression decisions. A performance improvement is valid only when user-facing correctness, privacy and accessibility still hold.
- **APP11 — Advanced Backend Architecture:** After APP3 + APP4 + APP6, deepen domain ownership, transactional outbox/inbox, replay correctness, compensation, projections, incremental extraction and operations. It does not re-teach APP3's basic framework API or require SYS distributed-protocol implementation.
- **APP12 — Realtime Systems:** After APP3 + APP5 + APP6, choose and implement appropriate polling/SSE/WebSocket transport, authenticated live updates, snapshot-and-cursor synchronization, multi-client conflicts, revocation, recovery and bounded fan-out. A permanent connection is not proof of durable delivery.
- **APP13 — Mobile Application Engineering:** After APP19 + APP3, deliver a real locally installed Android application with lifecycle/process-death resilience, transactional offline data, authorized two-client synchronization, native permissions, accessible input and a tested upgrade. React, iOS, macOS and paid app-store access are not compulsory.
- **APP14 — API Gateways & Edge Delivery:** After APP3 + APP7, investigate HTTP intermediary routing and forwarded trust, verified TLS, correct shared caching, fair admission, streaming, measured edge/origin behavior and incident recovery. A local gateway is sufficient; no paid CDN or WAF is mandatory.
- **APP15 — TypeScript–Rust Application Interoperability:** After APP19 + APP21 + APP6, and with demonstrated Rust foundations, implement and defend a real TypeScript-facing feature backed by an inspectable Rust component, safe versioned process communication, replay/error behavior and honest performance comparison. Rust ownership and C/Rust comparison belong to SYS; no unpublished SYS identifier is imposed.
- **APP16 — Platform Engineering:** After APP6 + APP7, design, build and defend a developer-facing platform product: measured consumer journeys, versioned golden paths and catalog ownership, persistent self-service operations, multi-consumer isolation, executable policy and artifact trust, recovery, adoption economics and responsible retirement. Its seven summative assessments require reproducible evidence and an unfamiliar technical defense. No mandatory portal, Kubernetes or paid cloud.

## Source format and readiness

All 21 APP courses publish OEE `v0.2.0` outcome and summative assessment contracts and remain `draft`. Formative practice provides feedback. Completion depends on the relevant required assessments, with evidence that reviewers can inspect independently. Successful source validation does not establish learner-tested effectiveness, `verified` status or formal OEE conformance. The [curriculum inventory](../INVENTORY.md) describes the current source structure and is not a second curriculum.

## Independent study

The [individual course definitions](README.md#courses) are authoritative for their prerequisites, outcomes, required assessments and acceptance evidence. Reading lists, affiliate purchases and commercial instruction remain outside the OEE completion contract. Learners may use [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) or another accessible learner-controlled environment; a paid platform, purchased book, private grader, commercial cloud account or specific paid service cannot be required merely to understand and complete the public work.

The binding educational contract is in [Course Format](../../spec/course-format.md) and [Evidence Rules](../../spec/evidence-rules.md). The non-normative [Curriculum Design Guide](../DESIGN-GUIDE.md) informs research, module/lesson cohesion and assessment review without adding fixed counts or changing those normative rules.
