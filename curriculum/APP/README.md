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

Core and elective courses appear in the **same list**. Durations are draft workload estimates based on the expanded scope and must be calibrated through teaching and learner evidence. Catalogue statuses combine a course's required/optional classification with its OEE readiness status: `Core · draft` or `Elective · draft`. The underlying OEE readiness status is independently `draft`, `tested` or `verified`; `elective` is a classification, **not** a fourth readiness status. Elective course files explicitly declare the `Classification` metadata field with the value `elective`.

| Course | Title | Duration | Prerequisites | Kind | Status |
| --- | --- | --- | --- | --- | --- |
| [APP1](APP1.md) | Web & Internet Foundations | 7 weeks | SEF10 | `course` | Core · draft |
| [APP2](APP2.md) | Frontend Engineering | 9 weeks | APP1 | `course` | Core · draft |
| [APP3](APP3.md) | Backend Engineering & API Design | 9 weeks | APP1 | `course` | Core · draft |
| [APP4](APP4.md) | Databases & Data Modeling | 8 weeks | APP3 | `course` | Core · draft |
| [APP5](APP5.md) | Full-Stack Architecture | 8 weeks | APP2, APP3, APP4 | `course` | Core · draft |
| [APP6](APP6.md) | Software Quality & Engineering Operations | 7 weeks | APP3, APP5 | `course` | Core · draft |
| [APP7](APP7.md) | Deployment, Cloud & DevOps | 9 weeks | APP3, APP6 | `course` | Core · draft |
| [APP8](APP8.md) | Production Application Architecture | 9 weeks | APP5, APP6, APP7 | `course` | Core · draft |
| [APP9](APP9.md) | Application Engineering Capstone | 12–16 weeks | APP1–APP8 | `project` | Core · draft |
| [APP10](APP10.md) | Advanced Frontend Performance | 7 weeks | APP2, APP6 | `course` | **Elective · draft** |
| [APP11](APP11.md) | Advanced Backend Architecture | 9 weeks | APP3, APP4, APP6 | `course` | **Elective · draft** |
| [APP12](APP12.md) | Realtime Systems | 7 weeks | APP3, APP5, APP6 | `course` | **Elective · draft** |
| [APP13](APP13.md) | Mobile Application Engineering | 9 weeks | APP2, APP3 | `course` | **Elective · draft** |
| [APP14](APP14.md) | API Gateways & Edge Delivery | 7 weeks | APP3, APP7 | `course` | **Elective · draft** |
| [APP15](APP15.md) | Advanced TypeScript/Rust Application Development | 10 weeks | APP2, APP3, APP6 | `course` | **Elective · draft** |
| [APP16](APP16.md) | Platform Engineering | 8 weeks | APP6, APP7 | `course` | **Elective · draft** |

**Totals:** 9 core courses (8 taught courses and one project capstone), plus 7 optional elective courses, all initially `draft`. Course definitions are public curriculum specifications, **not** finished teaching materials or readiness claims. APP9 remains the core capstone: APP10–APP16 are not required for graduation.

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

**Draft limitations:** The nine core and seven elective courses have expanded learning sequences and additional assessment/lab briefs. They still require educational review, independent lab reproduction, completed question banks, detailed tool-version checks, and learner feedback before any readiness promotion. The electives extend the public curriculum but do not alter the core progression, graduation or commercial content.

**Depth policy:** No course or module has an arbitrary fixed lesson or module count. The number and sequence follow distinct technical mechanisms, prerequisite knowledge, application, assessment, and evidence needs. A module may omit an assessment if an explicit outcome-based justification exists; the course must end in a substantial integration lab.
