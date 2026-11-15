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
| [APP2](APP2.md) | Frontend Engineering | 9 weeks | APP1 | `course` | Core · draft |
| [APP3](APP3.md) | Backend Engineering & API Design | 9 weeks | APP1 | `course` | Core · draft |
| [APP4](APP4.md) | Databases & Data Modeling | 8 weeks | APP3 | `course` | Core · draft |
| [APP5](APP5.md) | Full-Stack Architecture | 8 weeks | APP2, APP3, APP4 | `course` | Core · draft |
| [APP6](APP6.md) | Software Quality & Engineering Operations | 7 weeks | APP3, APP5 | `course` | Core · draft |
| [APP7](APP7.md) | Deployment, Cloud & DevOps | 9 weeks | APP3, APP6 | `course` | Core · draft |
| [APP8](APP8.md) | Production Application Architecture | 9 weeks | APP5, APP6, APP7 | `course` | Core · draft |
| [APP9](APP9.md) | Application Engineering Capstone | 12–16 weeks | APP1–APP8, APP17 | `project` | Core · draft |
| [APP10](APP10.md) | Advanced Frontend Performance | 7 weeks | APP2, APP6 | `course` | **Elective · draft** |
| [APP11](APP11.md) | Advanced Backend Architecture | 9 weeks | APP3, APP4, APP6 | `course` | **Elective · draft** |
| [APP12](APP12.md) | Realtime Systems | 7 weeks | APP3, APP5, APP6 | `course` | **Elective · draft** |
| [APP13](APP13.md) | Mobile Application Engineering | 9 weeks | APP2, APP3 | `course` | **Elective · draft** |
| [APP14](APP14.md) | API Gateways & Edge Delivery | 7 weeks | APP3, APP7 | `course` | **Elective · draft** |
| [APP15](APP15.md) | Advanced TypeScript/Rust Application Development | 10 weeks | APP2, APP3, APP6 | `course` | **Elective · draft** |
| [APP16](APP16.md) | Platform Engineering | 8 weeks | APP6, APP7 | `course` | **Elective · draft** |

**Current totals:** 10 core courses (including APP9's project capstone) and 7 optional electives, all `draft`. The electives APP10–APP16 are not required for graduation.

**Roadmap, not active prerequisites:** The approved [APP migration architecture](ARCHITECTURE.md) describes a future 14-course core, including APP18–APP21 and revised boundaries for existing courses. Only APP17 from that expansion is currently published. The proposed courses, target prerequisites, and revised graduation pathway are **not active** until the corresponding course files and this catalog are updated through reviewed changes.

```text
SEF10 → APP1
APP1 → APP17, APP2, APP3
APP3 → APP4
APP2 + APP3 + APP4 → APP5
APP3 + APP5 → APP6
APP3 + APP6 → APP7
APP5 + APP6 + APP7 → APP8
APP1–APP8 + APP17 → APP9
```

## Independent study

Every authored APP course is currently `draft`. Course files define public outcomes, module structure, required practical work and completion requirements. Reading lists, affiliate purchases and commercial teaching content remain outside OEE. Learners can work through the core sequence independently; a commercial course or proprietary platform is not a graduation requirement.

## Course maturity and scope

APP1 and APP17 use the outcome-driven `v0.2.0` draft format. The other 15 published APP courses retain their earlier format until individually reviewed and migrated. No course is yet `tested` or `verified`; educational quality, assessments, reproducibility, workload, and learner feedback require further evaluation. The [curriculum inventory](../INVENTORY.md) reports format and structural status without implying conformance.

APP1 covers first-principles Internet and browser mechanisms, not JavaScript application or backend implementation. APP17 provides the complementary HTML/CSS authoring capability. Course-specific outcomes and assessment expectations belong in their linked course definitions; the [Curriculum Design Guide](../DESIGN-GUIDE.md) provides non-normative guidance on lesson depth, scope, and sequencing.
