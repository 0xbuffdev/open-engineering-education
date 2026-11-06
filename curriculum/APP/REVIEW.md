# APP Curriculum Design Audit — Draft Expansion

> [Application Engineering](README.md) · [OEE Course Format](../../spec/course-format.md) · [Evidence Rules](../../spec/evidence-rules.md)

## Purpose and scope

This report records the first **structural and technical depth audit** of APP1–APP16. It is a design review, **not** a learner study, external expert endorsement, or readiness certification. The canonical course definitions remain the APP Markdown files, not this summary.

Before this audit, each APP course had exactly five modules; four instructional modules typically offered only two concept lessons before a test and micro-lab, while the final lab was a one-entry module. The validator enforced the same fixed module count, unintentionally incentivizing narrow coverage.

**Revised design:** Modules are driven by distinct prerequisite concepts, technical mechanisms, meaningful tests and hands-on investigations. There is **no fixed maximum** number of modules or lessons. We retain existing course identifiers and required outcomes, expand major technical gaps, and specify observable work and failure cases for added practical modules.

## Current draft coverage

| Course | Modules | Typed entries | Deepened scope | Still needs educational verification |
| --- | ---: | ---: | --- | --- |
| [APP1](APP1.md) | 8 | 48 | HTTP method semantics, TLS/CORS trust boundaries, browser execution, proxies, retries, service diagnostics | Confirm DNS/TLS trace environments, response caching tests and no private resource reuse |
| [APP2](APP2.md) | 9 | 55 | TypeScript architecture, async state, accessibility testing, client performance | Verify keyboard/screen-reader workflows, data invalidation and performance reproducibility |
| [APP3](APP3.md) | 9 | 54 | Domain isolation, transactional correctness, API compatibility, security, observability | Test concurrent updates, negative authorization and safe error contracts |
| [APP4](APP4.md) | 8 | 48 | Relational reasoning, advanced SQL, tenancy, data recovery and schema evolution | Reproduce migration/restore rehearsals and verify SQL fixtures |
| [APP5](APP5.md) | 8 | 48 | Client/server state boundaries, authorization, contract safety, fault recovery | Verify end-to-end access, asynchronous retries and partial dependency failure |
| [APP6](APP6.md) | 8 | 48 | Test strategy, CI/supply-chain checks, SLOs, regression measurement | Reproduce CI security gate, incident and load measurement |
| [APP7](APP7.md) | 9 | 54 | Declarative provisioning, recovery, monitoring, cloud economics | Rehearse backups and deployment rollback without paid-provider dependencies |
| [APP8](APP8.md) | 9 | 54 | Saturation testing, data scaling, cascading failures, incremental migration | Validate queue bounds, consistency and rollback under observed load |
| [APP9](APP9.md) | 9 | 54 | Product validation, privacy, operations and independent technical defense | Run a real reviewer reproduction, scope/ethics check and graduated project rubric |
| [APP10](APP10.md) | 8 | 50 | Deep profiling, network delivery, memory and performance governance | Control measurement variance and verify accessibility with optimization |
| [APP11](APP11.md) | 9 | 54 | Distributed coordination, tenancy, data migration and economic trade-offs | Reproduce compensations and data-consistency tests under network failure |
| [APP12](APP12.md) | 8 | 48 | Conflict handling, event security, outage and reconnection semantics | Prove state convergence and authorization with out-of-order events |
| [APP13](APP13.md) | 9 | 54 | Cross-platform lifecycle, permission handling, energy, release operations | Verify on real/simulated device matrix and test permission expiry |
| [APP14](APP14.md) | 7 | 42 | Caching, streaming, gateway identity, global failure containment | Validate private cache isolation, trusted proxy headers and fault injection |
| [APP15](APP15.md) | 9 | 57 | Rust ownership, typed packages, FFI/API compatibility, hybrid builds | Confirm versioned contracts, memory boundaries and reproducible benchmarks |
| [APP16](APP16.md) | 8 | 48 | Developer portals, artifact promotion, policy, service economics | Demonstrate unauthorized-deploy denial and real developer-task improvements |
| **Total** | **135** | **816** | | |

The entry count includes `lesson`, `test`, and `lab` types; it is **not** a count of lecture scripts or validated assessments. Course durations are preliminary workload estimates rather than measured completion times.

## Educational decisions

1. **Core progression stays stable:** APP1–APP8 remain the taught foundation for APP9. Expanded APP9 scope is still assessed through a single required capstone project and defense.
2. **Electives extend rather than gate graduation:** APP10–APP16 require selected core skills but do not become prerequisites for APP9. The `elective` classification stays separate from OEE course-readiness status.
3. **Lessons teach individual mechanisms:** New topics isolate concepts such as request replay versus idempotency, client state versus authoritative state, runtime validation versus static typing, and caching versus data consistency.
4. **Tests assess reasoning:** Checkpoints should ask learners to predict, compare, explain and debug behavior. Names and high-level test briefs in the curriculum are not substitutes for authored assessments with scoring criteria.
5. **Labs require evidence:** Added lab briefs name a task, repeatable environment assumptions, expected result, verification, evidence and representative failure analysis. The final integration lab remains required.
6. **Tool independence:** Curriculum requirements must be achievable with suitable local, free or open alternatives. Private teaching resources and book/chapter assignments remain outside OEE.
7. **Variable pacing:** The revised duration estimates reflect a larger technical scope, but must be calibrated through actual learners. A module's difficulty cannot be inferred from its entry count alone.

## Remaining quality gates before readiness promotion

The following work is intentionally **not** represented as completed by this draft:

- **Technical expert review:** Check architecture, security, database and platform claims, and eliminate any residual overlap between core and elective courses.
- **Instructional design:** Review prerequisite availability, learning progression, the cognitive load of each module, realistic pacing and meaningful transfer practice.
- **Assessment authoring:** Write actual checkpoint questions and evaluation rubrics with accepted responses, misconceptions, and explicit criteria tied to outcomes.
- **Lab reproduction:** Run each required practical task in a documented environment; include version assumptions, starter inputs, expected output, failure and safety conditions, and evidence reviewers can reproduce.
- **Capstone validation:** Trial the project scope and defense rubric independently, including requirements traceability, secure deployment, failure recovery, ethics and accessibility.
- **Learner testing:** Record learner feedback and remediation in accordance with OEE status labels and evidence rules. All APP courses remain `draft` until supported promotion.
- **Cross-program alignment:** Check APP dependencies against SEF and future SYS/AI/SEC boundaries before treating these outlines as a finished curriculum.
- **External resource separation:** Reconcile books, online resources, private 0xNAND teaching overlays, and machine-readable progress identifiers only after curriculum quality review. No private content repository change is part of this audit.

## Structural integrity checks

The APP checker validates course codes, required metadata, `draft` labels, core/elective classification, links, prerequisite cycles, sequential module numbering, module outcomes, sequential typed lesson entries, first-course orientation, final integration lab, project defense, and title/duration agreement with the course catalogue. It no longer assumes five modules.

A green check establishes **structural validity only**, not that the expanded scope is complete, educationally effective, or operationally verified.

## Suggested focused review sequence

1. Review APP1–APP4 for mechanism coverage and prerequisite readiness.
2. Review APP5–APP8 for complete application integration, operations, and architecture without avoidable duplication.
3. Review APP9 as a real capstone with bounded, observable graduation expectations.
4. Review APP10–APP16 for specialized depth, market/tool neutrality, and overlap with core.
5. After approvals, conduct lab reproduction and assessment-authoring passes in separate PRs.

Do not promote a course from `draft` or integrate the expanded tree into the private `content` repository merely because this audit PR passes CI.
