# Program 2 — APP: Application Engineering

> [OEE curriculum](../README.md) · [Specification](../../spec/README.md) · [OEE Workspace](https://github.com/0xbuffdev/oee-workspace)

## Overview

Application Engineering is the professional software-development pathway after Software Engineering Foundations. Learners build, test, deploy and operate modern applications, beginning with first-principles internet and browser foundations, then accessible HTML/CSS authoring, and progressing through frontend and backend engineering, databases, integrated architecture, quality, operations and production deployment. Work is cumulative: implementations developed in earlier courses may become inputs to later practice and outcome-based assessments.

## Prerequisites

**SEF — Software Engineering Foundations.** Course-level prerequisites are listed below. Equivalent prior competence may be demonstrated through an appropriate diagnostic assessment.

## Learning outcomes

By the end of the core program, the learner will be able to:

- Author accessible semantic documents and robust responsive styles, then design and build maintainable frontend, backend and full-stack applications.
- Design HTTP APIs with validation, authentication, authorization and explicit failure handling.
- Model relational data and reason about queries, indexes, transactions and schema migrations.
- Integrate asynchronous work, caching, realtime features and external services without obscuring boundaries.
- Build testing, CI, observability and production-debugging workflows.
- Deploy and operate an application with secure configuration, HTTPS, health checks, monitoring and rollback.
- Measure performance and capacity, investigate bottlenecks and make evidence-based architectural changes.
- Deliver and defend a complete product through implementation, deployment and operation.

## Program completion standard

Complete the required core courses and successfully deliver, evaluate and defend the APP9 capstone, with reproducible artifacts, documented design choices, verification results, failure analysis and a technical retrospective.

Electives provide optional specialization and are **not** prerequisites for the capstone or graduation.

---

## Courses

The table below is the **current** APP catalog, not its migration target. Core courses are required; electives are optional specializations. The `Core · draft` and `Elective · draft` entries show both course classification and educational readiness: `elective` is **not** an additional readiness label. Durations are provisional and require calibration with learner evidence.

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
| [APP8](APP8.md) | Production Application Architecture | 9 weeks | APP5, APP6, APP7 | `course` | Core · draft |
| [APP9](APP9.md) | Application Engineering Capstone | 12–16 weeks | APP1–APP8, APP17–APP21 | `project` | Core · draft |
| [APP10](APP10.md) | Advanced Frontend Performance | 7 weeks | APP2, APP6 | `course` | **Elective · draft** |
| [APP11](APP11.md) | Advanced Backend Architecture | 9 weeks | APP3, APP4, APP6 | `course` | **Elective · draft** |
| [APP12](APP12.md) | Realtime Systems | 7 weeks | APP3, APP5, APP6 | `course` | **Elective · draft** |
| [APP13](APP13.md) | Mobile Application Engineering | 9 weeks | APP2, APP3 | `course` | **Elective · draft** |
| [APP14](APP14.md) | API Gateways & Edge Delivery | 7 weeks | APP3, APP7 | `course` | **Elective · draft** |
| [APP15](APP15.md) | Advanced TypeScript/Rust Application Development | 10 weeks | APP2, APP3, APP6 | `course` | **Elective · draft** |
| [APP16](APP16.md) | Platform Engineering | 8 weeks | APP6, APP7 | `course` | **Elective · draft** |

**Current totals:** 14 core courses (including APP9's project capstone) and 7 optional electives, all `draft`. The electives APP10–APP16 are not required for graduation.

**Roadmap, not active prerequisites:** The approved [APP migration architecture](ARCHITECTURE.md) describes the target 14-course core, including the new APP17–APP21 capabilities and revised boundaries for existing courses. APP17–APP21 have been introduced as `v0.2.0` drafts, and APP4 and APP2 have been migrated. The full 14-course core identity set is now published. Unmigrated legacy courses and their *target* scope/prerequisite revisions remain **inactive** until their course files and this catalog are updated through reviewed changes. APP3's framework-based API scope and three direct foundations are now active in this catalog revision.

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

## Independent study

Every authored APP course is currently `draft`. Course files define public outcomes, module structure, required practical work and completion requirements. Reading lists, affiliate purchases and commercial teaching content remain outside OEE. Learners can work through the core sequence independently; a commercial course or proprietary platform is not a graduation requirement.

## Course maturity and scope

APP1, APP17, APP18, APP19, APP20, APP21, APP4, APP2, APP3, APP5, APP6 and APP7 use the outcome-driven `v0.2.0` draft format. The other 9 published APP courses retain their earlier format until individually reviewed and migrated. No course is yet `tested` or `verified`; educational quality, assessments, reproducibility, workload, and learner feedback require further evaluation. The [curriculum inventory](../INVENTORY.md) reports format and structural status without implying conformance.

APP1 covers first-principles Internet and browser mechanisms, not JavaScript application or backend implementation. APP17 provides the complementary HTML/CSS authoring capability. APP18 introduces JavaScript programming and local Node/npm development tooling without requiring APP1, DOM programming or backend implementation. APP19 builds on APP18 with static TypeScript models, type/runtime boundaries and reproducible compiler checking; it is not a React or backend framework course. APP4 now provides an independent SEF10-entry foundation in SQL, relational integrity, transactions, query planning, tenant security and recovery, before backend frameworks. APP21 follows APP18 and teaches the Node backend runtime, asynchronous I/O, streams and a small raw HTTP service without a TypeScript, database or framework prerequisite. APP2 now follows APP17 and APP19 and teaches framework-neutral browser DOM, event, form, state, network, navigation, accessibility, usability and security engineering without React or a mandatory backend server. APP20 follows APP2 and applies React-specific component/render identity, Hooks, lifecycle, data/routing, error boundaries, accessible interaction, testing and performance decisions to a complete client-side application; backend Node services and full-stack frameworks are not required. APP3 now follows APP19, APP21 and APP4, and teaches TypeScript/Fastify service architecture, runtime schemas, authenticated server-side authorization, PostgreSQL transaction orchestration, replay-safe asynchronous work, versioned consumer contracts, structured diagnostics and independent service defense. It does not repeat TypeScript, raw Node runtime or full SQL foundations. APP5 now follows APP20 and APP3 directly (with APP4 required transitively through APP3), assessing cross-layer user-journey requirements, authenticated client/server/data integration, state consistency, tenant-aware cache and file lifecycle, durable asynchronous work and progress, partial-failure recovery, compatible changes and independent full-stack defense. It does not replace APP6 quality strategy, APP7 deployment, or APP8 production-scale architecture. APP6 now follows APP5 directly (with APP3 and its language/runtime/data foundations inherited transitively) and deepens quality and maintainability strategy, deterministic tests, least-privilege CI, reproducible dependency/build evidence, supply-chain review, privacy-aware telemetry, SLO and performance investigations, incident analysis and independent reliability upgrades. APP7 now follows APP5 + APP6 directly and teaches deployment/process packaging, verified TLS/reverse proxy trust, environment secrets and isolation, applied IaC/drift, immutable artifact promotion, stateful compatible releases, actual backup/restore and operational recovery, and provider/cost decisions without a mandatory paid cloud. APP8 retains advanced production-scale architectural choices. Course-specific outcomes and assessment expectations belong in their linked course definitions; the [Curriculum Design Guide](../DESIGN-GUIDE.md) provides non-normative guidance on lesson depth, scope, and sequencing.
