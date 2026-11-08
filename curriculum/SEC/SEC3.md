# SEC3 — Systems & Binary Security

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** SEC1 and SEF5 *(legacy mapping; reconcile before activation)*
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SEC.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Study memory corruption, native binaries, debugging, and common exploitation mitigations in deliberately vulnerable local environments. The focus is on understanding how bugs arise and how engineering choices prevent them.

## Learning outcomes

- Explain how common native-code memory vulnerabilities arise.
- Inspect program behavior and memory using appropriate debugging tools.
- Explain the purpose and limits of ASLR, NX/DEP, canaries, and related mitigations.
- Connect unsafe C patterns to safer systems-design choices.
- Document a vulnerability and its mitigation within an isolated authorized lab.

## Modules

### Module 1 — Native Memory & Vulnerability Classes

#### Outcomes

By the end of this module, the learner can:

- Explain **Stack, heap, and memory-corruption conditions** in the context of the course.
- Apply **Common native-code vulnerability patterns** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Stack, heap, and memory-corruption conditions** — `lesson`
2. **Common native-code vulnerability patterns** — `lesson`
3. **Checkpoint: memory corruption** — `test`
4. **Micro-lab: Identify the unsafe operation in a deliberately vulnerable local program.** — `lab`

### Module 2 — Binary Analysis & Debugging

#### Outcomes

By the end of this module, the learner can:

- Explain **Binary inspection and debugging** in the context of the course.
- Apply **Understanding exploit preconditions in a sandbox** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Binary inspection and debugging** — `lesson`
2. **Understanding exploit preconditions in a sandbox** — `lesson`
3. **Checkpoint: binary reasoning** — `test`
4. **Micro-lab: Inspect a training binary and identify the relevant memory boundary.** — `lab`

### Module 3 — Platform Mitigations

#### Outcomes

By the end of this module, the learner can:

- Explain **ASLR and NX/DEP** in the context of the course.
- Apply **Canaries and defense-in-depth** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **ASLR and NX/DEP** — `lesson`
2. **Canaries and defense-in-depth** — `lesson`
3. **Checkpoint: mitigation mechanisms** — `test`
4. **Micro-lab: Observe how a mitigation changes the behavior of a controlled local program.** — `lab`

### Module 4 — Safer Native Design

#### Outcomes

By the end of this module, the learner can:

- Explain **Secure C coding practices** in the context of the course.
- Apply **Rust memory-safety boundaries** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Secure C coding practices** — `lesson`
2. **Rust memory-safety boundaries** — `lesson`
3. **Checkpoint: prevention versus mitigation** — `test`
4. **Micro-lab: Rewrite one vulnerable component in safe Rust and state the guarantee gained.** — `lab`

### Module 5 — Native Security Lab

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Work only in the private sandbox: demonstrate, mitigate, and compare vulnerable native programs** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- memory corruption
- stack/heap behavior
- common native-code vulnerabilities
- ASLR
- NX/DEP
- canaries
- debugging
- binary inspection
- secure coding
- Rust memory-safety boundaries

### Labs

- debugger exercises
- binary inspection
- sandboxed vulnerable programs
- mitigation experiments

### Substantial course lab

**Native Security Lab**

Create intentionally vulnerable C programs in a private sandbox, demonstrate the bug, explain the exploit condition at a high level, implement a mitigation, and compare with safer Rust designs.
