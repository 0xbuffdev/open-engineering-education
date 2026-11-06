# Program 2 — APP: Application Engineering

> [OEE curriculum](../README.md) · [Specification](../../spec/README.md) · [OEE Workspace](https://github.com/0xbuffdev/oee-workspace)

## Overview

Application Engineering is the professional software-development pathway after Software Engineering Foundations. Learners build, test, deploy and operate modern applications, beginning with internet foundations and progressing through frontend and backend engineering, databases, integrated architecture, quality, operations and production deployment. Work is cumulative: implementations developed in earlier courses become inputs to later practical exercises and labs.

## Prerequisites

**SEF — Software Engineering Foundations.** Course-level prerequisites are listed below. Equivalent prior competence may be demonstrated through an appropriate diagnostic assessment.

## Learning outcomes

By the end of the core program, the learner will be able to:

- Design and build maintainable frontend, backend and full-stack applications.
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

Core and elective courses appear in the **same list**. **Status** here indicates `Core · draft` versus `Elective · planned`; for authored courses, the actual OEE readiness status is separately specified in each course as `draft`, `tested` or `verified`. Elective classification is not a fourth readiness status.

| Course | Title | Duration | Prerequisites | Kind | Status |
| --- | --- | --- | --- | --- | --- |
| [APP1](APP1.md) | Web & Internet Foundations | 4 weeks | SEF10 | `course` | Core · draft |
| [APP2](APP2.md) | Frontend Engineering | 5 weeks | APP1 | `course` | Core · draft |
| [APP3](APP3.md) | Backend Engineering & API Design | 5 weeks | APP1 | `course` | Core · draft |
| [APP4](APP4.md) | Databases & Data Modeling | 5 weeks | APP3 | `course` | Core · draft |
| [APP5](APP5.md) | Full-Stack Architecture | 6 weeks | APP2, APP3, APP4 | `course` | Core · draft |
| [APP6](APP6.md) | Software Quality & Engineering Operations | 4 weeks | APP3, APP5 | `course` | Core · draft |
| [APP7](APP7.md) | Deployment, Cloud & DevOps | 5 weeks | APP3, APP6 | `course` | Core · draft |
| [APP8](APP8.md) | Production Application Architecture | 5 weeks | APP5, APP6, APP7 | `course` | Core · draft |
| [APP9](APP9.md) | Application Engineering Capstone | 8–10 weeks | APP1–APP8 | `project` | Core · draft |
| — | Advanced Frontend Performance | To be defined | Core APP knowledge; specific prerequisites pending | `course` (proposed) | **Elective · planned** |
| — | Advanced Backend Architecture | To be defined | Core APP knowledge; specific prerequisites pending | `course` (proposed) | **Elective · planned** |
| — | Realtime Systems | To be defined | Core APP knowledge; specific prerequisites pending | `course` (proposed) | **Elective · planned** |
| — | Mobile Application Engineering | To be defined | Core APP knowledge; specific prerequisites pending | `course` (proposed) | **Elective · planned** |
| — | API Gateways & Edge Delivery | To be defined | Core APP knowledge; specific prerequisites pending | `course` (proposed) | **Elective · planned** |
| — | Advanced TypeScript/Rust Application Development | To be defined | Core APP knowledge; specific prerequisites pending | `course` (proposed) | **Elective · planned** |
| — | Platform Engineering | To be defined | Core APP knowledge; specific prerequisites pending | `course` (proposed) | **Elective · planned** |

**Totals:** 9 core courses (8 taught courses and one project capstone), plus 7 proposed electives. Electives are listed to make the intended catalog visible; their final titles, stable identifiers, prerequisites, durations, outcomes, and course files have **not** been defined or approved. They must be authored and reviewed before being represented as available courses.

```text
SEF10 → APP1
APP1 → APP2, APP3
APP3 → APP4
APP2 + APP3 + APP4 → APP5
APP3 + APP5 → APP6
APP3 + APP6 → APP7
APP5 + APP6 + APP7 → APP8
APP1–APP8 → APP9
```

## Independent study

Every authored APP course is currently `draft`. Course files define public outcomes, module structure, required practical work and completion requirements. Reading lists, affiliate purchases and commercial teaching content remain outside OEE. Learners can work through the core sequence independently; a commercial course or proprietary platform is not a graduation requirement.

**Initial import limitations:** This port preserves the source's nine core course scopes, course-level outcomes, five-module structures and practical requirements but still requires review for unambiguous test success criteria, precise lab evaluation rubrics, reproducible environment instructions and evidence collection. The seven electives are planning entries only; no elective course has been invented or declared ready.
