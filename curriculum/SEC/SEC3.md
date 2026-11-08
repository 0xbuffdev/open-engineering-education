## SEC3 — Systems & Binary Security

**Duration:** 6 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** SEC1 and SEF5

**Recommended:** SYS1 and SYS2.

### Overview

Study memory corruption, native binaries, debugging, and common exploitation mitigations in deliberately vulnerable local environments. The focus is on understanding how bugs arise and how engineering choices prevent them.

### Prerequisites

**SEC1 — Security Foundations & Threat Modeling**
**SEF5 — Low-Level Programming with C & Linux**
**Recommended:** SYS1 and SYS2.

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Explain how common native-code memory vulnerabilities arise.
- Inspect program behavior and memory using appropriate debugging tools.
- Explain the purpose and limits of ASLR, NX/DEP, canaries, and related mitigations.
- Connect unsafe C patterns to safer systems-design choices.
- Document a vulnerability and its mitigation within an isolated authorized lab.


### Resource map

**Required**

- **B14** §3.7 and §3.10 (procedures; combining control and data — buffer overflow, GDB, countermeasures) and Ch. 7 (Linking) — added.
- **B2** Ch. 5 and §8.7 · **B5** Ch. 6–7 and §38.9 · **B4** Ch. 13–23 — carried from ZtP D2.
- **R64** pwn.college (isolated lab only) — carried from ZtP D2.
- **R65** SoK: Eternal War in Memory · **B15** Ch. 4 and §20.1 · **R36** — added for the safer-design comparison.

### Modules

#### Module 1 — Native Memory & Vulnerability Classes

**Reading:** **B14** §3.7 (Procedures — the stack frame), §3.10 (Combining Control and Data in Machine-Level Programs — out-of-bounds references and buffer overflow). **B5** §38.9 (Beware of Buffer Overruns), §6.3 (Memory Layout of a Process), Ch. 7 (Memory Allocation). **B2** Ch. 5 (Pointers and Arrays), §8.7 (A Storage Allocator). **R65** the overview of memory-error classes.


### Module outcomes

By the end of this module, the learner can:

- Explain **Stack, heap, and memory-corruption conditions** in the context of the course.
- Apply **Common native-code vulnerability patterns** in a problem, implementation, experiment, or design decision.

1. **Stack, heap, and memory-corruption conditions**
   - kind: `lesson`
2. **Common native-code vulnerability patterns**
   - kind: `lesson`
3. **Checkpoint: memory corruption**
   - kind: `test`

4. **Micro-lab: Identify the unsafe operation in a deliberately vulnerable local program.**
   - kind: `lab`
#### Module 2 — Binary Analysis & Debugging

**Reading:** **B14** §3.10.2 (Life in the Real World: Using the GDB Debugger), Ch. 7 (Linking — ELF object files). **R64** the reverse-engineering and memory-error modules (isolated lab only).


### Module outcomes

By the end of this module, the learner can:

- Explain **Binary inspection and debugging** in the context of the course.
- Apply **Understanding exploit preconditions in a sandbox** in a problem, implementation, experiment, or design decision.

1. **Binary inspection and debugging**
   - kind: `lesson`
2. **Understanding exploit preconditions in a sandbox**
   - kind: `lesson`
3. **Checkpoint: binary reasoning**
   - kind: `test`

4. **Micro-lab: Inspect a training binary and identify the relevant memory boundary.**
   - kind: `lab`
#### Module 3 — Platform Mitigations

**Reading:** **B14** §3.10.4 (Thwarting Buffer Overflow Attacks — stack randomization, stack corruption detection, limiting executable code regions). **B4** Ch. 13–23 (address spaces through swapping policies — the virtual-memory background for ASLR and NX). **R65** the defenses sections.


### Module outcomes

By the end of this module, the learner can:

- Explain **ASLR and NX/DEP** in the context of the course.
- Apply **Canaries and defense-in-depth** in a problem, implementation, experiment, or design decision.

1. **ASLR and NX/DEP**
   - kind: `lesson`
2. **Canaries and defense-in-depth**
   - kind: `lesson`
3. **Checkpoint: mitigation mechanisms**
   - kind: `test`

4. **Micro-lab: Observe how a mitigation changes the behavior of a controlled local program.**
   - kind: `lab`
#### Module 4 — Safer Native Design

**Reading:** **B15** Ch. 4 (Understanding Ownership), Ch. 20 §20.1 (Unsafe Rust). **R36** Meet Safe and Unsafe. **B5** Ch. 38. **B2** Ch. 5.


### Module outcomes

By the end of this module, the learner can:

- Explain **Secure C coding practices** in the context of the course.
- Apply **Rust memory-safety boundaries** in a problem, implementation, experiment, or design decision.

1. **Secure C coding practices**
   - kind: `lesson`
2. **Rust memory-safety boundaries**
   - kind: `lesson`
3. **Checkpoint: prevention versus mitigation**
   - kind: `test`

4. **Micro-lab: Rewrite one vulnerable component in safe Rust and state the guarantee gained.**
   - kind: `lab`
#### Module 5 — Native Security Lab

**Reading:** **R64** the sandboxed modules matching the chosen vulnerabilities. **B14** §3.10. **B15** Ch. 4 for the Rust rewrite.


1. **Work only in the private sandbox: demonstrate, mitigate, and compare vulnerable native programs**
   - kind: `lab`

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

---

