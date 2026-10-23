# Projects

Projects are the curriculum's evidence. A course teaches a mechanism; a project forces you to integrate it under constraints, measure it, break it, and explain it.

## The ladder

| Code | Project | Primary courses | Gate | What it proves |
| --- | --- | --- | --- | --- |
| [P1](project-ladder.md#p1--ledgerlab) | `ledgerlab` | F1–F3, F6 | F2 + F3 | You can build and test a real CLI with persistence and SQL |
| [P2](project-ladder.md#p2--sysprobe) | `sysprobe` | F5, S1–S2 | F5 + S1 | You can inspect a process from user space to ELF/syscalls |
| [P3](project-ladder.md#p3--cachebench) | `cachebench` | S3–S4, S7–S9 | S4 + S9 | You can measure a memory hierarchy and explain it |
| [P4](project-ladder.md#p4--workbenchd) | `workbenchd` | S6, S10, S14–S15 | S6 + S10 | You can build and operate a concurrent network service |
| [P5](project-ladder.md#p5--minikv) | `minikv` | S12 | S12 | You can build a durable storage engine and prove crash behaviour |
| [P6](project-ladder.md#p6--raftkv) | `raftkv` | S11, S12 | P5 + S11 | You can replicate state and state the client guarantee |
| [P7](project-ladder.md#p7--signal-score) | `signal-score` | AI1–AI4, AI13 | AI3 + AI4 | You can build an honest, reproducible ML baseline |
| [P8](project-ladder.md#p8--tinygpt) | `tinygpt` | AI5–AI8 | AI6 | You can implement, train, and evaluate a small transformer |
| [P9](project-ladder.md#p9--doc-compass) | `doc-compass` | AI9–AI12, S13 | AI10 + AI12 | You can serve a bounded generative system with evidence |
| [P10](project-ladder.md#p10--secure-review) | `secure-review` | D1–D3, D9 | D2 + D3 | You can find, fix, and verify security weaknesses |
| [P11](project-ladder.md#p11--authorized-assessment) | `authorized-assessment` | D4–D5, D7–D10 (D6 optional) | D4 + D5 | You can assess a system under scope and write actionable risk |

## Capstones

A capstone is not a new ladder project. It is a **hardening, evaluation, and integration** phase over work you already own.

| Code | Capstone | Builds on | Track |
| --- | --- | --- | --- |
| [C1](capstones.md#c1--resilient-backend-platform) | Resilient backend platform | P4 + P5 | Systems |
| [C2](capstones.md#c2--distributed-storage-service) | Distributed storage service | P5 + P6 | Systems |
| [C3](capstones.md#c3--evaluated-ai-assistant) | Evaluated AI assistant | P7 + P8 + P9 | AI |
| [C4](capstones.md#c4--authorized-security-assessment) | Authorized security assessment | P10 + P11 | Security |

## Rules

1. **Start only after the gate.** A project begun before its prerequisites turns into tutorial copying.
2. **One project at a time.** Small increments are fine; parallel half-built systems are not.
3. **Evidence over demo.** Every claim needs a test, benchmark, trace, or reproducible command.
4. **Failure is part of the deliverable.** Include at least one broken case, one wrong assumption, and one correction.
5. **Security boundary.** Networked, AI, and security projects include a threat model and an authorization note. Security testing only on systems you own or are explicitly authorized to test.
6. **No secrets, private data, weights, or copyrighted books in Git.** Use fixtures, synthetic data, and documented downloads.
7. **Clean checkout test.** A reviewer must be able to run the minimal demo and evaluation from a fresh clone.

## Workspace

Create a project workspace only when you start it:

```bash
./scripts/new-project-workspace ledgerlab
./scripts/new-project-workspace workbenchd
```

The script creates `projects/<slug>/` with a README, design doc, evaluation plan, and retrospective. The full brief stays in [project-ladder.md](project-ladder.md).

## Portfolio

Not every project belongs on a CV. Use [portfolio-guide.md](portfolio-guide.md) to choose two or three deep artifacts, write the case studies, and prepare to defend the design and the biggest failure.

## Definition of done

- [ ] README with problem, scope, setup, commands, and limitations.
- [ ] Tests for normal, boundary, invalid, and failure cases.
- [ ] A reproducible evaluation/benchmark or threat-model verification.
- [ ] Design doc with decisions and trade-offs.
- [ ] Threat model and authorization note where relevant.
- [ ] One significant failure and the evidence that changed the design.
- [ ] Retrospective with next steps.
- [ ] Clean-checkout reproduction.
